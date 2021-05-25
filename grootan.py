import pandas as pd

data = pd.read_csv (r'C:\Users\Desktop\Test\test file.csv')   
df = pd.DataFrame(data, columns= ['Item Type','Total Revenue','Total Cost'])

print(df)

