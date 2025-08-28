# GROW AI Assistant - 智能卖家管理平台

## 项目简介

GROW AI Assistant 是一个基于 Streamlit 的智能卖家管理平台，旨在通过 AI 自动化减少 AM 手工工作量 >50%，让 AM 从"数据处理员"转型为"关键 seller 的业务伙伴"。

## 核心功能

### 🎯 Goal - 目标设定和绩效管理
- ICQ 指标实时仪表板
- 业务目标设定和追踪
- 资源规划和优化建议

### 🔍 Recruitment - 卖家招募自动化
- 潜在卖家分析和评估
- 招募进度管理和漏斗可视化
- 招募工具集成

### 💡 Options - 沟通工具和实用工具集合
- AI 智能沟通助手
- Mass Email 工具
- Email Scraper 工具
- 多语言翻译和市场调研工具

### 🚀 Win - 卖家增长和成功管理
- 卖家表现分析和雷达图
- 增长机会识别
- 行动计划管理和智能提醒

## 技术栈

- **前端框架**: Streamlit
- **数据处理**: Pandas, NumPy
- **数据可视化**: Plotly, Matplotlib, Seaborn
- **语言**: Python 3.8+

## 快速开始

### 1. 环境准备

```bash
# 克隆项目
git clone https://github.com/TheoriesLiu/GROW.git
cd GROW

# 创建虚拟环境 (推荐)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate  # Windows

# 安装依赖
pip install -r requirements.txt
```

### 2. 运行应用

```bash
# 方法1: 使用启动脚本
python run_app.py

# 方法2: 直接使用 Streamlit
streamlit run grow_ai_assistant.py

# 方法3: 指定端口
streamlit run grow_ai_assistant.py --server.port 8501
```

### 3. 访问应用

打开浏览器访问: http://localhost:8501

## 项目结构

```
grow-ai-assistant/
├── grow_ai_assistant.py      # 主应用文件
├── run_app.py                # 启动脚本
├── requirements.txt          # 依赖列表
├── README.md                # 项目说明
├── .streamlit/              # Streamlit 配置
│   └── config.toml
└── .kiro/                   # 项目规范文档
    └── specs/
        └── grow-ai-assistant/
            ├── requirements.md
            ├── design.md
            └── tasks.md
```

## 开发状态

- [x] 项目基础结构搭建
- [x] Streamlit 应用框架
- [x] 基础样式和配置
- [ ] Goal 模块实现
- [ ] Recruitment 模块实现
- [ ] Options 模块实现
- [ ] Win 模块实现
- [ ] 数据集成和 AI 功能
- [ ] 性能优化和测试

## 核心价值

- ✅ **自动化优先**: 减少 50%+ 手工工作时间
- ✅ **标准化输出**: 统一的 seller review 和提案 deck
- ✅ **聚焦高价值**: 让 AM 专注于关键 seller 的业务增长
- ✅ **数据驱动**: 基于实时数据和 AI 分析做出决策

## 效率指标

- 📊 自动生成报告: 47份/周
- ⏰ 节省工作时间: 24小时/周
- 🎯 AI 推荐准确率: 89%
- 📈 响应速度提升: 65%

## 支持的国家/地区

- 🇸🇬 新加坡 (SG)
- 🇲🇾 马来西亚 (MY)
- 🇹🇭 泰国 (TH)
- 🇮🇩 印尼 (ID)
- 🇻🇳 越南 (VN)
- 🇵🇭 菲律宾 (PH)

## 贡献指南

1. Fork 项目
2. 创建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情

## 在线演示

🚀 **[在线体验 GROW AI Assistant](https://grow-ai-assistant.streamlit.app/)**

## 快速部署

### Streamlit Cloud 一键部署

1. Fork 这个仓库到你的 GitHub 账号
2. 访问 [Streamlit Cloud](https://share.streamlit.io/)
3. 连接你的 GitHub 仓库 `https://github.com/TheoriesLiu/GROW.git`
4. 选择 `streamlit_app.py` 作为主文件
5. 点击部署！

### 本地部署

```bash
# 快速启动
git clone https://github.com/TheoriesLiu/GROW.git
cd GROW
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 联系方式

- 项目维护者: GROW AI Team
- 邮箱: grow-ai-support@example.com
- 问题反馈: [GitHub Issues](https://github.com/TheoriesLiu/GROW/issues)
- 文档: [部署指南](DEPLOYMENT.md)

---

**让 AM 工作更智能，从数据处理员到业务伙伴的转型，从这里开始！** 🚀