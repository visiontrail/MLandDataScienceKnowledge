# 安装所需的库
# !pip install yfinance==0.2.4
#!pip install pandas==1.3.3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 使用yfinance库提取股票数据
apple = yf.Ticker("AAPL")

# 从JSON文件中提取股票信息
import json
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
apple_info['country']

# 提取股价历史数据
apple_share_price_data = apple.history(period="1y")
print(apple_share_price_data)

# 重置DataFrame的索引
apple_share_price_data.reset_index(inplace=True)

# 绘制开盘价与日期的关系图
apple_share_price_data.plot(x="Date", y="Open")

# 提取股息数据
apple.dividends

# 绘制股息随时间变化图
apple.dividends.plot()

# 使用yfinance库提取AMD股票数据
amd = yf.Ticker("AMD")
# curl -o amd.json https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json

import json
with open('amd.json') as json_file:
    amd_info = json.load(json_file)

# 提取AMD股票的股价历史数据
amd_share_price_data = amd.history(period="1y")
amd_share_price_data.head()