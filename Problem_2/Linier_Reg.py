import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")
from sklearn import linear_model
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn import preprocessing
from sklearn.metrics import r2_score
import statistics



def StackGraph(X_mean):
	summ = []
	ind = 0
	x = ['stack graph']
	plt.bar(x, reg_model.intercept_, color='r')
	for ind in range(0,len(X_mean)):
	  summ.append(coef[ind]*X_mean[ind])
	op = 0
	for i in summ:
	  op = op+i
	new = []
	for i in summ:
	  new.append((i/op)*(y_p-reg_model.intercept_))
	summ = new
	sum = reg_model.intercept_

	for cnt in range(0,len(summ)):
	  plt.bar(x,summ[cnt] , bottom=sum)
	  sum = sum+summ[cnt]
	plt.show()




def Reg():
	X_train,X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 100)
	#Did scaling to normalize it between 0 to 1
	min_max_scaler = preprocessing.MinMaxScaler()
	X_train = min_max_scaler.fit_transform(X_train)
	X_test = min_max_scaler.transform(X_test)

	reg_model = linear_model.LinearRegression()
	reg_model = LinearRegression().fit(X_train, y_train)
	return reg_model
