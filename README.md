# RezTest - Rez 包管理系统学习项目

## 📦 项目概述

这是一个完整的 **Rez 包管理系统** 学习和演示项目。包含：

- ✅ 4 个可运行的演示脚本
- ✅ 3 份详细的文档指南  
- ✅ 1 个完整的示例包
- ✅ 总计 ~50 KB 的学习资源

## 🚀 快速开始

```powershell
# 1. 查看项目说明
Get-Content _开始.txt

# 2. 运行基础演示
python test.py

# 3. 查看实践测试
python practice_test.py

# 4. 阅读快速参考
explorer "快速参考.md"
```

## 📚 文档结构

| 文件 | 说明 | 适合用户 |
|------|------|--------|
| `_开始.txt` | 项目总览和快速导航 | 🔰 新手 |
| `REZTEST_使用说明.md` | 详细的使用说明和建议 | 🔰 新手 |
| `快速参考.md` | 常用命令和 API 速查表 | 👨‍💻 所有人 |
| `REZ_完整指南.md` | 官方级详细指南 | 🎓 深度学习 |

## 📁 目录结构

```
RezTest/
├── test.py                          # 基础演示脚本
├── create_package_example.py        # 包创建脚本  
├── practice_test.py                 # 实践测试脚本
├── _开始.txt                        # 项目导航（推荐首先阅读）
├── REZTEST_使用说明.md              # 使用说明
├── 快速参考.md                      # 速查表
├── REZ_完整指南.md                  # 详细指南
└── my_packages/
    └── myapp/
        └── 1.0.0/
            ├── package.py           # 包配置文件
            ├── README.md
            ├── bin/
            │   └── myapp.py
            └── lib/
                └── __init__.py
```

## 🎯 学习路径

### 初级（15分钟）
1. 阅读 `_开始.txt` 了解项目结构
2. 运行 `python test.py` 看演示
3. 阅读 `快速参考.md` 前两部分

### 中级（45分钟）
1. 运行 `python create_package_example.py`
2. 运行 `python practice_test.py`
3. 阅读 `快速参考.md` 全部内容
4. 修改 `my_packages/myapp/1.0.0/package.py`

### 高级（2小时）
1. 阅读 `REZ_完整指南.md`
2. 研究 `package.py` 各个字段
3. 创建自己的 Rez 包
4. 访问 [Rez 官方文档](https://rez.readthedocs.io/)

## 🔧 可运行的脚本

### test.py
```bash
python test.py
```
演示 Rez 的基本功能和信息。

### create_package_example.py
```bash
python create_package_example.py
```
创建示例包 `my_packages/myapp/1.0.0`。

### practice_test.py
```bash
python practice_test.py
```
演示 Rez API 使用和包信息查询。

## 💡 核心概念

- **Package**: 自包含的软件单元
- **Requires**: 包的依赖项
- **Variants**: 包的不同配置
- **Context**: 已解析的包环境
- **Commands**: 环境加载时执行的配置

## 🌟 Rez 版本信息

- **Rez 版本**: 3.3.0
- **Python 版本**: 3.9
- **创建日期**: 2025年11月24日

## 📖 推荐首先阅读

1. **`_开始.txt`** - 项目导航和完整说明
2. **`REZTEST_使用说明.md`** - 使用建议和快速开始
3. **`快速参考.md`** - 最常用的参考资料

## ❓ 常见问题

**Q: 从哪里开始？**
A: 打开 `_开始.txt` 查看项目导航。

**Q: 如何创建自己的包？**
A: 参考 `快速参考.md` 中的 "创建包" 部分。

**Q: package.py 怎么写？**
A: 查看 `快速参考.md` 中的 "Package.py 完整示例"。

**Q: 如何使用本地包？**
A: 运行 `python practice_test.py` 查看示例。

## 🔗 相关资源

- [Rez 官方文档](https://rez.readthedocs.io/)
- [GitHub 仓库](https://github.com/nerdvegas/rez)
- [Rez 社区](https://rezdevelop.slack.com/)

## ✅ 开始学习

```powershell
# 首先查看项目说明
Get-Content _开始.txt

# 然后运行演示
python test.py

# 最后阅读文档
code 快速参考.md
```

---

**现在您已有完整的学习资源！祝您使用 Rez 愉快！** 🚀

