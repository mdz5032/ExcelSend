
from collections import Counter
import json
import matplotlib.pyplot as plt
import matplotlib


with open('dates.json', 'r') as f:
    dates = json.load(f)


c = Counter(dates)
print (c.most_common()[:10])

datesDict = dict(c)

dates = list(datesDict.keys())
bins = list(datesDict.values())

dateL = []

for date in dates:
    date = matplotlib.dates.datestr2num(date)
    dateL.append(date)

plt.plot_date(dateL,bins)
plt.grid(True)

fig = plt.figure(1)
fig.autofmt_xdate()

plt.show()
