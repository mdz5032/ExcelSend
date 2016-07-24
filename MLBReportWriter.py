import pandas as pd
import pandas_datareader.data as web
import numpy as np
import matplotlib
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


#Read in the first table from the website.
players = pd.read_html('http://www.usatoday.com/sports/mlb/salaries/2013/player/p/')


#Grab the DataFrame from a list of DataFrames and assign it a variable
df1 = pd.DataFrame(players[0])


#Get rid of the irrelevant columns and rename the ones that are kept
df1.drop(df1.columns[[0,3,4, 5, 6]], axis=1, inplace=True)
df1.columns = ['Player', 'Team', 'Avg_Annual']


#Cycle through the Avg_Annual column and get rid of the commas and the dollar signs.
#Then change it to an int type in order to perform calculations on it
df1['Avg_Annual'] = df1['Avg_Annual'].str.replace(',', '')
df1['Avg_Annual'] = df1['Avg_Annual'].str.replace('$', '')
df1['Avg_Annual'] = df1['Avg_Annual'].astype(int)



#Read in the second table
p2 = pd.read_html('http://www.sportingcharts.com/mlb/stats/pitching-pitch-count-leaders/2013/')

#Assign it to a variable
df2 = pd.DataFrame(p2[0])

#Drop irrelavnat columns
df2.drop(df2.columns[[0,2, 3]], axis=1, inplace=True)




#Set the indexes to make a merge point
df1.set_index ('Player')
df2.set_index('Player')



#Merge the two tables together on 'Players'
df3 = pd.merge(df1, df2, on='Player')

#Rename Columns for simplicity
df3.columns = ['Player', 'Team', 'Avg_Annual', 'Pitch_Count']


#Calculate Price Per Pitch that the players are throwing, then round the number
df3['Price_Per_Pitch'] = (df3.Avg_Annual) / (df3.Pitch_Count)
df3 = (np.round(df3, 2))



#Create Pivot table to put the players grouped with their teamates
p = df3.pivot_table(df3, index=['Team', 'Player'])

#Group the players by team to get wholisitc view
by_team = df3.groupby('Team')


#Load HTML template
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("myreport.html")

#Insert variables into template
template_vars = {"title" : "Price Per Pitch - By Team",
                #Add sums of the teams players
                 "pivot_table": by_team.sum().to_html(),
                #Get the most expensive players
                 "pivot_table2": df3.sort_values(by='Price_Per_Pitch', ascending=False).head().to_html(),
                #Get the cheapest
                 "pivot_table3": df3.sort_values(by='Price_Per_Pitch', ascending=False).tail().to_html(),
                 "pivot_table4": p.to_html()}

#Make it all into an HTML String
html_out = template.render(template_vars)

#Make that into a pdf file
HTML(string=html_out).write_pdf("report.pdf", stylesheets=["style.css"])



