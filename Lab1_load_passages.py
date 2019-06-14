import pandas as pd
import numpy as np
import os
from shapely.geometry import Point, Polygon
import geopandas as gpd

def get_passages_data():
    passages_folder="D:\\smarcitiesdata\\DatiAirQuality\\MI_Area_C"
    list_of_passages_files=os.listdir(passages_folder)
    filepath_gate=passages_folder+"\\"+list_of_passages_files[2]
    ## the other files include the header
    legend_passages_files=pd.read_csv(filepath_gate,sep=",",encoding='iso-8859-1',header=None)
    ## add names
    legend_passages_files.rename(inplace=True,columns={0:'ID_sensor',1:'Address',2:'Sensor type',3:'Pos_x',4:'Pos_y'})
    legend_passages_files
    legend_passages_files['ID_sensor'].astype(int,inplace=True)
    ## load the transit file
    filepath_transit=passages_folder+"\\"+list_of_passages_files[4]
    transit_file=pd.read_csv(filepath_transit,sep=",",encoding='iso-8859-1')
    transit_file.rename(inplace=True,columns={transit_file.columns[0]:'Timestamp',transit_file.columns[1]:'Plate',transit_file.columns[2]:'ID_sensor'})
    ## merge the transit and legend file....
    dataset_transit_legend=pd.merge(transit_file,legend_passages_files,on=['ID_sensor','ID_sensor'],how='left')

    filepath_vehicles_information=passages_folder+"\\"+list_of_passages_files[5]
    vechicles_file=pd.read_csv(filepath_vehicles_information,sep=",",encoding='iso-8859-1')

    ## same length...so we can merge without worries of missing
    len(vechicles_file['Plate'].unique())
    len(dataset_transit_legend['Plate'].unique())

    dataset=pd.merge(vechicles_file,dataset_transit_legend,on=['Plate','Plate'],how='left')

    geometry_passages=[Point(yx) for yx in zip(dataset['Pos_y'],dataset['Pos_x'])]
    dataset=gpd.GeoDataFrame(dataset,crs={'init': 'epsg:4326'},geometry=geometry_passages)
    return dataset

