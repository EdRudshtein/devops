import pandas as pd
import time
from datetime import datetime

a = pd.Series([1, 2, 3])
print(a)

for i in range(30):
	print(f'{i} / {datetime.now()}')
	time.sleep(1)
