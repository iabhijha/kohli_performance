import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Virat_Kohli.csv")
print(df.head())

#total number of runs Kohli has scored
print("Total Runs of Kohli", df["Runs"].sum())

#Find out the total number of balls kohli has faced
print("Total number of balls kohli has Faces", df["BF"].sum())

#Find out the average strike rate of kohli
print("Average strike rate of Kohli",df["SR"].mean())

#Number of matches he has played at different positions
print(df["Pos"].head(10))

positions = df["Pos"].unique()
print(positions)

df["Pos"] = df["Pos"].map({
    3.0: "Batting at 3",
    4.0: "Batting at 4",
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    5.0: "Batting at 5",
    6.0: "Batting at 6",
})
print(df.head(10))
pos_counts = df["Pos"].value_counts()
print(pos_counts)
print(type(pos_counts))


#Total runs scored in different positions

pos_counts_values = pos_counts.values
pos_counts_labels = pos_counts.index

fig = plt.figure(figsize=(10, 7))
plt.pie(pos_counts_values, labels=pos_counts_labels)
plt.show()

#Total sixes scored in different positions

runs_at_pos = df.groupby("POS")["6s"].sum()
print(runs_at_pos, type(runs_at_pos))
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos_values.index

fig = plt.figure(figsize=(10, 7))
plt.bar(
    runs_at_pos_labels,
    runs_at_pos_values,
    color="green",
    width=0.3
)
plt.show()

#Number of matches he has playes with different Oppostion
show_pie_plots(df, "Opposition")

#Number of mathces he has played at different Grounds
show_pie_plots(df, "Ground")

#Total runs scored with different countries
runs_with_countries = df.groupby("Opposition")

#Number of centuries scored by him in 1st and 2nd innings
centuries = df.query("Runs >= 100")
print(centuries)


#Calculate the dismissals of Kohli

#Against which teams he has scored the most runs

#Against which teams 