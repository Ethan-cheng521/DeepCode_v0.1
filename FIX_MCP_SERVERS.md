# 🔧 MCP 服务器启动失败修复指南

## 问题症状

您会看到以下错误：
```
MCP Server: 'code-implementation': Failed to initialize
Tool 'write_file' not found
Tool 'set_workspace' not found
```

## 根本原因

缺少必需的 Python 包：`mcp` 和 `fastmcp`

---

## ✅ 修复步骤（Windows）

### 步骤 1: 检查是否缺少包

打开 **PowerShell** 或 **命令提示符**，运行：

```powershell
python -c "import mcp; import fastmcp; print('OK')"
```

**如果看到错误** `ModuleNotFoundError`，说明需要安装。

### 步骤 2: 安装缺失的包

#### 方法 A: 重新安装所有依赖（推荐）

```powershell
cd "D:\AI\Deepcode\DeepCode_v0.1"  # 替换为您的实际路径
pip install -r requirements.txt --upgrade
```

#### 方法 B: 仅安装 MCP 相关包

```powershell
pip install mcp fastmcp
```

#### 方法 C: 使用国内镜像（如果网络慢）

```powershell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mcp fastmcp
```

### 步骤 3: 验证安装成功

```powershell
python -c "import mcp; import fastmcp; print('✅ 安装成功！')"
```

应该看到：`✅ 安装成功！`

### 步骤 4: 测试 MCP 服务器

```powershell
cd "D:\AI\Deepcode\DeepCode_v0.1"
python tools/code_implementation_server.py
```

**期望结果**：服务器启动，等待输入（按 Ctrl+C 退出）

**错误结果**：如果仍然报错 `ModuleNotFoundError`，继续阅读下面的故障排除。

### 步骤 5: 重启 DeepCode

```powershell
deepcode
```

---

## 🔧 故障排除

### 问题 1: 多个 Python 环境

**症状**：安装了包，但仍然报 `ModuleNotFoundError`

**解决方法**：确保安装到正确的 Python 环境

```powershell
# 查看 DeepCode 使用的 Python
where python

# 使用完整路径安装
"D:\Install software\Python\Python313\python.exe" -m pip install mcp fastmcp

# 验证
"D:\Install software\Python\Python313\python.exe" -c "import mcp; print('OK')"
```

### 问题 2: pip 版本过旧

```powershell
python -m pip install --upgrade pip
pip install mcp fastmcp
```

### 问题 3: 权限问题

**以管理员身份运行 PowerShell**，然后：

```powershell
pip install mcp fastmcp
```

### 问题 4: 网络连接问题

```powershell
# 使用清华镜像
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple mcp fastmcp

# 或阿里镜像
pip install -i https://mirrors.aliyun.com/pypi/simple/ mcp fastmcp
```

### 问题 5: 虚拟环境问题

如果您使用了虚拟环境，确保激活它：

```powershell
# 激活虚拟环境（如果有）
.\venv\Scripts\activate

# 然后安装
pip install mcp fastmcp
```

---

## 🧪 完整测试流程

### 1. 测试 Python 包导入

```powershell
python -c "import mcp; import fastmcp; import asyncio; print('✅ 所有包已安装')"
```

### 2. 测试 MCP 服务器脚本

```powershell
cd "D:\AI\Deepcode\DeepCode_v0.1"
python tools/code_implementation_server.py
```

按 `Ctrl+C` 停止。

### 3. 检查 Python 版本

```powershell
python --version
```

确保是 Python 3.10 或更高版本。

---

## 📦 所需的完整依赖列表

以下是 `requirements.txt` 中所有的包：

```
aiofiles>=0.8.0
aiohttp>=3.8.0
anthropic
asyncio-mqtt
docling
fastmcp>=0.2.0      ← 必需
google-genai
mcp>=1.0.0          ← 必需
mcp-agent
mcp-server-git
nest_asyncio
openai
pathlib2
PyPDF2>=2.0.0
reportlab>=3.5.0
streamlit
```

---

## ❓ 仍然无法解决？

### 收集诊断信息

```powershell
# 1. Python 版本
python --version

# 2. pip 版本
pip --version

# 3. 已安装的包
pip list | findstr mcp

# 4. Python 可执行文件路径
where python

# 5. 测试导入
python -c "import sys; print('\n'.join(sys.path))"
```

将以上输出发送给我，我会帮您进一步诊断。

---

## 🎯 快速检查清单

- [ ] Python 版本 >= 3.10
- [ ] 已安装 `pip`
- [ ] 已安装 `mcp` 包
- [ ] 已安装 `fastmcp` 包
- [ ] 可以成功导入 `import mcp`
- [ ] 可以成功导入 `import fastmcp`
- [ ] MCP 服务器脚本可以启动
- [ ] 重启了 DeepCode

---

## 📞 获取帮助

如果按照以上步骤仍然无法解决，请提供：

1. Python 版本 (`python --version`)
2. 已安装的 MCP 相关包 (`pip list | findstr mcp`)
3. 尝试导入时的完整错误信息
4. `python tools/code_implementation_server.py` 的完整输出

---

**最后更新**: 2025-12-19
