"""
WeMD AI 排版引擎 - Flask API 服务
微信公众号文章 AI 排版工具

API 使用方式:
  curl -X POST http://localhost:5000/api/generate \\
    -H "Content-Type: application/json" \\
    -H "Authorization: Bearer YOUR_DEEPSEEK_KEY" \\
    -d '{"article": "文章内容...", "theme": "editorial"}'
"""
import json, re, os
from pathlib import Path
from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
BASE_DIR = Path(__file__).parent

# ============================================================
# DeepSeek API 配置
# ============================================================
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
WEMD_API_KEY = os.environ.get("WEMD_API_KEY", "")  # 对外 API Key（可选）
DEEPSEEK_API_URL = "https://api.deepseek.com/chat/completions"
DEEPSEEK_MODEL = "deepseek-v4-flash"

# ============================================================
# 9套主题（内置）
# ============================================================
THEMES = [
    {"id": "handmade",  "name": "🌸 可爱手帐", "primary": "#f48fb1", "accent": "#f06292", "surface": "#fce4ec", "ink": "#4a3030"},
    {"id": "stripe",    "name": "💳 Stripe 金融", "primary": "#635bff", "accent": "#00d4aa", "surface": "#f8f9ff", "ink": "#1a1a2e"},
    {"id": "vercel",    "name": "⬛ Vercel 极客", "primary": "#000000", "accent": "#ffffff", "surface": "#fafafa", "ink": "#000000"},
    {"id": "apple",     "name": "🍎 Apple 极简", "primary": "#555555", "accent": "#007aff", "surface": "#f5f5f7", "ink": "#1d1d1f"},
    {"id": "ink",       "name": "🖌 新中式水墨", "primary": "#5c4a3a", "accent": "#8b6914", "surface": "#f5efe6", "ink": "#2c241c"},
    {"id": "cyber",     "name": "💜 赛博霓虹", "primary": "#c77dff", "accent": "#ff6b9d", "surface": "#1a1640", "ink": "#f0eaff"},
    {"id": "wabi",      "name": "🍃 日系侘寂", "primary": "#8b7355", "accent": "#6b8e6b", "surface": "#f5efe6", "ink": "#3d3430"},
    {"id": "editorial", "name": "📰 报刊社论", "primary": "#b8860b", "accent": "#b8860b", "surface": "#fcf9f4", "ink": "#1a1814"},
    {"id": "mono",      "name": "⬜ 极简黑白", "primary": "#333333", "accent": "#666666", "surface": "#fafafa", "ink": "#111111"},
]

# ============================================================
# 公众号 HTML 规则（精简版，注入给 AI）
# ============================================================
WECHAT_RULES = """
【微信公众号 HTML 铁律】
1. 唯一容器标签: <section>，禁止 <div>/<table>/<h1>-<h6>
2. 所有 CSS 必须内联 style=""，禁止 <style> 标签和 class
3. 每个元素强制: box-sizing:border-box; max-width:100%!important;
4. 布局: display:flex; flex-flow:row/column; 子元素 inline-block + flex:0 0 auto
5. 支持: linear-gradient, border-radius, text-shadow, transform(4前缀), opacity, z-index
6. 禁止: position:absolute/fixed, animation, vw/vh/rem, calc()
7. 正文基准14px, 行高1.85, 字间距0.3px
8. <img> 必须 display:block; draggable="false"
9. <p> 必须 margin:0; padding:0
10. 输出纯HTML片段（不含 <!DOCTYPE>/<html>/<head>/<body>），可直接粘贴到公众号
"""

