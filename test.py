#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 包管理系统使用示例
"""

import rez
from rez import packages
from rez.version import Version, VersionRange
from rez.config import config

print("=" * 60)
print("Rez 包管理系统使用演示")
print("=" * 60)

# 1. 查看 Rez 版本
print(f"\n1. Rez 版本: {rez.__version__}")

# 2. 获取默认包路径
print(f"\n2. 默认包搜索路径:")
if hasattr(config, 'packages_path'):
    for path in config.packages_path:
        print(f"   - {path}")
else:
    print("   - (未配置包路径)")

# 3. 列出可用的包
print(f"\n3. 搜索可用的包:")
try:
    pkg_families = list(packages.iter_package_families())
    if pkg_families:
        print(f"   找到 {len(pkg_families)} 个包族:")
        for family in pkg_families[:10]:  # 只显示前 10 个
            print(f"   - {family.name}")
        if len(pkg_families) > 10:
            print(f"   ... 还有 {len(pkg_families) - 10} 个包族")
    else:
        print("   未找到任何包")
except Exception as e:
    print(f"   搜索失败: {e}")

# 4. 创建简单的版本约束
print(f"\n4. 版本约束示例:")
versions = [
    "1.0.0",
    "1.2.3",
    "2.0.0+<3",
    "python-3.9+<4",
]

for v in versions:
    print(f"   {v}")

# 5. 解析版本
print(f"\n5. 版本解析:")
try:
    v = Version("1.2.3")
    print(f"   版本: {v}")
    print(f"   主版本: {v.major}, 次版本: {v.minor}, 修订版本: {v.patch}")
except Exception as e:
    print(f"   解析失败: {e}")

# 6. 环境相关信息
print(f"\n6. 环境信息:")
print(f"   Rez 版本: {rez.__version__}")
print(f"   Rez 本地包路径: {config.local_packages_path}")
print(f"   Rez 非本地包路径: {config.nonlocal_packages_path}")

print("\n" + "=" * 60)
print("更多 Rez 命令行工具（在终端中使用）:")
print("=" * 60)
print("""
# 查看 Rez CLI 工具
python -m rez.cli --help

# 常用命令
python -m rez.cli list              # 列出已安装的包
python -m rez.cli search            # 搜索包
python -m rez.cli env --help        # 创建环境（查看帮助）
python -m rez.cli build --help      # 构建包（查看帮助）
python -m rez.cli config --help     # 查看配置（查看帮助）

# 使用示例
python -m rez.cli env python       # 创建包含 python 的环境
python -m rez.cli search python    # 搜索 python 包
""")
