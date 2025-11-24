#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 可视化操作实践脚本
演示如何使用 Rez 的可视化工具进行操作
"""

import os
import sys
from pathlib import Path

# 设置包搜索路径
os.environ['REZ_PACKAGES_PATH'] = str(Path(__file__).parent / "my_packages")

print("=" * 75)
print("Rez 可视化操作实践")
print("=" * 75)

from rez import packages
from rez.resolved_context import ResolvedContext
from rez.version import Version

# 1. 可视化包浏览
print("\n1️⃣  包浏览 - 可视化查看所有包")
print("-" * 75)

families = list(packages.iter_package_families())
print(f"找到 {len(families)} 个包:\n")

for family in families:
    versions = []
    try:
        pkgs = list(packages.iter_packages(family.name))
        versions = [str(p.version) for p in pkgs]
        print(f"  📦 {family.name}")
        for v in versions:
            print(f"     ├─ v{v}")
    except:
        pass

# 2. 可视化包信息
print("\n2️⃣  包信息可视化 - 显示详细的包信息")
print("-" * 75)

try:
    pkg = packages.get_package('myapp', '1.0.0')
    if pkg:
        print(f"\n  📋 包详情:")
        print(f"    ├─ 名称: {pkg.name}")
        print(f"    ├─ 版本: {pkg.version}")
        print(f"    ├─ 描述: {pkg.description}")
        print(f"    ├─ 作者: {', '.join(pkg.authors)}")
        print(f"    ├─ 依赖项: {pkg.requires if pkg.requires else '无'}")
        print(f"    └─ 变体: {len(pkg.variants)} 个")
except Exception as e:
    print(f"  ⚠️  获取包信息失败: {e}")

# 3. 可视化版本树
print("\n3️⃣  版本可视化 - 显示版本层次")
print("-" * 75)

print("\n  Rez 版本树结构示例:")
print("""
  myapp/
  ├── 1.0.0
  │   ├── package.py
  │   ├── bin/
  │   └── lib/
  ├── 1.1.0
  │   ├── package.py
  │   ├── bin/
  │   └── lib/
  └── 2.0.0
      ├── package.py
      ├── bin/
      └── lib/
""")

# 4. 可视化依赖关系
print("\n4️⃣  依赖关系可视化 - 显示包的依赖树")
print("-" * 75)

print("\n  依赖树示例 (如果有依赖):\n")
print("""  myapp-1.0.0
  ├── python-3.9
  │   ├── openssl-1.1.1
  │   │   └── zlib-1.2.11
  │   └── zlib-1.2.11
  ├── maya-2022
  │   ├── boost-1.73
  │   ├── tbb-2020.2
  │   └── openssl-1.1.1
  └── perforce-2021.1
""")

# 5. 可视化环境配置
print("\n5️⃣  环境配置可视化 - 显示环境变量")
print("-" * 75)

try:
    # 由于本地可能没有完整的依赖，尝试创建简单环境
    print("\n  环境变量示例:\n")
    print("""  环境: myapp-1.0.0
  
  已解析的包:
  ├── myapp-1.0.0
  
  环境变量:
  ├── MYAPP_ROOT=/path/to/myapp/1.0.0
  ├── MYAPP_VERSION=1.0.0
  ├── PATH=/path/to/myapp/1.0.0/bin:...
  └── PYTHONPATH=/path/to/myapp/1.0.0/lib:...
  
  配置状态:
  └── 解析成功 (耗时: 0.234s)
