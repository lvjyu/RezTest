# Rez 可视化操作指南

## 📌 核心答案

**是的！Rez 完全支持可视化操作。** 

Rez 提供了多种可视化工具来直观地管理包和环境：

| 工具 | 功能 | 用途 |
|------|------|------|
| **gui** | 图形用户界面 | 最直观的包管理 |
| **view** | 环境查看器 | 可视化查看环境详情 |
| **context** | 上下文管理 | 环保存、加载、比较 |
| **depends** | 依赖可视化 | 显示依赖树 |
| **diff** | 环境对比 | 比较两个环境的差异 |

---

## 🎨 Rez GUI 工具

### 启动 GUI

```powershell
# 方式 1: 使用 Python 模块
python -m rez.cli gui

# 方式 2: 直接命令（如果配置了路径）
rez gui
```

### GUI 功能

**Rez GUI 提供完整的图形界面：**

| 功能 | 说明 |
|------|------|
| **包浏览器** | 可视化浏览所有已安装的包 |
| **包搜索** | 图形化搜索和过滤包 |
| **版本选择** | 可视化选择包的版本 |
| **环境编辑** | 拖放式创建和编辑环境 |
| **依赖可视化** | 显示包之间的依赖关系 |
| **环境导出** | 导出和保存环境配置 |
| **实时预览** | 即时预览环境配置 |

### GUI 使用步骤

```
1. 运行: python -m rez.cli gui
   ↓
2. 打开图形窗口
   ↓
3. 浏览已安装的包
   ↓
4. 选择需要的包（可以多选）
   ↓
5. 查看依赖关系和冲突
   ↓
6. 创建或编辑环境
   ↓
7. 导出或保存环境配置
```

---

## 📊 View 命令 - 快速可视化

### 基本用法

```powershell
# 查看环境的详细信息
python -m rez.cli view "python-3.9 maya-2022"

# 查看已保存的环境
python -m rez.cli view -c /path/to/context.rez

# 获取帮助
python -m rez.cli view --help
```

### 输出示例

```
=== Context Information ===
Resolved Packages:
  • python-3.9.5
  • maya-2022.2
  • boost-1.73.0

Environment Variables:
  PYTHONPATH=/path/to/lib
  MAYA_ROOT=/path/to/maya
  PATH=/path/to/bin:...

Dependencies:
  python-3.9 (no dependencies)
  maya-2022 → boost-1.73, openssl-1.1.1
  boost-1.73 → zlib-1.2.11

Status: SUCCESS (resolved in 0.234s)
```

---

## 📋 Context 命令 - 环境管理

### 基本用法

```powershell
# 创建并查看上下文
python -m rez.cli context python-3.9

# 列出所有保存的环境
python -m rez.cli context --list

# 导出环境为文件
python -m rez.cli context --serialize myenv.rez

# 加载保存的环境
python -m rez.cli context -c myenv.rez

# 比较两个环境
python -m rez.cli context --diff env1.rez env2.rez
```

### 实际示例

```powershell
# Step 1: 创建环境
python -m rez.cli context python-3.9 maya-2022

# Step 2: 导出环境
python -m rez.cli context --serialize dev_env.rez

# Step 3: 列出所有环境
python -m rez.cli context --list

# Step 4: 加载并使用环境
python -m rez.cli env -c dev_env.rez
```

---

## 🔗 Depends 命令 - 依赖可视化

### 显示依赖树

```powershell
# 显示包的依赖
python -m rez.cli depends myapp

# 图形显示（如果支持）
python -m rez.cli depends myapp --graph

# 获取帮助
python -m rez.cli depends --help
```

### 输出示例

```
myapp-1.0.0
├── python-3.9
│   ├── openssl-1.1.1
│   │   └── zlib-1.2.11
│   └── zlib-1.2.11
├── maya-2022
│   ├── boost-1.73
│   ├── tbb-2020.2
│   └── openssl-1.1.1
└── perforce-2021.1
```

---

## 📊 Diff 命令 - 环境对比

### 基本用法

```powershell
# 比较两个环境文件
python -m rez.cli diff env1.rez env2.rez

# 比较两个包版本
python -m rez.cli diff myapp-1.0.0 myapp-2.0.0

# 获取帮助
python -m rez.cli diff --help
```

### 输出示例

```
Diff between env1.rez and env2.rez:

New packages:
  + openssl-1.1.1
  + zlib-1.2.11

Removed packages:
  - boost-1.72

Updated packages:
  python-3.8 → python-3.9
  maya-2021 → maya-2022

Changed dependencies:
  myapp: python-3.8 → python-3.9
```

---

## 🔍 其他可视化命令

### Status - 系统状态

```powershell
python -m rez.cli status
```

显示：
- Rez 版本
- 配置文件位置
- 包搜索路径
- Python 版本
- 插件信息

### Config - 配置可视化

```powershell
python -m rez.cli config
```

显示所有配置选项和当前值。

### Search - 包搜索

```powershell
# 搜索包
python -m rez.cli search python

# 显示所有版本
python -m rez.cli search myapp

# 搜索特定模式
python -m rez.cli search "python-3.*"
```

---

