import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sandbox/all_weekly_excess_deaths.csv')

df["covid_deaths"].plot(color = "red")
df["non_covid_deaths"].plot(color = "green")

plt.show()