from Sensor_Node import dhtTopics
from Data_Schema_Node import Schema_Topics
from Prediction_Node import Prediction_Topics


def save_current_hundred_Readings():
    location='Data_Schema_Node/SensorData.csv'
    ACK=Schema_Topics.recordDATA(location)
    if(ACK==True):
        print('[DATA SAVED]')

def get_Predition():
        Prediction_Topics.Prediction()

def fetchTemp_Humid():
        dataFetched=dhtTopics.dhtMessages()
        print("TEMPERATURE:"+str(dataFetched[0]))
        print("HUMIDITY:"+str(dataFetched[1]))

print('[ CYBER PHYSICAL SYSTEM FOR ENVIRONMENTAL MONITORING ]')
while(True):
    MENU=input('Choose from the following menu:\n1.GET CURRENT READINGS\n2.SAVE CURRENT 100 READINGS\n3.GET PREDICTION\n')
    if(MENU=='1'):
        fetchTemp_Humid()
    elif(MENU=='2'):
        save_current_hundred_Readings()
    elif (MENU=='3'):
        get_Predition()
    else:
        print('[ ALERT:CHOOSE THE RIGHT MENU ]')