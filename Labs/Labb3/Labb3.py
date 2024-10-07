import pandas as pd
import matplotlib.pyplot as plt

class line:
    def __init__(self, k, m, path_to_data):
        self.k = k
        self.m = m
        self.df = self.get_labels(path_to_data)

    def classify(self, k, m, x, y):
        if k*x + m >= y:
            return 0
        else:
            return 1
    
    def get_labels(self, path_to_data):
        unlabelled = pd.read_csv(path_to_data)
        if len(unlabelled["x"].values) == len(unlabelled["y"].values):
            labels = list()
            for index in range(len(unlabelled["x"].values)):
                labels.append(self.classify(self.k, self.m, unlabelled["x"].values[index], unlabelled["y"].values[index]))

            labelled = unlabelled
            labelled["label"] = labels
            return labelled
        else:
            raise ValueError("first and second argument must have same length")
    def display(self):
        left = self.df[self.df["label"] == 0]
        right = self.df[self.df["label"] == 1]
        plt.scatter(left["x"],left["y"], color = "orange")
        plt.scatter(right["x"],right["y"], color = "blue")
        plt.plot([x for x in range(-5,6)], [self.k*x + self.m for x in range(-5,6)])
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.legend(["Beneath Line", "Above Line"])
        plt.show()

# def y_func(k, x, m):
#     return k*x + m

# def classify(k, m, x, y):
#     if y_func(k, x, m) >= y:
#         return 0
#     else:
#         return 1
    
# def get_labels(k, m, xlist, ylist):
#     if len(xlist) == len(ylist):
#         labels = list()
#         for index in range(len(xlist)):
#             labels.append(classify(k, m, xlist[index], ylist[index]))
#         return labels
#     else:
#         raise ValueError("first and second argument must have same length")

# def run(k, m):
#     unlabelled = pd.read_csv("unlabelled_data.csv")
#     xline = [x for x in range(-5,6)]
#     yline = [y_func(k, x, m) for x in xline]
    
#     labels = get_labels(k, m, unlabelled["x"].values, unlabelled["y"].values)

#     labelled = unlabelled
#     labelled["label"] = labels
#     left = labelled[labelled["label"] == 0]
#     right = labelled[labelled["label"] == 1]
#     labelled.to_csv("labelled_data.csv", index=False)

#     plt.scatter(left["x"],left["y"], color = "orange")
#     plt.scatter(right["x"],right["y"], color = "blue")
#     plt.plot(xline, yline)
#     plt.xlim(-5,5)
#     plt.ylim(-5,5)
#     plt.legend(["Beneath Line", "Above Line"])
#     plt.show()

line1 = line(-1, 0, "Labs/Labb3/unlabelled_data.csv")
line1.display()
    #kapslat in koden i funktioner för att användas i jupyter notebooks
    #run(-1, 0)

