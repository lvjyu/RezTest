#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 可视化工具启动器
支持多种 GUI 和可视化方式
"""

import os
import sys
from pathlib import Path

# 设置包搜索路径
os.environ['REZ_PACKAGES_PATH'] = str(Path(__file__).parent / "my_packages")

def main():
    """主菜单"""
    print("\n" + "=" * 70)
    print("🎨 Rez 可视化工具启动器")
    print("=" * 70)
    print("\n选择可视化方式:\n")
    
    options = [
        ("📊 快速命令行查看", "quick_view"),
        ("🖥️  交互式菜单 GUI", "cli_gui"),
        ("⚡ 快速命令参考", "quick_ref"),
        ("🔧 原生 Qt GUI (需要 PyQt5)", "qt_gui"),
        ("📈 演示脚本", "demo"),
        ("❌ 退出", "exit"),
    ]
    
    for i, (desc, _) in enumerate(options, 1):
        print(f"  {i}. {desc}")
    
    print()
    choice = input("请选择 (1-6): ").strip()
    
    if choice == "1":
        quick_view()
    elif choice == "2":
        launch_cli_gui()
    elif choice == "3":
        show_quick_ref()
    elif choice == "4":
        launch_qt_gui()
    elif choice == "5":
        run_demo()
    elif choice == "6":
        print("\n👋 再见！\n")
        return
    else:
        print("\n❌ 无效选择\n")
        main()

def quick_view():
    """快速命令行查看"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 70)
    print("📊 快速命令行查看")
    print("=" * 70 + "\n")
    
    print("执行 Rez 状态查询...\n")
    os.system("python -m rez.cli status")
    
    input("\n按 Enter 返回主菜单...")
    main()

def launch_cli_gui():
    """启动交互式 CLI GUI"""
    print("\n🖥️  启动交互式菜单 GUI...\n")
    print("=" * 70)
    os.system("python rez_cli_gui.py")
    main()

def show_quick_ref():
    """显示快速参考"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 70)
    print("⚡ Rez 命令行可视化 - 快速参考")
    print("=" * 70 + "\n")
    
    print("""【常用可视化命令】

1️⃣  查看包搜索状态
   > python -m rez.cli status

2️⃣  查看系统配置
   > python -m rez.cli config

3️⃣  搜索包
   > python -m rez.cli search python
   > python -m rez.cli search myapp

4️⃣  查看包信息（创建环境）
   > python -m rez.cli context python-3.9
   > python -m rez.cli context python-3.9 maya-2022

5️⃣  查看环境详情
   > python -m rez.cli view "python-3.9"
   > python -m rez.cli view "python-3.9 maya-2022"

6️⃣  显示依赖树
   > python -m rez.cli depends myapp
   > python -m rez.cli depends myapp --graph

7️⃣  保存环境
   > python -m rez.cli context --serialize myenv.rez

8️⃣  加载环境
   > python -m rez.cli context -c myenv.rez

9️⃣  对比环境
   > python -m rez.cli diff env1.rez env2.rez

🔟  列出所有环境
   > python -m rez.cli context --list

【快速示例】

# 创建并查看 Python 3.9 环境
> python -m rez.cli context python-3.9

# 显示所有已安装的包
> python -m rez.cli search ""

# 查看系统状态
> python -m rez.cli status
""")
    
    input("\n按 Enter 返回主菜单...")
    main()

def launch_qt_gui():
    """启动原生 Qt GUI"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" + "=" * 70)
    print("🔧 启动原生 Qt GUI")
    print("=" * 70 + "\n")
    
    # 检查 PyQt5
    try:
        import PyQt5
        print("✅ PyQt5 已安装，启动 GUI...\n")
        os.system("python -m rez.cli gui")
    except ImportError:
        print("❌ PyQt5 未安装\n")
        print("请运行以下命令安装:\n")
        print("  pip install PyQt5\n")
        print("或者:\n")
        print("  pip install PySide2\n")
        print("然后运行:\n")
        print("  python -m rez.cli gui\n")
    
    input("按 Enter 返回主菜单...")
    main()

def run_demo():
    """运行演示脚本"""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n选择演示脚本:\n")
    
    demos = [
        ("GUI 和可视化工具演示", "rez_gui_visualization.py"),
        ("可视化操作实践", "rez_visualization_practice.py"),
        ("返回", None),
    ]
    
    for i, (desc, _) in enumerate(demos, 1):
        print(f"  {i}. {desc}")
    
    choice = input("\n请选择: ").strip()
    
    if choice == "1":
        os.system("python rez_gui_visualization.py")
    elif choice == "2":
        os.system("python rez_visualization_practice.py")
    
    main()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 已退出\n")
    except Exception as e:
        print(f"\n❌ 错误: {e}\n")
        import traceback
        traceback.print_exc()
