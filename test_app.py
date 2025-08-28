#!/usr/bin/env python3
"""
简单的应用测试文件
运行: python test_app.py
"""

import sys
import importlib.util

def test_import():
    """测试主应用是否可以正常导入"""
    try:
        import grow_ai_assistant
        print("✅ grow_ai_assistant 导入成功")
        return True
    except Exception as e:
        print(f"❌ grow_ai_assistant 导入失败: {e}")
        return False

def test_dependencies():
    """测试依赖包是否正确安装"""
    required_packages = [
        'streamlit',
        'pandas', 
        'numpy',
        'plotly',
        'matplotlib'
    ]
    
    failed_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package} 已安装")
        except ImportError:
            print(f"❌ {package} 未安装")
            failed_packages.append(package)
    
    return len(failed_packages) == 0

def test_streamlit_config():
    """测试 Streamlit 配置文件"""
    import os
    
    config_path = ".streamlit/config.toml"
    if os.path.exists(config_path):
        print(f"✅ Streamlit 配置文件存在: {config_path}")
        return True
    else:
        print(f"⚠️  Streamlit 配置文件不存在: {config_path}")
        return False

def test_required_files():
    """测试必需文件是否存在"""
    import os
    
    required_files = [
        'grow_ai_assistant.py',
        'streamlit_app.py', 
        'requirements.txt',
        'README.md'
    ]
    
    missing_files = []
    
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file} 存在")
        else:
            print(f"❌ {file} 不存在")
            missing_files.append(file)
    
    return len(missing_files) == 0

def main():
    """运行所有测试"""
    print("🧪 开始测试 GROW AI Assistant...\n")
    
    tests = [
        ("文件检查", test_required_files),
        ("依赖检查", test_dependencies),
        ("配置检查", test_streamlit_config),
        ("导入测试", test_import)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}:")
        if test_func():
            passed += 1
        print("-" * 40)
    
    print(f"\n📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！应用可以正常运行。")
        print("\n🚀 运行应用:")
        print("   python run_app.py")
        print("   或")
        print("   streamlit run grow_ai_assistant.py")
        return True
    else:
        print("❌ 部分测试失败，请检查上述错误。")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)