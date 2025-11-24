# Rez 可视化操作 - 快速参考卡

## ✅ 核心答案

**Rez 完全支持可视化操作！**

| 工具 | 功能 | 命令 |
|------|------|------|
| **GUI** | 图形界面包管理 | `python -m rez.cli gui` |
| **View** | 查看环境详情 | `python -m rez.cli view` |
| **Context** | 环境管理和对比 | `python -m rez.cli context` |
| **Depends** | 依赖关系树 | `python -m rez.cli depends` |
| **Diff** | 环境对比 | `python -m rez.cli diff` |

---

## 🎨 GUI 工具 - 最直观的方式

### 启动 GUI

```powershell
python -m rez.cli gui
```

### GUI 功能
- 📦 包浏览和搜索
- 🔗 依赖关系可视化
- ➕ 拖放式环境创建
- 💾 环境导出和保存
- ⚠️ 冲突检测

---

## 📊 常用可视化命令速查

### 快速查看环境

```powershell
# 查看环境详情
python -m rez.cli view "python-3.9 maya-2022"

# 创建并查看环境
python -m rez.cli context python-3.9

# 列出所有环境
python -m rez.cli context --list
```

### 保存和加载环境

```powershell
# 导出环境
python -m rez.cli context --serialize myenv.rez

# 加载环境
python -m rez.cli context -c myenv.rez
```

### 依赖和对比

```powershell
# 显示依赖树
python -m rez.cli depends myapp

# 对比两个环境
python -m rez.cli diff env1.rez env2.rez
```

### 系统信息

```powershell
# 系统状态
python -m rez.cli status

# 查看配置
python -m rez.cli config

# 搜索包
python -m rez.cli search python
```

---

## 💻 工作流示例

### 方案 1: GUI 交互式操作

```
1. python -m rez.cli gui
   ↓
2. 在 GUI 中浏览包
   ↓
3. 选择需要的包（多选）
   ↓
4. 查看依赖关系
   ↓
5. 点击"创建环境"
   ↓
6. 导出环境配置
```

### 方案 2: 命令行可视化

```powershell
# 创建环境
python -m rez.cli context python-3.9 myapp

# 查看详情
python -m rez.cli view "python-3.9 myapp"

# 显示依赖
python -m rez.cli depends myapp --graph

# 保存配置
python -m rez.cli context --serialize dev.rez
```

### 方案 3: 环境对比分析

```powershell
# 创建两个不同的环境
python -m rez.cli context python-3.9 --serialize env1.rez
python -m rez.cli context python-3.10 --serialize env2.rez

# 对比差异
python -m rez.cli diff env1.rez env2.rez

# 查看详细信息
python -m rez.cli view -c env1.rez
python -m rez.cli view -c env2.rez
```

---

## 🔍 详细命令参考

### gui - 图形用户界面

```powershell
python -m rez.cli gui              # 启动 GUI
python -m rez.cli gui --help       # 查看帮助
```

**功能:**
- 可视化浏览包
- 搜索和过滤
- 环境编辑和创建
- 依赖关系显示
- 配置导出

### view - 查看环境

```powershell
# 查看环境
python -m rez.cli view "python-3.9"

# 查看已保存的环境
python -m rez.cli view -c myenv.rez

# 帮助信息
python -m rez.cli view --help
```

**输出内容:**
- 已解析的包
- 环境变量
- 依赖信息
- 性能统计

### context - 环境管理

```powershell
# 创建环境
python -m rez.cli context python-3.9

# 保存环境
python -m rez.cli context --serialize env.rez

# 加载环境
python -m rez.cli context -c env.rez

# 列出所有环境
python -m rez.cli context --list

# 比较环境
python -m rez.cli context --diff env1.rez env2.rez

# 帮助信息
python -m rez.cli context --help
```

### depends - 依赖关系

```powershell
# 显示依赖
python -m rez.cli depends myapp

# 图形显示
python -m rez.cli depends myapp --graph

# 帮助信息
python -m rez.cli depends --help
```

**输出格式:**
```
myapp-1.0.0
├── python-3.9
│   └── zlib-1.2.11
├── maya-2022
│   └── boost-1.73
└── perforce-2021.1
```

### diff - 环境对比

```powershell
# 对比两个环境
python -m rez.cli diff env1.rez env2.rez

# 对比两个包
python -m rez.cli diff myapp-1.0.0 myapp-2.0.0

# 帮助信息
python -m rez.cli diff --help
```

**显示内容:**
- 新增包
- 删除包
- 更新包
- 依赖变化

### search - 搜索包

```powershell
# 搜索包
python -m rez.cli search python

# 显示所有版本
python -m rez.cli search myapp

# 模式搜索
python -m rez.cli search "python-3.*"

# 帮助信息
python -m rez.cli search --help
```

---

## 📱 Python API 可视化

```python
from rez.resolved_context import ResolvedContext
from rez import packages

# 列出包
families = packages.iter_package_families()
for f in families:
    print(f"📦 {f.name}")

# 获取包信息
pkg = packages.get_package("myapp", "1.0.0")
print(f"🔹 {pkg.name} v{pkg.version}")
print(f"📝 {pkg.description}")
print(f"👥 {pkg.authors}")

# 查看已解析的包
ctx = ResolvedContext(["myapp"])
for pkg in ctx.resolved_packages:
    print(f"✓ {pkg.qualified_name}")

# 获取环境变量
env = ctx.get_environ()
for key in sorted(env.keys())[:5]:
    print(f"{key}={env[key][:50]}")
```

---

## 🎯 最佳实践

| 任务 | 推荐工具 | 命令 |
|------|--------|------|
| 交互式包管理 | GUI | `python -m rez.cli gui` |
| 快速查看环境 | view | `python -m rez.cli view` |
| 创建和编辑环境 | context | `python -m rez.cli context` |
| 分析依赖 | depends | `python -m rez.cli depends` |
| 对比环境 | diff | `python -m rez.cli diff` |
| 系统诊断 | status | `python -m rez.cli status` |

---

## ⚡ 5分钟快速开始

```powershell
# 1. 启动 GUI 浏览包
python -m rez.cli gui

# 2. 或查看系统信息
python -m rez.cli status

# 3. 创建一个环境
python -m rez.cli context python-3.9

# 4. 查看环境详情
python -m rez.cli view "python-3.9"

# 5. 保存环境
python -m rez.cli context --serialize myenv.rez
```

---

## 📚 本项目文件

- `rez_gui_visualization.py` - GUI 和可视化工具演示
- `rez_visualization_practice.py` - 可视化操作实践
- `Rez_可视化操作指南.md` - 详细指南（本文件）

---

## 🚀 下一步

1. ✅ 运行 `python rez_gui_visualization.py` 了解可用工具
2. ✅ 运行 `python rez_visualization_practice.py` 看示例
3. ✅ 执行 `python -m rez.cli gui` 启动图形界面
4. ✅ 使用各种命令进行可视化操作
5. ✅ 参考本文档和官方文档深入学习

---

**Rez 可视化工具让包管理变得轻松直观！** 🎉
