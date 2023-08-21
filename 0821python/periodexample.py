import pandas as pd
import numpy as np

date_strings = np.array([
    '2023-01-01',
    '2023-02-02',
    '2023-02-16',
    '2023-04-05'
])

pddates = pd.to_datetime(date_strings)

#월 단위로 변경
pr_m = pddates.to_period(freq='M')
print(pr_m)