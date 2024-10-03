import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

df = pd.read_csv("Labs/Labb2/datapoints.csv")

#Separerar testpunkter och träningspunkter och returnera dem som separata dataframes
def data_separation(dataframe, to_find):
    test_pokemons = pd.DataFrame()
    train_pokemons = pd.DataFrame()
    pikachu = 0
    pichu = 0
    for index, row in dataframe.iterrows():
        if pikachu < (to_find / 2):
            test_pokemons = pd.concat([test_pokemons, row.to_frame().T])
            pikachu += 1
        elif pichu < (to_find / 2):
            test_pokemons = pd.concat([test_pokemons, row.to_frame().T])
            pichu += 1
        else:
            train_pokemons = pd.concat([train_pokemons, row.to_frame().T])
    return test_pokemons, train_pokemons

#kopia från labb2.py men lagt till i return en konvertering från index i distance till index i dataframe
#Pga att jag har slumpade index i dataframe
def edistance(xwid, yhei , widlist, heilist):
    width = np.array(list(map(lambda x: np.pow(x - xwid, 2), widlist)))
    height = np.array(list(map(lambda x: np.pow(x - yhei, 2), heilist)))
    distance = np.sqrt(np.add(width, height))
    return widlist.index[np.argmin(distance)]

# trues == summan av alla true-positive och true-negative, motsvarande falses etc.

accuracy = list()

for _ in range(10):
    
    #slumpar
    df = df.sample(frac = 1)

    find = 50

    test, train = data_separation(df, find)

    TP = 0
    FP = 0
    FN = 0
    TN = 0
    
    #Kör igenom testpunkter och räknar alla klassifikationer om det är en true-positve etc.(pikachu = positive, pichu = negative)
    for _, row in test.iterrows():
        index = edistance(row.values[0], row.values[1], train["width (cm)"], train["height (cm)"])

        if int(row.values[2]) == 1 and int(train["(0-pichu 1-pikachu)"].loc[index]) == 1:
            TP += 1
        elif int(row.values[2]) == 1 and int(train["(0-pichu 1-pikachu)"].loc[index]) == 0:
            FP += 1
        elif int(row.values[2]) == 0 and int(train["(0-pichu 1-pikachu)"].loc[index]) == 1:
            FN += 1
        elif int(row.values[2]) == 0 and int(train["(0-pichu 1-pikachu)"].loc[index]) == 0:
            TN += 1
        else:
            print("Value Error?")
    accuracy.append(float((TP+TN)/(TP+TN+FP+FN)))

#utskrift av data
fig, axs = plt.subplots(2)
fig.suptitle('Accuracy on 10 iterations')
axs[0].bar([x for x in range(1, len(accuracy)+1)], accuracy)
axs[0].set_xlabel('N - Iterations') 
axs[0].set_ylabel('Accuracy') 
axs[0].yaxis.set_major_formatter(PercentFormatter(1))
axs[1].set_title("Average Accuracy")
axs[1].pie([np.average(accuracy), 1-np.average(accuracy)], autopct= "%1.1f%%",labels= ["True Prediction", "False Prediction"], colors= ["green", "red"])
plt.show()
