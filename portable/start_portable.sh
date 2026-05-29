#!/usr/bin/env bash
set -e
cd "$(dirname "$0")/.."

PYTHON_DIR="python"

# 查找嵌入式 Python
PYTHON_BIN=""
if [ -f "$PYTHON_DIR/bin/python" ]; then
    PYTHON_BIN="$PYTHON_DIR/bin/python"
elif [ -f "$PYTHON_DIR/Scripts/python.exe" ]; then
    PYTHON_BIN="$PYTHON_DIR/Scripts/python.exe"
elif [ -f "$PYTHON_DIR/python" ]; then
    PYTHON_BIN="$PYTHON_DIR/python"
elif [ -f "$PYTHON_DIR/python.exe" ]; then
    PYTHON_BIN="$PYTHON_DIR/python.exe"
fi

if [ -z "$PYTHON_BIN" ]; then
    echo ""
    echo "  [✗] 未找到便携 Python 环境！"
    echo ""
    echo "  请先运行 portable/setup_portable.sh 进行一键配置。"
    echo ""
    exit 1
fi

echo ""
echo "  ╔══════════════════════════════════════════╗"
echo "  ║     WeMD AI · 便携启动 (Portable)        ║"
echo "  ╚══════════════════════════════════════════╝"
echo ""

if [ -z "$DEEPSEEK_API_KEY" ]; then
    echo "  [⚠] 未设置 DEEPSEEK_API_KEY 环境变量"
    echo "      可以运行: export DEEPSEEK_API_KEY=sk-your-key"
    echo ""
fi

echo "  启动服务器..."
echo ""

exec "$PYTHON_BIN" server.py
