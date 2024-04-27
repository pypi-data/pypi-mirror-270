
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
        self.dfxy = dfy.copy()
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
  