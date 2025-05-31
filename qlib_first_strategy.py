#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Qlib 新手第一个量化策略
===================

这是一个专为新手设计的简单量化策略示例。
将展示如何使用Qlib构建一个完整的量化投资流程。

作者: Qlib 学习助手
"""

import warnings
warnings.filterwarnings('ignore')

def step1_check_environment():
    """第1步：检查环境和导入必要模块"""
    print("🔍 第1步：检查环境和导入模块")
    print("-" * 40)
    
    try:
        import qlib
        import pandas as pd
        import numpy as np
        from qlib.constant import REG_CN
        
        print("✅ 基础模块导入成功")
        print(f"✅ Qlib版本: {qlib.__version__}")
        return True
    except Exception as e:
        print(f"❌ 模块导入失败: {e}")
        return False

def step2_prepare_sample_data():
    """第2步：准备示例数据"""
    print("\n📊 第2步：准备示例数据")
    print("-" * 40)
    
    try:
        # 创建模拟数据（实际使用中应该使用真实数据）
        import pandas as pd
        import numpy as np
        from datetime import datetime, timedelta
        
        # 生成示例股票代码
        stocks = ['000001.SZ', '000002.SZ', '600000.SH', '600036.SH', '000858.SZ']
        
        # 生成示例时间序列
        start_date = datetime(2020, 1, 1)
        end_date = datetime(2021, 12, 31)
        dates = pd.date_range(start_date, end_date, freq='D')
        
        print(f"✅ 模拟数据包含 {len(stocks)} 只股票")
        print(f"✅ 时间范围: {start_date.date()} 到 {end_date.date()}")
        print(f"✅ 股票代码: {stocks}")
        
        return stocks, dates
        
    except Exception as e:
        print(f"❌ 数据准备失败: {e}")
        return None, None

def step3_define_simple_strategy():
    """第3步：定义简单的均线策略"""
    print("\n📈 第3步：定义简单的均线策略")
    print("-" * 40)
    
    strategy_description = """
    📋 策略说明：
    1. 计算每只股票的5日和20日移动平均线
    2. 当5日均线上穿20日均线时，认为是买入信号
    3. 当5日均线下穿20日均线时，认为是卖出信号
    4. 选择信号最强的前10只股票进行投资
    """
    
    print(strategy_description)
    
    # 模拟策略逻辑（实际使用中需要真实数据）
    def simple_ma_strategy(prices):
        """简单移动平均策略"""
        # 计算移动平均线
        ma5 = prices.rolling(window=5).mean()
        ma20 = prices.rolling(window=20).mean()
        
        # 生成信号
        signal = (ma5 > ma20).astype(int)  # 1表示买入，0表示持有/卖出
        
        return signal, ma5, ma20
    
    print("✅ 策略定义完成")
    return simple_ma_strategy

def step4_simulate_backtest():
    """第4步：模拟回测过程"""
    print("\n🔄 第4步：模拟回测过程")
    print("-" * 40)
    
    # 模拟回测结果
    backtest_results = {
        "总收益率": "15.6%",
        "年化收益率": "7.8%", 
        "最大回撤": "-8.2%",
        "夏普比率": 1.25,
        "胜率": "58.3%",
        "交易次数": 145
    }
    
    print("📊 回测结果概要:")
    for metric, value in backtest_results.items():
        print(f"   {metric}: {value}")
    
    # 模拟月度收益
    monthly_returns = [2.1, -1.5, 3.2, 0.8, -2.1, 4.5, 1.2, -0.8, 2.8, 1.1, 0.5, 3.1]
    print(f"\n📈 月度收益率: {monthly_returns}")
    
    return backtest_results

def step5_risk_analysis():
    """第5步：风险分析"""
    print("\n⚠️ 第5步：风险分析")
    print("-" * 40)
    
    risk_metrics = {
        "波动率": "12.8%",
        "Beta系数": 0.85,
        "信息比率": 0.42,
        "跟踪误差": "4.2%",
        "最大连续亏损": 3,
        "VaR(95%)": "-2.1%"
    }
    
    print("📊 风险指标:")
    for metric, value in risk_metrics.items():
        print(f"   {metric}: {value}")
    
    print("\n💡 风险提示:")
    print("   • 策略在震荡市场中可能表现不佳")
    print("   • 需要考虑交易成本对收益的影响")
    print("   • 建议进行样本外测试验证策略稳定性")
    
    return risk_metrics

def step6_optimization_suggestions():
    """第6步：优化建议"""
    print("\n🔧 第6步：策略优化建议")
    print("-" * 40)
    
    suggestions = [
        "1. 参数优化：尝试不同的移动平均线周期组合",
        "2. 风控改进：添加止损止盈机制",
        "3. 选股增强：结合基本面指标进行股票筛选",
        "4. 择时优化：添加市场情绪指标判断",
        "5. 成本控制：优化交易频率降低手续费",
        "6. 多因子模型：结合更多技术和基本面因子"
    ]
    
    print("💡 优化方向:")
    for suggestion in suggestions:
        print(f"   {suggestion}")

def step7_next_steps():
    """第7步：后续学习路径"""
    print("\n🚀 第7步：后续学习路径")
    print("-" * 40)
    
    learning_path = [
        ("📚 深入学习", "详细阅读Qlib官方文档和教程"),
        ("💻 实战练习", "使用真实数据运行完整的workflow"),
        ("🔬 模型研究", "学习机器学习模型在量化中的应用"),
        ("📊 因子挖掘", "研究有效的量化因子构建方法"),
        ("🎛️ 参数调优", "掌握超参数优化技巧"),
        ("🏭 系统部署", "了解策略的生产环境部署"),
        ("🤝 社区参与", "加入Qlib社区分享和学习")
    ]
    
    print("📋 建议学习顺序:")
    for step, description in learning_path:
        print(f"   {step}: {description}")
    
    print("\n📖 推荐资源:")
    print("   • examples/tutorial/detailed_workflow.ipynb")
    print("   • examples/benchmarks/ (各种模型对比)")
    print("   • https://qlib.readthedocs.io/ (官方文档)")
    print("   • https://github.com/microsoft/qlib (GitHub社区)")

def main():
    """主函数：执行完整的新手教程"""
    print("🎯 Qlib 新手第一个量化策略教程")
    print("=" * 50)
    
    # 执行各个步骤
    if not step1_check_environment():
        print("❌ 环境检查失败，请先安装必要的依赖")
        return
    
    stocks, dates = step2_prepare_sample_data()
    if stocks is None:
        print("❌ 数据准备失败")
        return
    
    strategy_func = step3_define_simple_strategy()
    
    backtest_results = step4_simulate_backtest()
    
    risk_metrics = step5_risk_analysis()
    
    step6_optimization_suggestions()
    
    step7_next_steps()
    
    print("\n" + "=" * 50)
    print("🎉 恭喜完成第一个量化策略学习！")
    print("💪 现在你可以开始使用真实数据进行实战了！")
    
    print("\n🚀 立即开始实战:")
    print("   python examples/workflow_by_code.py")
    print("   jupyter notebook examples/tutorial/detailed_workflow.ipynb")

if __name__ == "__main__":
    main() 