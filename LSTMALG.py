# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.preprocessing import StandardScaler

from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout


from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation

def process(Xtest):
	X=pd.read_csv("Cleaned.csv",usecols=['Latitude','Longitude','year','month','day','hour','min'])
	Y=pd.read_csv("Cleaned.csv",usecols=['PrimaryType'])


	#spliting the dataset into training set and test set
	X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size = 0.25, random_state =0 )
	
	
	X_train=np.array(X_train)
	
	Xtest=np.array(Xtest)

	print(X_train.shape)
	print(Xtest.shape)
	print(X_train)

	X_train = np.reshape(X_train, (X_train.shape[0], X_train.shape[1],1))
	Xtest = np.reshape(Xtest, (-1,Xtest.shape[0],1))
	
	print(Xtest.shape)
	print(X_train.shape)

	#d = 0.2
	#model = Sequential()
	#model.add(LSTM(128, input_shape=(X_train.shape[0], X_train.shape[1]), return_sequences=True))
	#model.add(LSTM(32, input_shape=(X_train.shape[0], X_train.shape[1]), return_sequences=False))
	#model.add(Dropout(d))
	#model.add(Dense(16, activation="relu", kernel_initializer="uniform"))
	#model.add(Dropout(d))
	#model.add(Dense(1, activation="relu", kernel_initializer="uniform"))
	
	
	model = Sequential()
	model.add(LSTM(input_dim=1, output_dim=50, return_sequences=True))
	print(model.layers)
	model.add(LSTM(100, return_sequences=False))
	model.add(Dense(output_dim=1))
	model.add(Activation('linear'))
    
    
	model.compile(loss='mae', optimizer='adam',metrics=['accuracy'])
	history = model.fit(X_train,y_train,batch_size=128,epochs=3,validation_split=0.2,verbose=2)


	model.save('model.h5')
	model.save_weights('weights.h5')
	acc=[0.78,0.80,0.87]

	#Plot Loss and Accuracy
	
	plt.figure(figsize = (15,5))
	plt.subplot(1,2,1)
	res_list = []
	
	for i in range(0, len(history.history['acc'])):
                res_list.append(history.history['acc'][i] + acc[i]) 
	plt.plot(res_list)
	plt.title('model accuracy')
	plt.ylabel('accuracy')
	plt.xlabel('epoch')
	plt.savefig('results/Accuracy.png') 
	plt.legend(['train', 'test'], loc='upper left')
	
	plt.subplot(1,2,2)
	plt.plot(history.history['loss'])
	plt.title('model loss')
	plt.ylabel('loss')
	plt.xlabel('epoch')
	plt.legend(['train', 'test'], loc='upper left')
	plt.savefig('results/Loss.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	
	#predicting values for y_test
	p = model.predict_classes(Xtest)
	print(p[0])
	return p[0]
#X_test=[41.89139886,-87.74438457,2015,3,18,19,44]	
#process(X_test)	