def build_ai_prompt(article, theme_name, design_spec, custom_style=""):
    """构建发给 DeepSeek 的 prompt"""

    # 构建主题描述
    if custom_style:
        theme_desc = f"用户自定义风格: {custom_style}\n请严格按此风格设计配色方案，不要使用预置的9套主题。"
    elif theme_name == "auto":
        theme_desc = "自动选择风格: 请根据文章内容的调性、情感、主题，自主选择一个最匹配的视觉风格（不要使用已有的9套预设主题）。例如：科技感文章→霓虹暗黑风、温馨故事→水彩手绘风、商业分析→极简商务风等。自行决定配色和组件风格。"
    else:
        theme_info = get_theme_info(theme_name)
        theme_desc = f"""当前主题: {theme_info['name']}
配色方案（请严格使用以下4个精确色值）:
- 主色: {theme_info.get('primary', '#333333')}
- 强调色: {theme_info.get('accent', '#666666')}
- 底色（背景）: {theme_info.get('surface', '#ffffff')}
- 文字色: {theme_info.get('ink', '#111111')}
请严格以这4个色值为基准进行排版配色，不要使用近似值。"""

    return f"""你是一个微信公众号排版专家。请根据以下设计规范，将用户文章排版为公众号兼容的 HTML。

## 设计规范
{design_spec}

## 风格要求
{theme_desc}

## 公众号 HTML 规则
{WECHAT_RULES}

## 文章内容
{article}

## 核心要求
1. 严格遵循设计规范中的 HTML 标签规则、CSS 属性白名单
2. 根据规范第12部分，自由设计文章头部卡片（字数/阅读时间/话题标签/一句话概览）
3. 根据规范第12.2部分，自由设计文章尾部卡片——重点是图标设计：从5种风格(A经典三连/B胶囊渐变/C大图标/D极简文字/E暗色标签)中选一个，emoji图标 + 文字组合，每个按钮颜色有区分
4. 根据规范第11部分，可以适度优化文章内容：提取金句做大字引用、拆分长段落、数据可视化、重组结构
5. 文章容器背景必须用 transparent（透明），不设底色。卡片用 rgba 半透明。让微信自动处理暗黑模式
6. 排版精美、有呼吸感、有视觉层次

## 输出格式
只输出 HTML 代码片段（从第一个 <section> 开始），不要任何解释说明，不要 markdown 代码块标记。"""

# ============================================================
# API 路由
# ============================================================

MAIN_SPEC_FILE = BASE_DIR / "docs" / "公众号HTML排版设计规范.md"
_SPEC_CACHE = None

# ============================================================
# CORS 跨域支持（API 对外使用）
# ============================================================
@app.after_request
def add_cors(resp):
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    resp.headers["Access-Control-Allow-Headers"] = "Content-Type, Authorization"
    return resp

# ============================================================
# 对外 API 网关校验（可选）
# 设置 WEMD_API_KEY 环境变量后，外部请求必须带此 Key
# ============================================================
@app.before_request
def check_gateway_key():
    if request.path.startswith("/api/") and request.method != "OPTIONS":
        gateway_key = os.environ.get("WEMD_API_KEY", "")
        if gateway_key:
            auth = request.headers.get("Authorization", "")
            if not auth.startswith("Bearer ") or auth[7:] != gateway_key:
                return jsonify({"error": "无效的网关 API Key，请在 Authorization header 中传入正确的 WEMD_API_KEY"}), 401

@app.route("/api/generate", methods=["OPTIONS"])
def api_generate_options():
    return jsonify({}), 200

# ============================================================
# API Key 校验
# ============================================================
def require_api_key():
    """校验请求中的 API Key。优先级：Authorization header > 请求体 > 环境变量"""
    auth = request.headers.get("Authorization", "")
    if auth.startswith("Bearer "):
        key = auth[7:]
        if key:
            return key
    data = request.get_json(silent=True) or {}
    key = (data.get("api_key") or "").strip()
    if key:
        return key
    return DEEPSEEK_API_KEY

def load_main_spec():
    global _SPEC_CACHE
    if _SPEC_CACHE is None:
        if MAIN_SPEC_FILE.exists():
            _SPEC_CACHE = MAIN_SPEC_FILE.read_text(encoding="utf-8")
        else:
            _SPEC_CACHE = ""
    return _SPEC_CACHE

def get_theme_info(theme_id):
    for t in THEMES:
        if t["id"] == theme_id:
            return t
    return THEMES[-1]

@app.route("/api/balance", methods=["POST"])
def api_balance():
    data = request.get_json(force=True)
    api_key = (data.get("api_key") or "").strip() or DEEPSEEK_API_KEY
    if not api_key:
        return jsonify({"error": "No API key"}), 400
    try:
        resp = requests.get(
            "https://api.deepseek.com/user/balance",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10,
        )
        resp.raise_for_status()
        bal = resp.json()
        return jsonify({"data": bal})
    except Exception as e:
        return jsonify({"error": f"Balance query failed: {str(e)[:100]}"}), 500

