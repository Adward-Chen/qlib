# Qlib 数据准备指南

## 📊 数据是量化投资的基础

Qlib支持多种数据源和格式，作为量化新手，了解如何准备和使用数据是非常重要的第一步。

## 🗂️ 数据类型

### 1. 基础行情数据
- **日线数据**: 开盘价、最高价、最低价、收盘价、成交量
- **分钟数据**: 1分钟、5分钟等高频数据
- **复权数据**: 前复权、后复权价格

### 2. 衍生指标数据
- **技术指标**: MA、RSI、MACD、布林带等
- **基本面数据**: PE、PB、ROE等财务指标
- **市场数据**: 换手率、涨跌幅、振幅等

## 🚀 数据获取方式

### 方式1: 使用Qlib提供的示例数据
```bash
# 下载CSI300数据集（推荐新手使用）
python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/cn_data --region cn

# 下载美股数据集
python scripts/get_data.py qlib_data --target_dir ~/.qlib/qlib_data/us_data --region us
```

### 方式2: 使用开源数据源
- **AKShare**: 免费的中文财经数据库
- **tushare**: 中文股票数据源
- **yfinance**: Yahoo Finance数据
- **ccxt**: 加密货币数据

### 方式3: 使用商业数据源
- **Wind**: 万得数据库
- **Bloomberg**: 彭博数据
- **Choice**: 同花顺数据

## 🔧 数据格式

### Qlib标准格式
```
~/.qlib/qlib_data/
├── cn_data/               # 中国市场数据
│   ├── instruments/       # 股票列表
│   ├── features/          # 特征数据
│   └── calendars/         # 交易日历
└── us_data/               # 美国市场数据
    ├── instruments/       
    ├── features/          
    └── calendars/         
```

### 数据文件示例
```python
# 获取股票数据的示例代码
from qlib.data import D

# 获取CSI300股票列表
instruments = D.instruments(market='csi300')

# 获取价格数据
data = D.features(
    instruments, 
    ['$open', '$high', '$low', '$close', '$volume'],
    start_time='2020-01-01',
    end_time='2021-12-31'
)
```

## 📝 数据配置

### 1. 初始化Qlib
```python
import qlib
from qlib.constant import REG_CN

# 初始化中国市场
qlib.init(provider_uri="~/.qlib/qlib_data/cn_data", region=REG_CN)
```

### 2. 数据Handler配置
```python
from qlib.contrib.data.handler import Alpha158

# 使用Alpha158因子集
data_handler_config = {
    "start_time": "2008-01-01",
    "end_time": "2020-08-01", 
    "fit_start_time": "2008-01-01",
    "fit_end_time": "2014-12-31",
    "instruments": "csi300",
    "infer_processors": [
        {"class": "RobustZScoreNorm", "kwargs": {"fields_group": "feature", "clip_outlier": True}},
        {"class": "Fillna", "kwargs": {"fields_group": "feature"}}
    ],
    "learn_processors": [
        {"class": "DropnaLabel"},
        {"class": "CSRankNorm", "kwargs": {"fields_group": "label"}},
    ]
}
```

## 🛠️ 自定义数据接入

### 1. CSV数据转换
```python
import pandas as pd
from qlib.data.dataset.utils import load_dataset

# 读取CSV数据
df = pd.read_csv('your_data.csv')

# 转换为Qlib格式
# 需要包含: instrument, datetime, feature columns
df = df.set_index(['instrument', 'datetime'])

# 保存为Qlib数据格式
# 参考 scripts/data_collector/ 中的示例
```

### 2. 实时数据接入
```python
from qlib.data.provider.base import PitProvider

class CustomDataProvider(PitProvider):
    """自定义数据提供者"""
    
    def __init__(self):
        super().__init__()
    
    def get_data(self, instruments, start_time, end_time, fields):
        # 实现你的数据获取逻辑
        pass
```

## 📊 数据质量检查

### 1. 数据完整性检查
```python
from qlib.data import D

# 检查数据是否存在
instruments = D.instruments(market='csi300')
print(f"股票数量: {len(instruments)}")

# 检查时间范围
data = D.features(instruments[:5], ['$close'], '2020-01-01', '2020-12-31')
print(f"数据形状: {data.shape}")
print(f"缺失值: {data.isna().sum()}")
```

### 2. 数据质量验证
```python
import matplotlib.pyplot as plt

# 绘制价格趋势
stock_data = D.features(['000001.SZ'], ['$close'], '2020-01-01', '2020-12-31')
stock_data.plot(title='Stock Price Trend')
plt.show()

# 检查异常值
print("价格统计:")
print(stock_data.describe())
```

## ⚠️ 常见问题

### Q1: 数据下载失败怎么办？
- 检查网络连接
- 确认目标目录权限
- 尝试使用代理

### Q2: 如何添加自定义因子？
- 在data handler中定义新的特征
- 实现特征计算逻辑
- 添加到配置文件中

### Q3: 数据更新频率？
- 日线数据通常每天更新
- 分钟数据需要实时或准实时更新
- 基本面数据通常季度更新

## 🎯 新手建议

1. **从示例数据开始**: 先使用Qlib提供的示例数据集学习
2. **理解数据格式**: 熟悉Qlib的数据组织方式
3. **验证数据质量**: 总是检查数据的完整性和准确性
4. **逐步扩展**: 从简单的价量数据开始，逐步添加更多因子
5. **文档先行**: 详细记录你的数据处理流程

## 📚 进阶学习

- 📖 [Qlib数据文档](https://qlib.readthedocs.io/en/latest/component/data.html)
- 🔧 [数据处理示例](examples/data_demo/)
- 🤖 [自定义Handler](qlib/contrib/data/handler.py)
- 📊 [因子工程](qlib/data/dataset/processor.py) 