import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer
from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig
# Configuration class jisme store hoga data ingestion ke output paths
@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join('artifact', 'train.csv')
    test_data_path: str = os.path.join('artifact', 'test.csv')
    raw_data_path: str = os.path.join('artifact', 'raw.csv')

class DataIngestion:
    def __init__(self):
        # config class initialize
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the Data Ingestion method/component")

        try:
            # Step 1: Read dataset
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Read the dataset as dataframe")

            # Step 2: Create artifact folder agar na ho
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            # Step 3: Raw data save karo
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Train-Test Split Initiated")

            # Step 4: Train Test split
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            # Step 5: Train CSV save
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            # Step 6: Test CSV save  (pehle yaha galti thi)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed successfully")

            # return paths to next component
            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            # Custom exception handle karega error + file + line number
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    # train_data,test_data = obj.initiate_data_ingestion()
    data_transformation = DataTransformation()
    train_data, test_data = obj.initiate_data_ingestion()
    train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_data, test_data)

    modeltrainer = ModelTrainer()
    print(modeltrainer.initiate_model_trainer(train_arr, test_arr))