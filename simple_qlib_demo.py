#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qlib 简单演示脚本
================

这是一个简化的Qlib演示，展示基本功能和概念，专为新手设计。

作者: Qlib 学习助手
"""

def show_qlib_info():
    """显示Qlib基本信息"""
    print("🎯 Qlib 量化投资平台新手指南")
    print("=" * 50)
    
    try:
        import qlib
        print(f"✅ Qlib版本: {qlib.__version__}")
    except Exception as e:
        print(f"❌ 导入Qlib失败: {e}")
        return False
    
    return True

def explain_qlib_concepts():
    """解释Qlib核心概念"""
    print("\n📚 Qlib 核心概念:")
    
    concepts = {
        "📊 数据层 (Data)": "处理金融数据，包括股票价格、成交量等",
        "🧠 模型层 (Model)": "机器学习模型，用于预测股票收益率",
        "📈 策略层 (Strategy)": "基于模型预测制定投资决策",
        "🔄 回测层 (Backtest)": "验证策略在历史数据上的表现",
        "📊 分析层 (Analysis)": "评估策略的风险收益特征"
    }
    
    for concept, description in concepts.items():
        print(f"   {concept}: {description}")

def show_qlib_structure():
    """显示Qlib项目结构"""
    print("\n🏗️ 项目目录结构:")
    
    structure = {
        "qlib/": "核心库代码",
        "├── data/": "数据处理模块",
        "├── model/": "机器学习模型",
        "├── strategy/": "投资策略",
        "├── backtest/": "回测引擎",
        "├── contrib/": "社区贡献模型",
        "├── workflow/": "完整工作流",
        "examples/": "示例代码",
        "├── tutorial/": "新手教程",
        "├── benchmarks/": "基准测试",
        "└── workflow_by_code.py": "代码工作流示例"
    }
    
    for path, description in structure.items():
        print(f"   {path:<25} {description}")

def show_learning_path():
    """显示学习路径"""
    print("\n🚀 推荐学习路径:")
    
    path = [
        ("第1步", "🏗️ 环境配置", "安装Qlib和相关依赖"),
        ("第2步", "📊 数据准备", "了解金融数据格式和获取方法"),
        ("第3步", "📖 基础教程", "学习examples/tutorial/详细教程"),
        ("第4步", "🤖 模型训练", "尝试不同的机器学习模型"),
        ("第5步", "📈 策略开发", "设计你的第一个交易策略"),
        ("第6步", "🔄 回测验证", "验证策略的历史表现"),
        ("第7步", "🔧 优化改进", "根据结果优化策略参数")
    ]
    
    for step, title, description in path:
        print(f"   {step}: {title} - {description}")

def show_key_files():
    """显示关键文件"""
    print("\n📁 关键文件说明:")
    
    files = [
        "📔 examples/tutorial/detailed_workflow.ipynb - 详细的Jupyter教程",
        "🐍 examples/workflow_by_code.py - Python代码工作流示例",
        "📊 examples/benchmarks/ - 各种模型的基准测试",
        "🔧 qlib/config.py - 全局配置文件",
        "📈 qlib/data/ - 数据处理相关代码",
        "🤖 qlib/model/ - 机器学习模型实现"
    ]
    
    for file_info in files:
        print(f"   {file_info}")

def show_next_actions():
    """显示下一步行动"""
    print("\n✨ 建议的下一步行动:")
    
    actions = [
        "1. 📔 打开 examples/tutorial/detailed_workflow.ipynb 学习详细教程",
        "2. 🏃 运行 examples/workflow_by_code.py 体验完整工作流",
        "3. 📊 准备或下载金融数据集",
        "4. 🔍 浏览 qlib/contrib/ 目录了解可用模型",
        "5. 📖 阅读官方文档: https://qlib.readthedocs.io/",
        "6. 🤝 加入社区: https://github.com/microsoft/qlib"
    ]
    
    for action in actions:
        print(f"   {action}")

def check_dependencies():
    """检查关键依赖"""
    print("\n🔍 检查关键依赖:")
    
    dependencies = ['numpy', 'pandas', 'sklearn', 'matplotlib']
    
    for dep in dependencies:
        try:
            __import__(dep)
            print(f"   ✅ {dep}")
        except ImportError:
            print(f"   ❌ {dep} - 未安装")

def main():
    """主函数"""
    # 显示基本信息
    if not show_qlib_info():
        return
    
    # 解释核心概念
    explain_qlib_concepts()
    
    # 显示项目结构
    show_qlib_structure()
    
    # 检查依赖
    check_dependencies()
    
    # 显示学习路径
    show_learning_path()
    
    # 显示关键文件
    show_key_files()
    
    # 显示下一步行动
    show_next_actions()
    
    print("\n" + "=" * 50)
    print("🎉 欢迎来到Qlib的世界！祝你量化投资之路顺利！")

if __name__ == "__main__":
    main() 