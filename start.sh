#!/bin/bash
# WeMD AI - AI Layout Engine
echo ""
echo "  WeMD AI - AI Layout Engine"
echo "  ================================"
echo ""
echo "  Starting server..."
echo ""
taskkill //f //im python.exe 2>/dev/null
python server.py
