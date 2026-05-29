#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║     WeMD AI · 便携 Python 环境配置       ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""
echo "  正在准备嵌入式 Python 环境..."
echo ""

# ============================================================
# 配置
# ============================================================
PYTHON_VERSION="3.10.11"
PYTHON_DIR="python"
PYTHON_TAR="python-${PYTHON_VERSION}-embed-$(uname -m).tar.xz"
GET_PIP_URL="https://bootstrap.pypa.io/get-pip.py"

# 检测架构
ARCH=$(uname -m)
if [ "$ARCH" = "x86_64" ]; then
    PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz"
    USE_EMBED=false
elif [ "$ARCH" = "aarch64" ] || [ "$ARCH" = "arm64" ]; then
    PYTHON_URL="https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz"
    USE_EMBED=false
else
    echo "  [✗] 不支持的架构: $ARCH"
    exit 1
fi

# ============================================================
# 检查是否已安装
# ============================================================
if [ -f "$PYTHON_DIR/bin/python3" ] || [ -f "$PYTHON_DIR/python" ]; then
    echo "  [✓] 检测到已有 python/ 目录"
    echo ""
    read -p "  是否重新配置？(y/N): " -t 10 -n 1 CONFIRM
    echo ""
    if [ "$CONFIRM" != "y" ] && [ "$CONFIRM" != "Y" ]; then
        echo "  跳过配置..."
        python "$PYTHON_DIR/bin/python3" --version 2>/dev/null || "$PYTHON_DIR/python" --version 2>/dev/null
        exit 0
    fi
    echo "  正在删除旧的 python/ 目录..."
    rm -rf "$PYTHON_DIR"
fi

# ============================================================
# Linux/macOS: 使用系统 Python 或 pyenv 更具可移植性
# 这里提供两种策略：
#   A) 优先使用系统已安装的 Python（如果有）
#   B) 否则下载 miniconda 或编译版 Python
# ============================================================
echo "  [注意] Linux/macOS 嵌入式 Python 需要从源码编译，比较耗时。"
echo "  推荐直接安装系统 Python 后使用原始 start.sh。"
echo "  本脚本将尝试使用系统 Python 创建虚拟环境到 python/ 目录。"
echo ""

# 查找系统 Python
PYTHON_BIN=""
for p in python3 python; do
    if command -v "$p" &>/dev/null; then
        VER=$("$p" --version 2>&1 | grep -oP '\d+\.\d+')
        MAJOR=$(echo "$VER" | cut -d. -f1)
        MINOR=$(echo "$VER" | cut -d. -f2)
        if [ "$MAJOR" -ge 3 ] && [ "$MINOR" -ge 8 ]; then
            PYTHON_BIN="$p"
            break
        fi
    fi
done

if [ -z "$PYTHON_BIN" ]; then
    echo "  [✗] 未找到 Python 3.8+！"
    echo "  请先安装 Python:"
    echo "    macOS: brew install python@3.10"
    echo "    Ubuntu/Debian: sudo apt install python3 python3-venv python3-pip"
    echo "    CentOS/RHEL: sudo yum install python3 python3-pip"
    exit 1
fi

echo "  [1/3] 使用系统 Python: $($PYTHON_BIN --version)"
echo "        创建虚拟环境到 python/ ..."
"$PYTHON_BIN" -m venv "$PYTHON_DIR"

# 激活并安装依赖
echo ""
echo "  [2/3] 安装项目依赖..."
if [ -f "$PYTHON_DIR/bin/activate" ]; then
    source "$PYTHON_DIR/bin/activate"
    pip install --upgrade pip -q
    pip install flask requests -q
    deactivate
elif [ -f "$PYTHON_DIR/Scripts/activate" ]; then
    source "$PYTHON_DIR/Scripts/activate"
    pip install --upgrade pip -q
    pip install flask requests -q
    deactivate
fi

# ============================================================
# 验证
# ============================================================
echo ""
echo "  [3/3] 验证环境..."
echo ""
if [ -f "$PYTHON_DIR/bin/python" ]; then
    "$PYTHON_DIR/bin/python" -c "import flask; import requests; print(f'  Python {__import__(\"sys\").version.split()[0]}'); print(f'  Flask {flask.__version__}'); print(f'  requests {requests.__version__}')"
elif [ -f "$PYTHON_DIR/Scripts/python.exe" ]; then
    "$PYTHON_DIR/Scripts/python.exe" -c "import flask; import requests; print(f'  Python {__import__(\"sys\").version.split()[0]}'); print(f'  Flask {flask.__version__}'); print(f'  requests {requests.__version__}')"
fi

# ============================================================
# 完成
# ============================================================
echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║         ✓ 配置完成！                     ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""
echo "  启动方式:"
echo "    bash portable/start_portable.sh"
echo ""
echo "  首次使用需设置 DeepSeek API Key:"
echo "    export DEEPSEEK_API_KEY=sk-your-key"
echo "    bash portable/start_portable.sh"
echo ""
