import pandas as pd
import matplotlib.pyplot as plt

class line:
    def __init__(self, k, m, path_to_data):
        self.k = k
        self.m = m
        self.df = self.get_labels(path_to_data)
        self.left = self.df[self.df["label"] == 0]
        self.right = self.df[self.df["label"] == 1]

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
    def save_dataframe(self, path):
        self.df.to_csv(path, index=False)
    def display(self, color):
        plt.scatter(self.left["x"],self.left["y"], color = "orange")
        plt.scatter(self.right["x"],self.right["y"], color = "blue")
        plt.plot([x for x in range(-5,6)], [self.k*x + self.m for x in range(-5,6)], color = color)
        plt.xlim(-5,5)
        plt.ylim(-5,5)
        plt.legend(["Left", "Right"])

if __name__ == '__main__':
    line1 = line(-1, 0, "Labs/Labb3/unlabelled_data.csv")
    line1.save_dataframe("labelled_data.csv")
    print(f"{len(line1.left)}/{len(line1.right)}")
    line1.display("green")
    plt.show()


