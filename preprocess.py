import csv
import numpy as np
import pandas as pd
from pandas import read_csv
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="whitegrid")

def process(path):

	print("preprocess")
	
	df_main = pd.read_csv(path)
	names=list(df_main.columns)

	correlations = df_main.corr()
	# plot correlation matrix
	fig = plt.figure()
##	fig.canvas.set_window_title('Correlation Matrix')
##	ax = fig.add_subplot(111)
##	cax = ax.matshow(correlations, vmin=-1, vmax=1)
##	fig.colorbar(cax)
##	ticks = np.arange(0,9,1)
##	ax.set_xticks(ticks)
##	ax.set_yticks(ticks)
##	ax.set_xticklabels(names)
##	ax.set_yticklabels(names)
##	fig.savefig('results/Correlation Matrix.png')
	    
	#plt.pause(5)
	#plt.show(block=False)
	#plt.close() 
	crimes = read_csv(path, index_col='Date')
	s = crimes[['PrimaryType']]
	crimes.index = pd.to_datetime(crimes.index)
	crime_count = pd.DataFrame(s.groupby('PrimaryType').size().sort_values(ascending=False).rename('counts').reset_index())
	
	# Initialize the matplotlib figure
	f, ax = plt.subplots(figsize=(16, 15))
	
	
	# Plot the total crashes
	sns.set_color_codes("pastel")
	sns.barplot(x="counts", y="PrimaryType", data=crime_count.iloc[:10, :],label="Total", color="b")
	
	
	ax.legend(ncol=2, loc="lower right", frameon=True)
	ax.set(ylabel="Type",xlabel="Crimes")
	sns.despine(left=True, bottom=True)
	plt.savefig('results/Top10Crimes.png')
	
	# Add a legend and informative axis label
	plt.pause(5)
	plt.show(block=False)
	plt.close() 
	
	crimes_2015 = crimes.loc['2015']
	
	## Yearly crimes
	arrest_yearly = crimes[crimes['Arrest'] == True]['Arrest']
	
	plt.subplot()
	# Monthly arrest
	arrest_yearly.resample('M').sum().plot()
	plt.title('Monthly arrests')
	plt.savefig('results/Monthly arrests.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close() 
	# Weekly arrest
	arrest_yearly.resample('W').sum().plot()
	plt.title('Weekly arrests')
	plt.savefig('results/Weekly arrests.png')
	
	plt.pause(5)
	plt.show(block=False)
	plt.close() 
	# daily arrest
	arrest_yearly.resample('D').sum().plot()
	plt.title('Daily arrests')
	plt.savefig('results/Daily arrests.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close() 
	
	domestic_yearly = crimes[crimes['Domestic'] == True]['Domestic']
	
	plt.subplot()
	# Monthly domestic violence
	domestic_yearly.resample('M').sum().plot()
	plt.title('Monthly domestic violence')
	plt.savefig('results/Monthly domestic violence.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	# Weekly domestic violence
	domestic_yearly.resample('W').sum().plot()
	plt.title('Weekly domestic violence')
	plt.savefig('results/Weekly domestic violence.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()	# daily domestic violence
	domestic_yearly.resample('D').sum().plot()
	plt.title('Daily domestic violence')
	plt.savefig('results/Daily domestic violence.png')
	plt.pause(5)
	plt.show(block=False)
	plt.close()
	
	
	data = pd.read_csv(path,usecols=['Date', 'PrimaryType','Latitude','Longitude']) 
	# Preview the first 5 lines of the loaded data 
	data.dropna(inplace=True)
	print(data)
	
	print(data.head())
	print(data.PrimaryType.unique())

	data[["PrimaryType"]] = data[["PrimaryType"]].replace(['BATTERY','OTHER OFFENSE','ROBBERY','NARCOTICS','CRIMINAL DAMAGE','WEAPONS VIOLATION','THEFT','BURGLARY','MOTOR VEHICLE THEFT','PUBLIC PEACE VIOLATION','ASSAULT','CRIMINAL TRESPASS','CRIM SEXUAL ASSAULT','INTERFERENCE WITH PUBLIC OFFICER','ARSON','DECEPTIVE PRACTICE','LIQUOR LAW VIOLATION','KIDNAPPING','SEX OFFENSE','OFFENSE INVOLVING CHILDREN','PROSTITUTION','GAMBLING','INTIMIDATION','STALKING','OBSCENITY','PUBLIC INDECENCY','HUMAN TRAFFICKING','CONCEALED CARRY LICENSE VIOLATION','OTHER NARCOTIC VIOLATION','HOMICIDE','NON-CRIMINAL'], [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
	print(data.PrimaryType.unique())
	print(data)

	data['year'] = pd.DatetimeIndex(data['Date']).year
	data['month'] = pd.DatetimeIndex(data['Date']).month
	data['day'] = pd.DatetimeIndex(data['Date']).day
	data['hour'] = pd.DatetimeIndex(data['Date']).hour
	data['min'] = pd.DatetimeIndex(data['Date']).minute
	print(data)
	data.to_csv("cleaned.csv")
