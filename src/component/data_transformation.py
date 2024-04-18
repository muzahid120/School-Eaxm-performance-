import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.impute import SimpleImputer 
from sklearn.pipeline import Pipeline
import os 
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.utils import save_obj

@dataclass
class DataTransformationconfig:
    preprocessor_obj_file=os.path.join('artsfit','preprocessor.pkl')

class Data_Transformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationconfig()

    def get_data_transformer_obj(self):
        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(steps=[('imputer',SimpleImputer(strategy='mean')),
            ('scaler',StandardScaler())])

            cat_pipeline=Pipeline(steps=[("imputer",SimpleImputer(strategy='most_frequent')),
            ('OnehotEncoder',OneHotEncoder())
            ])

            logging.info(f'Categorical_columns:-{categorical_columns}')
            logging.info(f'Categorical_columns:-{categorical_columns}')
            preprocessor=ColumnTransformer([('numTrasformer',num_pipeline,numerical_columns),
            ('catagorical_transformer',cat_pipeline,categorical_columns)])

            return preprocessor
        except Exception as e:
            raise CustomException(e,sys)


    def initial_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info('read train and test data are completed')

            logging.info('obtainig the preprocessor object')
            preprocessor_obj=self.get_data_transformer_obj()

            target_columns_name='math_score'

            input_feature_train_df=train_df.drop(columns=[target_columns_name],axis=1)
            target_feature_train_df=train_df[target_columns_name]

            input_feature_test_df=test_df.drop(columns=[target_columns_name],axis=1)
            target_feature_test_df=test_df[target_columns_name]

            logging.info('split the target columns are compeleted')
            input_transform_train_df=preprocessor_obj.fit_transform(input_feature_train_df)
            input_transform_test_df=preprocessor_obj.transform(input_feature_test_df)
            logging.info('apply preprocessore of train and test input features are compeleted')

            train_arr=np.c_[input_transform_train_df,np.array(target_feature_train_df)]
            test_arr=np.c_[input_transform_test_df,np.array(target_feature_test_df)]
            logging.info('convert train data and test data to array with both target columns re compeleted ! ')



            save_obj(file_path=self.data_transformation_config.preprocessor_obj_file,
            obj=preprocessor_obj)

            return(
                train_arr,test_arr,self.data_transformation_config.preprocessor_obj_file

            )


        except Exception as e:
            raise CustomException(e,sys)
        
