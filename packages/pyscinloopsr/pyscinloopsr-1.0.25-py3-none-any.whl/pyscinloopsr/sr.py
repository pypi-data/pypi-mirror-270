"""
Module to fit PySR and perform analysis on the results
"""

from pysr import PySRRegressor
import joblib
from datetime import datetime
import pandas as pd
import numpy as np
from scipy import stats
import seaborn as snsi
import matplotlib.pyplot as plt
from sklearn.inspection import PartialDependenceDisplay
from matplotlib.pylab import rcParams
rcParams["figure.figsize"] = 15,6
plt.figure(figsize=(15, 10))


class pysr:
    """Class for handling PySR interactions"""

    def __init__(self, modelObjtRef):
        """
        Initiate the object with your PySRRegressor defined object\n
        Example:\n
            from pyscinloopsr import sr\n
            pysrHandlerObject = sr.pysr(PySRRegressorObject)
        """
        self.model = modelObjtRef
        """Internal model reference"""
        self.dfxn = None
        """Internal predictors Dataframe name"""
        self.dfyn = None
        """Internal target Dataframe name"""


    def runPySR(self, dfx, dfy, featuresDrop=None):
        """
        Method to fit the PySR model\n
        Args: predictors DataFrame, target DataFrame, optional list of features names to drop\n
        Example:\n
            pysrHandlerObject.runPySR(X, y)\n
        Example:\n
            pysrHandlerObject.runPySR(X, y, ["featureNameOne", "featureNameTwo"])    
        """       
        self.dfxn = dfx.copy()
        self.dfyn = dfy.copy()
        if featuresDrop is not None:
            for i in featuresDrop:
                print("\ndropping: ", i)
                self.dfxn = self.dfxn.drop(i, axis=1)


        self.model.fit(self.dfxn, self.dfyn.values.ravel())
    

    def exportModel(self, directory):
        """
        Method to export the fitted PySR model\n
        Args: directory to place the file\n
        File name is set automatically as YYYYMMDDHHMISS.joblib (e.g. 20240427124411.joblib)\n
        Example:\n
            pysrHandlerObject.exportModel("/content/")
        """        
        now = datetime.now()
        time = now.strftime("%Y%m%d%H%M%S")
        joblib.dump(self.model, directory + time + ".joblib")
 
    def importModel(self, fullPath):
        """
        Method to import a PySR model previously exported\n
        Args: full directory with file name to recover the file\n
        File name is set automatically as YYYYMMDDHHMISS.joblib (e.g. 20240427124411.joblib)\n
        Example:\n
            pysrHandlerObject.importModel("/content/20240427124411.joblib")
        """           
        self.model = joblib.load(fullPath)

    def setModelToAccuracy(self):
        """
        Method to change PySR mode to accuracy\n
        Example:\n
            pysrHandlerObject.setModelToBest()
        """
        self.model.model_selection = "accuracy"

    def setModelToBest(self):
        """
        Method to change PySR mode to best\n
        Example:\n
            pysrHandlerObject.setModelToBest()
        """        
        self.model.model_selection = "best"

    def printEquationFormats(self):
        """
        Method to print the generated equation in three formats (equation, latex, sympy)\n
        Example:\n
            pysrHandlerObject.printEquationFormats()
        """          
        print("equation:\n", self.model.get_best().equation, "\n")
        print("latex:\n", self.model.latex(), "\n") 
        print("sympy:\n", self.model.sympy(), "\n")   

    def score(self):
        """
        Method to print the model score\n
        Example:\n
            pysrHandlerObject.score()
        """            
        print(self.model.score(self.dfxn, self.dfyn))

    def compare(self):
        """
        Method to scatterplot the True target value against model Prediction\n
        Example:\n
            pysrHandlerObject.compare()
        """           
        plt.figure(figsize=(5, 5))
        plt.scatter(self.dfyn, self.model.predict(self.dfxn))
        plt.xlabel('Truth')
        plt.ylabel('Prediction')
        plt.show()

    def compareKde(self):
        """
        Method to plot KDE of True target value against model Prediction\n
        Example:\n
            pysrHandlerObject.compareKde()
        """         
        rcParams["figure.figsize"] = 8,8
        plt.figure(figsize=(8, 8))
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
        """
        Method to predict an instance with user defined values for probing the mode\n
        Example:\n
            pysrHandlerObject.predictCase([1.67, 0.9, -0.77, -1.7, -0.6, 0.03, 1.04, -0.91,	1.42, -0.91])
        """          
        print(self.model.predict(np.array(example).reshape(1, -1)))     


    def pdp(self, featureList=None):
        """
        Method to print PDP\n
        Args: Optional list of features names to plot\n
        Example (all features):\n
            pysrHandlerObject.pdp()\n
        Example (specified features):\n
            pysrHandlerObject.pdp(["featureNameOne", "featureNameTwo", "featureNameThree"])    
        """       
        if featureList is None:
            allFeatures = list(range(self.dfxn.shape[1]))
        else:
            allFeatures = featureList
        fig, ax = plt.subplots(figsize=(10, 20))
        ax.set_title("Partial Dependence Plots")
        PartialDependenceDisplay.from_estimator(
            estimator=self.model,
            X=self.dfxn,
            features=(allFeatures),
            random_state=42,
            ax=ax
        )
        plt.show()         