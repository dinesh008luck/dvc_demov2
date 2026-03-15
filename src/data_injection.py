import numpy as np
import pandas as pd
import os

df= pd.read_csv(r'C:\Users\SLS0822\Downloads\sqllab_sap_live_mtd_sales_20260314T153733.csv')

df= df.iloc[:,3:]

df= df [df['Quantity Sold'] >10]

df= df.pivot_table(index='Customer Code',
                   columns='Sales UOM',
                   values='Quantity Sold',
                   aggfunc = 'sum',
                   fill_value=0
                   )
df.to_csv(os.path.join('data','sales.csv'))

