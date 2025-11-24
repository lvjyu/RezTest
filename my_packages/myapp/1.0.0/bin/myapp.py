#!/usr/bin/env python
"""示例应用脚本"""
print("Hello from myapp v1.0.0!")
import os
print(f"MYAPP_ROOT: {os.environ.get('MYAPP_ROOT', 'Not set')}")
