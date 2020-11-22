import pandas as p
import quandl as q
import numpy as n
from sklearn import *
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt
from matplotlib import style
import datetime
import pickle

style.use('ggplot')

df= q.get("WIKI/GOOGL")
df=df[['Adj. Open',  'Adj. High',  'Adj. Low',  'Adj. Close', 'Adj. Volume']]
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col='Adj. Close'
df.fillna(value=-99999, inplace=True)
forecast_out= int(math.ceil(0.01 * len(df)))
df['label']= df[forecast_col].shift(-forecast_out)

X = n.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
df.dropna(inplace=True)
y = n.array(df['label'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = LinearRegression(n_jobs=-1)
#clf=svm.SVR(kernel='linear')
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)
pickle_in = open('linearregression.pickle','rb')
clf = pickle.load(pickle_in)
#with open('linearregression.pickle','wb') as f:
#    pickle.dump(clf, f)

forecast_set = clf.predict(X_lately)
df['Forecast'] = n.nan

#print(confidence)
#print(forecast_set, confidence, forecast_out)

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [n.nan for _ in range(len(df.columns)-1)]+[i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
