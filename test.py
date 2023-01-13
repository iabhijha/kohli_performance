#pandas
import pandas as pd

data = {
    "apples": [4, 3, 6, 1],
    "oranges": [3, 7, 4, 1]
}

index_titles = [
    "Aaron", "Shaun", "James", "Wilson"
]    
df = pd.DataFrame(data, index_titles)

# print(df.loc["Aaron"])
# print(df.loc["Aaron"]["apples"])
print(df["oranges"].iloc[1:])
print(type(df))