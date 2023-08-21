import pandas as pd
import numpy as np

#2023년 1월 1일부터 월단위로 12개를 생성
ts_ms = pd.date_range(start="2023-01-01", periods=12, freq='M', tz='Asia/Seoul')
print(ts_ms)