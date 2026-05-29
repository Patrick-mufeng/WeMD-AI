# WeMD AI API 文档

> 微信公众号文章 AI 排版引擎 — REST API

**版本**: v1.0  
**基础 URL**: `http://localhost:5000`  
**协议**: HTTP/JSON

---

## 目录

- [快速开始](#快速开始)
- [身份认证](#身份认证)
- [API 端点](#api-端点)
  - [GET /api — API 信息](#get-api--api-信息)
  - [GET /api/docs — API 文档](#get-apidocs--api-文档)
  - [GET /api/themes — 获取主题列表](#get-apithemes--获取主题列表)
  - [POST /api/generate — 生成排版](#post-apigenerate--生成排版)
  - [POST /api/balance — 查询余额](#post-apibalance--查询余额)
- [主题说明](#主题说明)
- [错误码](#错误码)
- [示例](#示例)
  - [cURL](#示例-curl)
  - [Python](#示例-python)
  - [JavaScript](#示例-javascript)
  - [Node.js axios](#示例-nodejs-axios)
- [部署与安全](#部署与安全)

---

## 快速开始

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-deepseek-api-key" \
  -d '{"article": "你的文章内容...", "theme": "editorial"}'
```

成功响应：

```json
{
  "html": "<section>...</section>",
  "theme": "editorial",
  "tokens": 2856,
  "prompt_tokens": 1843,
  "completion_tokens": 1013,
  "latency": 12.4,
  "logs": [...]
}
```

返回的 `html` 是公众号兼容的 HTML 片段，可直接粘贴到微信编辑器。

---

## 身份认证

### 方式一：Authorization Header（推荐）

```bash
curl -H "Authorization: Bearer sk-your-deepseek-api-key" ...
```

### 方式二：请求体 api_key 字段

```bash
curl -d '{"api_key": "sk-your-deepseek-api-key", ...}' ...
```

### 方式三：环境变量

启动服务时设置 `DEEPSEEK_API_KEY` 环境变量：

```bash
set DEEPSEEK_API_KEY=sk-your-key
python server.py
```

优先级：Authorization Header > 请求体 > 环境变量

### 网关鉴权（可选）

设置 `WEMD_API_KEY` 环境变量后，所有 `/api/*` 请求必须经过网关校验：

```bash
set WEMD_API_KEY=my-gateway-key
```

请求时必须带：

```bash
curl -H "Authorization: Bearer my-gateway-key" ...
```

> 注意：网关 Key 和 DeepSeek Key 是独立的。网关 Key 控制 API 访问权限，DeepSeek Key 用于调用 AI 模型。

---

## API 端点

### GET /api — API 信息

返回 API 基本信息和支持的端点列表。

**请求示例：**

```bash
curl http://localhost:5000/api
```

**响应：**

```json
{
  "name": "WeMD AI API",
  "version": "1.0",
  "endpoints": [
    {"path": "/api", "method": "GET", "desc": "API 信息"},
    {"path": "/api/docs", "method": "GET", "desc": "API 文档"},
    {"path": "/api/themes", "method": "GET", "desc": "获取所有主题"},
    {"path": "/api/generate", "method": "POST", "desc": "生成排版 HTML"},
    {"path": "/api/balance", "method": "POST", "desc": "查询 DeepSeek 余额"}
  ]
}
```

---

### GET /api/docs — API 文档

返回完整的 API 文档（JSON 格式），包含每个端点的请求参数和响应结构。

**请求示例：**

```bash
curl http://localhost:5000/api/docs
```

---

### GET /api/themes — 获取主题列表

返回所有内置排版主题。

**请求示例：**

```bash
curl http://localhost:5000/api/themes
```

**响应：**

```json
{
  "themes": [
    {
      "id": "handmade",
      "name": "🌸 可爱手帐",
      "primary": "#f48fb1",
      "accent": "#f06292",
      "surface": "#fce4ec",
      "ink": "#4a3030"
    },
    {
      "id": "stripe",
      "name": "💳 Stripe 金融",
      "primary": "#635bff",
      "accent": "#00d4aa",
      "surface": "#f8f9ff",
      "ink": "#1a1a2e"
    }
  ]
}
```

每个主题包含 4 个色值：

| 字段 | 说明 |
|------|------|
| `primary` | 主色 — 按钮、重点标记、活跃状态 |
| `accent` | 强调色 — 加粗文字、引用、编号 |
| `surface` | 背景色 — 文章底色 |
| `ink` | 文字色 — 正文颜色 |

---

### POST /api/generate — 生成排版

核心接口。将文章内容排版为微信公众号兼容的 HTML。

#### 请求参数

| 参数 | 类型 | 必填 | 默认值 | 说明 |
|------|------|------|--------|------|
| `article` | string | **是** | — | 文章内容（支持 Markdown 格式） |
| `theme` | string | 否 | `editorial` | 主题 ID，可选值见下方 |
| `custom_style` | string | 否 | `""` | 自定义风格描述，仅在 `theme=custom` 时生效 |
| `model` | string | 否 | `deepseek-v4-flash` | AI 模型：`deepseek-v4-flash`（快速经济）或 `deepseek-v4-pro`（更强能力） |
| `api_key` | string | 否 | — | DeepSeek API Key（也可通过 Header 传入） |

#### theme 可选值

| 值 | 主题 | 风格 |
|----|------|------|
| `handmade` | 🌸 可爱手帐 | 粉色系，温暖柔和 |
| `stripe` | 💳 Stripe 金融 | 科技蓝紫，专业 |
| `vercel` | ⬛ Vercel 极客 | 黑白极简，现代 |
| `apple` | 🍎 Apple 极简 | 灰色调，精致 |
| `ink` | 🖌 新中式水墨 | 棕褐色系，传统 |
| `cyber` | 💜 赛博霓虹 | 暗色霓虹，酷炫 |
| `wabi` | 🍃 日系侘寂 | 大地色，自然 |
| `editorial` | 📰 报刊社论 | 米白底，经典 |
| `mono` | ⬜ 极简黑白 | 纯黑白，干净 |
| `auto` | 🤖 自动识别 | AI 根据文章内容自主选择风格 |
| `custom` | ✏️ 自定义 | 通过 `custom_style` 描述想要的风格 |

#### 请求示例

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "article": "# 标题\n\n正文内容...",
    "theme": "cyber",
    "custom_style": ""
  }'
```

#### 成功响应

```json
{
  "html": "<section style=\"width:100%;max-width:677px;...\">...</section>",
  "theme": "cyber",
  "tokens": 2856,
  "prompt_tokens": 1843,
  "completion_tokens": 1013,
  "latency": 12.4,
  "logs": [
    {"step": "1-prepare", "msg": "article=342chars theme=cyber", "level": "info", "elapsed": 0.0},
    {"step": "2-request", "msg": "sending to DeepSeek API...", "level": "info", "elapsed": 0.1},
    {"step": "3-response", "msg": "HTTP 200 | tokens=2856 latency=12.4s", "level": "info", "elapsed": 12.4}
  ]
}
```

| 响应字段 | 类型 | 说明 |
|---------|------|------|
| `html` | string | 排版后的 HTML 片段 |
| `theme` | string | 实际使用的主题 ID |
| `tokens` | int | 总 token 消耗数 |
| `prompt_tokens` | int | 请求（prompt）token 数 |
| `completion_tokens` | int | 生成（completion）token 数 |
| `latency` | float | 总耗时（秒） |
| `logs` | array | 执行日志（调试用） |

#### 输出 HTML 规范

生成的 HTML 遵循以下规则：

- **标签**：仅使用 `<section>`、`<p>`、`<span>`、`<strong>`、`<em>`、`<br>`、`<img>`
- **样式**：100% 内联 `style=""`，无 `<style>` 标签
- **布局**：使用 `display:flex`，无 `<div>` 或 `<table>`
- **容器**：背景为 `transparent`，卡片使用 `rgba` 半透明
- **头部卡片**：自动生成文章字数、阅读时间、标签、概览
- **尾部卡片**：自动生成点赞/在看/转发互动引导
- **暗黑模式**：通过透明底色自动兼容

#### 错误响应

```json
{
  "error": "文章内容不能为空",
  "logs": [...]
}
```

可能的错误：

| HTTP 状态码 | 说明 |
|------------|------|
| 400 | 参数错误（文章为空） |
| 401 | API Key 未配置或无效 |
| 404 | 设计规范文件缺失 |
| 500 | 服务器内部错误 |
| 504 | AI 生成超时（>120 秒） |

---

### POST /api/balance — 查询余额

查询 DeepSeek 账户余额。

**请求：**

```bash
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx"
```

**响应：**

```json
{
  "data": {
    "balance_infos": [{"total_balance": "5.00", "currency": "CNY"}]
  }
}
```

---

## 错误码

| 状态码 | 含义 | 处理方式 |
|--------|------|---------|
| 200 | 成功 | 正常解析响应 |
| 400 | 请求参数错误 | 检查 `article` 是否为空 |
| 401 | API Key 无效或未提供 | 检查 Key 配置 |
| 404 | 资源不存在 | 检查设计规范文件是否存在 |
| 500 | 服务端错误 | 查看服务器日志 |
| 504 | AI 生成超时 | 重试或缩短文章长度 |

---

## 示例

### 示例 cURL

**基础用法：**

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{"article": "## AI 时代\n\n人工智能正在改变世界。", "theme": "cyber"}'
```

**自定义风格：**

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{
    "article": "你的文章...",
    "theme": "custom",
    "custom_style": "赛博朋克故障风，霓虹紫色调，未来感"
  }'
```

**自动识别风格：**

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-xxx" \
  -d '{"article": "...", "theme": "auto"}'
```

---

### 示例 Python

```python
import requests

API_URL = "http://localhost:5000/api/generate"
DEEPSEEK_KEY = "sk-your-key"

resp = requests.post(API_URL, json={
    "article": "# 标题\n\n正文内容...",
    "theme": "editorial"
}, headers={
    "Authorization": f"Bearer {DEEPSEEK_KEY}"
})

if resp.status_code == 200:
    data = resp.json()
    html = data["html"]
    print(f"✅ 生成成功: {data['tokens']} tokens, {data['latency']}s")
    # 保存 HTML 文件
    with open("output.html", "w", encoding="utf-8") as f:
        f.write(html)
else:
    print(f"❌ 失败: {resp.json().get('error')}")
```

**批量处理：**

```python
import requests, time

articles = [
    {"file": "article1.md", "theme": "handmade"},
    {"file": "article2.md", "theme": "cyber"},
]

for item in articles:
    with open(item["file"], "r", encoding="utf-8") as f:
        article = f.read()

    resp = requests.post("http://localhost:5000/api/generate", json={
        "article": article,
        "theme": item["theme"]
    }, headers={"Authorization": "Bearer sk-xxx"})

    if resp.status_code == 200:
        data = resp.json()
        name = item["file"].replace(".md", ".html")
        with open(name, "w", encoding="utf-8") as f:
            f.write(data["html"])
        print(f"✅ {name} — {data['tokens']} tokens, {data['latency']}s")
    else:
        print(f"❌ {item['file']} — {resp.json().get('error')}")

    time.sleep(1)  # 避免频率限制
```

---

### 示例 JavaScript

```javascript
// 浏览器 fetch
async function generateWechatHTML(article, theme = "editorial") {
  const resp = await fetch("http://localhost:5000/api/generate", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "Authorization": "Bearer sk-xxx"
    },
    body: JSON.stringify({ article, theme })
  });

  if (!resp.ok) {
    const err = await resp.json();
    throw new Error(err.error);
  }

  return await resp.json();
}

// 使用
generateWechatHTML("## 标题\n\n正文...", "cyber")
  .then(data => console.log(data.html))
  .catch(err => console.error(err));
```

---

### 示例 Node.js axios

```javascript
const axios = require("axios");

async function generate(article, theme = "editorial") {
  const { data } = await axios.post("http://localhost:5000/api/generate", {
    article,
    theme
  }, {
    headers: { Authorization: "Bearer sk-xxx" },
    timeout: 120000  // AI 生成可能较慢
  });

  console.log(`✅ ${data.tokens} tokens, ${data.latency}s`);
  return data.html;
}

generate("## AI 时代\n\n正文...", "cyber").then(html => {
  console.log(html.slice(0, 200));
});
```

---

## 部署与安全

### 启动服务

```bash
# 基本启动
python server.py

# 设置 DeepSeek Key（AI 生成必需）
set DEEPSEEK_API_KEY=sk-your-key
python server.py

# 设置网关 Key（保护 API 访问）
set WEMD_API_KEY=my-secret-gateway-key
python server.py
```

### 生产部署建议

```bash
# 使用 gunicorn 部署（Linux/Mac）
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 server:app

# 使用 waitress 部署（Windows）
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 server:app

# 建议通过 Nginx 反向代理添加 HTTPS
```

### 安全建议

1. **生产环境务必设置 `WEMD_API_KEY`**，防止 API 被未授权访问
2. **使用 HTTPS** 保护 API Key 传输
3. **限制请求频率**（可通过 Nginx `limit_req` 或自行添加）
4. **不要在客户端代码中暴露 DeepSeek API Key**
