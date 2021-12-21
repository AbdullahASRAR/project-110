import pandas as pd
import random
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()
def random_state_of_mean(counter):
    dataSet=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataSet.append(value)
    mean=statistics.mean(dataSet)
    return mean
def show_fig(mean_list):
    df=mean_list
    mean= statistics.mean(df)
    fig = ff.create_distplot([df],["reading_time"],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1.5],mode="lines",name="MEAN"))
    fig.show()
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means=random_state_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    std_deviation = statistics.stdev(mean_list) 
    print("Standard deviation of sampling distribution:- ", std_deviation)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )
setup()  
population_mean=statistics.mean(data)
population_stdev=statistics.stdev(data)
print("population mean:- ", population_mean)
print("population standerd diviation:- ", population_stdev)
