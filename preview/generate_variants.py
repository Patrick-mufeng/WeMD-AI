#!/usr/bin/env python3
"""Generate preview/all-variants.html — 10 variants per component."""
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Theme colors
P = "#171717"  # primary
A = "#888888"  # accent
S = "#fafafa"  # surface
I = "#171717"  # ink
M = "#aaaaaa"  # mute

def sec(style, inner=""):
    return f'<section style="{style};box-sizing:border-box;max-width:100%!important;">{inner}</section>'

def p(style, text):
    return f'<p style="{style};box-sizing:border-box;max-width:100%!important;">{text}</p>'

def label(n, name):
    return p(f"font-size:8px;color:{M};margin:0 0 4px;text-transform:uppercase;letter-spacing:1px", f"V{n} · {name}")

def variant(n, name, html):
    return f'<section style="margin:12px 0;padding:6px 0;box-sizing:border-box;max-width:100%!important;">{label(n, name)}{html}</section>'

def section_header(num, title):
    return f"""
<section style="margin:36px 0 8px;display:flex;align-items:flex-start;gap:8px;box-sizing:border-box;">
  <section style="width:3px;height:18px;background:{P};flex-shrink:0;box-sizing:border-box;"></section>
  <section style="flex:1;box-sizing:border-box;">
    <p style="font-size:10px;font-weight:bold;color:{A};letter-spacing:2px;margin:0 0 2px;">{num}</p>
    <p style="font-size:16px;font-weight:bold;color:{P};margin:0;">{title}</p>
  </section>
</section>"""

parts = []
def add_section(num, title, variants_html):
    parts.append(section_header(num, title) + variants_html)

# ════════════════════════════════════════════════════════════
# 5.1 文章头部
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "标准居中", sec("text-align:center;padding:20px 0",
    sec("display:inline-block;padding:2px 10px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;letter-spacing:1.5px", "标签") +
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:8px 0 0","大标题文字") +
    p("font-size:10px;color:"+A+";margin:4px 0 0","副标题或日期")
)))
v.append(variant(2, "左对齐", sec("text-align:left;padding:20px 0",
    sec("display:inline-block;padding:2px 8px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;letter-spacing:1px", "TOPIC") +
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:10px 0 0","标题左对齐，更有力度") +
    p("font-size:10px;color:"+A+";margin:6px 0 0","副标题信息")
)))
v.append(variant(3, "标签在下方", sec("text-align:center;padding:20px 0",
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:0","先声夺人的标题") +
    sec("display:inline-block;padding:2px 10px;background:rgba(0,0,0,0.05);color:"+A+";font-size:8px;font-weight:bold;letter-spacing:1px;margin-top:8px", "标签 · 分类")
)))
v.append(variant(4, "双行标签", sec("text-align:center;padding:20px 0",
    sec("display:flex;flex-flow:row;justify-content:center;gap:6px;margin-bottom:10px",
        sec("display:inline-block;padding:2px 8px;background:"+P+";color:#fff;font-size:7px;font-weight:bold;letter-spacing:1px", "标签A") +
        sec("display:inline-block;padding:2px 8px;background:rgba(0,0,0,0.05);color:"+A+";font-size:7px;letter-spacing:1px", "标签B")
    ) +
    p("font-size:20px;font-weight:bold;color:"+I+";line-height:1.4;margin:0","带多个标签的标题样式")
)))
v.append(variant(5, "竖排装饰线", sec("text-align:center;padding:20px 0",
    sec("width:1px;height:20px;background:"+P+";margin:0 auto 8px;display:block") +
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:0","装饰线引导视觉聚焦") +
    sec("width:1px;height:20px;background:"+P+";margin:8px auto 0;display:block")
)))
v.append(variant(6, "数字编号式", sec("text-align:left;padding:20px 0",
    p("font-size:36px;font-weight:bold;color:"+P+";line-height:1;margin:0;opacity:0.15","01") +
    p("font-size:18px;font-weight:bold;color:"+I+";line-height:1.3;margin:-12px 0 0","编号叠加标题") +
    p("font-size:10px;color:"+A+";margin:4px 0 0","副标题信息")
)))
v.append(variant(7, "英文大写标签", sec("text-align:left;padding:20px 0",
    sec("display:inline-block;padding:2px 0;border-bottom:2px solid "+P+";font-size:8px;font-weight:bold;letter-spacing:2px;color:"+P, "FEATURE") +
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:12px 0 0","下划线标签 + 标题") +
    p("font-size:10px;color:"+A+";margin:6px 0 0","描述文字")
)))
v.append(variant(8, "圆点装饰", sec("text-align:center;padding:20px 0",
    sec("width:6px;height:6px;border-radius:50%;background:"+P+";margin:0 auto 10px;display:block") +
    p("font-size:20px;font-weight:bold;color:"+I+";line-height:1.4;margin:0","圆点极简引导标题") +
    p("font-size:10px;color:"+A+";margin:4px 0 0","副标题或日期信息")
)))
v.append(variant(9, "英文 + 中文双层", sec("text-align:center;padding:20px 0",
    p("font-size:9px;font-weight:bold;color:"+A+";letter-spacing:3px;margin:0;text-transform:uppercase","DESIGN SYSTEM") +
    p("font-size:22px;font-weight:bold;color:"+I+";line-height:1.3;margin:6px 0 0","设计系统标题") +
    p("font-size:10px;color:"+A+";margin:4px 0 0","中英文搭配更国际范")
)))
v.append(variant(10, "无标签纯标题", sec("text-align:left;padding:20px 0",
    p("font-size:24px;font-weight:bold;color:"+I+";line-height:1.35;margin:0","一句话就能说清楚的文章标题") +
    p("font-size:10px;color:"+A+";margin:8px 0 0","作者 / 日期")
)))
add_section("5.1", "文章头部", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.2 章节标题
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "左边框 + 编号", sec("display:flex;align-items:flex-start;gap:8px",
    sec("width:3px;height:18px;background:"+P+";flex-shrink:0") +
    sec("flex:1",
        p("font-size:9px;font-weight:bold;color:"+A+";letter-spacing:2px;margin:0 0 2px","SECTION 01") +
        p("font-size:16px;font-weight:bold;color:"+I+";margin:0","章节标题")
    ))))
