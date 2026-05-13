import pandas as pd

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as ptl

data= pd.read_csv('vgsales.csv')
data.describe()
print(data.values)
