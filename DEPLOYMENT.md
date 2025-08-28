# 部署指南

## Streamlit Cloud 部署

### 1. 准备工作

1. 将代码推送到 GitHub 仓库
2. 确保仓库是公开的或者你有 Streamlit Cloud 的私有仓库权限
3. 确保 `requirements.txt` 文件包含所有依赖

### 2. 部署步骤

1. 访问 [Streamlit Cloud](https://share.streamlit.io/)
2. 使用 GitHub 账号登录
3. 点击 "New app"
4. 选择你的 GitHub 仓库
5. 设置以下参数：
   - **Repository**: 你的仓库名
   - **Branch**: main (或你的主分支)
   - **Main file path**: `streamlit_app.py` 或 `grow_ai_assistant.py`
6. 点击 "Deploy!"

### 3. 环境变量配置（如果需要）

在 Streamlit Cloud 的 "Advanced settings" 中添加环境变量：

```
STREAMLIT_SERVER_HEADLESS=true
STREAMLIT_SERVER_ENABLE_CORS=false
```

## 本地开发部署

### 1. 克隆仓库

```bash
git clone https://github.com/TheoriesLiu/GROW.git
cd GROW
```

### 2. 创建虚拟环境

```bash
# 使用 venv
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 或使用 conda
conda create -n grow-ai python=3.9
conda activate grow-ai
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 运行应用

```bash
# 方法1: 使用启动脚本
python run_app.py

# 方法2: 直接运行
streamlit run grow_ai_assistant.py

# 方法3: 使用 Streamlit Cloud 兼容文件
streamlit run streamlit_app.py
```

## Docker 部署

### 1. 创建 Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "grow_ai_assistant.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

### 2. 构建和运行

```bash
# 构建镜像
docker build -t grow-ai-assistant .

# 运行容器
docker run -p 8501:8501 grow-ai-assistant
```

## 故障排除

### 常见问题

1. **依赖安装失败**
   - 检查 Python 版本兼容性
   - 更新 pip: `pip install --upgrade pip`
   - 使用特定版本: `pip install streamlit==1.28.0`

2. **端口冲突**
   - 更改端口: `streamlit run app.py --server.port 8502`
   - 检查端口占用: `lsof -i :8501`

3. **内存不足**
   - 减少数据集大小
   - 使用 `@st.cache_data` 优化缓存
   - 增加服务器内存配置

4. **Streamlit Cloud 部署失败**
   - 检查 requirements.txt 格式
   - 确保没有本地路径依赖
   - 查看部署日志获取详细错误信息

### 性能优化

1. **缓存优化**
   ```python
   @st.cache_data
   def load_data():
       return pd.read_csv('data.csv')
   ```

2. **内存管理**
   ```python
   # 清理大型对象
   del large_dataframe
   import gc
   gc.collect()
   ```

3. **异步加载**
   ```python
   with st.spinner('Loading data...'):
       data = load_large_dataset()
   ```

## 监控和维护

### 1. 应用监控

- 使用 Streamlit Cloud 内置监控
- 设置 GitHub Actions 进行持续集成
- 监控应用性能和错误日志

### 2. 更新部署

```bash
# 推送更新到 GitHub
git add .
git commit -m "Update features"
git push origin main

# Streamlit Cloud 会自动重新部署
```

### 3. 回滚版本

```bash
# 回滚到上一个版本
git revert HEAD
git push origin main
```

## 安全注意事项

1. **敏感信息**
   - 使用 `secrets.toml` 存储 API 密钥
   - 不要在代码中硬编码密码
   - 使用环境变量管理配置

2. **访问控制**
   - 考虑添加身份验证
   - 限制敏感功能的访问
   - 定期更新依赖包

3. **数据保护**
   - 不要提交敏感数据到 Git
   - 使用 `.gitignore` 排除数据文件
   - 考虑数据加密存储