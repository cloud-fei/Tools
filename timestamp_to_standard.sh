i#!/bin/bash

# 检查参数是否存在
if [ $# -ne 1 ]; then
    echo "Usage: $0 timestamp"
    exit 1
fi

# 将时间戳转换为标准时间
timestamp=$1
date=$(date -d @$timestamp)

echo "Timestamp: $timestamp"
echo "Standard Time: $date"

