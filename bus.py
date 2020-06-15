import json
import pandas as pd
import os

fin_path = input('請輸入解壓縮後的檔名 (預設值 GetRoute)：')
if fin_path == '':
    fin_path = 'GetRoute'
with open(fin_path, 'r') as fin:
    content = fin.read()
data = json.loads(content)
df = pd.DataFrame(data=data['BusInfo'])
df_need = df.loc[:, ['providerName', 'nameZh', 'pathAttributeName', 'realSequence', 'distance']]
filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), '路線.xlsx'))
df_need.to_excel(filepath, index = False)
print('已經輸出至 ' + filepath)