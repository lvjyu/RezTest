#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Rez Web GUI - 基于 Flask 的 Web 界面
可以在浏览器中访问 http://localhost:5000
"""

from flask import Flask, render_template_string, jsonify, request
import json
import os

# 配置 Rez 包搜索路径
os.environ['REZ_PACKAGES_PATH'] = r'E:\UE\RezTest\my_packages'

from rez import packages
from rez.config import config
from rez.resolved_context import ResolvedContext

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rez 包管理系统 - Web GUI</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        
        .container {
            max-width: 1400px;
            margin: 0 auto;
            background: white;
            border-radius: 12px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            overflow: hidden;
        }
        
        header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }
        
        header h1 {
            font-size: 32px;
            margin-bottom: 10px;
        }
        
        header p {
            font-size: 14px;
            opacity: 0.9;
        }
        
        nav {
            display: flex;
            background: #f8f9fa;
            border-bottom: 2px solid #e9ecef;
        }
        
        nav button {
            flex: 1;
            padding: 15px;
            border: none;
            background: none;
            cursor: pointer;
            font-size: 14px;
            font-weight: 600;
            color: #495057;
            transition: all 0.3s;
            border-bottom: 3px solid transparent;
        }
        
        nav button:hover {
            background: #e9ecef;
        }
        
        nav button.active {
            color: #667eea;
            border-bottom-color: #667eea;
        }
        
        .content {
            padding: 30px;
        }
        
        .tab {
            display: none;
        }
        
        .tab.active {
            display: block;
        }
        
        .section {
            margin-bottom: 30px;
        }
        
        .section h2 {
            font-size: 20px;
            margin-bottom: 15px;
            color: #333;
            padding-bottom: 10px;
            border-bottom: 2px solid #667eea;
        }
        
        .search-box {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .search-box input {
            flex: 1;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
            font-size: 14px;
        }
        
        .search-box button {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
            transition: background 0.3s;
        }
        
        .search-box button:hover {
            background: #5568d3;
        }
        
        .package-list {
            list-style: none;
            max-height: 400px;
            overflow-y: auto;
            border: 1px solid #ddd;
            border-radius: 6px;
        }
        
        .package-item {
            padding: 12px 15px;
            border-bottom: 1px solid #eee;
            cursor: pointer;
            transition: background 0.2s;
        }
        
        .package-item:hover {
            background: #f8f9fa;
        }
        
        .package-item.active {
            background: #e7f1ff;
            color: #667eea;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 15px;
        }
        
        th {
            background: #f8f9fa;
            padding: 12px;
            text-align: left;
            font-weight: 600;
            color: #333;
            border-bottom: 2px solid #ddd;
        }
        
        td {
            padding: 12px;
            border-bottom: 1px solid #eee;
        }
        
        tr:hover {
            background: #f8f9fa;
        }
        
        .input-group {
            display: flex;
            gap: 10px;
            margin-bottom: 15px;
        }
        
        .input-group input {
            flex: 1;
            padding: 10px 15px;
            border: 1px solid #ddd;
            border-radius: 6px;
        }
        
        .input-group button {
            padding: 10px 20px;
            background: #667eea;
            color: white;
            border: none;
            border-radius: 6px;
            cursor: pointer;
            font-weight: 600;
        }
        
        .input-group button:hover {
            background: #5568d3;
        }
        
        .info-box {
            background: #f0f4ff;
            border-left: 4px solid #667eea;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 15px;
        }
        
        .info-box strong {
            color: #667eea;
        }
        
        .tree {
            background: #f8f9fa;
            padding: 15px;
            border-radius: 6px;
            border: 1px solid #ddd;
            font-family: 'Courier New', monospace;
            font-size: 13px;
            max-height: 400px;
            overflow-y: auto;
        }
        
        .tree-item {
            padding: 3px 0;
            margin-left: 20px;
        }
        
        footer {
            background: #f8f9fa;
            padding: 20px 30px;
            text-align: center;
            color: #6c757d;
            font-size: 12px;
            border-top: 1px solid #ddd;
        }
        
        .loading {
            text-align: center;
            color: #667eea;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📦 Rez 包管理系统</h1>
            <p>Web 版图形界面</p>
        </header>
        
        <nav>
            <button class="tab-btn active" onclick="showTab('packages')">📦 包浏览器</button>
            <button class="tab-btn" onclick="showTab('dependencies')">🔗 依赖分析</button>
            <button class="tab-btn" onclick="showTab('environment')">⚙️ 环境管理</button>
            <button class="tab-btn" onclick="showTab('status')">📊 系统状态</button>
        </nav>
        
        <div class="content">
            <!-- 包浏览器标签 -->
            <div id="packages" class="tab active">
                <div class="section">
                    <h2>📦 包浏览器</h2>
                    <div class="search-box">
                        <input type="text" id="search-pkg" placeholder="搜索包名...">
                        <button onclick="searchPackages()">搜索</button>
                    </div>
                    <ul id="package-list" class="package-list">
                        <li class="package-item loading">加载中...</li>
                    </ul>
                    <table>
                        <thead>
                            <tr>
                                <th>属性</th>
                                <th>值</th>
                            </tr>
                        </thead>
                        <tbody id="package-details">
                            <tr><td colspan="2" class="loading">选择包查看详情</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
            
            <!-- 依赖分析标签 -->
            <div id="dependencies" class="tab">
                <div class="section">
                    <h2>🔗 依赖分析</h2>
                    <div class="input-group">
                        <input type="text" id="dep-package" placeholder="输入包名 (例: python-3.9)">
                        <button onclick="showDependencies()">分析依赖</button>
                    </div>
                    <div id="dep-result" class="tree">
                        <div class="loading">输入包名并点击分析</div>
                    </div>
                </div>
            </div>
            
            <!-- 环境管理标签 -->
            <div id="environment" class="tab">
                <div class="section">
                    <h2>⚙️ 环境管理</h2>
                    <div class="info-box">
                        <strong>提示:</strong> 输入多个包名，用空格或逗号分隔，例: python-3.9 maya-2022
                    </div>
                    <div class="input-group">
                        <input type="text" id="env-packages" placeholder="输入包名列表...">
                        <button onclick="resolveEnvironment()">解析环境</button>
                    </div>
                    <div class="section">
                        <h2>解析结果</h2>
                        <table>
                            <thead>
                                <tr>
                                    <th>包名</th>
                                    <th>版本</th>
                                </tr>
                            </thead>
                            <tbody id="env-result">
                                <tr><td colspan="2" class="loading">待解析</td></tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
            
            <!-- 系统状态标签 -->
            <div id="status" class="tab">
                <div class="section">
                    <h2>📊 系统状态</h2>
                    <table>
                        <thead>
                            <tr>
                                <th>配置项</th>
                                <th>值</th>
                            </tr>
                        </thead>
                        <tbody id="status-info">
                            <tr><td colspan="2" class="loading">加载中...</td></tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        
        <footer>
            <p>Rez 包管理系统 Web GUI | 在浏览器中管理您的包环境</p>
        </footer>
    </div>
    
    <script>
        // 初始化
        window.addEventListener('load', function() {
            loadPackages();
            loadStatus();
        });
        
        // 标签页切换
        function showTab(tabName) {
            // 隐藏所有标签页
            const tabs = document.querySelectorAll('.tab');
            tabs.forEach(tab => tab.classList.remove('active'));
            
            // 取消所有按钮激活状态
            const buttons = document.querySelectorAll('.tab-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            
            // 显示选中的标签页
            document.getElementById(tabName).classList.add('active');
            event.target.classList.add('active');
        }
        
        // 加载包列表
        function loadPackages() {
            fetch('/api/packages')
                .then(r => r.json())
                .then(data => {
                    const list = document.getElementById('package-list');
                    list.innerHTML = '';
                    data.packages.forEach(pkg => {
                        const li = document.createElement('li');
                        li.className = 'package-item';
                        li.textContent = pkg;
                        li.onclick = () => showPackageDetails(pkg);
                        list.appendChild(li);
                    });
                });
        }
        
        // 搜索包
        function searchPackages() {
            const search = document.getElementById('search-pkg').value.toLowerCase();
            const items = document.querySelectorAll('.package-item');
            items.forEach(item => {
                if (item.textContent.toLowerCase().includes(search)) {
                    item.style.display = '';
                } else {
                    item.style.display = 'none';
                }
            });
        }
        
        // 显示包详情
        function showPackageDetails(pkgName) {
            fetch(`/api/package/${pkgName}`)
                .then(r => r.json())
                .then(data => {
                    const tbody = document.getElementById('package-details');
                    tbody.innerHTML = '';
                    Object.entries(data).forEach(([key, value]) => {
                        const row = tbody.insertRow();
                        row.insertCell(0).textContent = key;
                        row.insertCell(1).textContent = value;
                    });
                });
            
            // 突出显示选中项
            document.querySelectorAll('.package-item').forEach(item => {
                item.classList.remove('active');
            });
            event.target.classList.add('active');
        }
        
        // 显示依赖
        function showDependencies() {
            const pkg = document.getElementById('dep-package').value;
            if (!pkg) return;
            
            fetch(`/api/dependencies/${pkg}`)
                .then(r => r.json())
                .then(data => {
                    const result = document.getElementById('dep-result');
                    if (data.error) {
                        result.innerHTML = `<div class="info-box"><strong>错误:</strong> ${data.error}</div>`;
                    } else {
                        result.innerHTML = '<div class="tree">' + data.tree.replace(/\n/g, '<br>') + '</div>';
                    }
                });
        }
        
        // 解析环境
        function resolveEnvironment() {
            const input = document.getElementById('env-packages').value;
            if (!input) return;
            
            const packages = input.split(/[,\s]+/).filter(p => p);
            
            fetch('/api/resolve', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({packages: packages})
            })
                .then(r => r.json())
                .then(data => {
                    const tbody = document.getElementById('env-result');
                    tbody.innerHTML = '';
                    if (data.error) {
                        const row = tbody.insertRow();
                        row.innerHTML = `<td colspan="2" class="info-box"><strong>错误:</strong> ${data.error}</td>`;
                    } else {
                        data.resolved.forEach(pkg => {
                            const row = tbody.insertRow();
                            row.insertCell(0).textContent = pkg.name;
                            row.insertCell(1).textContent = pkg.version;
                        });
                    }
                });
        }
        
        // 加载系统状态
        function loadStatus() {
            fetch('/api/status')
                .then(r => r.json())
                .then(data => {
                    const tbody = document.getElementById('status-info');
                    tbody.innerHTML = '';
                    Object.entries(data).forEach(([key, value]) => {
                        const row = tbody.insertRow();
                        row.insertCell(0).textContent = key;
                        row.insertCell(1).textContent = value;
                    });
                });
        }
    </script>
</body>
</html>
"""


