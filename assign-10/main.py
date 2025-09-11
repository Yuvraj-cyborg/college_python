import pandas as pd

s1 = pd.Series([2,4,6,8,10])
s2 = pd.Series([1,3,5,7,9])

s = s1 + s2
print(s)

s = s1 - s2
print(s)

movies = pd.read_csv('http://bit.ly/imdbratings')
print(movies.head())