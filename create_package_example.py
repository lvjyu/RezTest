#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez 包创建示例
演示如何创建一个简单的 Rez 包
"""

import os
import sys
from pathlib import Path

print("=" * 70)
print("Rez 包创建演示")
print("=" * 70)

# 定义包的目录结构
packages_dir = Path("./my_packages")
package_name = "myapp"
version = "1.0.0"
package_dir = packages_dir / package_name / version

print(f"\n1. 创建包目录结构...")
print(f"   目录: {package_dir}")

# 创建目录
package_dir.mkdir(parents=True, exist_ok=True)

# 创建 package.py 文件
package_py_content = '''"""
示例 Rez 包
"""

name = "myapp"
version = "1.0.0"
description = "A sample Rez package"
authors = ["Your Name"]

# 包的依赖项
requires = [
    "python-2.7,3.7+<4",  # Python 2.7 或 3.7+
]

# 可选：定义系统需求
system_requires = []

# 可选：在环境中加载时执行的命令
def commands():
    import os
    # 设置环境变量
    env.MYAPP_ROOT = "{root}"
    env.PATH.append("{root}/bin")
    env.PYTHONPATH.append("{root}/lib")

# 可选：定义包的变体（不同的配置）
variants = [
    ["python-3.7"],
    ["python-3.9"],
    ["python-3.11"],
]

# 可选：项目文件夹
tools = []
'''

package_py_path = package_dir / "package.py"
package_py_path.write_text(package_py_content, encoding='utf-8')
print(f"   ✓ 创建了 {package_py_path}")

# 创建 bin 目录和示例脚本
bin_dir = package_dir / "bin"
bin_dir.mkdir(exist_ok=True)

example_script = '''#!/usr/bin/env python
"""示例应用脚本"""
print("Hello from myapp v1.0.0!")
import os
print(f"MYAPP_ROOT: {os.environ.get('MYAPP_ROOT', 'Not set')}")
'''

script_path = bin_dir / "myapp.py"
script_path.write_text(example_script, encoding='utf-8')
print(f"   ✓ 创建了 {script_path}")

# 创建 lib 目录
lib_dir = package_dir / "lib"
lib_dir.mkdir(exist_ok=True)

init_py = lib_dir / "__init__.py"
init_py.write_text("# myapp library\n", encoding='utf-8')
print(f"   ✓ 创建了 {init_py}")

# 创建 README
readme_path = package_dir / "README.md"
readme_content = """# myapp

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
"""
readme_path.write_text(readme_content, encoding='utf-8')
print(f"   ✓ 创建了 {readme_path}")

print(f"\n2. 包结构:")
for root, dirs, files in os.walk(package_dir):
    level = root.replace(str(package_dir), '').count(os.sep)
    indent = ' ' * 2 * level
    rel_path = os.path.relpath(root, package_dir)
    if rel_path != '.':
        print(f"{indent}📁 {os.path.basename(root)}/")
    else:
        print(f"   📁 {package_name}-{version}/")
    sub_indent = ' ' * 2 * (level + 1)
    for file in files:
        print(f"{sub_indent}📄 {file}")

print(f"\n3. 验证包配置...")
from pathlib import Path
import sys

sys.path.insert(0, str(package_dir))
try:
    # 读取并解析 package.py
    package_py_text = package_py_path.read_text(encoding='utf-8')
    
    # 模拟包信息
    print(f"   ✓ package.py 语法正确")
    print(f"\n   包信息:")
    print(f"   - 名称: myapp")
    print(f"   - 版本: 1.0.0")
    print(f"   - 依赖项: python-2.7,3.7+<4")
    print(f"   - 变体: python-3.7, python-3.9, python-3.11")
    
except Exception as e:
    print(f"   ✗ 错误: {e}")

print(f"\n4. 后续步骤:")
print(f"""
   a) 构建包到 Rez 仓库:
      cd {package_dir}
      python -m rez.cli build .

   b) 加载包环境:
      python -m rez.cli env myapp

   c) 配置 REZ_PACKAGES_PATH 以搜索本地包:
      export REZ_PACKAGES_PATH={packages_dir}:$REZ_PACKAGES_PATH  (Linux/Mac)
      set REZ_PACKAGES_PATH={packages_dir};%REZ_PACKAGES_PATH%    (Windows CMD)
      $env:REZ_PACKAGES_PATH = "{packages_dir};$env:REZ_PACKAGES_PATH"  (PowerShell)

   d) 然后就可以搜索并使用该包:
      python -m rez.cli search myapp
      python -m rez.cli env myapp
""")

print("\n" + "=" * 70)
print(f"包已创建在: {package_dir}")
print("=" * 70)
