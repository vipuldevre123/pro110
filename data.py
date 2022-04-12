import plotly.figure_factory as ff
import statistics
import random
import pandas as pd

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].to_list()

#fig=ff.create_distplot([data],["reading_time"],show_hist=False)
#fig.show()

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data))
        value=data[randomindex]
        dataset.append(value)
    mean=statistics.mean(dataset)    
    return(mean)

def showfigure(meanlist):
    df=meanlist
    fig=ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.show()

meanlist=[]
for i in range(0,1000):
    s=randomsetofmean(100)
    meanlist.append(s)

showfigure(meanlist)
 