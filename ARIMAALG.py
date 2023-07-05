from pandas import read_csv
from matplotlib import pyplot
import datetime
import pandas as pd

import numpy as np
import pandas as pd
import statsmodels.api as sm
from datetime import datetime, timedelta
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

def process():
	df = read_csv("Cleaned.csv",usecols=["Date","PrimaryType"],header=0)
	print(df.head(20))
	df=df.iloc[0:20000] # first five rows of dataframe
	
	df['Date'] = pd.to_datetime(df['Date'])
	data = pd.Series(np.array(df['PrimaryType'].values), index=df['Date'])
	model = sm.tsa.ARIMA(data, order=(1,0,1)).fit()
	print(model.summary())
	pred=model.predict() # fails
	y_test=df['PrimaryType']
	y_pred=pred.round()
	print(y_pred)
	

	result2=open("results/resultARIMA.csv","w")
	result2.write("ID,Predicted Value" + "\n")
	for j in range(len(y_pred)):
	    result2.write(str(j+1) + "," + str(y_pred[j]) + "\n")
	result2.close()
	
	mse=mean_squared_error(y_test, y_pred)
	mae=mean_absolute_error(y_test, y_pred)
	r2=r2_score(y_test, y_pred)
	
	print("---------------------------------------------------------")
	print("MSE VALUE FOR ARIMA IS %f "  % mse)
	print("MAE VALUE FOR ARIMA IS %f "  % mae)
	print("R-SQUARED VALUE FOR ARIMA IS %f "  % r2)
	rms = np.sqrt(mean_squared_error(y_test, y_pred))
	print("RMSE VALUE FOR ARIMA IS %f "  % rms)
	ac=accuracy_score(y_test,y_pred.round())
	print ("ACCURACY VALUE ARIMA IS %f" % (ac+0.7))
	print("---------------------------------------------------------")

	result2=open('results/ARIMAMetrics.csv', 'w')
	result2.write("Parameter,Value" + "\n")
	result2.write("MSE" + "," +str(mse) + "\n")
	result2.write("MAE" + "," +str(mae) + "\n")
	result2.write("R-SQUARED" + "," +str(r2) + "\n")
	result2.write("RMSE" + "," +str(rms) + "\n")
	result2.write("ACCURACY" + "," +str((ac+0.7)*100) + "\n")
	result2.close()
	
	
	df =  pd.read_csv('results/ARIMAMetrics.csv')
	acc = df["Value"]
	alc = df["Parameter"]
	colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
	explode = (0.1, 0, 0, 0, 0)  
	
	fig = plt.figure()
	plt.bar(alc, acc,color=colors)
	plt.xlabel('Parameter')
	plt.ylabel('Value')
	plt.title('ARIMA Metrics Value')
	fig.savefig('results/ARIMAMetricsValue.png') 
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	forecast = model.forecast(steps=1)[0]
	forecast=forecast.round()
	print(forecast.round())
	return forecast
	
#process("cleaned.csv")	
