#!/usr/bin/env python3
"""
GROW AI Assistant 启动脚本
用于本地开发和测试
"""

import subprocess
import sys
import os
from pathlib import Path

def check_dependencies():
    """检查依赖是否已安装"""
    try:
        import streamlit
        print("✅ Streamlit 已安装")
        return True
    except ImportError:
        print("❌ Streamlit 未安装，请运行: pip install -r requirements.txt")
        return False

def main():
    """主启动函数"""
    print("🚀 启动 GROW AI Assistant...")
    print("=" * 50)
    
    # 检查依赖
    if not check_dependencies():
        sys.exit(1)
    
    # 获取当前目录
    current_dir = Path(__file__).parent
    app_file = current_dir / "grow_ai_assistant.py"
    
    if not app_file.exists():
        print(f"❌ 找不到应用文件: {app_file}")
        sys.exit(1)
    
    # 启动 Streamlit 应用
    try:
        print(f"📂 工作目录: {current_dir}")
        print(f"📄 应用文件: {app_file}")
        print("🌐 启动 Web 服务器...")
        print("📱 应用将在浏览器中自动打开")
        print("🔗 如果没有自动打开，请访问: http://localhost:8501")
        print("=" * 50)
        
        # 运行 Streamlit
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            str(app_file),
            "--server.port", "8501",
            "--server.address", "localhost"
        ])
        
    except KeyboardInterrupt:
        print("\n👋 应用已停止")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()