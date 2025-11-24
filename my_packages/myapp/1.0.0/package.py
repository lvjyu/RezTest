"""
示例 Rez 包
"""

name = "myapp"
version = "1.0.0"
description = "A sample Rez package"
authors = ["Your Name"]

# 包的依赖项（可选）
requires = []  # 留空表示无依赖

# 可选：定义系统需求
system_requires = []

# 可选：在环境中加载时执行的命令
def commands():
    import os
    # 设置环境变量
    env.MYAPP_ROOT = "{root}"
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib")

# 可选：定义包的变体（不同的配置）
variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
]

# 可选：项目文件夹
tools = []
