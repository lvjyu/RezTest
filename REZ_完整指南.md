# Rez 包管理系统完整指南

## 目录
1. [Rez 简介](#rez-简介)
2. [安装](#安装)
3. [核心概念](#核心-概念)
4. [常用命令](#常用命令)
5. [创建包](#创建包)
6. [环境管理](#环境管理)
7. [版本约束](#版本约束)
8. [实际示例](#实际示例)
9. [常见问题](#常见问题)

---

## Rez 简介

Rez 是一个专为 VFX、游戏开发和其他复杂项目设计的**包和环境管理系统**。

### 主要特点
- ✅ **版本冲突解决**：自动解决包之间的版本依赖
- ✅ **隔离环境**：为不同项目创建独立的虚拟环境
- ✅ **灵活配置**：支持多个包搜索路径
- ✅ **可扩展性**：支持自定义包和变体
- ✅ **多平台**：支持 Linux、Windows、macOS

---

## 安装

### 1. 使用 pip 安装
```powershell
pip install rez
```

### 2. 验证安装
```powershell
python -c "import rez; print(f'Rez {rez.__version__} 已安装')"
```

### 3. 查看配置
```powershell
python -m rez.cli config
```

---

## 核心 概念

### Package（包）
- 一个自包含的单元，包含软件及其元数据
- 必须有 `package.py` 配置文件
- 每个版本存储在独立的目录中

### Requires（依赖项）
- 指定包所需的其他包
- 支持版本约束（如 `python-3.9+<4`）

### Variants（变体）
- 同一包的不同配置
- 例如：针对不同 Python 版本的变体

### Resolve（解析）
- 根据依赖关系生成有效的环境
- 自动检测和解决版本冲突

### Context（上下文）
- 一个特定的包组合集合
- 包含所有已解析的包及其环境变量

---

## 常用命令

### 基础命令

```powershell
# 列出已安装的包
python -m rez.cli list

# 搜索特定的包
python -m rez.cli search python

# 查看包信息
python -m rez.cli package-info python-3.9

# 查看 Rez 配置
python -m rez.cli config

# 查看版本
python -m rez.cli version
```

### 环境命令

```powershell
# 创建环境（进入 shell）
python -m rez.cli env python-3.9

# 创建包含多个包的环境
python -m rez.cli env python-3.9 maya-2022

# 查看环境信息（不进入 shell）
python -m rez.cli env python-3.9 --print

# 在环境中执行命令（不进入 shell）
python -m rez.cli env python-3.9 -- python script.py

# 保存环境配置
python -m rez.cli env python-3.9 --create C:\path\to\env
```

### 包构建命令

```powershell
# 验证 package.py 配置
python -m rez.cli validate ./package/path

# 构建包到仓库
python -m rez.cli build ./package/path

# 构建并指定目标目录
python -m rez.cli build ./package/path --install-dir C:\packages
```

---

## 创建包

### 基本结构

```
my_package/
├── package.py           # 包配置（必需）
├── README.md            # 说明文档
├── bin/                 # 可执行文件
│   └── myapp.py
├── lib/                 # 库文件
│   └── myapp/
│       └── __init__.py
└── src/                 # 源代码（可选）
```

### package.py 示例

```python
"""
包配置文件
"""

# 基本信息
name = "myapp"
version = "1.0.0"
description = "My application"
authors = ["Your Name"]

# 依赖项
requires = [
    "python-3.9+<4",           # Python 3.9 到 3.x
    "maya-2022+<2023",         # Maya 2022
]

# 系统需求
system_requires = []

# 定义包在环境中的行为
def commands():
    import os
    # 设置环境变量
    env.MYAPP_ROOT = "{root}"
    env.MYAPP_BIN = "{root}/bin"
    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/lib")

# 包的变体
variants = [
    ["python-3.9"],
    ["python-3.10"],
    ["python-3.11"],
]

# 在 resolve 之前运行
pre_resolve_function = None

# 在 resolve 之后运行
post_resolve_function = None
```

### 关键属性

| 属性 | 说明 | 示例 |
|------|------|------|
| `name` | 包名称 | `"myapp"` |
| `version` | 版本号 | `"1.0.0"` |
| `description` | 描述 | `"My application"` |
| `authors` | 作者列表 | `["John Doe"]` |
| `requires` | 依赖项 | `["python-3.9+"]` |
| `variants` | 变体列表 | `[["python-3.9"], ["python-3.10"]]` |
| `commands()` | 环境命令 | 设置环境变量 |

---

## 环境管理

### 创建环境

```powershell
# 基础用法
python -m rez.cli env python-3.9

# 多个依赖项
python -m rez.cli env python-3.9 maya-2022 perforce

# 带版本约束
python -m rez.cli env "python-3.9+" "maya-2022,<2023"
```

### 环境变量

在 `commands()` 函数中设置环境变量：

```python
def commands():
    import os
    
    # 设置路径前缀（追加到 PATH 开头）
    env.PATH.prepend("{root}/bin")
    
    # 设置路径后缀（追加到 PATH 结尾）
    env.PATH.append("{root}/lib")
    
    # 设置自定义变量
    env.MYAPP_HOME = "{root}"
    env.CUSTOM_VAR = "value"
    
    # 条件设置（在 Windows 上）
    if platform.system() == "Windows":
        env.PATH.append("{root}/bin/windows")
```

### 占位符

- `{root}` - 包的根目录
- `{version}` - 包的版本
- `{name}` - 包的名称

---

## 版本约束

### 版本格式

| 格式 | 说明 | 示例 |
|------|------|------|
| `1.0.0` | 精确版本 | 仅 1.0.0 |
| `1.0.0+` | 大于等于 | 1.0.0 及以上 |
| `1.0+<2` | 范围 | 1.0 到 2.0（不含） |
| `1,<2` | 可用版本 | 1.x 或更高（但小于 2） |
| `1.0,1.5,1.9` | 多个版本 | 仅这些版本 |

### 复杂约束

```python
requires = [
    "python-2.7,3.7+<4",           # Python 2.7 或 3.7+
    "maya-2020+",                  # Maya 2020 及以上
    "perforce-2021.1,2021.2",      # 特定版本
    "boost-1.70+<1.80",            # 版本范围
]
```

---

## 实际示例

### 示例 1：创建简单包

已为您生成了 `create_package_example.py` 脚本。运行它：

```powershell
python create_package_example.py
```

这会创建一个 `my_packages/myapp/1.0.0` 目录。

### 示例 2：使用本地包

```powershell
# 1. 设置包搜索路径（PowerShell）
$env:REZ_PACKAGES_PATH = "E:\UE\RezTest\my_packages;$env:REZ_PACKAGES_PATH"

# 2. 搜索包
python -m rez.cli search myapp

# 3. 进入环境
python -m rez.cli env myapp

# 4. 在环境中验证
python bin/myapp.py
```

### 示例 3：多包环境

```powershell
# 创建包含 Python 和其他工具的环境
python -m rez.cli env python-3.9 git perforce

# 在该环境中执行 Python 脚本
python -m rez.cli env python-3.9 -- python my_script.py
```

---

## 常见问题

### Q: 找不到包？

**A:** 检查包搜索路径
```powershell
# 查看当前搜索路径
python -c "from rez.config import config; print('\n'.join(config.packages_path))"

# 添加自定义路径
$env:REZ_PACKAGES_PATH = "C:\my_packages;$env:REZ_PACKAGES_PATH"
```

### Q: 版本冲突怎么解决？

**A:** Rez 会自动尝试解决，如果冲突无法解决会报错
```powershell
# 查看冲突详情
python -m rez.cli solve python-3.7 python-3.9
```

### Q: 如何卸载包？

**A:** Rez 没有卸载命令，直接删除包目录即可
```powershell
# 删除包
rm -r C:\packages\myapp\1.0.0
```

### Q: 如何指定特定版本？

**A:** 在环境中指定版本范围
```powershell
# 使用特定版本
python -m rez.cli env "python-3.9"

# 使用版本范围
python -m rez.cli env "python-3.9,<3.10"

# 最新版本
python -m rez.cli env "python-3+"
```

### Q: 如何调试环境变量？

**A:** 使用 `--print` 选项
```powershell
python -m rez.cli env python-3.9 --print
```

---

## 资源

- [Rez 官方文档](https://rez.readthedocs.io/)
- [GitHub 仓库](https://github.com/nerdvegas/rez)
- [Rez 社区](https://rez.readthedocs.io/en/latest/community.html)

---

**快速开始：**

1. ✅ 已安装 Rez 3.3.0
2. 📝 查看 `test.py` - 演示基本功能
3. 📦 运行 `create_package_example.py` - 创建示例包
4. 🚀 按照本指南创建自己的包！
