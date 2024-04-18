from src.exception import CustomException
from src.logger import logging
import pandas as pd 
import numpy as np 
from sklearn.model_selection import train_test_split
import sys
import os 
from src.component.data_transformation import DataTransformationconfig
from src.component.data_transformation import Data_Transformation

class Data_Ingestion_Config:
    train_data_path:str=os.path.join('artsfit','train_data.csv')
    test_data_path:str=os.path.join('artsfit','test_data.csv')
    row_data_path:str=os.path.join('artsfit','row_data.csv')


class Data_Ingestion:
    def __init__(self):
        self.data_ingestion=Data_Ingestion_Config()

    def initial_data_Ingestion(self):
        logging.info('Entered the data ingestion method or component')
        try:
            df=pd.read_csv(r'C:\Users\SDS\Downloads\stud.csv')
            logging.info('Initial row data is reading compelet')

            os.makedirs(os.path.dirname(self.data_ingestion.train_data_path),exist_ok=True)
            logging.info('Create directory for data ingestion')

            df.to_csv(self.data_ingestion.row_data_path,header=True,index=False)
            logging.info('Row data save into row data file ')

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            logging.info('Data split is succcessful !')
            train_set.to_csv(self.data_ingestion.train_data_path,header=True,index=False)
            logging.info('Train data is successfully save to that path')
            test_set.to_csv(self.data_ingestion.test_data_path,header=True,index=False)
            logging.info('Test data set is successfully save to the path ')

            return (self.data_ingestion.train_data_path,
            self.data_ingestion.test_data_path)
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':

    obj=Data_Ingestion()
    obj.initial_data_Ingestion()
    transformation=Data_Transformation()
    train_data=r'artsfit\train_data.csv'
    test_data=r'artsfit\test_data.csv'
    train_arr,test_arr,_=transformation.initial_data_transformation(train_data,test_data)