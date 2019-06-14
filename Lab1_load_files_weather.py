import pandas as pd
import numpy as np
import os
from shapely.geometry import Point, Polygon
import geopandas as gpd





def get_weather_data():

    weather_folder="D:\\smarcitiesdata\\DatiAirQuality\\MI_Weather_Station_Data\\data"
    list_of_weather_files=os.listdir(weather_folder)
    filepath_legend=weather_folder+"\\"+list_of_weather_files[34]
    # only use csv files
    list_of_weather_files=list_of_weather_files[1:34]
    legend_weather_files=pd.read_csv(filepath_legend,sep=",",encoding='iso-8859-1',header=None)
    ## add names
    legend_weather_files.rename(inplace=True,columns={0:'ID_sensor',1:'Address',2:'Pos_x',3:'Pos_y',4:'Sensor_type',5:'Unit_measurement'})
    legend_weather_files['ID_sensor'].astype(int,inplace=True)
    legend_weather_files.dtypes


    df=pd.DataFrame()
    for weather_name in range(0,len(list_of_weather_files)):
        filepath_weather_files=weather_folder+"\\"+list_of_weather_files[weather_name]
        df=df.append(pd.read_csv(filepath_weather_files,header=None))
    df.rename(inplace=True,columns={0:'ID_sensor',1:'DateObs',2:'Weather_Indicator'})
    dataset=pd.merge(df,legend_weather_files,on=['ID_sensor','ID_sensor'],how='left')
    geometry_weather=[Point(yx) for yx in zip(dataset['Pos_y'],dataset['Pos_x'])]
    dataset=gpd.GeoDataFrame(dataset,crs={'init': 'epsg:4326'},geometry=geometry_weather)
    return dataset
