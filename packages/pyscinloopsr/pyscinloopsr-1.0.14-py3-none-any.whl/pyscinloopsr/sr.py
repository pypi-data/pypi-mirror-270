
from pysr import PySRRegressor
import joblib
from datetime import datetime

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
        print(self.model.score(dfxn, dfyn))