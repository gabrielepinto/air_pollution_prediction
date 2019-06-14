
import pandas as pd
import numpy as np
import os
from shapely.geometry import Point, Polygon
import geopandas as gpd

def get_pollution_dataset():
    # ciao grandi
    pollution_folder="D:\\smarcitiesdata\\DatiAirQuality\\MI_Air_Quality\\data"
    list_of_pollution_files=os.listdir(pollution_folder)
    ## onluy use the csv files
    list_of_pollution_files[0:37]

    ## the 36th file in the folder
    filepath_legend=pollution_folder+"\\"+list_of_pollution_files[36]
    legend_pollution_files=pd.read_csv(filepath_legend,sep=",",encoding='iso-8859-1',header=None)
    ## add names
    legend_pollution_files.rename(inplace=True,columns={0:'ID_sensor',1:'Address',2:'Pos_x',3:'Pos_y',4:'Sensor_type',5:'Unit_measurement',6:'Temporal_aggregation'})
    legend_pollution_files['ID_sensor'].astype(int,inplace=True)
    legend_pollution_files.dtypes
    df=pd.DataFrame()
    for pollution_name in range(0,36):
        filepath_pollution_files=pollution_folder+"\\"+list_of_pollution_files[pollution_name]
        df=df.append(pd.read_csv(filepath_pollution_files,header=None))

    df.rename(inplace=True,columns={0:'ID_sensor',1:'DateObs',2:'Pollution'})
    dataset=pd.merge(df,legend_pollution_files,on=['ID_sensor','ID_sensor'],how='left')
    geometry_polluted=[Point(yx) for yx in zip(dataset['Pos_y'],dataset['Pos_x'])]
    dataset=gpd.GeoDataFrame(dataset,crs={'init': 'epsg:4326'},geometry=geometry_polluted)
    dataset.drop('Temporal_aggregation',axis=1,inplace=True)
    return dataset