v.append(variant(2, "纯编号 + 标题", sec("",
    p("font-size:28px;font-weight:bold;color:rgba(0,0,0,0.08);line-height:1;margin:0","02") +
    p("font-size:16px;font-weight:bold;color:"+I+";margin:-8px 0 0","大号透明编号叠加标题")
)))
v.append(variant(3, "英文标签", sec("",
    p("font-size:9px;font-weight:bold;color:"+A+";letter-spacing:3px;margin:0 0 4px;text-transform:uppercase","overview") +
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0","英文小标 + 中文标题")
)))
v.append(variant(4, "双色装饰条", sec("display:flex;align-items:center;gap:8px",
    sec("width:3px;height:16px;background:"+P) +
    sec("width:12px;height:3px;background:"+A) +
    p("font-size:15px;font-weight:bold;color:"+I+";margin:0","双色装饰标题")
)))
v.append(variant(5, "左侧圆点", sec("display:flex;align-items:center;gap:8px",
    sec("width:8px;height:8px;border-radius:50%;background:"+P+";flex-shrink:0") +
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0","圆点引导标题")
)))
v.append(variant(6, "方括号编号", sec("display:flex;align-items:baseline;gap:8px",
    p("font-size:13px;font-weight:bold;color:"+P+";margin:0;letter-spacing:1px","[ 03 ]") +
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0","方括号编号标题")
)))
v.append(variant(7, "竖排编号条", sec("display:flex;align-items:stretch;gap:10px",
    sec("width:20px;background:"+P+";display:flex;align-items:center;justify-content:center;flex-shrink:0",
        p("font-size:9px;color:#fff;font-weight:bold;margin:0;letter-spacing:2px;writing-mode:vertical-lr","PART") ) +
    sec("flex:1", p("font-size:16px;font-weight:bold;color:"+I+";margin:0","竖排色块标题"))
)))
v.append(variant(8, "下划线式", sec("",
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0 0 6px","下划线标题") +
    sec("width:30px;height:2px;background:"+P)
)))
v.append(variant(9, "标签 + 标题", sec("",
    sec("display:inline-block;padding:2px 8px;background:"+P+";color:#fff;font-size:7px;font-weight:bold;letter-spacing:1.5px;margin-bottom:6px","NEW") +
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0","标签前缀标题")
)))
v.append(variant(10, "两段式带说明", sec("",
    p("font-size:16px;font-weight:bold;color:"+I+";margin:0","章节主标题") +
    p("font-size:11px;color:"+A+";margin:4px 0 0;line-height:1.6","一句话说明此章节将讨论什么内容")
)))
add_section("5.2", "章节标题", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.3 正文段落
# ════════════════════════════════════════════════════════════
base = "font-size:14px;color:#333;line-height:1.85;letter-spacing:0.3px"
v = []
v.append(variant(1, "标准正文（两端对齐）", p(f"{base};text-align:justify;margin:8px 0", "这是标准正文段落。使用两端对齐、14px 字号、1.85 行高、0.3px 字间距，是公众号阅读体验的基准设置。")))
v.append(variant(2, "左对齐（不强制两端）", p(f"{base};text-align:left;margin:8px 0", "左对齐的自然段落。适合短句或对话型内容，右侧不强制对齐，阅读节奏更轻松自然。")))
v.append(variant(3, "小号注释", p(f"font-size:12px;color:{A};line-height:1.7;margin:4px 0", "这是注释或辅助说明文字，12px 灰色，适合脚注、来源说明、版权信息等。")))
v.append(variant(4, "加粗强调段", p(f"{base};font-weight:bold;color:{I};text-align:justify;margin:8px 0", "整段加粗用于强调核心观点。适合放在关键结论之前，制造停顿和期待感。")))
v.append(variant(5, "高行距呼吸段", p(f"{base};line-height:2.2;text-align:justify;margin:12px 0", "高行距段落让文字有呼吸感。适合情感类、散文类、需要读者慢下来细品的内容。")))
v.append(variant(6, "缩进引用段", p(f"{base};text-align:left;margin:8px 0;padding-left:12px;border-left:2px solid #ddd;color:#555", "左侧缩进 + 淡色竖线的段落。制造一种被引用的感觉，但不是正式的金句组件。")))
v.append(variant(7, "居中短句", p(f"font-size:16px;color:{I};line-height:1.6;text-align:center;margin:12px 0;letter-spacing:1px", "短句居中。无需装饰，留白即是力量。")))
v.append(variant(8, "胶囊首句", p(f"{base};text-align:justify;margin:8px 0",
    "<span style=\"display:inline-block;background:"+P+";color:#fff;font-size:8px;font-weight:bold;padding:1px 6px;margin-right:6px;letter-spacing:1px;vertical-align:middle\">要点</span>" +
    "段落开头用胶囊标签引导。适合教程/干货类文章，快速标识段落主题。")))
v.append(variant(9, "提问式开头", p(f"font-size:16px;font-weight:bold;color:{I};line-height:1.6;margin:12px 0", "你有没有遇到过这样的情况？👇") +
    p(f"{base};text-align:justify;margin:4px 0", "用一个问题开头，然后展开回答。这是公众号最经典的内容钩子模式。")))
v.append(variant(10, "列表式段落", p(f"font-size:12px;color:{I};line-height:2;margin:6px 0",
    "<strong>· </strong>第一项说明内容<br/>" +
    "<strong>· </strong>第二项说明内容<br/>" +
    "<strong>· </strong>第三项说明内容")))
add_section("5.3", "正文段落", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.4 强调卡片
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "左边框 + 标签", sec("margin:12px 0;padding:12px 14px;background:linear-gradient(135deg,#f8f8f8,#f4f4f4);border-left:4px solid "+P,
    sec("display:inline-block;padding:2px 8px;background:"+P+";color:#fff;font-size:7px;font-weight:bold;letter-spacing:1px;margin-bottom:6px","重点") +
    p("font-size:14px;font-weight:bold;color:"+I+";margin:4px 0","核心结论") +
    p("font-size:12px;color:#555;line-height:1.7;margin:4px 0 0","此处为详细说明文字。")
)))
v.append(variant(2, "顶部色条", sec("margin:12px 0;border-radius:6px;overflow:hidden;border:1px solid #eee",
    sec("height:3px;background:"+P) +
    sec("padding:10px 14px", p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","顶部色条卡片") + p("font-size:12px;color:#555;line-height:1.7;margin:0","这种风格更现代简洁。"))
)))
v.append(variant(3, "纯色底 + 白字", sec("margin:12px 0;padding:14px 16px;background:"+P+";border-radius:6px",
    p("font-size:14px;font-weight:bold;color:#fff;margin:0 0 4px","纯色反转卡片") +
    p("font-size:12px;color:rgba(255,255,255,0.75);line-height:1.7;margin:0","适合需要强烈对比的强调内容。")
)))
v.append(variant(4, "双色渐变底", sec("margin:12px 0;padding:14px 16px;background:linear-gradient(135deg,#f5f5f5,#eee);border-radius:6px",
    p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","双色渐变底卡片") +
    p("font-size:12px;color:#555;line-height:1.7;margin:0","柔和的渐变背景。")
)))
v.append(variant(5, "图标 + 标题", sec("margin:12px 0;padding:12px 14px;background:#f8f8f8;border-radius:6px;display:flex;align-items:flex-start;gap:10px",
    sec("font-size:28px;line-height:1;flex-shrink:0","💡") +
    sec("flex:1",
        p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","提示卡片") +
        p("font-size:12px;color:#555;line-height:1.7;margin:0","带 emoji 图标的强调卡片。")
    ))))
v.append(variant(6, "虚线边框", sec("margin:12px 0;padding:12px 14px;border:1px dashed #ccc;border-radius:6px",
    p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","虚线边框卡片") +
    p("font-size:12px;color:#555;line-height:1.7;margin:0","虚线制造轻量感，适合温和提示。")
)))
v.append(variant(7, "右下角标签", sec("margin:12px 0;padding:14px 16px;background:#f8f8f8;border-radius:6px;position:static",
    p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","结论先行卡片") +
    p("font-size:12px;color:#555;line-height:1.7;margin:0","说明文字补充细节。") +
    sec("text-align:right;margin-top:8px", sec("display:inline-block;padding:2px 8px;background:rgba(0,0,0,0.05);color:"+A+";font-size:7px;font-weight:bold;letter-spacing:1px","CONCLUSION"))
)))
v.append(variant(8, "左侧双竖线", sec("margin:12px 0;padding:8px 14px;border-left:2px solid "+P+";border-left-style:double",
    p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","双竖线强调") +
    p("font-size:12px;color:#555;line-height:1.7;margin:0","double border 制造独特视觉效果。")
)))
v.append(variant(9, "黑底白字标签顶", sec("margin:12px 0;border-radius:6px;overflow:hidden;border:1px solid #eee",
    sec("padding:5px 14px;background:"+P, p("font-size:8px;color:#fff;font-weight:bold;margin:0;letter-spacing:1.5px","IMPORTANT")) +
    sec("padding:10px 14px",
        p("font-size:14px;font-weight:bold;color:"+I+";margin:0 0 4px","黑条标签卡片") +
        p("font-size:12px;color:#555;line-height:1.7;margin:0","顶部深色标签条 + 下方内容。")
    ))))
v.append(variant(10, "圆角大卡片", sec("margin:12px 0;padding:18px 16px;background:linear-gradient(135deg,#fafafa,#f0f0f0);border-radius:12px",
    p("font-size:15px;font-weight:bold;color:"+I+";margin:0 0 6px;text-align:center","🌟 圆角大卡片") +
    p("font-size:13px;color:#555;line-height:1.8;text-align:center;margin:0","更大的圆角和内边距，适合作为段落之间的过渡块。")))
add_section("5.4", "强调卡片", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.5 引用/金句
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "左侧竖线（经典）", sec("margin:12px 0;padding:4px 0 4px 12px;border-left:3px solid "+P,
    p("font-size:15px;font-weight:bold;color:"+I+";line-height:1.85;letter-spacing:0.5px;margin:0","少即是多。最经典的 editorial 引文。")))
v.append(variant(2, "大引号装饰", sec("margin:12px 0",
    p("font-size:36px;color:"+P+";line-height:0.6;margin:0 0 -8px","\"") +
    p("font-size:14px;color:#333;line-height:1.85;letter-spacing:0.5px;margin:0;padding-left:8px","好的文字自己会呼吸。")))
v.append(variant(3, "渐变底色条", sec("margin:12px 0;padding:10px 14px;background:linear-gradient(90deg,rgba(0,0,0,0.04),transparent);border-radius:4px",
    p("font-size:14px;font-weight:bold;color:"+I+";line-height:1.8;letter-spacing:0.5px;margin:0","这个价格已经低到，合规手段低于7折就不可能盈利。")))
v.append(variant(4, "标签徽章式", sec("margin:12px 0;padding:10px 14px;background:rgba(0,0,0,0.02);border-radius:6px",
    sec("display:inline-block;padding:2px 8px;background:"+P+";color:#fff;font-size:7px;font-weight:bold;letter-spacing:1.5px;margin-bottom:6px","金句") +
    p("font-size:14px;color:"+I+";line-height:1.85;letter-spacing:0.5px;margin:0","你以为你在挑模型，其实你是在赌人品。")))
v.append(variant(5, "双引号包裹", sec("margin:12px 0;text-align:center",
    p("font-size:12px;color:"+A+";margin:0 0 6px;letter-spacing:1px","\u201C") +
    p("font-size:14px;font-weight:bold;color:"+I+";line-height:1.85;margin:0","引号在上方居中的形式") +
    p("font-size:12px;color:"+A+";margin:6px 0 0;letter-spacing:1px","\u201D")))
v.append(variant(6, "倾斜手写感", sec("margin:12px 0;padding:10px 14px;text-align:center",
    p("font-size:16px;font-weight:bold;color:"+I+";line-height:1.9;letter-spacing:1px;margin:0;font-style:italic","有点倾斜的强调引文")))
v.append(variant(7, "破折号署名", sec("margin:12px 0;padding:10px 0;text-align:right",
    p("font-size:14px;color:"+I+";line-height:1.85;margin:0","\u201C 引用的那句话。\u201D") +
    p("font-size:10px;color:"+A+";margin:4px 0 0","\u2014\u2014 署名来源")))
v.append(variant(8, "色块底反白", sec("margin:12px 0;padding:14px 16px;background:"+P+";border-radius:4px;text-align:center",
    p("font-size:14px;font-weight:bold;color:#fff;line-height:1.85;letter-spacing:0.5px;margin:0","反白金句，黑底白字，极强对比。")))
v.append(variant(9, "上下装饰线", sec("margin:12px 0;padding:12px 0;text-align:center",
    sec("width:40px;height:1px;background:"+P+";margin:0 auto 8px;display:block") +
    p("font-size:15px;font-weight:bold;color:"+I+";line-height:1.85;margin:0","上下横线框住一句话") +
    sec("width:40px;height:1px;background:"+P+";margin:8px auto 0;display:block")))
v.append(variant(10, "气泡对话式", sec("margin:12px 0;display:flex;align-items:flex-start;gap:8px",
    sec("width:6px;height:6px;border-radius:50%;background:"+P+";margin-top:7px;flex-shrink:0") +
    sec("flex:1;padding:10px 14px;background:#f5f5f5;border-radius:8px",
        p("font-size:13px;color:"+I+";line-height:1.8;letter-spacing:0.3px;margin:0","对话气泡式的引用，左侧圆点模拟头像。"))))
add_section("5.5", "引用/金句", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.6 数据展示
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "三列等宽", sec("display:flex;flex-flow:row;justify-content:space-around;margin:12px 0",
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:12px 6px;background:#f8f8f8;border-radius:6px",
        p("font-size:24px;font-weight:bold;color:"+P+";margin:0;line-height:1.2","85%") + p("font-size:8px;color:"+A+";margin:4px 0 0","增长率")) +
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:12px 6px;background:#f8f8f8;border-radius:6px",
        p("font-size:24px;font-weight:bold;color:"+P+";margin:0;line-height:1.2","10M") + p("font-size:8px;color:"+A+";margin:4px 0 0","用户数")) +
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:12px 6px;background:#f8f8f8;border-radius:6px",
        p("font-size:24px;font-weight:bold;color:"+P+";margin:0;line-height:1.2","99%") + p("font-size:8px;color:"+A+";margin:4px 0 0","满意度"))
)))
v.append(variant(2, "两列对比", sec("display:flex;flex-flow:row;gap:8px;margin:12px 0",
    sec("display:inline-block;flex:1;text-align:center;padding:14px 8px;background:linear-gradient(135deg,#f8f8f8,#f0f0f0);border-radius:8px",
        p("font-size:10px;color:"+A+";margin:0 0 4px;letter-spacing:1px","BEFORE") + p("font-size:22px;font-weight:bold;color:"+P+";margin:0","3h")) +
    sec("display:inline-block;flex:1;text-align:center;padding:14px 8px;background:"+P+";border-radius:8px",
        p("font-size:10px;color:rgba(255,255,255,0.6);margin:0 0 4px;letter-spacing:1px","AFTER") + p("font-size:22px;font-weight:bold;color:#fff;margin:0","3min"))
)))
v.append(variant(3, "四列紧凑", sec("display:flex;flex-flow:row;justify-content:space-between;margin:12px 0",
    sec("display:inline-block;flex:0 0 22%;text-align:center",
        p("font-size:18px;font-weight:bold;color:"+P+";margin:0","4.8") + p("font-size:7px;color:"+A+";margin:2px 0 0;letter-spacing:0.5px","评分")) +
    sec("display:inline-block;flex:0 0 22%;text-align:center",
        p("font-size:18px;font-weight:bold;color:"+P+";margin:0","12K") + p("font-size:7px;color:"+A+";margin:2px 0 0;letter-spacing:0.5px","Star")) +
    sec("display:inline-block;flex:0 0 22%;text-align:center",
        p("font-size:18px;font-weight:bold;color:"+P+";margin:0","300+") + p("font-size:7px;color:"+A+";margin:2px 0 0;letter-spacing:0.5px","Fork")) +
    sec("display:inline-block;flex:0 0 22%;text-align:center",
        p("font-size:18px;font-weight:bold;color:"+P+";margin:0","50") + p("font-size:7px;color:"+A+";margin:2px 0 0;letter-spacing:0.5px","Contrib"))
)))
v.append(variant(4, "纵向排列", sec("margin:12px 0;display:flex;flex-flow:column;gap:6px",
    sec("display:flex;flex-flow:row;align-items:center;gap:10px;padding:8px 12px;background:#f8f8f8;border-radius:4px",
        p("font-size:20px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0;width:50px","85%") +
        p("font-size:11px;color:#555;margin:0;flex:1","用户增长率 · Year over Year")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px;padding:8px 12px;background:#f8f8f8;border-radius:4px",
        p("font-size:20px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0;width:50px","10M") +
        p("font-size:11px;color:#555;margin:0;flex:1","月活跃用户数")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px;padding:8px 12px;background:#f8f8f8;border-radius:4px",
        p("font-size:20px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0;width:50px","99%") +
        p("font-size:11px;color:#555;margin:0;flex:1","客户满意度"))
)))
v.append(variant(5, "大数字 + 趋势箭头", sec("display:flex;flex-flow:row;justify-content:space-around;margin:12px 0",
    sec("display:inline-block;flex:0 0 45%;text-align:center;padding:14px 8px",
        p("font-size:10px;color:"+A+";margin:0 0 4px","总交易额") +
        p("font-size:28px;font-weight:bold;color:"+P+";margin:0;line-height:1.1","$2.4B") +
        p("font-size:9px;color:#4caf50;margin:4px 0 0","\u2191 18%")) +
    sec("display:inline-block;flex:0 0 45%;text-align:center;padding:14px 8px",
        p("font-size:10px;color:"+A+";margin:0 0 4px","活跃商家") +
        p("font-size:28px;font-weight:bold;color:"+P+";margin:0;line-height:1.1","850K") +
        p("font-size:9px;color:#4caf50;margin:4px 0 0","\u2191 32%")))
))
v.append(variant(6, "进度条式", sec("margin:12px 0;display:flex;flex-flow:column;gap:8px",
    sec("",
        p("font-size:10px;font-weight:bold;color:"+P+";margin:0 0 2px","完成度 78%") +
        sec("height:4px;background:#eee;border-radius:2px", sec("width:78%;height:100%;background:"+P+";border-radius:2px"))) +
    sec("",
        p("font-size:10px;font-weight:bold;color:"+P+";margin:0 0 2px","覆盖率 92%") +
        sec("height:4px;background:#eee;border-radius:2px", sec("width:92%;height:100%;background:"+P+";border-radius:2px")))
)))
v.append(variant(7, "图标数字卡", sec("display:flex;flex-flow:row;justify-content:space-around;margin:12px 0",
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:10px 6px;border:1px solid #eee;border-radius:8px",
        p("font-size:20px;margin:0;line-height:1.2","📊") + p("font-size:16px;font-weight:bold;color:"+P+";margin:4px 0 0","97") + p("font-size:8px;color:"+A+";margin:2px 0 0","报告数")) +
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:10px 6px;border:1px solid #eee;border-radius:8px",
        p("font-size:20px;margin:0;line-height:1.2","👥") + p("font-size:16px;font-weight:bold;color:"+P+";margin:4px 0 0","2.1K") + p("font-size:8px;color:"+A+";margin:2px 0 0","团队")) +
    sec("display:inline-block;flex:0 0 30%;text-align:center;padding:10px 6px;border:1px solid #eee;border-radius:8px",
        p("font-size:20px;margin:0;line-height:1.2","⭐") + p("font-size:16px;font-weight:bold;color:"+P+";margin:4px 0 0","4.9") + p("font-size:8px;color:"+A+";margin:2px 0 0","评分"))
)))
v.append(variant(8, "双色背景卡", sec("display:flex;flex-flow:row;gap:8px;margin:12px 0",
    sec("flex:1;padding:16px 10px;background:"+P+";border-radius:8px;text-align:center",
        p("font-size:24px;font-weight:bold;color:#fff;margin:0","+128%") + p("font-size:8px;color:rgba(255,255,255,0.6);margin:4px 0 0;letter-spacing:1px","REVENUE")) +
    sec("flex:1;padding:16px 10px;background:#f0f0f0;border-radius:8px;text-align:center",
        p("font-size:24px;font-weight:bold;color:"+P+";margin:0","-43%") + p("font-size:8px;color:"+A+";margin:4px 0 0;letter-spacing:1px","COST"))
)))
v.append(variant(9, "环形占比", sec("display:flex;flex-flow:row;justify-content:space-around;align-items:center;margin:12px 0",
    sec("text-align:center",
        sec("width:50px;height:50px;border-radius:50%;border:3px solid "+P+";display:flex;align-items:center;justify-content:center;margin:0 auto 6px",
            p("font-size:12px;font-weight:bold;color:"+P+";margin:0","72%")) +
        p("font-size:8px;color:"+A+";margin:0","移动端")) +
    sec("text-align:center",
        sec("width:50px;height:50px;border-radius:50%;border:3px solid #ddd;display:flex;align-items:center;justify-content:center;margin:0 auto 6px",
            p("font-size:12px;font-weight:bold;color:"+A+";margin:0","28%")) +
        p("font-size:8px;color:"+A+";margin:0","桌面端"))
)))
v.append(variant(10, "时间线数据", sec("display:flex;flex-flow:column;gap:6px;margin:12px 0",
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        p("font-size:9px;font-weight:bold;color:"+A+";margin:0;flex-shrink:0;width:35px","2023") +
        sec("flex:1;height:4px;background:#eee;border-radius:2px", sec("width:30%;height:100%;background:"+P+";border-radius:2px")) +
        p("font-size:9px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0","30%")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        p("font-size:9px;font-weight:bold;color:"+A+";margin:0;flex-shrink:0;width:35px","2024") +
        sec("flex:1;height:4px;background:#eee;border-radius:2px", sec("width:60%;height:100%;background:"+P+";border-radius:2px")) +
        p("font-size:9px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0","60%")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        p("font-size:9px;font-weight:bold;color:"+A+";margin:0;flex-shrink:0;width:35px","2025") +
        sec("flex:1;height:4px;background:#eee;border-radius:2px", sec("width:90%;height:100%;background:"+P+";border-radius:2px")) +
        p("font-size:9px;font-weight:bold;color:"+P+";margin:0;flex-shrink:0","90%"))
)))
add_section("5.6", "数据展示", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.7 步骤流（横向）
# ════════════════════════════════════════════════════════════
def hstep(n, name, desc, highlight=False):
    bg = P if highlight else "rgba(0,0,0,0.04)"
    tc = "#fff" if highlight else I
    return sec("display:inline-block;flex:0 0 auto;text-align:center;padding:8px 6px;box-sizing:border-box",
        sec(f"display:inline-block;width:24px;height:24px;line-height:24px;background:{bg};color:{tc};font-size:10px;font-weight:bold;text-align:center;margin-bottom:4px;border-radius:50%", str(n)) +
        p(f"font-size:10px;font-weight:bold;color:{I};margin:0", name) +
        p(f"font-size:8px;color:{A};margin:2px 0 0", desc[:8]))

v = []
v.append(variant(1, "默认圆形编号", sec("margin:12px 0;padding:12px 10px;background:#f8f8f8;border-radius:6px",
    sec("display:flex;flex-flow:row;justify-content:space-around",
        hstep(1,"输入","喂知识库") + hstep(2,"管理","有序运转",True) + hstep(3,"输出","取素材")))))
v.append(variant(2, "箭头连接", sec("margin:12px 0;padding:12px 10px;background:#f8f8f8;border-radius:6px",
    sec("display:flex;flex-flow:row;justify-content:center;align-items:center;gap:4px",
        hstep(1,"注册","") + p(f"font-size:10px;color:{A};margin:0","→") + hstep(2,"认证","",True) + p(f"font-size:10px;color:{A};margin:0","→") + hstep(3,"使用","")))))
v.append(variant(3, "方角编号", sec("margin:12px 0;padding:12px 10px;background:#f8f8f8",
    sec("display:flex;flex-flow:row;justify-content:space-around",
        sec("display:inline-block;flex:0 0 auto;text-align:center",
            sec(f"display:inline-block;padding:3px 10px;background:{P};color:#fff;font-size:9px;font-weight:bold;margin-bottom:4px","STEP 1") +
            p(f"font-size:10px;font-weight:bold;color:{I};margin:0","分析") + p(f"font-size:8px;color:{A};margin:2px 0 0","需求调研")) +
        sec("display:inline-block;flex:0 0 auto;text-align:center",
            sec(f"display:inline-block;padding:3px 10px;background:{P};color:#fff;font-size:9px;font-weight:bold;margin-bottom:4px","STEP 2") +
            p(f"font-size:10px;font-weight:bold;color:{I};margin:0","设计") + p(f"font-size:8px;color:{A};margin:2px 0 0","原型方案")) +
        sec("display:inline-block;flex:0 0 auto;text-align:center",
            sec(f"display:inline-block;padding:3px 10px;background:rgba(0,0,0,0.04);color:{A};font-size:9px;font-weight:bold;margin-bottom:4px","STEP 3") +
            p(f"font-size:10px;font-weight:bold;color:{I};margin:0","开发") + p(f"font-size:8px;color:{A};margin:2px 0 0","迭代上线"))))))
v.append(variant(4, "图标式", sec("margin:12px 0;display:flex;flex-flow:row;justify-content:space-around;text-align:center",
    sec("display:inline-block;flex:0 0 auto;padding:8px",
        p("font-size:20px;margin:0","📝") + p(f"font-size:9px;font-weight:bold;color:{I};margin:4px 0 0","撰写") + p(f"font-size:7px;color:{A};margin:2px 0 0","Write")) +
    sec("display:inline-block;flex:0 0 auto;padding:8px",
        p("font-size:20px;margin:0","🎨") + p(f"font-size:9px;font-weight:bold;color:{I};margin:4px 0 0","排版") + p(f"font-size:7px;color:{A};margin:2px 0 0","Design")) +
    sec("display:inline-block;flex:0 0 auto;padding:8px",
        p("font-size:20px;margin:0","🚀") + p(f"font-size:9px;font-weight:bold;color:{I};margin:4px 0 0","发布") + p(f"font-size:7px;color:{A};margin:2px 0 0","Publish")))))
v.append(variant(5, "进度条连接", sec("margin:12px 0;padding:12px 10px",
    sec("display:flex;flex-flow:row;align-items:center;justify-content:center",
        sec("width:20px;height:20px;border-radius:50%;background:"+P+";flex-shrink:0") +
        sec("flex:0 0 40px;height:2px;background:"+P) +
        sec("width:20px;height:20px;border-radius:50%;background:"+P+";flex-shrink:0") +
        sec("flex:0 0 40px;height:2px;background:#ddd") +
        sec("width:20px;height:20px;border-radius:50%;background:#ddd;flex-shrink:0")) +
    sec("display:flex;flex-flow:row;justify-content:space-around;margin-top:6px",
        p(f"font-size:8px;color:{I};margin:0","完成") + p(f"font-size:8px;color:{I};margin:0","进行中") + p(f"font-size:8px;color:{A};margin:0","待开始")))))
v.append(variant(6, "卡片式流程", sec("display:flex;flex-flow:row;gap:6px;margin:12px 0",
    sec("flex:1;padding:10px 6px;background:#f5f5f5;border-radius:6px;text-align:center",
        p(f"font-size:18px;font-weight:bold;color:{P};margin:0","1") + p(f"font-size:9px;font-weight:bold;color:{I};margin:4px 0 0","收集") + p(f"font-size:7px;color:{A};margin:2px 0 0","Collect")) +
    sec("flex:1;padding:10px 6px;background:{P};border-radius:6px;text-align:center",
        p("font-size:18px;font-weight:bold;color:#fff;margin:0","2") + p("font-size:9px;font-weight:bold;color:#fff;margin:4px 0 0","整理") + p("font-size:7px;color:rgba(255,255,255,0.6);margin:2px 0 0","Organize")) +
    sec("flex:1;padding:10px 6px;background:#f5f5f5;border-radius:6px;text-align:center",
        p(f"font-size:18px;font-weight:bold;color:{P};margin:0","3") + p(f"font-size:9px;font-weight:bold;color:{I};margin:4px 0 0","输出") + p(f"font-size:7px;color:{A};margin:2px 0 0","Output")))))
v.append(variant(7, "标签横幅式", sec("margin:12px 0;display:flex;flex-flow:row;gap:4px",
    sec("flex:1;padding:8px;background:"+P+";text-align:center",
        p("font-size:9px;color:rgba(255,255,255,0.5);margin:0;letter-spacing:1px","01") + p("font-size:11px;font-weight:bold;color:#fff;margin:2px 0 0","规划")) +
    sec("flex:1;padding:8px;background:"+P+";text-align:center",
        p("font-size:9px;color:rgba(255,255,255,0.5);margin:0;letter-spacing:1px","02") + p("font-size:11px;font-weight:bold;color:#fff;margin:2px 0 0","执行")) +
    sec("flex:1;padding:8px;background:rgba(0,0,0,0.04);text-align:center",
        p(f"font-size:9px;color:{A};margin:0;letter-spacing:1px","03") + p(f"font-size:11px;font-weight:bold;color:{A};margin:2px 0 0","复盘")))))
v.append(variant(8, "时间轴横排", sec("margin:12px 0;display:flex;flex-flow:row;gap:0",
    sec("flex:1;text-align:center;padding:8px 0;border-top:2px solid "+P,
        p(f"font-size:8px;color:{A};margin:0 0 4px","Q1") + p(f"font-size:10px;font-weight:bold;color:{I};margin:0","调研")) +
    sec("flex:1;text-align:center;padding:8px 0;border-top:2px solid "+P,
        p(f"font-size:8px;color:{A};margin:0 0 4px","Q2") + p(f"font-size:10px;font-weight:bold;color:{I};margin:0","开发")) +
    sec("flex:1;text-align:center;padding:8px 0;border-top:2px solid #ddd",
        p(f"font-size:8px;color:{A};margin:0 0 4px","Q3") + p(f"font-size:10px;font-weight:bold;color:{A};margin:0","上线")))))
v.append(variant(9, "三列对比卡", sec("display:flex;flex-flow:row;gap:6px;margin:12px 0",
    sec("flex:1;padding:10px 6px;border:1px solid #eee;border-radius:6px;text-align:center",
        sec("width:16px;height:16px;line-height:16px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;text-align:center;margin:0 auto 6px;border-radius:50%","A") +
        p(f"font-size:10px;font-weight:bold;color:{I};margin:0","方案A") + p(f"font-size:7px;color:{A};margin:2px 0 0","低成本")) +
    sec("flex:1;padding:10px 6px;border:2px solid "+P+";border-radius:6px;text-align:center",
        sec("width:16px;height:16px;line-height:16px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;text-align:center;margin:0 auto 6px;border-radius:50%","B") +
        p(f"font-size:10px;font-weight:bold;color:{I};margin:0","方案B") + p(f"font-size:7px;color:{A};margin:2px 0 0","推荐")) +
    sec("flex:1;padding:10px 6px;border:1px solid #eee;border-radius:6px;text-align:center",
        sec("width:16px;height:16px;line-height:16px;background:rgba(0,0,0,0.04);color:"+A+";font-size:8px;font-weight:bold;text-align:center;margin:0 auto 6px;border-radius:50%","C") +
        p(f"font-size:10px;font-weight:bold;color:{I};margin:0","方案C") + p(f"font-size:7px;color:{A};margin:2px 0 0","高收益")))))
v.append(variant(10, "极简数字条", sec("display:flex;flex-flow:row;align-items:center;gap:0;margin:12px 0",
    p(f"font-size:22px;font-weight:bold;color:{P};margin:0;flex-shrink:0","01") +
    sec("flex:1;height:1px;background:#ddd;margin:0 10px") +
    p(f"font-size:22px;font-weight:bold;color:{P};margin:0;flex-shrink:0","02") +
    sec("flex:1;height:1px;background:#ddd;margin:0 10px") +
    p(f"font-size:22px;font-weight:bold;color:{A};margin:0;flex-shrink:0","03")) +
    sec("display:flex;flex-flow:row;justify-content:space-around;margin-top:4px",
        p(f"font-size:8px;color:{I};margin:0","发现") + p(f"font-size:8px;color:{I};margin:0","定义") + p(f"font-size:8px;color:{A};margin:0","交付"))))
add_section("5.7", "步骤流（横向）", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.8 步骤流（纵向）
# ════════════════════════════════════════════════════════════
v = []
vsteps = [
    ("1","注册账号","填写基本信息完成注册",""),
    ("2","实名认证","上传证件完成身份验证","active"),
    ("3","开始使用","选择功能模块开始体验",""),
]
def vstep(num, title, desc, state):
    bg = P if state=="active" else "rgba(0,0,0,0.04)"
    tc = "#fff" if state=="active" else I
    return sec("display:flex;flex-flow:row;align-items:flex-start;gap:10px",
        sec(f"width:22px;height:22px;line-height:22px;background:{bg};color:{tc};font-size:9px;font-weight:bold;text-align:center;flex-shrink:0;border-radius:50%", num) +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{I};margin:0", title) + p(f"font-size:10px;color:{A};margin:2px 0 0", desc)))

v.append(variant(1, "默认圆形编号", sec("margin:12px 0;padding:14px;background:#f8f8f8;border-radius:6px;display:flex;flex-flow:column;gap:10px",
    vstep("1","注册账号","填写基本信息") + vstep("2","实名认证","上传证件验证",True) + vstep("3","开始使用","选择功能模块"))))
v.append(variant(2, "时间轴竖线", sec("margin:12px 0;display:flex;flex-flow:column",
    sec("display:flex;flex-flow:row;gap:10px",
        sec("display:flex;flex-flow:column;align-items:center;flex-shrink:0;width:20px",
            sec("width:10px;height:10px;border-radius:50%;background:"+P) + sec("width:1px;flex:1;background:#ddd")) +
        sec("flex:1;padding-bottom:14px",
            p(f"font-size:8px;color:{A};margin:0 0 2px","2024.06") + p(f"font-size:12px;font-weight:bold;color:{I};margin:0","项目启动") + p(f"font-size:10px;color:{A};margin:2px 0 0","完成团队组建和需求分析"))) +
    sec("display:flex;flex-flow:row;gap:10px",
        sec("display:flex;flex-flow:column;align-items:center;flex-shrink:0;width:20px",
            sec("width:10px;height:10px;border-radius:50%;background:"+P) + sec("width:1px;flex:1;background:#ddd")) +
        sec("flex:1;padding-bottom:14px",
            p(f"font-size:8px;color:{A};margin:0 0 2px","2024.12") + p(f"font-size:12px;font-weight:bold;color:{I};margin:0","一期上线") + p(f"font-size:10px;color:{A};margin:2px 0 0","核心功能发布，用户破万"))) +
    sec("display:flex;flex-flow:row;gap:10px",
        sec("width:10px;height:10px;border-radius:50%;background:#ddd;flex-shrink:0;margin-top:0") +
        sec("flex:1", p(f"font-size:8px;color:{A};margin:0 0 2px","2025.06") + p(f"font-size:12px;font-weight:bold;color:{A};margin:0","二期迭代") + p(f"font-size:10px;color:{A};margin:2px 0 0","规划中...")))
)))
v.append(variant(3, "左侧编号条", sec("margin:12px 0;display:flex;flex-flow:column;gap:8px",
    sec("display:flex;flex-flow:row;gap:10px",
        sec("padding:2px 6px;background:"+P+";color:#fff;font-size:10px;font-weight:bold;flex-shrink:0;text-align:center;min-width:24px","01") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{I};margin:0","信息收集") + p(f"font-size:10px;color:{A};margin:2px 0 0","Gather requirements"))) +
    sec("display:flex;flex-flow:row;gap:10px",
        sec("padding:2px 6px;background:"+P+";color:#fff;font-size:10px;font-weight:bold;flex-shrink:0;text-align:center;min-width:24px","02") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{I};margin:0","方案设计") + p(f"font-size:10px;color:{A};margin:2px 0 0","Design solution"))) +
    sec("display:flex;flex-flow:row;gap:10px",
        sec("padding:2px 6px;background:rgba(0,0,0,0.04);color:"+A+";font-size:10px;font-weight:bold;flex-shrink:0;text-align:center;min-width:24px","03") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{A};margin:0","交付上线") + p(f"font-size:10px;color:{A};margin:2px 0 0","Deploy"))))))
v.append(variant(4, "卡片堆叠", sec("display:flex;flex-flow:column;gap:8px;margin:12px 0",
    sec("padding:12px 14px;background:#f5f5f5;border-radius:6px;border-left:3px solid "+P,
        p(f"font-size:9px;font-weight:bold;color:{A};margin:0 0 4px;letter-spacing:1px","STEP 01") +
        p(f"font-size:13px;font-weight:bold;color:{I};margin:0","环境配置") +
        p(f"font-size:10px;color:{A};margin:4px 0 0","安装依赖并设置环境变量")) +
    sec("padding:12px 14px;background:"+P+";border-radius:6px",
        p("font-size:9px;font-weight:bold;color:rgba(255,255,255,0.5);margin:0 0 4px;letter-spacing:1px","STEP 02") +
        p("font-size:13px;font-weight:bold;color:#fff;margin:0","数据迁移") +
        p("font-size:10px;color:rgba(255,255,255,0.6);margin:4px 0 0","从旧系统迁移到新平台")) +
    sec("padding:12px 14px;background:#f5f5f5;border-radius:6px",
        p(f"font-size:9px;font-weight:bold;color:{A};margin:0 0 4px;letter-spacing:1px","STEP 03") +
        p(f"font-size:13px;font-weight:bold;color:{I};margin:0","验证测试") +
        p(f"font-size:10px;color:{A};margin:4px 0 0","确保功能正常后上线")))))
v.append(variant(5, "图标列表", sec("display:flex;flex-flow:column;gap:10px;margin:12px 0",
    sec("display:flex;flex-flow:row;align-items:flex-start;gap:10px",
        p("font-size:16px;margin:0;flex-shrink:0","✅") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{I};margin:0","已完成：基础架构搭建") + p(f"font-size:10px;color:{A};margin:2px 0 0","2025-01 交付"))) +
    sec("display:flex;flex-flow:row;align-items:flex-start;gap:10px",
        p("font-size:16px;margin:0;flex-shrink:0","🔄") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{I};margin:0","进行中：性能优化") + p(f"font-size:10px;color:{A};margin:2px 0 0","预计 2025-03"))) +
    sec("display:flex;flex-flow:row;align-items:flex-start;gap:10px",
        p("font-size:16px;margin:0;flex-shrink:0","📋") +
        sec("flex:1", p(f"font-size:12px;font-weight:bold;color:{A};margin:0","计划中：国际化") + p(f"font-size:10px;color:{A};margin:2px 0 0","Q3 启动"))))))
v.append(variant(6, "数字 + 竖线", sec("margin:12px 0;display:flex;flex-flow:column;gap:0",
    sec("display:flex;flex-flow:row;gap:12px",
        p(f"font-size:28px;font-weight:bold;color:{P};margin:0;line-height:1;flex-shrink:0","1") +
        sec("flex:1;padding-bottom:8px;border-left:2px solid "+P+";padding-left:12px",
            p(f"font-size:13px;font-weight:bold;color:{I};margin:0","发现问题") + p(f"font-size:10px;color:{A};margin:4px 0 0","Identify pain points"))) +
    sec("display:flex;flex-flow:row;gap:12px",
        p(f"font-size:28px;font-weight:bold;color:{P};margin:0;line-height:1;flex-shrink:0","2") +
        sec("flex:1;padding-bottom:8px;border-left:2px solid "+P+";padding-left:12px",
            p(f"font-size:13px;font-weight:bold;color:{I};margin:0","设计方案") + p(f"font-size:10px;color:{A};margin:4px 0 0","Propose solution"))) +
    sec("display:flex;flex-flow:row;gap:12px",
        p(f"font-size:28px;font-weight:bold;color:{A};margin:0;line-height:1;flex-shrink:0","3") +
        sec("flex:1;border-left:2px solid #ddd;padding-left:12px",
            p(f"font-size:13px;font-weight:bold;color:{A};margin:0","落地执行") + p(f"font-size:10px;color:{A};margin:4px 0 0","Implementation"))))))
v.append(variant(7, "进度百分比", sec("display:flex;flex-flow:column;gap:8px;margin:12px 0",
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        sec("flex:1", p(f"font-size:11px;font-weight:bold;color:{I};margin:0 0 2px","需求分析") + sec("height:5px;background:#eee;border-radius:3px", sec("width:100%;height:100%;background:#4caf50;border-radius:3px"))) +
        p("font-size:9px;font-weight:bold;color:#4caf50;margin:0;flex-shrink:0","100%")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        sec("flex:1", p(f"font-size:11px;font-weight:bold;color:{I};margin:0 0 2px","UI 设计") + sec("height:5px;background:#eee;border-radius:3px", sec("width:80%;height:100%;background:"+P+";border-radius:3px"))) +
        p(f"font-size:9px;font-weight:bold;color:{P};margin:0;flex-shrink:0","80%")) +
    sec("display:flex;flex-flow:row;align-items:center;gap:10px",
        sec("flex:1", p(f"font-size:11px;font-weight:bold;color:{A};margin:0 0 2px","后端开发") + sec("height:5px;background:#eee;border-radius:3px", sec("width:30%;height:100%;background:#ccc;border-radius:3px"))) +
        p(f"font-size:9px;font-weight:bold;color:{A};margin:0;flex-shrink:0","30%")))))
v.append(variant(8, "折叠面板风", sec("display:flex;flex-flow:column;gap:2px;margin:12px 0",
    sec("padding:10px 12px;background:"+P+";display:flex;flex-flow:row;justify-content:space-between;align-items:center",
        p("font-size:11px;font-weight:bold;color:#fff;margin:0","▾ 第一步：环境准备") + p("font-size:8px;color:rgba(255,255,255,0.5);margin:0","Done")) +
    sec("padding:10px 12px;background:#f5f5f5;display:flex;flex-flow:row;justify-content:space-between;align-items:center",
        p(f"font-size:11px;font-weight:bold;color:{I};margin:0","▸ 第二步：数据导入") + p(f"font-size:8px;color:{A};margin:0","In progress")) +
    sec("padding:10px 12px;background:#f5f5f5;display:flex;flex-flow:row;justify-content:space-between;align-items:center",
        p(f"font-size:11px;font-weight:bold;color:{A};margin:0","▸ 第三步：效果验证") + p(f"font-size:8px;color:{A};margin:0","Pending")))))
v.append(variant(9, "问答式", sec("display:flex;flex-flow:column;gap:8px;margin:12px 0",
    sec("", p(f"font-size:12px;font-weight:bold;color:{P};margin:0 0 2px","Q1: 如何安装？") + p(f"font-size:11px;color:#555;margin:0;line-height:1.7","运行 portable\\setup_portable.bat 一键配置。"))) +
    sec("", p(f"font-size:12px;font-weight:bold;color:{P};margin:0 0 2px","Q2: 如何启动？") + p(f"font-size:11px;color:#555;margin:0;line-height:1.7","双击 portable\\start_portable.bat 即可。"))) +
    sec("", p(f"font-size:12px;font-weight:bold;color:{P};margin:0 0 2px","Q3: 需要 API Key 吗？") + p(f"font-size:11px;color:#555;margin:0;line-height:1.7","需要 DeepSeek API Key，注册即送额度。"))))))
v.append(variant(10, "双列对比", sec("display:flex;flex-flow:row;gap:8px;margin:12px 0",
    sec("flex:1;padding:12px 10px;background:#f8f8f8;border-radius:6px",
        p(f"font-size:8px;font-weight:bold;color:{A};margin:0 0 6px;letter-spacing:1px","DO")) +
        sec("display:flex;flex-flow:column;gap:4px",
            p(f"font-size:10px;color:#4caf50;margin:0","✓ 用 section") + p(f"font-size:10px;color:#4caf50;margin:0","✓ 内联样式") + p(f"font-size:10px;color:#4caf50;margin:0","✓ box-sizing"))) +
    sec("flex:1;padding:12px 10px;background:#f8f8f8;border-radius:6px",
        p(f"font-size:8px;font-weight:bold;color:{A};margin:0 0 6px;letter-spacing:1px","DONT")) +
    sec("display:flex;flex-flow:column;gap:4px",
        p(f"font-size:10px;color:#e74c3c;margin:0","✗ 禁用 div") + p(f"font-size:10px;color:#e74c3c;margin:0","✗ 禁用 style标签") + p(f"font-size:10px;color:#e74c3c;margin:0","✗ 禁用 position"))))))
add_section("5.8", "步骤流（纵向）", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.9 标签徽章
# ════════════════════════════════════════════════════════════
def badge(text, bg=None, color=None, size="8px"):
    b = bg or P
    c = color or "#fff"
    return sec(f"display:inline-block;padding:2px 8px;background:{b};color:{c};font-size:{size};font-weight:bold;letter-spacing:0.5px;border-radius:3px", text)

v = []
v.append(variant(1, "默认实心", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:4px",
    badge("Vue")+badge("TypeScript")+badge("Vite")+badge("Tailwind"))))
v.append(variant(2, "描边空心", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:4px",
    sec("display:inline-block;padding:2px 8px;border:1px solid "+P+";color:"+P+";font-size:8px;font-weight:bold;letter-spacing:0.5px","React")+
    sec("display:inline-block;padding:2px 8px;border:1px solid "+P+";color:"+P+";font-size:8px;font-weight:bold;letter-spacing:0.5px","Next.js")+
    sec("display:inline-block;padding:2px 8px;border:1px solid "+P+";color:"+P+";font-size:8px;font-weight:bold;letter-spacing:0.5px","Prisma"))))
v.append(variant(3, "圆角胶囊", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:4px",
    sec("display:inline-block;padding:3px 12px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;letter-spacing:0.5px;border-radius:20px","Python")+
    sec("display:inline-block;padding:3px 12px;background:"+P+";color:#fff;font-size:8px;font-weight:bold;letter-spacing:0.5px;border-radius:20px","Django")+
    sec("display:inline-block;padding:3px 12px;background:rgba(0,0,0,0.04);color:"+A+";font-size:8px;font-weight:bold;letter-spacing:0.5px;border-radius:20px","Redis"))))
v.append(variant(4, "彩色标签", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:4px",
    badge("紧急","#e74c3c")+badge("重要","#f39c12")+badge("普通","#3498db")+badge("可选","#95a5a6"))))
v.append(variant(5, "左侧圆点", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:6px",
    sec("display:flex;align-items:center;gap:4px;font-size:8px;font-weight:bold;color:"+I,
        sec("width:5px;height:5px;border-radius:50%;background:"+P)+"进行中")+
    sec("display:flex;align-items:center;gap:4px;font-size:8px;font-weight:bold;color:#4caf50",
        sec("width:5px;height:5px;border-radius:50%;background:#4caf50")+"已完成")+
    sec("display:flex;align-items:center;gap:4px;font-size:8px;font-weight:bold;color:"+A,
        sec("width:5px;height:5px;border-radius:50%;background:"+A)+"待审核"))))
v.append(variant(6, "emoji 前缀", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:6px",
    sec("display:inline-block;padding:2px 8px;background:rgba(0,0,0,0.04);font-size:8px;font-weight:bold;color:"+I+";letter-spacing:0.5px;border-radius:3px","📌 置顶")+
    sec("display:inline-block;padding:2px 8px;background:rgba(0,0,0,0.04);font-size:8px;font-weight:bold;color:"+I+";letter-spacing:0.5px;border-radius:3px","🔥 热门")+
    sec("display:inline-block;padding:2px 8px;background:rgba(0,0,0,0.04);font-size:8px;font-weight:bold;color:"+I+";letter-spacing:0.5px;border-radius:3px","🆕 新上"))))
v.append(variant(7, "方形标签", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:3px",
    badge("DESIGN","","", "7px")+badge("DEV","","", "7px")+badge("OPS","","", "7px")+badge("QA","","", "7px"))))
v.append(variant(8, "双色分割", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:2px",
    sec("display:flex;flex-flow:row;border-radius:3px;overflow:hidden",
        sec("padding:2px 6px;background:"+P+";color:#fff;font-size:7px;font-weight:bold","难度")+
        sec("padding:2px 6px;background:rgba(0,0,0,0.04);color:"+I+";font-size:7px;font-weight:bold","中等"))+
    sec("display:flex;flex-flow:row;border-radius:3px;overflow:hidden",
        sec("padding:2px 6px;background:"+P+";color:#fff;font-size:7px;font-weight:bold","时间")+
        sec("padding:2px 6px;background:rgba(0,0,0,0.04);color:"+I+";font-size:7px;font-weight:bold","3天")))))
v.append(variant(9, "数字角标", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:8px",
    sec("display:inline-block;position:static;font-size:10px;font-weight:bold;color:"+I,
        "消息"+sec("display:inline-block;margin-left:4px;padding:0 5px;background:#e74c3c;color:#fff;font-size:7px;font-weight:bold;border-radius:8px;line-height:16px","3"))+
    sec("display:inline-block;position:static;font-size:10px;font-weight:bold;color:"+I,
        "评论"+sec("display:inline-block;margin-left:4px;padding:0 5px;background:"+P+";color:#fff;font-size:7px;font-weight:bold;border-radius:8px;line-height:16px","12")))))
v.append(variant(10, "渐变彩条", sec("display:flex;flex-flow:row;flex-wrap:wrap;gap:4px",
    sec("display:inline-block;padding:2px 10px;background:linear-gradient(135deg,#667eea,#764ba2);color:#fff;font-size:7px;font-weight:bold;letter-spacing:1px;border-radius:3px","PREMIUM")+
    sec("display:inline-block;padding:2px 10px;background:linear-gradient(135deg,#f093fb,#f5576c);color:#fff;font-size:7px;font-weight:bold;letter-spacing:1px;border-radius:3px","HOT")+
    sec("display:inline-block;padding:2px 10px;background:linear-gradient(135deg,#4facfe,#00f2fe);color:#fff;font-size:7px;font-weight:bold;letter-spacing:1px;border-radius:3px","NEW"))))
add_section("5.9", "标签徽章", "".join(v))

# ════════════════════════════════════════════════════════════
# 5.10 提示块
# ════════════════════════════════════════════════════════════
v = []
v.append(variant(1, "TIP 左边框", sec("margin:12px 0;padding:8px 14px;background:rgba(0,0,0,0.02);border-left:3px solid "+P,
    p(f"font-size:11px;color:#555;line-height:1.7;margin:0", "<strong style=\"color:"+P+"\">TIP</strong> 这是一个提示信息，内容简洁明了。")))
v.append(variant(2, "WARNING 样式", sec("margin:12px 0;padding:8px 14px;background:#fff8e1;border-left:3px solid #f39c12",
    p("font-size:11px;color:#555;line-height:1.7;margin:0", "<strong style=\"color:#f39c12\">⚠️ 注意</strong> 该操作不可逆，请谨慎执行。")))
v.append(variant(3, "INFO 圆角卡片", sec("margin:12px 0;padding:10px 14px;background:#e3f2fd;border-radius:6px",
    p("font-size:11px;color:#1565c0;line-height:1.7;margin:0", "<strong>ℹ️ 信息</strong> 新版本已发布，建议尽快升级。")))
v.append(variant(4, "SUCCESS 绿色", sec("margin:12px 0;padding:10px 14px;background:#e8f5e9;border-radius:6px;border-left:3px solid #4caf50",
    p("font-size:11px;color:#2e7d32;line-height:1.7;margin:0", "<strong>✅ 成功</strong> 部署完成，服务已正常运行。")))
v.append(variant(5, "ERROR 红色", sec("margin:12px 0;padding:10px 14px;background:#ffebee;border-radius:6px;border-left:3px solid #e74c3c",
    p("font-size:11px;color:#c62828;line-height:1.7;margin:0", "<strong>❌ 错误</strong> 连接超时，请检查网络后重试。")))
v.append(variant(6, "引述块", sec("margin:12px 0;padding:10px 14px;background:#f5f5f5;border-radius:6px;border:1px solid #eee",
    p("font-size:11px;color:#555;line-height:1.7;margin:0", "<strong style=\"color:"+P+"\">📖 引用</strong> 以上数据来自 2025 年行业白皮书。")))
v.append(variant(7, "FAQ 折叠风", sec("margin:12px 0;padding:10px 14px;background:linear-gradient(135deg,#fafafa,#f5f5f5);border-radius:6px",
    p(f"font-size:12px;font-weight:bold;color:{P};margin:0 0 4px","常见问题") +
    p("font-size:10px;color:#555;line-height:1.7;margin:0","Q: 为什么要用 section 而不是 div？A: 公众号只识别 section 作为容器标签。")))
v.append(variant(8, "前置感叹号", sec("display:flex;flex-flow:row;align-items:flex-start;gap:10px;margin:12px 0;padding:10px 14px;background:rgba(0,0,0,0.02);border-radius:6px",
    sec("width:24px;height:24px;line-height:24px;background:"+P+";color:#fff;font-size:12px;font-weight:bold;text-align:center;flex-shrink:0;border-radius:50%","!") +
    sec("flex:1", p("font-size:11px;color:#555;line-height:1.7;margin:0","重要提示：生产环境务必设置 WEMD_API_KEY 网关保护。")))))
v.append(variant(9, "顶部标签条", sec("margin:12px 0;border-radius:6px;overflow:hidden;border:1px solid #eee",
    sec("padding:4px 14px;background:"+P, p("font-size:8px;color:#fff;font-weight:bold;margin:0;letter-spacing:1.5px","QUICK NOTE")) +
    sec("padding:8px 14px", p("font-size:11px;color:#555;line-height:1.7;margin:0","一句话快速提示，不展开。")))))
v.append(variant(10, "无边框轻提示", sec("margin:12px 0;padding:4px 0",
    p(f"font-size:11px;color:{A};line-height:1.7;margin:0","<strong style=\"color:{P}\">*</strong> 轻量提示：不带任何背景和边框，直接融入正文流。")))
add_section("5.10", "提示块", "".join(v))

# Build full HTML
html = f"""<!DOCTYPE html>
<html lang="zh-CN"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>WeMD AI · 全组件变体预览</title>
<style>*{{margin:0;padding:0;box-sizing:border-box}}body{{background:#fff;padding:12px;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif}}</style>
</head><body>
<section style="width:100%;max-width:677px;background:transparent;padding:0 8px 24px;font-family:-apple-system,'PingFang SC','Microsoft YaHei',sans-serif;font-size:14px;line-height:1.85;color:{I};letter-spacing:0.3px;box-sizing:border-box;margin:0 auto">

<section style="text-align:center;padding:24px 0 10px;box-sizing:border-box;">
  <section style="display:inline-block;padding:3px 12px;background:{P};color:#fff;font-size:8px;font-weight:bold;letter-spacing:2px;box-sizing:border-box;">COMPONENTS</section>
  <p style="font-size:20px;font-weight:bold;color:{P};line-height:1.4;margin:8px 0 0;box-sizing:border-box;">全组件变体预览</p>
  <p style="font-size:10px;color:{A};margin:4px 0 0;box-sizing:border-box;">15 个组件 × 10 种样式 = 150 个变体</p>
</section>

{''.join(parts)}

<section style="margin:36px 0 24px;padding:24px 16px;text-align:center;background:linear-gradient(135deg,#fafafa,#f5f5f5);box-sizing:border-box;max-width:100%!important;">
  <p style="font-size:10px;font-weight:bold;color:{A};letter-spacing:2px;margin:0 0 4px;">— END OF PREVIEW —</p>
  <p style="font-size:12px;color:{A};margin:0;">Vercel 极客主题 · 纯黑白灰配色 · {P}</p>
</section>

</section></body></html>"""

# Write
import pathlib
out = pathlib.Path("preview/all-variants.html")
out.write_text(html, encoding="utf-8")
print(f"Written: {out} ({len(html)} chars)")