""")
except Exception as e:
    print(f"  环境解析信息: {e}")

# 6. 可视化命令列表
print("\n6️⃣  可用的可视化命令")
print("-" * 75)

from rez.cli._main import subcommands

viz_commands = {
    "🎨 GUI 工具": ["gui"],
    "📊 查看工具": ["view", "context"],
    "🔗 依赖分析": ["depends"],
    "📋 比较工具": ["diff"],
    "🔍 查询工具": ["search", "list"],
    "ℹ️  信息工具": ["status", "config", "plugins"],
}

print("\n  推荐的可视化命令:\n")
for category, cmds in viz_commands.items():
    available = [c for c in cmds if c in subcommands]
    if available:
        print(f"  {category}")
        for cmd in available:
            print(f"    • python -m rez.cli {cmd}")
        print()

# 7. 可视化工作流
print("\n7️⃣  推荐的可视化工作流")
print("-" * 75)

workflow = """
  【交互式工作流】
  
  Step 1: 启动 GUI
  ┌──────────────────────────────────────┐
  │ python -m rez.cli gui               │
  │ ↓                                    │
  │ 图形界面打开                          │
  └──────────────────────────────────────┘
  
  Step 2: 在 GUI 中
  ┌──────────────────────────────────────┐
  │ • 浏览可用的包                         │
  │ • 搜索需要的包                         │
  │ • 选择包版本                           │
  │ • 查看依赖关系                         │
  │ • 预览冲突                             │
  └──────────────────────────────────────┘
  
  Step 3: 创建环境
  ┌──────────────────────────────────────┐
  │ python -m rez.cli context pkg1 pkg2 │
  │ ↓                                    │
  │ 显示环境详情                           │
  └──────────────────────────────────────┘
  
  Step 4: 可视化检查
  ┌──────────────────────────────────────┐
  │ python -m rez.cli view "pkg1 pkg2"  │
  │ ↓                                    │
  │ 显示完整的环境信息                     │
  └──────────────────────────────────────┘
  
  Step 5: 导出保存
  ┌──────────────────────────────────────┐
  │ python -m rez.cli context            │
  │   --serialize myenv.rez              │
  │ ↓                                    │
  │ 保存环境配置文件                       │
  └──────────────────────────────────────┘
"""

print(workflow)

# 8. 命令行可视化示例
print("\n8️⃣  命令行可视化示例")
print("-" * 75)

print("""
  【快速命令参考】
  
  # 查看包信息
  python -m rez.cli search myapp
  
  # 显示系统状态
  python -m rez.cli status
  
  # 查看配置
  python -m rez.cli config
  
  # 创建并查看环境
  python -m rez.cli context python-3.9
  python -m rez.cli view "python-3.9"
  
  # 显示依赖树
  python -m rez.cli depends myapp
  python -m rez.cli depends myapp --graph
  
  # 保存和加载环境
  python -m rez.cli context --serialize myenv.rez
  python -m rez.cli context -c myenv.rez
  
  # 对比环境
  python -m rez.cli diff env1.rez env2.rez
  
  # 列出所有环境
  python -m rez.cli context --list
""")

# 9. 可视化输出示例
print("\n9️⃣  Rez View 的输出示例")
print("-" * 75)

view_example = """
  === Context View ===
  
  Resolved Packages (2):
    • myapp-1.0.0
    • python-3.9.5
  
  Request:
    • myapp
    • python-3.9
  
  Status: solved
  Solve time: 0.123 seconds
  
  Packages:
    myapp-1.0.0:
      • description: My Application
      • location: /path/to/myapp/1.0.0
      • requires: []
      • variants: 3
    
    python-3.9.5:
      • description: Python 3.9.5
      • location: /path/to/python/3.9.5
      • requires: []
      • variants: 0
  
  Environment Variables:
    MYAPP_ROOT: /path/to/myapp/1.0.0
    MYAPP_VERSION: 1.0.0
    PATH: /path/to/myapp/1.0.0/bin:...
    PYTHONPATH: /path/to/myapp/1.0.0/lib:...
"""

print(view_example)

# 10. 总结
print("\n🔟 可视化操作总结")
print("-" * 75)

print("""
  ✅ Rez 可视化工具特点:
  
  • GUI 界面    - 最直观的包管理体验
  • View 命令   - 快速查看环境详情
  • Context 命令 - 完整的环境管理
  • Depends 命令 - 依赖关系可视化
  • Diff 命令   - 环境对比分析
  
  📊 可视化优势:
  
  • 简化复杂操作   - 无需记住所有命令
  • 快速定位问题   - 一眼看出问题所在
  • 避免手误       - 图形化选择更安全
  • 便于共享       - 导出配置易于分享
  • 学习友好       - 初学者容易上手
  
  🎯 最佳实践:
  
  1. 使用 GUI 进行交互式操作
  2. 用 view 快速查看环境
  3. 用 diff 对比不同配置
  4. 用 depends 分析依赖
  5. 用 context --serialize 保存环境
""")

print("\n" + "=" * 75)
print("✨ 现在就开始使用 Rez 的可视化工具吧！")
print("=" * 75)

# 显示如何启动 GUI
print("\n【立即启动 GUI】")
print("  > python -m rez.cli gui")
print()
