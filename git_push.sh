#!/bin/bash

# 拉取最新的 Wiki 仓库内容
git pull origin main

# 提交本地更改
git add .
git commit -m "更新 Wiki 页面"

# 推送到 GitHub
git push origin main

if [ $? -eq 0 ]; then
    echo "Wiki 页面更新成功！"
else
    echo "Wiki 页面更新失败！"
fi