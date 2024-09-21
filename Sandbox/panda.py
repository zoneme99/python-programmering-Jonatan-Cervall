import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Sandbox/all_weekly_excess_deaths.csv')

df["covid_deaths"].plot()
df["non_covid_deaths"].plot()

plt.show()