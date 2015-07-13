# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 16:17:39 2015

@author: rafeltaye
"""

#read necessary datas and import useful libraries

import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic(u'matplotlib inline')
spray=pd.read_csv('spray.csv')
test=pd.read_csv('test.csv')
train=pd.read_csv('train.csv')
weather=pd.read_csv('weather.csv')

#EXPLORATORY DATA ANALYSIS
#train data 
train.head(5)
train.shape
train.Trap.value_counts()
train.Date.count
train.groupby(['Date','Trap','NumMosquitos']).head()
train.Species.value_counts()
train[train.Date =='2007-08-01'].head(5)
train['Species_num'] = train.Species.map({'CULEX PIPIENS/RESTUANS':0, 'CULEX RESTUANS':1, 'CULEX PIPIENS':2, 'CULEX TERRITANS':3, 'CULEX SALINARIUS':4, 'CULEX TARSALIS':5,'CULEX ERRATICUS':6})
train.corr()
sns.heatmap(train.corr())
train['Date'] = pd.to_datetime(train.Date)
train['Month'] = train.Date.dt.month #created new column with months

train.head()
from matplotlib.colors import ListedColormap
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF','#FFF00F','#00FFF0','#F00FFF'])
train.plot(kind='scatter', x='Longitude', y='Species_num',c='Species_num',colormap=cmap_bold) 

#weather data 
weather.head()
weather.shape
weather.corr()
sns.heatmap(weather.corr())

spray.head()
spray.shape

test.head(5) #(116293, 11)

test.shape
import numpy as np 
SumNumMosq=train.groupby(['Date','Address','Species','Trap','Latitude','Longitude'])[['NumMosquitos','WnvPresent']].agg([np.sum,np.max])
SumNumMosq.reset_index()
SumNumMosq['VirusSum']=SumNumMosq['WnvPresent']['sum']
SumNumMosq['VirusMax']=SumNumMosq['WnvPresent']['amax']
SumNumMosq['MosqSum']=SumNumMosq['NumMosquitos']['sum']

#only keep columns of interest
SumNumMosq = SumNumMosq[[ 'VirusSum','VirusMax','MosqSum']]
SumNumMosq.reset_index()
SumNumMosq.head(2)
train.columns
SumNumMosq.columns
Newtrain=pd.merge(train,SumNumMosq,on=['Date','Address','Species','Trap','Latitude','Longitude'],how='inner')