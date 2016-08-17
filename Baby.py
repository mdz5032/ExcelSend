import sqlite3
import pandas as pd
from pandas.io import sql
import matplotlib.pyplot as plt

sqlite_file = '/home/mdz5032/Downloads/database.sqlite'

#Connect to the SQL database
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#Query the data that we want
query = "SELECT Name, Count, Year, Gender FROM NationalNames WHERE Gender = 'M' AND Year>1965"

#Get that data
df = sql.read_sql(query, con=conn)


#df.set_index('Year', inplace=True)


MVPs = pd.read_html('http://www.topendsports.com/events/super-bowl/mvp-winners-list.htm')
df_MVPs = pd.DataFrame(MVPs[0])

df_MVPs.drop(df_MVPs.columns[[0,3]], axis=1, inplace=True)
df_MVPs.columns = ['Year', 'Player']

df_MVPs.drop(df_MVPs.head(1).index, inplace=True)

df_MVPs['Year'] = df_MVPs['Year'].str[-4:]

df_MVPs['Player'] = df_MVPs['Player'].str.split(' ').str.get(0)


#Calculate the percent change
df['pct_change'] = df.sort_values('Year').groupby('Name').Count.pct_change() * 100

df_ = pd.DataFrame()
df_ = df_.fillna(0) # with 0s rather than NaNs

for i in range (1,51):
    x = (df_MVPs['Player'][i])
    y = (df_MVPs['Year'][i])
    y = int(y)
    i=i+1

    dfn = df.loc[df['Name'] == x]

    dfn = (dfn.loc[dfn['Year'] == y])


    df_ = df_.append(dfn)


df_ = df_.sort_values('pct_change')
print (df_)



##df['Count'].plot(grid=True, color='red')
##plt.ylabel('Count')
##plt.show()
