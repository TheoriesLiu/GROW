import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# 设置页面配置
st.set_page_config(
    page_title="GROW AI Assistant",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 2rem;
        background: linear-gradient(90deg, #FF6B6B, #4ECDC4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #4ECDC4;
    }
    .success-box {
        background-color: #d4edda;
        border: 1px solid #c3e6cb;
        border-radius: 0.25rem;
        padding: 0.75rem;
        margin: 1rem 0;
    }
</style>
""", unsafe_allow_html=True)

# 主标题
st.markdown('<h1 class="main-header">🚀 GROW AI Assistant</h1>', unsafe_allow_html=True)
st.markdown("**智能卖家管理平台 - 基于重新定义的GROW方法论**")

# 侧边栏配置
with st.sidebar:
    st.header("🎛️ 系统配置")
    
    # 数据刷新设置
    auto_refresh = st.checkbox("自动刷新数据", value=True)
    refresh_interval = st.selectbox("刷新间隔", ["5分钟", "15分钟", "30分钟", "1小时"])
    
    # 地区设置
    st.subheader("🌏 地区设置")
    selected_countries = st.multiselect(
        "选择国家/地区",
        ["SG", "MY", "TH", "ID", "VN", "PH"],
        default=["SG", "MY", "TH"]
    )
    
    # 语言设置
    language = st.selectbox("界面语言", ["中文", "English"])
    
    # 系统状态
    st.subheader("📊 系统状态")
    st.success("🟢 所有服务正常")
    st.info("📡 数据同步: 2分钟前")
    st.info("🤖 AI服务: 正常")

# 生成模拟数据
@st.cache_data
def generate_mock_data():
    """生成模拟的卖家数据"""
    np.random.seed(42)
    
    sellers = [
        "TechGiant_SG", "ElectroMax_ID", "FashionHub_MY", "BeautyPro_VN", 
        "HomeDecor_TH", "SportsPro_PH", "GadgetWorld_SG", "StyleMax_MY",
        "KitchenPro_TH", "HealthPlus_ID"
    ]
    
    seller_data = pd.DataFrame({
        "Seller": sellers,
        "Country": ["SG", "ID", "MY", "VN", "TH", "PH", "SG", "MY", "TH", "ID"],
        "Category": ["Electronics", "Electronics", "Fashion", "Beauty", "Home", 
                    "Sports", "Electronics", "Fashion", "Home", "Health"],
        "GMV": np.random.randint(20000, 200000, 10),
        "Growth Rate": np.random.uniform(-5, 25, 10),
        "Compliance Score": np.random.randint(60, 95, 10),
        "Active Days": np.random.randint(30, 365, 10),
        "Tier": np.random.choice(["T0", "T1", "T2", "T3"], 10, p=[0.1, 0.2, 0.4, 0.3])
    })
    
    # AI分析结果
    ai_analysis = pd.DataFrame({
        "Seller": sellers,
        "AI_Growth_Score": np.random.randint(60, 95, 10),
        "Product_Gap_Count": np.random.randint(0, 15, 10),
        "Compliance_Risk": np.random.choice(["Low", "Medium", "High"], 10, p=[0.6, 0.3, 0.1]),
        "VOS_Sentiment": np.random.uniform(3.0, 5.0, 10),
        "Revenue_Potential": np.random.randint(10000, 80000, 10),
        "AI_Recommendation": [
            "扩展产品线", "优化listing质量", "提升合规分数", "增加广告投入",
            "改善客户服务", "扩展到新类目", "优化价格策略", "提升品牌形象",
            "增加库存深度", "改善物流效率"
        ]
    })
    
    return seller_data, ai_analysis

# 加载数据
seller_data, ai_analysis = generate_mock_data()

# 创建四个主要标签页
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 Goal - 目标设定和绩效跟踪", 
    "🔍 Recruitment - 卖家招募自动化", 
    "📋 Onboarding - 入驻流程管理", 
    "🚀 Win - 卖家增长和成功管理"
])

# ----------------------
# 1️⃣ Goal Module - 目标设定和绩效跟踪
# ----------------------
with tab1:
    st.header("🎯 Goal - 目标设定和绩效跟踪")
    st.info("📊 明确定义和跟踪个人AM业务目标，确保与组织目标保持一致")
    
    # 核心KPI仪表板
    st.subheader("📊 核心KPI仪表板")
    
    # ICQ指标数据 - 显示实际值、目标值和WoW变化
    icq_col1, icq_col2, icq_col3, icq_col4, icq_col5 = st.columns(5)
    
    with icq_col1:
        st.metric("Launched Sellers", "45", delta="+3 WoW", delta_color="normal")
        st.caption("目标: 50 (缺口: -5)")
    with icq_col2:
        st.metric("FBA Adopted Sellers", "28", delta="+2 WoW", delta_color="normal")
        st.caption("目标: 30 (缺口: -2)")
    with icq_col3:
        st.metric("FBA BA Count", "15", delta="+1 WoW", delta_color="normal")
        st.caption("目标: 12 (超额: +3)")
    with icq_col4:
        st.metric("GMS", "$2.8M", delta="+$0.3M WoW", delta_color="normal")
        st.caption("目标: $3.0M (缺口: -$0.2M)")
    with icq_col5:
        st.metric("Ads Adoption Rate", "67%", delta="+2% WoW", delta_color="normal")
        st.caption("目标: 70% (缺口: -3%)")
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🔍 AI行动计划推荐")
        
        # 基于缺口的AI推荐
        st.write("**基于当前绩效缺口的AI推荐：**")
        
        recommendations = [
            {
                "问题": "GMS缺口较大 (-$0.2M)",
                "AI推荐": "重点关注高潜力卖家 TechGiant_SG (WoW增长+25%)",
                "预期影响": "+$150K GMS",
                "优先级": "🔴 高"
            },
            {
                "问题": "FBA采用率低于目标",
                "AI推荐": "推荐ElectroMax_ID进行FBA BA扩展 (当前GMS强劲)",
                "预期影响": "+5个FBA BA",
                "优先级": "🟡 中"
            },
            {
                "问题": "Listing质量缺口",
                "AI推荐": "优先处理FashionHub_MY的图片和标题优化",
                "预期影响": "+15%转化率",
                "优先级": "🟡 中"
            }
        ]
        
        for rec in recommendations:
            with st.expander(f"{rec['优先级']} {rec['问题']}"):
                st.write(f"**AI推荐**: {rec['AI推荐']}")
                st.write(f"**预期影响**: {rec['预期影响']}")
                if st.button(f"执行推荐", key=f"exec_{rec['问题']}"):
                    st.success("✅ 推荐已添加到行动计划！")
    
    with col2:
        st.subheader("📈 YTD目标进度")
        
        # YTD进度追踪
        ytd_progress = pd.DataFrame({
            "指标": ["Launched Sellers", "FBA Adopted", "FBA BA", "GMS", "Ads Adoption"],
            "YTD实际": [180, 120, 58, "$11.2M", "65%"],
            "YTD目标": [200, 130, 50, "$12.0M", "70%"],
            "完成率": ["90%", "92%", "116%", "93%", "93%"],
            "状态": ["🔴 需努力", "🔴 需努力", "🟢 超额完成", "🔴 需努力", "🔴 需努力"]
        })
        st.dataframe(ytd_progress, use_container_width=True)
        
        # 高潜力卖家识别
        st.subheader("⭐ 高潜力卖家识别")
        
        high_potential = pd.DataFrame({
            "卖家": ["TechGiant_SG", "ElectroMax_ID", "FashionHub_MY"],
            "WoW GMS增长": ["+25%", "+18%", "+12%"],
            "当前GMS": ["$180K", "$120K", "$95K"],
            "AI推荐行动": ["扩大产品线", "启用FBA BA", "优化Listing"],
            "潜在影响": ["+$50K", "+$30K", "+$20K"]
        })
        st.dataframe(high_potential, use_container_width=True)
        
        if st.button("🤖 重新分析高潜力卖家", type="primary"):
            st.success("✅ AI重新分析完成！发现2个新的高潜力机会。")

# ----------------------
# 2️⃣ Recruitment Module - 卖家招募自动化
# ----------------------
with tab2:
    st.header("🔍 Recruitment - 卖家招募自动化")
    st.info("🎯 识别、优先排序和接触能够推动市场增长的卖家")
    
    # 卖家画像和优先级排序
    st.subheader("📊 卖家画像和优先级排序")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**基于GMS表现的卖家实力分析**")
        
        # 潜在卖家分析
        prospect_analysis = pd.DataFrame({
            "卖家": ["TechCorp_VN", "FashionPlus_TH", "HomeStyle_MY", "BeautyMax_SG"],
            "现有市场GMS": ["$2.5M", "$1.8M", "$1.2M", "$2.1M"],
            "品牌地位": ["领先品牌", "区域品牌", "新兴品牌", "领先品牌"],
            "跨市场匹配度": ["95%", "87%", "78%", "92%"],
            "优先级": ["P0", "P1", "P2", "P0"],
            "业务潜力": ["Very High", "High", "Medium", "Very High"]
        })
        st.dataframe(prospect_analysis, use_container_width=True)
        
        # 手动调整优先级
        st.write("**优先级手动调整**")
        selected_seller = st.selectbox("选择卖家进行调整", prospect_analysis["卖家"])
        new_priority = st.selectbox("调整优先级", ["P0", "P1", "P2"])
        
        if st.button("更新优先级"):
            st.success(f"✅ {selected_seller} 的优先级已更新为 {new_priority}")
    
    with col2:
        st.write("**接触路线图和邮件节奏**")
        
        # 接触计划
        engagement_plan = pd.DataFrame({
            "接触点": ["Day 1", "Day 3", "Day 7", "Day 14", "电话跟进"],
            "渠道": ["邮件", "邮件", "邮件", "邮件", "电话"],
            "内容类型": ["初次介绍", "价值主张", "案例分享", "最后机会", "直接沟通"],
            "响应率": ["25%", "18%", "12%", "8%", "35%"],
            "状态": ["✅ 已发送", "✅ 已发送", "📅 待发送", "📅 计划中", "📅 计划中"]
        })
        st.dataframe(engagement_plan, use_container_width=True)
        
        # 动态调整设置
        st.write("**动态调整设置**")
        response_threshold = st.slider("响应阈值 (天)", 1, 14, 7)
        escalation_channel = st.selectbox("升级渠道", ["电话", "LinkedIn", "WhatsApp"])
        
        if st.button("应用动态调整"):
            st.success("✅ 接触频率和渠道已根据响应度动态调整")
    
    st.markdown("---")
    
    # 招募漏斗跟踪
    st.subheader("📈 招募漏斗跟踪")
    
    col3, col4 = st.columns(2)
    
    with col3:
        # 漏斗可视化
        funnel_stages = ["潜在对象", "已联系", "谈判中", "已签约"]
        funnel_counts = [150, 80, 25, 8]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
        bars = ax.barh(funnel_stages, funnel_counts, color=colors)
        
        # 添加数值标签
        for i, (bar, count) in enumerate(zip(bars, funnel_counts)):
            conversion_rate = count / funnel_counts[0] * 100 if i > 0 else 100
            ax.text(bar.get_width() + 2, bar.get_y() + bar.get_height()/2, 
                   f'{count} ({conversion_rate:.1f}%)', 
                   ha='left', va='center')
        
        ax.set_title('招募漏斗分析')
        ax.set_xlabel('数量')
        st.pyplot(fig)
    
    with col4:
        st.write("**招募绩效指标**")
        
        # 绩效指标
        perf_col1, perf_col2 = st.columns(2)
        with perf_col1:
            st.metric("总转化率", "5.3%", delta="+0.8%")
            st.metric("平均招募周期", "18天", delta="-3天")
        with perf_col2:
            st.metric("本月新签约", "8个", delta="+3个")
            st.metric("预期月度完成", "12个", delta="目标10个")
        
        st.write("**按优先级分布**")
        priority_dist = pd.DataFrame({
            "优先级": ["P0", "P1", "P2"],
            "数量": [25, 45, 80],
            "签约率": ["32%", "18%", "8%"],
            "平均周期": ["12天", "18天", "28天"]
        })
        st.dataframe(priority_dist, use_container_width=True)
        
        if st.button("🔄 刷新招募数据", type="primary"):
            st.success("✅ 招募数据已刷新！发现5个新的高优先级机会。")

# ----------------------
# 3️⃣ Onboarding Module - 入驻流程管理
# ----------------------
with tab3:
    st.header("📋 Onboarding - 入驻流程管理")
    st.info("🛠️ 确保卖家顺利完成激活流程，提供逐步可见性和AI指导")
    
    # 入驻进度跟踪
    st.subheader("📊 入驻进度跟踪")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**关键入驻里程碑**")
        
        # 入驻里程碑数据
        onboarding_milestones = pd.DataFrame({
            "卖家": ["TechCorp_VN", "FashionPlus_TH", "HomeStyle_MY", "BeautyMax_SG"],
            "账户设置": ["✅ 完成", "✅ 完成", "✅ 完成", "✅ 完成"],
            "KYC验证": ["✅ 完成", "⚠️ 待处理", "✅ 完成", "✅ 完成"],
            "产品Listing": ["✅ 完成", "✅ 完成", "🔄 进行中", "📅 待开始"],
            "首次发货": ["✅ 完成", "📅 待开始", "📅 待开始", "📅 待开始"],
            "整体进度": ["100%", "60%", "75%", "50%"]
        })
        st.dataframe(onboarding_milestones, use_container_width=True)
        
        # AI监控和瓶颈识别
        st.write("**AI瓶颈识别**")
        bottlenecks = [
            "🔴 FashionPlus_TH: KYC文档缺失，已延迟3天",
            "🟡 HomeStyle_MY: Listing图片质量需要改善",
            "🟢 BeautyMax_SG: 进展正常，无瓶颈"
        ]
        
        for bottleneck in bottlenecks:
            st.write(f"• {bottleneck}")
    
    with col2:
        st.write("**AI推荐干预行动**")
        
        # AI推荐的干预行动
        intervention_actions = pd.DataFrame({
            "卖家": ["FashionPlus_TH", "HomeStyle_MY", "BeautyMax_SG"],
            "识别问题": ["KYC延迟", "Listing质量", "无问题"],
            "推荐行动": ["联系协助KYC", "提供图片指导", "继续监控"],
            "预期解决时间": ["2天", "1天", "N/A"],
            "优先级": ["高", "中", "低"]
        })
        st.dataframe(intervention_actions, use_container_width=True)
        
        # 卖家赋能资源
        st.write("**卖家赋能资源**")
        
        enablement_resources = [
            "📄 快速入门指南 (中英文)",
            "❓ 常见问题FAQ",
            "🎥 产品Listing最佳实践视频",
            "📞 专属客服热线",
            "💬 卖家社群支持"
        ]
        
        for resource in enablement_resources:
            st.write(f"• {resource}")
        
        if st.button("📤 发送定制化指导", type="primary"):
            st.success("✅ 已向所有入驻中的卖家发送定制化指导文档！")
    
    st.markdown("---")
    
    # 入驻成功率分析
    st.subheader("📈 入驻成功率分析")
    
    col3, col4 = st.columns(2)
    
    with col3:
        # 入驻转化漏斗
        onboarding_funnel = ["初次接触", "签约意向", "开始入驻", "完成入驻", "首次销售"]
        onboarding_counts = [100, 75, 60, 45, 38]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#feca57']
        bars = ax.bar(onboarding_funnel, onboarding_counts, color=colors)
        
        # 添加数值标签
        for bar, count in zip(bars, onboarding_counts):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                   f'{count}', ha='center', va='bottom')
        
        ax.set_title('入驻转化漏斗')
        ax.set_ylabel('数量')
        plt.xticks(rotation=45)
        st.pyplot(fig)
    
    with col4:
        st.write("**入驻绩效指标**")
        
        # 入驻绩效指标
        onboard_col1, onboard_col2 = st.columns(2)
        with onboard_col1:
            st.metric("入驻成功率", "75%", delta="+5%")
            st.metric("平均入驻时间", "14天", delta="-2天")
        with onboard_col2:
            st.metric("首次销售转化", "84%", delta="+8%")
            st.metric("30天留存率", "92%", delta="+3%")
        
        # 预测入驻时间
        st.write("**入驻时间预测**")
        time_prediction = pd.DataFrame({
            "卖家": ["FashionPlus_TH", "HomeStyle_MY", "BeautyMax_SG"],
            "当前进度": ["60%", "75%", "50%"],
            "预计完成": ["5天", "3天", "7天"],
            "风险等级": ["中", "低", "低"]
        })
        st.dataframe(time_prediction, use_container_width=True)
        
        if st.button("🔮 更新预测模型", type="primary"):
            st.success("✅ 基于最新数据更新预测模型！准确率提升至89%。")

# ----------------------
# 4️⃣ Win Module - 卖家增长和成功管理
# ----------------------
with tab4:
    st.header("🚀 Win - 卖家增长和成功管理")
    st.info("📈 专注于推动可持续的卖家增长，基于功能采用和质量评分评估绩效")
    
    # 功能采用跟踪
    st.subheader("📊 功能采用跟踪")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("**关键增长功能采用情况**")
        
        # 功能采用数据
        feature_adoption = pd.DataFrame({
            "卖家": ["TechGiant_SG", "ElectroMax_ID", "FashionHub_MY", "BeautyPro_VN"],
            "FBA": ["✅ 已启用", "❌ 未启用", "✅ 已启用", "✅ 已启用"],
            "广告": ["✅ 已启用", "✅ 已启用", "❌ 未启用", "✅ 已启用"],
            "促销": ["✅ 已启用", "❌ 未启用", "✅ 已启用", "❌ 未启用"],
            "优惠券": ["❌ 未启用", "✅ 已启用", "✅ 已启用", "✅ 已启用"],
            "采用率": ["75%", "50%", "75%", "75%"]
        })
        st.dataframe(feature_adoption, use_container_width=True)
        
        # 功能采用建议
        st.write("**AI功能采用建议**")
        adoption_recommendations = [
            "🎯 ElectroMax_ID: 强劲目录但广告采用低 → 推荐启用广告",
            "📈 FashionHub_MY: 高广告支出但ROI低 → 建议优化活动",
            "🏷️ TechGiant_SG: 缺少优惠券功能 → 推荐启用促销工具"
        ]
        
        for rec in adoption_recommendations:
            st.write(f"• {rec}")
    
    with col2:
        st.write("**绩效记分卡**")
        
        # 绩效记分卡
        performance_scorecard = pd.DataFrame({
            "卖家": ["TechGiant_SG", "ElectroMax_ID", "FashionHub_MY", "BeautyPro_VN"],
            "Listing质量": ["85/100", "72/100", "68/100", "91/100"],
            "广告ROI": ["3.2x", "2.1x", "1.8x", "4.1x"],
            "库存健康": ["优秀", "良好", "需改善", "优秀"],
            "整体评分": ["A", "B", "C+", "A+"]
        })
        st.dataframe(performance_scorecard, use_container_width=True)
        
        # 改善建议
        st.write("**质量改善建议**")
        quality_improvements = pd.DataFrame({
            "卖家": ["FashionHub_MY", "ElectroMax_ID"],
            "主要问题": ["图片质量低", "标题不完整"],
            "建议行动": ["更新产品图片", "优化标题关键词"],
            "预期提升": ["+20%转化率", "+15%搜索排名"]
        })
        st.dataframe(quality_improvements, use_container_width=True)
        
        if st.button("📧 发送改善建议", type="primary"):
            st.success("✅ 已向相关卖家发送个性化改善建议！")
    
    st.markdown("---")
    
    # 成功结果定义和跟踪
    st.subheader("🎯 成功结果定义和跟踪")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.write("**收入提升跟踪**")
        
        # 收入提升数据
        revenue_lift = pd.DataFrame({
            "卖家": ["TechGiant_SG", "ElectroMax_ID", "FashionHub_MY", "BeautyPro_VN"],
            "基准收入": ["$150K", "$80K", "$60K", "$120K"],
            "当前收入": ["$195K", "$98K", "$72K", "$156K"],
            "收入提升": ["+30%", "+23%", "+20%", "+30%"],
            "功能贡献": ["广告+FBA", "FBA", "促销", "全功能"]
        })
        st.dataframe(revenue_lift, use_container_width=True)
        
        # 持续参与度
        st.write("**持续参与度指标**")
        engagement_metrics = pd.DataFrame({
            "指标": ["月活跃天数", "新品上架", "广告活动", "客服响应"],
            "平均值": ["28天", "5个", "3个", "2小时"],
            "目标值": ["25天", "3个", "2个", "4小时"],
            "达成状态": ["✅ 超额", "✅ 超额", "✅ 超额", "✅ 超额"]
        })
        st.dataframe(engagement_metrics, use_container_width=True)
    
    with col4:
        st.write("**增长潜力预测**")
        
        # 增长潜力预测
        growth_potential = pd.DataFrame({
            "卖家": ["TechGiant_SG", "ElectroMax_ID", "FashionHub_MY", "BeautyPro_VN"],
            "当前表现": ["优秀", "良好", "一般", "优秀"],
            "功能采用": ["75%", "50%", "75%", "75%"],
            "预测增长": ["+40%", "+35%", "+25%", "+45%"],
            "信心度": ["92%", "78%", "65%", "95%"]
        })
        st.dataframe(growth_potential, use_container_width=True)
        
        # 成功案例展示
        st.write("**成功案例**")
        success_stories = [
            "🏆 TechGiant_SG: 启用全功能后3个月收入增长30%",
            "📈 BeautyPro_VN: 优化Listing质量后转化率提升25%",
            "🎯 ElectroMax_ID: 启用FBA后客户满意度提升至4.8分"
        ]
        
        for story in success_stories:
            st.write(f"• {story}")
        
        if st.button("📊 生成成功报告", type="primary"):
            st.success("✅ 成功案例报告已生成！包含详细的ROI分析和最佳实践。")

# 页面底部信息
st.markdown("---")
col1, col2, col3 = st.columns(3)

with col1:
    st.info("📊 **数据源**: Quicksight, VOS Hub, Selection AI")
with col2:
    st.info("🤖 **AI引擎**: AWS Bedrock Claude 3")
with col3:
    st.info("🔄 **最后更新**: " + datetime.now().strftime("%Y-%m-%d %H:%M"))

# 版权信息
st.markdown("""
<div style='text-align: center; color: #666; margin-top: 2rem;'>
    <p>© 2025 GROW AI Assistant | Powered by Amazon Web Services</p>
</div>
""", unsafe_allow_html=True)