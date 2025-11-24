# myapp

示例 Rez 包

## 用途
这是一个演示如何使用 Rez 包管理系统的示例包。

## 依赖项
- python-2.7 或 3.7+

## 使用方法

### 加载环境
```bash
python -m rez.cli env myapp
```

### 在环境中执行命令
```bash
python -m rez.cli env myapp -- python bin/myapp.py
```

### 使用特定的 Python 版本
```bash
python -m rez.cli env myapp-3.11
```