## 💻 完整的可视化工作流

### 工作流 1: 交互式包管理

```powershell
# 1. 启动 GUI
python -m rez.cli gui

# 2. 在 GUI 中进行以下操作：
#    - 浏览包
#    - 选择需要的包
#    - 查看依赖关系
#    - 创建环境

# 3. 导出环境
# (在 GUI 中或命令行)
python -m rez.cli context --serialize myenv.rez

# 4. 加载环境使用
python -m rez.cli env -c myenv.rez
```

### 工作流 2: 命令行可视化分析

```powershell
# 1. 创建环境
$env:REZ_PACKAGES_PATH = "E:\UE\RezTest\my_packages"
python -m rez.cli context python-3.9 myapp

# 2. 查看环境详情
python -m rez.cli view "python-3.9 myapp"

# 3. 显示依赖树
python -m rez.cli depends myapp --graph

# 4. 保存环境
python -m rez.cli context --serialize myenv.rez

# 5. 在未来加载使用
python -m rez.cli context -c myenv.rez
```

### 工作流 3: 环境对比和调试

```powershell
# 1. 创建两个不同的环境
python -m rez.cli context python-3.9 --serialize env1.rez
python -m rez.cli context python-3.10 --serialize env2.rez

# 2. 对比差异
python -m rez.cli diff env1.rez env2.rez

# 3. 查看详细信息
python -m rez.cli view -c env1.rez
python -m rez.cli view -c env2.rez

# 4. 分析哪个更合适
# (基于对比结果选择)
```

---

## 🎯 快速参考

### 常用可视化命令

| 需求 | 命令 |
|------|------|
| 打开 GUI | `python -m rez.cli gui` |
| 查看环境 | `python -m rez.cli view "pkg1 pkg2"` |
| 创建环境 | `python -m rez.cli context pkg1 pkg2` |
| 保存环境 | `python -m rez.cli context --serialize env.rez` |
| 加载环境 | `python -m rez.cli context -c env.rez` |
| 显示依赖 | `python -m rez.cli depends myapp` |
| 对比环境 | `python -m rez.cli diff env1.rez env2.rez` |
| 列出环境 | `python -m rez.cli context --list` |
| 系统状态 | `python -m rez.cli status` |
| 查看配置 | `python -m rez.cli config` |

---

## 📚 Python API 可视化

### 通过 Python 代码获取可视化数据

```python
from rez.resolved_context import ResolvedContext
from rez import packages

# 1. 创建上下文
ctx = ResolvedContext(["python-3.9", "maya-2022"])

# 2. 获取已解析的包
print("Resolved packages:")
for pkg in ctx.resolved_packages:
    print(f"  • {pkg.qualified_name}")

# 3. 显示依赖
print("\nDependencies:")
for pkg in ctx.resolved_packages:
    if hasattr(pkg, 'requires'):
        for req in pkg.requires:
            print(f"  {pkg.name} → {req}")

# 4. 显示环境变量
print("\nEnvironment variables:")
env = ctx.get_environ()
for key in sorted(env.keys())[:10]:
    print(f"  {key}={env[key][:50]}...")
```

---

## 🔧 高级可视化技巧

### 1. 生成依赖图

```powershell
# 使用 graphviz（如果安装）
python -m rez.cli depends myapp --format=dot | dot -Tpng -o deps.png
```

### 2. 批量对比环境

```powershell
# 创建脚本对比多个环境
python -c "
import subprocess
envs = ['env1.rez', 'env2.rez', 'env3.rez']
for i, env1 in enumerate(envs):
    for env2 in envs[i+1:]:
        print(f'\n=== Diff {env1} vs {env2} ===')
        subprocess.run(['python', '-m', 'rez.cli', 'diff', env1, env2])
"
```

### 3. 导出为人类可读格式

```powershell
# 导出环境信息
python -m rez.cli context python-3.9 > env_info.txt
python -m rez.cli view "python-3.9" >> env_info.txt
```

---

## ✨ 优势总结

**为什么使用 Rez 的可视化工具？**

✅ **直观** - GUI 界面简单易用
✅ **完整** - 查看所有环境信息
✅ **对比** - 轻松比较不同环境
✅ **调试** - 快速定位问题
✅ **导出** - 保存和共享环境配置
✅ **可扩展** - 支持自定义插件和扩展

---

## 🚀 立即开始

```powershell
# 1. 首先打开 GUI 体验可视化界面
python -m rez.cli gui

# 2. 或者使用命令行可视化工具
python -m rez.cli status          # 查看系统状态
python -m rez.cli search python   # 搜索包
python -m rez.cli view "python-3.9"  # 查看环境

# 3. 导出和比较
python -m rez.cli context --serialize myenv.rez
python -m rez.cli context --list
```

---

## 📖 更多信息

- [Rez 官方 GUI 文档](https://rez.readthedocs.io/en/latest/cli/gui.html)
- [View 命令文档](https://rez.readthedocs.io/en/latest/cli/view.html)
- [Context 命令文档](https://rez.readthedocs.io/en/latest/cli/context.html)
- [Rez CLI 完整文档](https://rez.readthedocs.io/en/latest/cli/)
