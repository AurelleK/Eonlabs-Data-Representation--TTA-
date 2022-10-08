#Data Representation Take-home Tech Assessment (TTA)
# by Aurelle TCHAGNA KOUANOU (tkaurelle@gmail.com)
from datetime import datetime
import numpy as np
import pandas as pd
import plotly.express as px

def data():
    hourly=pd.read_csv("hourly_data.csv")
    weekly=pd.read_csv("weekly_data.csv")
    monthly=pd.read_csv("monthly_data.csv")   
    hourly['value_week']=np.nan     
    hourly['value_month']=np.nan    
    hourly['value_unormalized']=np.nan    
    hourly['value_normalized']=np.nan 
    j=0
    k=0
    for i in range(0, len(weekly)-1):        
        while hourly.loc[j,'time_hour']<weekly.loc[i+1,'time_week'] :
            if(k<len(monthly)-1 and weekly.loc[i,'time_week']<monthly.loc[k+1,'time_month']):
                hourly.loc[j,'value_month']=monthly.loc[k,'value_month']
            if(k<len(monthly)-1 and hourly.loc[j,'time_hour']==monthly.loc[k+1,'time_month']):
                hourly.loc[j,'value_month']=monthly.loc[k+1,'value_month']
                k+=1                
            hourly.loc[j,'value_week']=weekly.loc[i,'value_week']
            hourly.loc[j,'value_unormalized']=hourly.loc[j,'value_week']*hourly.loc[j,'value_month']*hourly.loc[j,'value_hour']
            j+=1     
    max=hourly["value_unormalized"].max()
    for i in range(0,len(hourly)):
        hourly.loc[i,'value_normalized']=hourly.loc[i,"value_unormalized"]*100/max                     
    hourly.to_csv('hourly.csv',index=False)
    
def read():    
    hourly=pd.read_csv("hourly.csv")   
    fig = px.line(x=hourly["date"], y=hourly["value_normalized"], title="Trends") #Curve when representing scaled normalized trends
    fig2 = px.line(x=hourly["date"], y=hourly["value_hour"], title="Trends Hour") #Curve when representing only trends per hour
    print(fig)
    fig.show()
    fig2.show()
    
data()   #to generate the Trends hourly.csv
read() #to read and plot