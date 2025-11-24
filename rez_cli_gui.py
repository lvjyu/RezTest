#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 可视化命令行界面 (CLI GUI)
提供交互式菜单，无需 Qt 依赖
"""

import os
import sys
from pathlib import Path

# 设置包搜索路径
os.environ['REZ_PACKAGES_PATH'] = str(Path(__file__).parent / "my_packages")

from rez import packages
from rez.resolved_context import ResolvedContext
from rez.cli._main import run as cli_run

def clear_screen():
    """清屏"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(title):
    """打印标题"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70 + "\n")

def print_menu(options):
    """打印菜单"""
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print(f"  0. 返回\n")

def show_main_menu():
    """主菜单"""
    while True:
        clear_screen()
        print_header("🎨 Rez 可视化操作界面 (CLI)")
        
        print("  选择功能:\n")
        options = [
            "📦 包管理 - 浏览和管理包",
            "🔗 依赖分析 - 查看包的依赖关系",
            "⚙️  环境管理 - 创建和管理环境",
            "📊 状态查看 - 查看 Rez 系统状态",
            "ℹ️  配置信息 - 查看配置选项",
            "🔍 搜索包 - 搜索特定的包",
            "❌ 退出"
        ]
        print_menu(options)
        
        choice = input("请选择 (0-6): ").strip()
        
        if choice == "1":
            show_packages_menu()
        elif choice == "2":
            show_depends_menu()
        elif choice == "3":
            show_environment_menu()
        elif choice == "4":
            show_status()
        elif choice == "5":
            show_config()
        elif choice == "6":
            search_packages()
        elif choice == "7":
            print("\n👋 再见！")
            break
        else:
            print("❌ 无效的选择，请重试")
            input("按 Enter 继续...")

def show_packages_menu():
    """包管理菜单"""
    while True:
        clear_screen()
        print_header("📦 包管理")
        
        # 列出所有包
        families = list(packages.iter_package_families())
        
        if not families:
            print("  ⚠️  未找到任何包\n")
            input("按 Enter 返回...")
            return
        
        print(f"  找到 {len(families)} 个包:\n")
        
        package_list = []
        for i, family in enumerate(families, 1):
            versions = []
            try:
                pkgs = list(packages.iter_packages(family.name))
                versions = [str(p.version) for p in pkgs]
            except:
                pass
            
            version_str = ", ".join(versions) if versions else "unknown"
            print(f"  {i}. {family.name}")
            print(f"     版本: {version_str}\n")
            package_list.append(family.name)
        
        print("  0. 返回主菜单")
        
        choice = input("选择包查看详情 (0 返回): ").strip()
        
        if choice == "0":
            break
        
        try:
            idx = int(choice) - 1
            if 0 <= idx < len(package_list):
                show_package_details(package_list[idx])
        except:
            pass

def show_package_details(package_name):
    """显示包详情"""
    clear_screen()
    print_header(f"📋 包详情: {package_name}")
    
    try:
        families = list(packages.iter_package_families())
        versions = []
        
        for family in families:
            if family.name == package_name:
                pkgs = list(packages.iter_packages(package_name))
                for pkg in pkgs:
                    versions.append(pkg)
                break
        
        if versions:
            # 显示最新版本的详情
            pkg = versions[-1]
            print(f"  📦 名称: {pkg.name}")
            print(f"  📌 版本: {pkg.version}")
            print(f"  📝 描述: {pkg.description}")
            print(f"  👥 作者: {', '.join(pkg.authors) if pkg.authors else '未知'}")
            print(f"  🔗 依赖项: {pkg.requires if pkg.requires else '无'}")
            print(f"  🔄 变体: {len(pkg.variants) if hasattr(pkg, 'variants') else 0} 个")
            print(f"  📂 位置: {pkg.root}\n")
        else:
            print(f"  ❌ 找不到包 {package_name}")
    
    except Exception as e:
        print(f"  ❌ 错误: {e}")
    
    input("按 Enter 返回...")

def show_depends_menu():
    """依赖分析菜单"""
    clear_screen()
    print_header("🔗 依赖分析")
    
    families = list(packages.iter_package_families())
    
    if not families:
        print("  ⚠️  未找到任何包\n")
        input("按 Enter 返回...")
        return
    
    print("  可用的包:\n")
    
    package_list = []
    for i, family in enumerate(families, 1):
        print(f"  {i}. {family.name}")
        package_list.append(family.name)
    
    print("\n  0. 返回主菜单")
    
    choice = input("选择包查看依赖 (0 返回): ").strip()
    
    if choice == "0":
        return
    
    try:
        idx = int(choice) - 1
        if 0 <= idx < len(package_list):
            package_name = package_list[idx]
            show_dependencies(package_name)
    except:
        pass

def show_dependencies(package_name):
    """显示包的依赖关系"""
    clear_screen()
    print_header(f"🔗 {package_name} 的依赖关系")
    
    try:
        pkg = packages.get_package(package_name, "")  # 获取最新版本
        
        if pkg:
            print(f"  {package_name}\n")
            
            if pkg.requires:
                print("  依赖于:\n")
                for req in pkg.requires:
                    print(f"    └── {req}")
                print()
            else:
                print("  此包没有依赖项\n")
        else:
            print(f"  ❌ 找不到包 {package_name}")
    
    except Exception as e:
        print(f"  ❌ 错误: {e}")
    
    input("按 Enter 返回...")

def show_environment_menu():
    """环境管理菜单"""
    clear_screen()
    print_header("⚙️  环境管理")
    
    print("  选择功能:\n")
    options = [
        "创建新环境",
        "查看已保存的环境",
        "对比两个环境"
    ]
    print_menu(options)
    
    choice = input("请选择: ").strip()
    
    if choice == "1":
        create_environment()
    elif choice == "2":
        view_saved_environments()
    elif choice == "3":
        compare_environments()

def create_environment():
    """创建新环境"""
    clear_screen()
    print_header("⚙️  创建新环境")
    
    families = list(packages.iter_package_families())
    
    if families:
        print("  可用的包:\n")
        for i, family in enumerate(families, 1):
            print(f"  {i}. {family.name}")
        
        choice = input("\n选择包 (输入数字，多个用逗号分隔): ").strip()
        
        try:
            indices = [int(x.strip())-1 for x in choice.split(",")]
            selected = [families[i].name for i in indices if 0 <= i < len(families)]
            
            if selected:
                print(f"\n  正在创建环境: {', '.join(selected)}\n")
                
                try:
                    ctx = ResolvedContext(selected)
                    
                    print(f"  ✅ 环境创建成功！\n")
                    print(f"  已解析的包:")
                    for pkg in ctx.resolved_packages:
                        print(f"    ✓ {pkg.qualified_name}")
                except Exception as e:
                    print(f"  ❌ 创建失败: {e}")
        except:
            print("  ❌ 输入有误")
    
    input("\n按 Enter 返回...")

def view_saved_environments():
    """查看已保存的环境"""
    clear_screen()
    print_header("💾 已保存的环境")
    
    print("  此功能需要先使用 context --serialize 保存环境\n")
    print("  保存环境的方法:")
    print("    python -m rez.cli context --serialize myenv.rez\n")
    print("  加载环境的方法:")
    print("    python -m rez.cli context -c myenv.rez\n")
    
    input("按 Enter 返回...")

def compare_environments():
    """对比环境"""
    clear_screen()
    print_header("📊 对比环境")
    
    print("  此功能需要已保存的环境文件\n")
    print("  对比命令:")
    print("    python -m rez.cli diff env1.rez env2.rez\n")
    
    input("按 Enter 返回...")

def show_status():
    """显示系统状态"""
    clear_screen()
    print_header("📊 Rez 系统状态")
    
    try:
        import rez
        print(f"  Rez 版本: {rez.__version__}")
        print(f"  Rez 位置: {rez.__file__}")
        
        from rez.config import config
        print(f"\n  包搜索路径:")
        if hasattr(config, 'packages_path'):
            for path in config.packages_path:
                print(f"    • {path}")
        
        families = list(packages.iter_package_families())
        print(f"\n  已安装的包: {len(families)} 个")
        
        if families:
            print("\n  包列表:")
            for family in families:
                print(f"    • {family.name}")
    
    except Exception as e:
        print(f"  ❌ 错误: {e}")
    
    input("\n按 Enter 返回...")

def show_config():
    """显示配置信息"""
    clear_screen()
    print_header("ℹ️  Rez 配置信息")
    
    try:
        from rez.config import config
        
        print("  主要配置项:\n")
        
        # 显示关键配置
        if hasattr(config, 'packages_path'):
            print(f"  📦 包搜索路径:")
            for path in config.packages_path:
                print(f"     {path}")
        
        if hasattr(config, 'local_packages_path'):
            print(f"\n  📂 本地包路径: {config.local_packages_path}")
        
        if hasattr(config, 'nonlocal_packages_path'):
            print(f"\n  📂 非本地包路径:")
            for path in config.nonlocal_packages_path:
                print(f"     {path}")
        
        print("\n  查看完整配置: python -m rez.cli config")
    
    except Exception as e:
        print(f"  ❌ 错误: {e}")
    
    input("\n按 Enter 返回...")

def search_packages():
    """搜索包"""
    clear_screen()
    print_header("🔍 搜索包")
    
    keyword = input("  输入搜索关键词: ").strip()
    
    if not keyword:
        return
    
    clear_screen()
    print_header(f"🔍 搜索结果: '{keyword}'")
    
    try:
        families = list(packages.iter_package_families())
        results = [f for f in families if keyword.lower() in f.name.lower()]
        
        if results:
            print(f"  找到 {len(results)} 个结果:\n")
            
            for family in results:
                versions = []
                try:
                    pkgs = list(packages.iter_packages(family.name))
                    versions = [str(p.version) for p in pkgs]
                except:
                    pass
                
                version_str = ", ".join(versions) if versions else "unknown"
                print(f"  📦 {family.name}")
                print(f"     版本: {version_str}\n")
        else:
            print(f"  ❌ 未找到匹配 '{keyword}' 的包")
    
    except Exception as e:
        print(f"  ❌ 搜索失败: {e}")
    
    input("\n按 Enter 返回...")

if __name__ == "__main__":
    try:
        show_main_menu()
    except KeyboardInterrupt:
        print("\n\n👋 已退出")
    except Exception as e:
        print(f"\n❌ 错误: {e}")
        import traceback
        traceback.print_exc()
