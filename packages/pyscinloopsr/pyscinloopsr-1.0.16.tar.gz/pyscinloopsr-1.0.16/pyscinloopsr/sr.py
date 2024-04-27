
from pysr import PySRRegressor
import joblib
from datetime import datetime
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as snsi
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams["figure.figsize"] = 15,6
plt.figure(figsize=(40, 20))


class pysr:

    def __init__(self, modelObjtRef):
        self.model = modelObjtRef
        self.dfxn = None
        self.dfyn = None


    def runPySR(self, dfx, dfy, featuresDrop=None):
        self.dfxn = dfx.copy()
        self.dfyn = dfy.copy()
        if featuresDrop is not None:
            for i in featuresDrop:
                print("\ndropping: ", i)
                self.dfxn = self.dfxn.drop(i, axis=1)

        #self.model = modelObjt
        self.model.fit(self.dfxn, self.dfyn.values.ravel())
    

    def exportModel(self, directory):
        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")
        joblib.dump(self.model, directory + time + ".joblib")
 
    def importModel(self, fullPath):
        self.model = joblib.load(fullPath)

    def setModelToAccuracy(self):
        self.model.model_selection = "accuracy"

    def setModelToBest(self):
        self.model.model_selection = "best"

    def printEquationFormats(self):
        print("equation:\n", self.model.get_best().equation, "\n")
        print("latex:\n", self.model.latex(), "\n") 
        print("sympy:\n", self.model.sympy(), "\n")   

    def score(self):
        print(self.model.score(self.dfxn, self.dfyn))

    def compare(self):
        plt.scatter(self.dfyn, self.model.predict(self.dfxn))
        plt.xlabel('Truth')
        plt.ylabel('Prediction')
        plt.show()

    def compareKde(self):
        realXpredicted = self.dfyn.copy()
        realXpredicted.columns = ["target"]
        realXpredicted["predicted"] = self.model.predict(self.dfxn)
        minAux = realXpredicted.target.min()
        min = minAux
        minAux = realXpredicted.predicted.min()
        if minAux<min:
            min=minAux
        maxAux = realXpredicted.target.max()
        max = maxAux
        maxAux = realXpredicted.predicted.max()
        if maxAux>max:
            max=maxAux
        xAxis = np.linspace(min, max, num=200)
        ax = realXpredicted.plot.kde(ind=xAxis)
        plt.xlabel("Values")
        plt.ylabel("Density")
        plt.grid(False)
        plt.show()


    def predictCase(self, example):
        print(self.model.predict(np.array(example).reshape(1, -1)))     