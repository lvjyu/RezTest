#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez GUI 和可视化工具演示
展示 Rez 如何进行可视化操作
"""

import subprocess
import sys

print("=" * 70)
print("Rez 可视化工具和 GUI 支持")
print("=" * 70)

# 1. 列出所有可用命令
print("\n1️⃣  Rez 所有可用命令:")
print("-" * 70)

from rez.cli._main import subcommands

commands = sorted(subcommands.keys())
print(f"总共 {len(commands)} 个命令:\n")

# 按功能分类显示
categories = {
    "🎨 可视化工具": ["gui", "view"],
    "📦 包管理": ["build", "release", "bind", "bundle"],
    "🔍 查询工具": ["search", "list", "depends", "context", "package-info"],
    "🛠️ 工具命令": ["env", "python", "test", "config"],
    "📋 文件操作": ["cp", "mv", "rm"],
    "🔧 系统工具": ["status", "memcache", "pkg-cache", "benchmark"],
    "⚙️ 其他": ["complete", "help", "plugins", "yaml2py", "suite", "bind", "forward", "diff"],
}

# 优先显示包含的命令
for category, cmds in categories.items():
    available = [c for c in cmds if c in commands]
    if available:
        print(f"{category}")
        for cmd in available:
            print(f"  • {cmd}")
        print()

# 2. GUI 工具信息
print("\n2️⃣  🎨 Rez GUI 工具 (可视化操作)")
print("-" * 70)

print("""
Rez 提供了原生的 GUI 工具进行可视化操作！

【启动 GUI】
  命令行运行:
    python -m rez.cli gui
  
  或者:
    rez gui

【GUI 功能】
  • 包浏览器 - 可视化浏览所有已安装的包
  • 包搜索 - 图形化搜索包
  • 版本管理 - 可视化管理包版本
  • 环境编辑 - 创建和编辑包环境
  • 依赖可视化 - 显示包之间的依赖关系图
  • 环境导出 - 导出和保存环境配置
""")

# 3. View 命令
print("\n3️⃣  📊 View 命令 (可视化查看环境)")
print("-" * 70)

print("""
用途: 以易于阅读的格式显示上下文和包信息

【基本用法】
  rez view <context>
  rez view --help

【显示内容】
  • 已解析的包及版本
  • 包之间的依赖关系
  • 环境变量配置
  • 解析时间和其他元数据
  
【示例】
  rez view "python-3.9 maya-2022"
  rez view -c /path/to/context.rez
""")

# 4. Context 命令
print("\n4️⃣  📋 Context 命令 (可视化环境信息)")
print("-" * 70)

print("""
用途: 查看、保存、比较环境上下文

【基本用法】
  rez context python-3.9               # 创建并查看上下文
  rez context --list                   # 列出所有保存的上下文
  rez context --serialize myenv.rez    # 导出上下文
  rez context -c myenv.rez             # 加载保存的上下文
  rez context --diff ctx1.rez ctx2.rez # 比较两个上下文
  
【可视化效果】
  显示完整的环境配置，包括:
  • 已解析的包列表
  • 环境变量
  • 冲突信息（如果有）
  • 性能统计
""")

# 5. Depends 命令
print("\n5️⃣  🔗 Depends 命令 (可视化依赖关系)")
print("-" * 70)

print("""
用途: 显示包的依赖关系树

【基本用法】
  rez depends <package>
  rez depends python-3.9
  rez depends --graph <package>  # 图形显示
  
【可视化格式】
  以树状或图形格式显示包的依赖树:
  
  Example:
  myapp-1.0.0
  ├── python-3.9
  │   ├── openssl-1.1.1
  │   └── zlib-1.2.11
  ├── maya-2022
  │   └── boost-1.73
  └── perforce-2021.1
""")

# 6. Diff 命令
print("\n6️⃣  📊 Diff 命令 (比较环境差异)")
print("-" * 70)

print("""
用途: 比较两个上下文或包配置的差异

【基本用法】
  rez diff ctx1.rez ctx2.rez    # 比较两个环境
  rez diff myapp-1.0.0 myapp-1.1.0  # 比较包版本
  
【显示内容】
  • 包版本差异
  • 新增/删除的包
  • 依赖关系变化
  • 环境变量变化
""")

# 7. 状态查询命令
print("\n7️⃣  ℹ️ Status 和其他查询命令")
print("-" * 70)

print("""
【rez status】
  查看 Rez 系统状态和配置信息
  
【rez config】
  查看完整的配置选项
  
【rez plugins】
  列出所有已安装的插件
  
【rez package-info】
  显示包的详细信息
  
【rez search】
  搜索包（支持过滤和排序）
""")

# 8. 综合示例
print("\n8️⃣  💻 综合使用示例")
print("-" * 70)

print("""
【场景 1: 浏览和查看包】
  1. rez gui                    # 打开 GUI 包浏览器
  2. 在 GUI 中搜索并点击包     # 可视化查看包信息
  
【场景 2: 创建并可视化环境】
  1. rez context python-3.9 maya-2022     # 创建环境
  2. rez view "python-3.9 maya-2022"     # 可视化查看
  3. rez context --serialize myenv.rez   # 保存环境
  
【场景 3: 比较和分析】
  1. rez context --list                  # 列出所有环境
  2. rez context --diff env1.rez env2.rez # 比较差异
  3. rez depends myapp-1.0.0 --graph     # 显示依赖图
  
【场景 4: 调试环境问题】
  1. rez context --serialize ctx.rez     # 导出上下文
  2. rez view -c ctx.rez                 # 分析上下文
  3. rez diff ctx1.rez ctx2.rez          # 比较历史版本
""")

# 9. 可视化工作流
print("\n9️⃣  🔄 完整的可视化工作流")
print("-" * 70)

print("""
【推荐工作流】

Step 1: 启动 GUI 浏览器
  > rez gui
  或者在代码中:
  > python -m rez.cli gui

Step 2: 创建环境
  > 在 GUI 中选择包
  > 或使用命令行: rez context python-3.9

Step 3: 可视化检查
  > rez view "python-3.9"          # 查看环境详情
  > rez depends myapp --graph      # 显示依赖
  > rez context --list             # 列出环境

Step 4: 对比分析
  > rez diff env1.rez env2.rez     # 比较两个环境
  > rez context --serialize save.rez # 保存当前环境

Step 5: 导出使用
  > 在 GUI 中导出环境
  > 或在脚本中加载: rez env -c saved.rez
""")

# 10. 获取帮助
print("\n🔟 获取更多帮助")
print("-" * 70)

print("""
【查看命令帮助】
  python -m rez.cli gui --help
  python -m rez.cli view --help
  python -m rez.cli context --help
  python -m rez.cli depends --help

【Rez 官方文档】
  https://rez.readthedocs.io/en/latest/cli/

【常用可视化工具】
  • GUI: 最直观的包管理界面
  • view: 快速查看环境
  • context: 完整的环境管理
  • depends: 依赖关系可视化
  • diff: 环境对比分析
""")

print("\n" + "=" * 70)
print("✅ Rez 提供多种可视化工具进行直观操作！")
print("=" * 70)