@app.route("/api/test-connection", methods=["POST"])
def api_test_connection():
    """测试 DeepSeek API 连接是否正常（轻量请求，只列出模型列表）"""
    import time
    data = request.get_json(force=True)
    api_key = (data.get("api_key") or "").strip() or DEEPSEEK_API_KEY
    if not api_key:
        return jsonify({"ok": False, "error": "未提供 API Key"}), 400
    t0 = time.time()
    try:
        resp = requests.get(
            "https://api.deepseek.com/models",
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=10,
        )
        elapsed = int((time.time() - t0) * 1000)
        if resp.status_code == 200:
            models = resp.json().get("data", [])
            model_ids = [m.get("id", "") for m in models[:5]]
            return jsonify({"ok": True, "model": ", ".join(model_ids), "latency": elapsed})
        elif resp.status_code == 401:
            return jsonify({"ok": False, "error": "API Key 无效（401）"})
        else:
            return jsonify({"ok": False, "error": f"HTTP {resp.status_code}: {resp.text[:100]}"})
    except requests.exceptions.ConnectionError:
        return jsonify({"ok": False, "error": "无法连接到 DeepSeek API，请检查网络"})
    except requests.exceptions.Timeout:
        return jsonify({"ok": False, "error": "请求超时（10s）"})
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)[:100]})

@app.route("/")
def index():
    return render_template("index.html", themes=THEMES)

@app.route("/api/themes")
def api_themes():
    return jsonify({"themes": THEMES})

@app.route("/api")
def api_index():
    return jsonify({
        "name": "WeMD AI API",
        "version": "1.0",
        "endpoints": [
            {"path": "/api", "method": "GET", "desc": "API 信息"},
            {"path": "/api/docs", "method": "GET", "desc": "API 文档"},
            {"path": "/api/themes", "method": "GET", "desc": "获取所有主题"},
            {"path": "/api/generate", "method": "POST", "desc": "生成排版 HTML"},
            {"path": "/api/balance", "method": "POST", "desc": "查询 DeepSeek 余额"},
        ]
    })

@app.route("/api/docs")
def api_docs():
    return jsonify({
        "name": "WeMD AI API",
        "version": "1.0",
        "description": "微信公众号文章 AI 排版引擎",
        "base_url": "http://localhost:5000",
        "authentication": "支持两种传 Key 方式：1) Authorization: Bearer <key>  2) JSON body 中 api_key 字段",
        "endpoints": {
            "GET /api": {
                "desc": "API 信息",
                "response": {"name": "str", "version": "str", "endpoints": "list"}
            },
            "GET /api/themes": {
                "desc": "获取所有内置主题",
                "response": {"themes": "list[dict]"}
            },
            "POST /api/generate": {
                "desc": "将文章排版为公众号兼容 HTML",
                "request": {
                    "article": "string (必填) 文章内容",
                    "theme": "string (可选，默认 editorial) 主题ID，可选值: " + ", ".join([t["id"] for t in THEMES]) + ", auto, custom",
                    "custom_style": "string (可选) 自定义风格描述，仅在 theme=custom 时生效",
                    "model": "string (可选，默认 deepseek-v4-flash) AI 模型: deepseek-v4-flash / deepseek-v4-pro",
                    "api_key": "string (可选) DeepSeek API Key，也可通过 Authorization header 传入"
                },
                "response": {
                    "html": "string 排版后的 HTML 片段",
                    "theme": "string 使用的主题",
                    "tokens": "int 消耗的总 tokens",
                    "prompt_tokens": "int prompt tokens",
                    "completion_tokens": "int completion tokens",
                    "latency": "float 耗时(秒)",
                    "logs": "list 执行日志"
                },
                "example": {
                    "curl": 'curl -X POST http://localhost:5000/api/generate -H "Content-Type: application/json" -H "Authorization: Bearer sk-xxx" -d \'{"article":"你的文章内容...","theme":"editorial"}\'',
                    "python": 'import requests\nresp = requests.post("http://localhost:5000/api/generate", json={"article":"文章","theme":"handmade"}, headers={"Authorization":"Bearer sk-xxx"})\nprint(resp.json()["html"])'
                }
            },
            "POST /api/balance": {
                "desc": "查询 DeepSeek 账户余额",
                "request": {"api_key": "string (可选)"},
                "response": {"data": "dict DeepSeek 余额响应"}
            }
        }
    })

