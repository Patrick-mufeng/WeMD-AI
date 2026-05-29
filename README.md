# 🎨 WeMD AI — 微信公众号 AI 排版引擎

> 把 Markdown 文章一键排版为公众号兼容的 HTML，让 DeepSeek 做你的专属排版设计师。

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0+-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)

---

## 📖 简介

**WeMD AI** 是一个基于 Flask 的后端服务 + Web 前端，通过 DeepSeek API 的 AI 能力，将你的 Markdown 文章自动排版为**微信公众号兼容的 HTML 片段**——可直接粘贴到微信编辑器，样式完整保留，完美适配暗黑模式。

它解决了公众号创作者最头疼的问题：给文章做排版。不再需要 135 编辑器/秀米一个个拖组件，AI 会根据你的文章内容自动设计版面、选择配色、生成头部信息卡和尾部互动引导。

---

## ✨ 功能特性

| 功能 | 说明 |
|------|------|
| 🤖 **AI 智能排版** | 调用 DeepSeek API，根据文章调性自动生成排版 HTML |
| 🎨 **9 套内置主题** | 可爱手帐 / Stripe 金融 / Vercel 极客 / Apple 极简 / 新中式水墨 / 赛博霓虹 / 日系侘寂 / 报刊社论 / 极简黑白 |
| 🔄 **auto 自动模式** | 不指定主题时，AI 会根据文章内容自主选定视觉风格 |
| ✏️ **custom 自定义风格** | 用自然语言描述你想要的风格，例如「赛博朋克故障风，霓虹紫色调」 |
| 🧩 **丰富组件** | AI 自动生成：头部信息卡（字数/阅读时间/标签/概览）、金句引用、数据展示、步骤流、分割线、CTA 按钮、尾部互动卡（点赞/在看/转发） |
| 🌙 **暗黑模式兼容** | 容器背景透明 + 卡片 rgba 半透明，微信自动处理暗黑模式切换 |
| 🔌 **完整 REST API** | `/api/generate` 生成排版、`/api/balance` 查询余额、`/api/themes` 主题列表、`/api/docs` 接口文档 |
| 🌐 **CORS 跨域** | API 开箱即用，浏览器 fetch / axios 可直接调用 |
| 🔑 **灵活鉴权** | 支持 Authorization Header / JSON body / 环境变量三种传 Key 方式 + 网关 Key 二次保护 |
| 🖥️ **Web 前端** | 玻璃拟态 UI，在线编辑文章、选择主题、实时预览生成的 HTML |
| 📐 **严格规范** | 设计规范基于 135 编辑器/秀米真实公众号文章源码逆向，确保生成的 HTML 完整可用 |

---

## 🚀 快速开始

### 环境要求

