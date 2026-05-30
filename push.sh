#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"

MAX_RETRIES=20
RETRIES=0

echo ""
echo "  =========================================="
echo "    WeMD AI - Git Push"
echo "  =========================================="
echo ""

while [ $RETRIES -lt $MAX_RETRIES ]; do
    RETRIES=$((RETRIES + 1))
    echo "  [$RETRIES/$MAX_RETRIES] Pushing to GitHub..."

    if git push 2>&1; then
        echo ""
        echo "  =========================================="
        echo "    Push successful!"
        echo "  =========================================="
        exit 0
    fi

    echo "  [FAIL] Push failed (attempt $RETRIES/$MAX_RETRIES)"

    if [ $RETRIES -ge $MAX_RETRIES ]; then
        echo ""
        echo "  [ABORT] Max retries reached."
        echo "  Try again later or check your connection."
        exit 1
    fi

    echo "  Retrying in 5 seconds..."
    sleep 5
done