@app.route("/api/generate", methods=["POST"])
def api_generate():
    import time
    logs = []
    t0 = time.time()
    def log(step, msg, level="info"):
        elapsed = time.time() - t0
        logs.append({"step": step, "msg": msg, "level": level, "elapsed": round(elapsed, 3)})
        print(f"[{elapsed:.3f}s] [{level.upper()}] {step}: {msg}")

    data = request.get_json(force=True)
    article = (data.get("article") or "").strip()
    theme_name = data.get("theme") or "editorial"
    custom_style = (data.get("custom_style") or "").strip()
    model_name = (data.get("model") or "").strip() or DEEPSEEK_MODEL

    log("1-request", f"article={len(article)}chars theme={theme_name} model={model_name}{' custom='+custom_style if custom_style else ''}")

    if not article:
        log("1-request", "article is empty", "error")
        return jsonify({"error": "文章内容不能为空", "logs": logs}), 400

    # 始终使用根目录的 公众号HTML排版设计规范.md
    design_spec = load_main_spec()
    if not design_spec:
        log("2-spec", "公众号HTML排版设计规范.md not found", "error")
        return jsonify({"error": "设计规范未找到", "logs": logs}), 404
    log("2-spec", f"loaded spec: {len(design_spec)} chars, {len(design_spec.splitlines())} lines")

    # 附加主题信息
    if custom_style:
        log("3-theme", f"custom: {custom_style}")
    elif theme_name == "auto":
        log("3-theme", "auto: AI will pick style based on article")
    else:
        theme_info = get_theme_info(theme_name)
        log("3-theme", f"theme: {theme_info['name']}")

    # 检查 API Key（支持 Authorization header 或请求体 api_key 字段）
    api_key = require_api_key()
    if not api_key:
        log("4-auth", "no API key configured", "error")
        return jsonify({"error": "未配置 API Key，请在请求头 Authorization: Bearer <key> 中传入", "logs": logs}), 401
    log("4-auth", f"key: {api_key[:8]}...{api_key[-4:]}")

    # 构建 Prompt
    prompt = build_ai_prompt(article, theme_name, design_spec, custom_style)
    log("5-prompt", f"prompt built: {len(prompt)} chars total")

    try:
        log("6-request", f"sending to {model_name} (timeout=120s)")
        resp = requests.post(
            DEEPSEEK_API_URL,
            headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
            json={
                "model": model_name,
                "messages": [
                    {"role": "system", "content": "你是公众号HTML排版专家。只输出HTML片段，不输出任何解释。"},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.3, "max_tokens": 16384,
            },
            timeout=120,
        )
        elapsed = time.time() - t0
        resp.raise_for_status()
        result = resp.json()
        usage = result.get("usage", {})
        log("7-response", f"HTTP {resp.status_code} | model={result.get('model','?')} | tok_in={usage.get('prompt_tokens','?')} tok_out={usage.get('completion_tokens','?')} tok_total={usage.get('total_tokens','?')} | latency={elapsed:.1f}s")

        html = result["choices"][0]["message"]["content"].strip()
        html = re.sub(r'^```html?\s*', '', html)
        html = re.sub(r'\s*```$', '', html)
        log("8-output", f"html cleaned: {len(html)} chars | starts with: {html[:80].strip()}...")

        return jsonify({
            "html": html,
            "theme": theme_name,
            "tokens": usage.get("total_tokens", 0),
            "prompt_tokens": usage.get("prompt_tokens", 0),
            "completion_tokens": usage.get("completion_tokens", 0),
            "latency": round(elapsed, 1),
            "logs": logs,
        })

    except requests.exceptions.Timeout:
        log("7-response", "request timeout (>120s)", "error")
        return jsonify({"error": "AI 生成超时，请重试", "logs": logs}), 504
    except Exception as e:
        log("7-response", f"request failed: {str(e)[:200]}", "error")
        return jsonify({"error": f"AI 生成失败: {str(e)[:200]}", "logs": logs}), 500

# ============================================================
# 启动
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("  WeMD AI 排版引擎服务")
    print("  http://localhost:5000")
    print("=" * 50)
    if not DEEPSEEK_API_KEY:
        print("⚠️  未设置 DEEPSEEK_API_KEY 环境变量")
        print("   AI 生成功能将不可用，但仍可使用参数调整功能")
        print("   设置方法: set DEEPSEEK_API_KEY=your_key")
    app.run(debug=True, host="0.0.0.0", port=5000)