- Python 3.10+
- DeepSeek API Key（[注册获取](https://platform.deepseek.com/)）

### 安装

```bash
# 克隆项目
git clone https://github.com/Patrick-mufeng/WeMD-AI.git
cd WeMD-AI

# 安装依赖
pip install -r requirements.txt
```

### 启动

```bash
# Windows
set DEEPSEEK_API_KEY=sk-your-deepseek-api-key
python server.py

# Linux / macOS
export DEEPSEEK_API_KEY=sk-your-deepseek-api-key
python server.py
```

打开浏览器访问 **http://localhost:5000** 即可使用 Web 前端。

也可以使用 `start.bat`（Windows）或 `start.sh`（Linux/Mac）一键启动。

### 🚀 无需安装 Python（开箱即用）

> 项目已内置 **Python 3.10 + Flask + requests**（`python/` 目录），clone 后无需任何配置。

```bash
# 直接启动（Windows）
set DEEPSEEK_API_KEY=sk-your-key
portable\start_portable.bat

# 直接启动（Linux / macOS）
export DEEPSEEK_API_KEY=sk-your-key
bash portable/start_portable.sh
```

> 💡 如果 `python/` 目录丢失或需要更新，运行 `portable/setup_portable.bat`（Windows）或 `portable/setup_portable.sh`（Linux/Mac）即可重新下载。

---

## 🔌 API 调用

### 生成排版（核心接口）

```bash
curl -X POST http://localhost:5000/api/generate \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-deepseek-api-key" \
  -d '{
    "article": "## AI 时代\n\n人工智能正在改变世界...",
    "theme": "cyber"
  }'
```

**返回示例：**

```json
{
  "html": "<section style=\"...\">...</section>",
  "theme": "cyber",
  "tokens": 2856,
  "prompt_tokens": 1843,
  "completion_tokens": 1013,
  "latency": 12.4,
  "logs": [...]
}
```

### 主题列表

```bash
curl http://localhost:5000/api/themes
```

### 查询 DeepSeek 余额

```bash
curl -X POST http://localhost:5000/api/balance \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-your-deepseek-api-key"
```

> 完整 API 文档见 [`docs/API.md`](./docs/API.md)，包含 Python / JavaScript / Node.js 多语言示例。

---

## 🎨 主题一览

| ID | 名称 | 主色 | 风格 |
|----|------|------|------|
| `handmade` | 🌸 可爱手帐 | `#f48fb1` | 粉色系，温暖柔和 |
| `stripe` | 💳 Stripe 金融 | `#635bff` | 科技蓝紫，专业感 |
| `vercel` | ⬛ Vercel 极客 | `#000000` | 黑白极简，现代 |
| `apple` | 🍎 Apple 极简 | `#555555` | 灰色调，精致 |
| `ink` | 🖌 新中式水墨 | `#5c4a3a` | 棕褐色系，传统 |
| `cyber` | 💜 赛博霓虹 | `#c77dff` | 暗色霓虹，酷炫 |
| `wabi` | 🍃 日系侘寂 | `#8b7355` | 大地色，自然 |
| `editorial` | 📰 报刊社论 | `#b8860b` | 米白底，经典（默认） |
| `mono` | ⬜ 极简黑白 | `#333333` | 纯黑白，干净 |
| `auto` | 🤖 自动识别 | — | AI 根据文章内容自选 |
| `custom` | ✏️ 自定义 | — | 通过 `custom_style` 描述风格 |

---

## 📁 项目结构

```
WeMD-AI/
├── server.py                          # Flask API 主服务
├── requirements.txt                   # Python 依赖
├── start.bat                          # Windows 一键启动
├── start.sh                           # Linux/Mac 一键启动
│
├── python/                            # 嵌入式 Python 3.10 + 依赖（开箱即用）
├── portable/                          # 便携方案脚本
│   ├── setup_portable.bat             #   Windows 重新下载/配置
│   ├── setup_portable.sh              #   Linux/Mac 重新下载/配置
│   ├── start_portable.bat             #   Windows 便携启动 ← 推荐
│   └── start_portable.sh              #   Linux/Mac 便携启动 ← 推荐
│
├── templates/
│   └── index.html                     # Web 前端（玻璃拟态 UI）
│
├── docs/
│   ├── API.md                         # API 完整文档
│   └── 公众号HTML排版设计规范.md        # 公众号 HTML 设计规范
│
├── articles/                          # 示例/测试文章
│   ├── 文案.md
│   ├── markdown格式.md
│   └── 2026-05-25_khazix_API中转站行业揭秘.md
│
└── reference/                         # 真实公众号 HTML 源码（规范逆向参考）
    ├── 公众号支持的源码.html
    ├── 公众号支持的源码2.html
    ├── ...
    └── 公众号支持的源码8.html
```

---

## ⚙️ 鉴权配置

项目支持三层 Key 传递（优先级从高到低）：

| 层级 | 方式 | 说明 |
|------|------|------|
| 1 | `Authorization: Bearer <key>` | HTTP Header 传入（推荐） |
| 2 | `{ "api_key": "<key>" }` | JSON 请求体传入 |
| 3 | `DEEPSEEK_API_KEY` 环境变量 | 服务启动时设置 |

### 网关保护（可选）

设置 `WEMD_API_KEY` 环境变量后，所有 `/api/*` 请求必须额外携带此 Key，适用于对外部署：

```bash
export WEMD_API_KEY=my-gateway-secret
# 请求时必须带: Authorization: Bearer my-gateway-secret
```

---

## 🖥️ Web 前端

内置于 `templates/index.html`，特性：

- 🪟 **玻璃拟态 UI** — 毛玻璃面板 + 动态渐变背景
- ✨ **鼠标流光** — 跟随鼠标的渐变光晕
- 🎨 **主题选择器** — 下拉切换 9 套内置主题
- 📝 **Markdown 编辑器** — 左侧编辑、右侧预览
- ⚡ **实时生成** — 点击按钮，AI 排版结果渲染在预览区
- 📋 **一键复制** — 复制生成的 HTML 到剪贴板

---

## 📐 设计规范

本项目的设计规范文件 [`docs/公众号HTML排版设计规范.md`](./docs/公众号HTML排版设计规范.md) 基于对 **8 篇 135 编辑器/秀米产出的真实公众号文章源码** 的逆向分析，定义了：

- ✅ 允许的 HTML 标签（仅 `<section>` / `<p>` / `<span>` / `<strong>` / `<em>` / `<img>`）
- ✅ 完整的 CSS 属性白名单（布局、盒模型、文字、背景、边框、阴影、Transform）
- ❌ 禁止的标签和 CSS（`<div>` / `<style>` / `position:absolute` / `animation` / `calc()` 等）
- 🧩 15 个经过验证的组件配方（头部卡、章节标题、正文、引用、数据展示、步骤流、CTA、分割线等）

---

## 🔒 安全建议

1. **生产环境务必设置 `WEMD_API_KEY`**，防止 API 被未授权调用
2. **使用 HTTPS 反向代理**（Nginx / Caddy），保护 API Key 传输
3. **限制请求频率**（Nginx `limit_req` 或中间件）
4. **不要在客户端代码中暴露 DeepSeek API Key**
5. **推荐使用 gunicorn / waitress** 替代 Flask 内置服务器

---

## 🚢 生产部署

```bash
# Linux/Mac — gunicorn
pip install gunicorn
gunicorn -w 2 -b 0.0.0.0:5000 server:app

# Windows — waitress
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 server:app

# 建议前面加一层 Nginx 反向代理 + Let's Encrypt HTTPS
```

---

## 📄 依赖

| 包 | 版本 | 用途 |
|----|------|------|
| Flask | ≥3.0 | Web 框架 + 模板渲染 |
| requests | ≥2.31 | DeepSeek API HTTP 调用 |

---

## 📝 License

MIT © [Patrick-mufeng](https://github.com/Patrick-mufeng)

---

## 🙏 致谢

- [DeepSeek](https://platform.deepseek.com/) — 提供 AI 排版能力
- 135 编辑器 / 秀米 — 公众号排版实践参考
