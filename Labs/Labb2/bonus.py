import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
trues = list()
falses = list()


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
    trues.append(TP+TN)
    falses.append(FP+FN)

#medelvärdet av alla 10 iterationer
trueoutput = sum(trues)/len(trues)
falseoutput = sum(falses)/len(falses)

plt.pie([trueoutput, falseoutput], autopct= "%1.1f%%",labels= ["True Prediction", "False Prediction"], colors= ["green", "red"])
plt.show()
