#!/bin/bash

# 检查是否提供了参数
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <name>"
    exit 1
fi

# 定义输出文件的路径
output_file="../result/$1/$1.html"

# 检查输出目录是否存在，如果不存在则创建
output_dir=$(dirname "$output_file")
if [ ! -d "$output_dir" ]; then
    mkdir -p "$output_dir"
fi

# 执行xray命令并将输出重定向到文件
./xray webscan --listen 127.0.0.1:7777 --html-output "$output_file"

# 检查命令是否执行成功
if [ $? -eq 0 ]; then
    echo "Scan results saved to $output_file"
else
    echo "Failed to run xray webscan"
    exit 1
fi