@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)


@app.route('/api/packages')
def api_packages():
    """获取包列表"""
    try:
        pkg_list = []
        for family in packages.iter_package_families():
            pkg_list.append(family.name)
        pkg_list.sort()
        return jsonify({'packages': pkg_list[:50]})  # 返回前 50 个
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/package/<name>')
def api_package(name):
    """获取包详情"""
    try:
        family = packages.get_package_family(name)
        if not family:
            return jsonify({'error': f'包 {name} 不存在'}), 404
        
        versions = [str(p.version) for p in family.iter_packages()]
        return jsonify({
            '包名': family.name,
            '版本数': str(len(versions)),
            '最新版本': versions[-1] if versions else 'N/A',
            '版本列表': ', '.join(versions[-5:])  # 显示最后 5 个版本
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/api/dependencies/<name>')
def api_dependencies(name):
    """获取依赖树"""
    try:
        ctx = ResolvedContext([name])
        tree_lines = []
        tree_lines.append(f"📦 {name}")
        for pkg in ctx.resolved_packages:
            tree_lines.append(f"  └─ {pkg.qualified_name}")
        return jsonify({'tree': '\n'.join(tree_lines)})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/resolve', methods=['POST'])
def api_resolve():
    """解析环境"""
    try:
        data = request.get_json()
        pkg_list = data.get('packages', [])
        
        ctx = ResolvedContext(pkg_list)
        resolved = []
        for pkg in ctx.resolved_packages:
            resolved.append({
                'name': pkg.qualified_name,
                'version': str(pkg.version)
            })
        return jsonify({'resolved': resolved})
    except Exception as e:
        return jsonify({'error': str(e)})


@app.route('/api/status')
def api_status():
    """获取系统状态"""
    try:
        import rez
        family_count = len(list(packages.iter_package_families()))
        return jsonify({
            'Rez 版本': rez.__version__,
            '已安装包族数': str(family_count),
            '包搜索路径': str(config.package_paths[0]) if config.package_paths else 'N/A',
            '缓存路径': str(config.cache_dir),
            'Python 版本': __import__('sys').version.split()[0]
        })
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    print("\n" + "="*60)
    print("✅ Rez Web GUI 已启动!")
    print("="*60)
    print("\n📱 请在浏览器中打开:")
    print("   http://localhost:5000")
    print("\n功能:")
    print("   • 📦 包浏览器 - 搜索和浏览已安装的包")
    print("   • 🔗 依赖分析 - 查看包的依赖关系")
    print("   • ⚙️  环境管理 - 解析和管理环境")
    print("   • 📊 系统状态 - 查看 Rez 配置信息")
    print("\n按 Ctrl+C 停止服务器")
    print("="*60 + "\n")
    
    app.run(debug=False, host='localhost', port=5000)
