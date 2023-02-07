import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt 

def Prediction():
    data=pd.read_csv('Cybernetics_Rpi\Data_Schema_Node\SensorData.csv')
    X=data[["TEMP","HUMIDITY"]]

    K=2
    Centroids=(X.sample(n=K))

    diff = 1
    j=0

    while(diff!=0):
        XD=X
        i=1
        for index1,row_c in Centroids.iterrows():
            ED=[]
            for index2,row_d in XD.iterrows():
                d1=(row_c["TEMP"]-row_d["TEMP"])**2
                d2=(row_c["HUMIDITY"]-row_d["HUMIDITY"])**2
                d=np.sqrt(d1+d2)
                ED.append(d)
            X[i]=ED
            i=i+1

        C=[]
        for index,row in X.iterrows():
            min_dist=row[1]
            pos=1
            for i in range(K):
                if row[i+1] < min_dist:
                    min_dist = row[i+1]
                    pos=i+1
            C.append(pos)
        X["Cluster"]=C
        Centroids_new = X.groupby(["Cluster"]).mean()[["HUMIDITY","TEMP"]]
        if j == 0:
            diff=1
            j=j+1
        else:
            diff = (Centroids_new['HUMIDITY'] - Centroids['HUMIDITY']).sum() + (Centroids_new['TEMP'] - Centroids['TEMP']).sum()
            print(diff.sum())
        Centroids = X.groupby(["Cluster"]).mean()[["HUMIDITY","TEMP"]]


    color=['blue','green','cyan','yellow']
    for k in range(K):
        data=X[X["Cluster"]==k+1]
        plt.scatter(data["TEMP"],data["HUMIDITY"],c=color[k])
    plt.scatter(Centroids["TEMP"],Centroids["HUMIDITY"],c='red')
    plt.title("CROP PREDICTION SYSTEM")
    plt.xlabel('Temperature in Celcius')
    plt.ylabel('Humidity')  
    plt.grid(True)
    print('[BLUE:Crop1,GREEN:Crop2]')
    plt.show()

