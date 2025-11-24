#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 实践测试脚本
演示如何使用 Rez API 进行包管理和环境操作
"""

import os
import sys
from pathlib import Path

# 配置本地包路径
os.environ['REZ_PACKAGES_PATH'] = str(Path(__file__).parent / "my_packages")

print("=" * 70)
print("Rez 实践测试")
print("=" * 70)

# 导入 Rez
from rez import packages
from rez.config import config
from rez.version import Version, VersionRange
from rez.resolved_context import ResolvedContext

print(f"\n1. 配置信息")
print(f"   Rez 版本: 3.3.0")
print(f"   包搜索路径: {config.packages_path}")

# 列出可用包
print(f"\n2. 搜索可用的包")
try:
    families = list(packages.iter_package_families())
    if families:
        print(f"   找到 {len(families)} 个包族:")
        for fam in families:
            versions = []
            try:
                pkgs = list(packages.iter_packages(fam.name))
                versions = [str(p.version) for p in pkgs]
            except:
                pass
            
            if versions:
                print(f"   - {fam.name}: {', '.join(versions)}")
            else:
                print(f"   - {fam.name}")
    else:
        print("   未找到任何包")
except Exception as e:
    print(f"   错误: {e}")

# 获取特定包信息
print(f"\n3. 获取包信息")
try:
    pkg = packages.get_package("myapp", "1.0.0")
    if pkg:
        print(f"   包名: {pkg.name}")
        print(f"   版本: {pkg.version}")
        print(f"   描述: {pkg.description}")
        print(f"   作者: {', '.join(pkg.authors)}")
        if hasattr(pkg, 'requires'):
            print(f"   依赖项: {pkg.requires}")
        if hasattr(pkg, 'variants'):
            print(f"   变体: {pkg.variants}")
    else:
        print("   未找到 myapp 包")
except Exception as e:
    print(f"   错误: {e}")

# 演示版本约束
print(f"\n4. 版本约束演示")
try:
    examples = [
        ("1.0.0", "精确版本"),
        ("1.0.0+", "1.0.0 及以上"),
        ("1.0+<2", "1.0 到 2.0（不含）"),
        ("python-3.9+<4", "Python 3.9 到 4.0"),
    ]
    
    for ver_str, desc in examples:
        try:
            v = VersionRange(ver_str)
            print(f"   {ver_str:20} → {desc}")
        except:
            v = Version(ver_str)
            print(f"   {ver_str:20} → 版本对象: {v}")
except Exception as e:
    print(f"   错误: {e}")

# 环境解析
print(f"\n5. 尝试解析环境")
try:
    # 这只是演示，可能会失败（如果缺少依赖项）
    contexts = ResolvedContext(["myapp"])
    print(f"   ✓ 成功解析环境")
    print(f"   已解析包: {[str(p) for p in contexts.resolved_packages]}")
except Exception as e:
    print(f"   环境解析失败（预期），原因: {type(e).__name__}")
    print(f"   说明: {str(e)[:100]}")

# 显示命令帮助
print(f"\n6. Rez 命令速查表")
print("""
   列表命令:
   • python -m rez.cli list                    # 列出包
   • python -m rez.cli search myapp            # 搜索包
   • python -m rez.cli package-info myapp-1.0.0  # 查看信息

   环境命令:
   • python -m rez.cli env myapp               # 进入环境
   • python -m rez.cli env myapp -- python -c "print('hello')"
   
   包管理:
   • python -m rez.cli build ./my_packages/myapp/1.0.0
   • python -m rez.cli validate ./package.py

   配置:
   • python -m rez.cli config                  # 查看配置
   • python -m rez.cli version                 # 查看版本
""")

# 构建建议
print(f"\n7. 后续建议")
print("""
   建议步骤：
   
   1️⃣  编辑 my_packages/myapp/1.0.0/package.py
      修改依赖项和环境配置
   
   2️⃣  在本地环境中测试包
      python -m rez.cli env myapp --print
   
   3️⃣  构建包到 Rez 仓库
      python -m rez.cli build ./my_packages/myapp/1.0.0
   
   4️⃣  创建包含多个依赖的环境
      python -m rez.cli env "myapp-1.0.0" "python-3.9"
   
   5️⃣  导出环境配置
      python -m rez.cli env myapp --create C:\\path\\to\\env
""")

print("\n" + "=" * 70)
print("✅ 测试完成！现在可以开始使用 Rez 了")
print("=" * 70)
