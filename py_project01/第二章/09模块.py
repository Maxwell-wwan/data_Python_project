#导入模块 import
#
# import numpy as np
#
# prices = np.array([100, 102, 101, 105, 107])
# print(type(prices))
# # 日收益率（对数收益）
# returns = np.diff(np.log(prices))
# print("Daily returns:", returns)
#
# # 波动率（std）
# vol = np.std(returns)
# print("Volatility:", vol)



import yfinance as yf
# 下载苹果、微软、标普500 的日线数据
data = yf.download("AAPL MSFT ^GSPC", start="2020-01-01", auto_adjust=True)
print(data.head())