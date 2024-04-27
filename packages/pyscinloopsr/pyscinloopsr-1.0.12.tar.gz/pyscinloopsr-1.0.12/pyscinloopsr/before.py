

import pandas as pd
import numpy as np
import seaborn as snsi
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
rcParams["figure.figsize"] = 15,6
plt.figure(figsize=(40, 20))

class view:

  def __init__(self, dfx):
    self.xdf = dfx



  def box(self, feature):
    self.xdf.boxplot(feature)
  def scatter(self, featureA, featureB):
    self.xdf.plot.scatter(x=featureA, y = featureB, color='r')
  def correlation(self):
    snsi.heatmap(self.xdf.corr().abs(),  annot=True, center=1,  fmt=".2f", cmap='Greens')



class regressors:

  def __init__(self):
    self.model = None
    self.prettytable = None

  @staticmethod
  def printTestNoSelf():
    print("\nBBBBBBBBBBBBBB\n")



  def haversine(self, lon1: float, lat1: float, lon2: float, lat2: float) -> float:
    """
    Calculate the great circle distance between two points on the 
    earth (specified in decimal degrees), returns the distance in
    kilometers.
    All arguments must be of equal length.
    :param lon1: longitude of first place
    :param lat1: latitude of first place
    :param lon2: longitude of second place
    :param lat2: latitude of second place
    :return: distance in kilometers between the two sets of coordinates
    """
    print("Hola2")
    from math import radians, cos, sin, asin, sqrt

    # Convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers
    return c * r


 


  def runBasicRegressors(self, dfxbr, dfybr, featuresDrop=None):

    if featuresDrop is not None:
      for i in featuresDrop:
        print("\ndropping: ", i)
        dfxbr = dfxbr.drop(i, axis=1)
    print("\n")

    from sklearn.ensemble import RandomForestRegressor, BaggingRegressor
    from sklearn.ensemble import AdaBoostRegressor
    from sklearn.ensemble import GradientBoostingRegressor
    from sklearn.tree import DecisionTreeRegressor
    from sklearn.neighbors import KNeighborsRegressor
    from sklearn.linear_model import LogisticRegression
    from sklearn.linear_model import LinearRegression
    from sklearn.linear_model import Lasso, ElasticNet, Ridge, SGDRegressor
    from sklearn.svm import SVR, NuSVR
    from sklearn.neural_network import MLPRegressor
    from datetime import datetime

    from sklearn import metrics
    from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error




    rfr = RandomForestRegressor()
    gbr = GradientBoostingRegressor()
    abr = AdaBoostRegressor()

    #!pip install torch
    #import torch


    import numpy as np
    #np.random.seed(42)


    models = [


        SVR(gamma='auto', kernel='linear', C=1e-1),
        SVR(gamma=1e-1, kernel='linear', C=1e-1),
        SVR(gamma=1, kernel='linear', C=1e-1),
        SVR(gamma=10, kernel='linear', C=1e-1),

        SVR(gamma='auto', kernel='linear', C=1),
        SVR(gamma=1e-1, kernel='linear', C=1),
        SVR(gamma=1, kernel='linear', C=1),
        SVR(gamma=10, kernel='linear', C=1),

        SVR(gamma='auto', kernel='linear', C=10),
        SVR(gamma=1e-1, kernel='linear', C=10),
        SVR(gamma=1, kernel='linear', C=10),
        SVR(gamma=10, kernel='linear', C=10),

        SVR(gamma='auto', kernel='rbf', C=1e-1),
        SVR(gamma=1e-1, kernel='rbf', C=1e-1),
        SVR(gamma=1, kernel='rbf', C=1e-1),
        SVR(gamma=10, kernel='rbf', C=1e-1),

        SVR(gamma='auto', kernel='rbf', C=1),
        SVR(gamma=1e-1, kernel='rbf', C=1),
        SVR(gamma=1, kernel='rbf', C=1),
        SVR(gamma=10, kernel='rbf', C=1),

        SVR(gamma='auto', kernel='rbf', C=10),
        SVR(gamma=1e-1, kernel='rbf', C=10),
        SVR(gamma=1, kernel='rbf', C=10),
        SVR(gamma=10, kernel='rbf', C=10),

        MLPRegressor(random_state=None, max_iter=100, activation='relu', learning_rate_init=0.001),
        MLPRegressor(random_state=None, max_iter=200, activation='relu', learning_rate_init=0.01),
        MLPRegressor(random_state=None, max_iter=800, activation='relu', learning_rate_init=0.1),

        MLPRegressor(random_state=None, max_iter=50, activation='tanh', learning_rate_init=0.001),
        MLPRegressor(random_state=None, max_iter=100, activation='tanh', learning_rate_init=0.001),
        MLPRegressor(random_state=None, max_iter=150, activation='tanh', learning_rate_init=0.001),

        MLPRegressor(random_state=None, max_iter=200, activation='tanh', learning_rate_init=0.01),
        MLPRegressor(random_state=None, max_iter=800, activation='tanh', learning_rate_init=0.1),

        MLPRegressor(random_state=None, max_iter=100, activation='logistic', learning_rate_init=0.001),

        MLPRegressor(random_state=None, max_iter=50, activation='logistic', learning_rate_init=0.01),
        MLPRegressor(random_state=None, max_iter=100, activation='logistic', learning_rate_init=0.01),
        MLPRegressor(random_state=None, max_iter=150, activation='logistic', learning_rate_init=0.01),

        MLPRegressor(random_state=None, max_iter=800, activation='logistic', learning_rate_init=0.1),


        # very sensitive to scaling:  use StandardScaler
        SGDRegressor(max_iter=300, tol=1e-3, eta0=0.01),
        SGDRegressor(max_iter=300, tol=1e-3, eta0=0.0001),
        SGDRegressor(max_iter=300, tol=1e-3, eta0=0.000001),



        RandomForestRegressor( random_state=None, n_estimators=10),
        RandomForestRegressor( random_state=None, n_estimators=40),
        RandomForestRegressor( random_state=None, n_estimators=60),
        RandomForestRegressor( random_state=None, n_estimators=80),
        RandomForestRegressor( random_state=None, n_estimators=100),
        RandomForestRegressor( random_state=None, n_estimators=150),
        RandomForestRegressor( random_state=None, n_estimators=200),
        RandomForestRegressor( random_state=None, n_estimators=300),
        RandomForestRegressor( random_state=None, n_estimators=400),
        RandomForestRegressor( random_state=None, n_estimators=500),
        RandomForestRegressor( random_state=None, n_estimators=600),
        RandomForestRegressor( random_state=None, n_estimators=700),
        RandomForestRegressor( random_state=None, n_estimators=800),

        Lasso(alpha=0.05),
        Lasso(alpha=0.1),
        Lasso(alpha=0.15),
        Lasso(alpha=0.2),

        Ridge(alpha=.1),
        Ridge(alpha=.2),
        Ridge(alpha=.3),
        Ridge(alpha=.4),
        Ridge(alpha=.5),
        Ridge(alpha=.6),
        Ridge(alpha=.7),

        ElasticNet(),
        BaggingRegressor(),
        NuSVR(gamma='auto'),

        #param_grid_gbr = {"n_estimators":[72, 100, 128], "learning_rate":[0.1, 0.05, 0.2],"max_depth":[3,4,5]}
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.1, max_depth=3),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.1, max_depth=4),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.1, max_depth=5),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.05, max_depth=3),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.05, max_depth=4),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.05, max_depth=5),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.2, max_depth=3),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.2, max_depth=4),
        GradientBoostingRegressor(n_estimators=72, learning_rate=0.2, max_depth=5),

        GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=4),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=5),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.05, max_depth=3),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.05, max_depth=4),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.05, max_depth=5),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.2, max_depth=3),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.2, max_depth=4),
        GradientBoostingRegressor(n_estimators=100, learning_rate=0.2, max_depth=5),

        GradientBoostingRegressor(n_estimators=128, learning_rate=0.1, max_depth=3),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.1, max_depth=4),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.1, max_depth=5),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.05, max_depth=3),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.05, max_depth=4),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.05, max_depth=5),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.2, max_depth=3),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.2, max_depth=4),
        GradientBoostingRegressor(n_estimators=128, learning_rate=0.2, max_depth=5),


        #param_grid_abr = {"n_estimators":[5, 10, 15, 25, 40], "learning_rate":[0.1, 0.05, 0.2]}
        AdaBoostRegressor(n_estimators=5, learning_rate=0.1),
        AdaBoostRegressor(n_estimators=5, learning_rate=0.05),
        AdaBoostRegressor(n_estimators=15, learning_rate=0.1),
        AdaBoostRegressor(n_estimators=15, learning_rate=0.05),
        AdaBoostRegressor(n_estimators=40, learning_rate=0.1),
        AdaBoostRegressor(n_estimators=40, learning_rate=0.05),

        #linear_reg.fit(X_train_scaled, y_train)
        LinearRegression(),


        #knn = KNeighborsRegressor(n_neighbors=10)
        #knn.fit(X_train_scaled,y_train)
        KNeighborsRegressor(n_neighbors=5),
        KNeighborsRegressor(n_neighbors=10)

    ]




    from sklearn.model_selection import train_test_split

    # X and y already set

    # split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(dfxbr, dfybr, test_size=0.2, random_state=42)



    class ConsoleColor:
        # Color
        BLACK = '\033[90m'
        RED = '\033[91m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        BLUE = '\033[94m'
        PURPLE = '\033[95m'
        CYAN = '\033[96m'
        GRAY = '\033[97m'

        # Style
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

        # BackgroundColor
        BgBLACK = '\033[40m'
        BgRED = '\033[41m'
        BgGREEN = '\033[42m'
        BgORANGE = '\033[43m'
        BgBLUE = '\033[44m'
        BgPURPLE = '\033[45m'
        BgCYAN = '\033[46m'
        BgGRAY = '\033[47m'

        # End
        END = '\033[0m'






    from prettytable import PrettyTable
    table = PrettyTable()
    table.field_names = ["Model", "MSE", "SCORE", "R2", "TrainingTime"]



    j = 1
    for i in models:
        then = datetime.now()

        i.fit(X_train, y_train.values.ravel())
        y_res = i.predict(X_test)

        now = datetime.now()
        print ("Tempo de processamento do ",type(i).__name__,": ", now-then)
        mse = mean_squared_error(y_test, y_res)
        r2 = metrics.r2_score(y_test, y_res)
        score = i.score(X_test, y_test)

        newLine = [type(i).__name__, format(mse, ',.2f'), format(score, '.2f'), format(r2, '.2f'), now-then]

        if r2>0.9:
          newLine[3] = ConsoleColor.BLUE + newLine[3] + ConsoleColor.END
        elif r2>0.8:
          newLine[3] = ConsoleColor.GREEN + newLine[3] + ConsoleColor.END
        elif r2>0.6:
          newLine[3] = ConsoleColor.PURPLE + newLine[3] + ConsoleColor.END
        elif r2>0.4:
          newLine[3] = ConsoleColor.RED + newLine[3] + ConsoleColor.END





        table.add_row(newLine)


        #mytable = PrettyTable(['Name', 'Age', 'City', 'Sex', 'Marital', 'PhoneNo'])
        #for x in people:
        #lis = [x for x in people]
        #li = [y for x, y in people[x].items()]
        #li[1] = ConsoleColor.GREEN + li[1] + ConsoleColor.END
        #mytable.add_row(li)
        #table.add_row([type(i).__name__, format(mse, ',.2f'), format(score, '.2f'), format(r2, '.2f'), now-then])

        #model_save_name = type(model).__name__ + str(i) + "_exec1_semTratamentos.pt"
        #path = F"/content/drive/MyDrive/data/dissertacao/moniqueUfabc/V2/SAVED/cycle1/{model_save_name}"
        #raiz = "/content/drive/MyDrive/data/dissertacao/moniqueUfabc/V2"
        #cycle = "/cycle1"         # YOU HAVE TO ADJUST TO THE CURRENT CYCLE (NOT OVERWRITE) AND THEN UNCOMMENT
        #path = F""+(raiz+"/SAVED"+cycle+"/{model_save_name}")
        #torch.save(model, path)


        j = j + 1


    self.prettytable = table
    print(self.prettytable)

    return self.prettytable
