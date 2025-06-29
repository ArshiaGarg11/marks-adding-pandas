import pandas as pd

df = pd.read_csv('marks.csv')

result= df.groupby("Roll Num", as_index=False)["Marks"].sum()

result.to_csv("Output.csv", index=False)

print("Output saved to Output.csv") 
