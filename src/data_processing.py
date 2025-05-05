import pandas as pd
import os
import sys
from config.paths_config import *
from src.logger import get_logger
from src.custom_exception import CustomException

logger = get_logger(__name__)

class DataProcessor:

    def __init__(self):
        self.train_path = TRAIN_DATA_PATH
        self.processed_data_path = PROCESSED_DATA_PATH

    def load_data(self):
        try:
            logger.info("Data Processing Started")
            df = pd.read_csv(self.train_path)
            logger.info(f"Data read successful: Data shape = {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Problem while loading data: {str(e)}")
            raise CustomException(f"Error while loading data: {e}", sys)

    def drop_unnecessary_columns(self, df, columns):
        try:
            logger.info(f"Dropping Unnecessary Columns: {columns}")
            df = df.drop(columns=columns, axis=1)
            logger.info(f"Columns dropped successfully: Shape = {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Problem while dropping columns: {str(e)}")
            raise CustomException(f"Error while dropping columns: {e}", sys)

    def handle_outliers(self, df, columns):
        try:
            logger.info(f"Handling outliers in columns: {columns}")
            for column in columns:
                Q1 = df[column].quantile(0.25)
                Q3 = df[column].quantile(0.75)
                IQR = Q3 - Q1
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR
                df[column] = df[column].clip(lower=lower_bound, upper=upper_bound)
            logger.info(f"Outliers handled successfully: Shape = {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Problem while handling outliers: {str(e)}")
            raise CustomException(f"Error while handling outliers: {e}", sys)

    def handle_null_values(self, df, columns):
        try:
            logger.info("Handling null values")
            for col in columns:
                if df[col].dtype == 'object':
                    df[col] = df[col].fillna(df[col].mode()[0])
                else:
                    df[col] = df[col].fillna(df[col].median())
            logger.info(f"Missing values handled successfully: Shape = {df.shape}")
            return df
        except Exception as e:
            logger.error(f"Problem while handling null values: {str(e)}")
            raise CustomException(f"Error while handling null values: {e}", sys)

    def save_data(self, df):
        try:
            os.makedirs(PROCESSED_DIR, exist_ok=True)
            df.to_csv(self.processed_data_path, index=False)
            logger.info("Processed data saved successfully")
        except Exception as e:
            logger.error(f"Problem while saving data: {str(e)}")
            raise CustomException(f"Error while saving data: {e}", sys)

    def run(self):
        try:
            logger.info("Starting the data processing pipeline")

            df = self.load_data()

            # Drop columns (duplicates removed with set)
            columns_to_drop = list(set([
                'days_in_waiting_list', 'arrival_date_year', 'assigned_room_type',
                'booking_changes', 'reservation_status', 'country'
            ]))
            df = self.drop_unnecessary_columns(df, columns_to_drop)

            # Choose numeric columns to handle outliers (update as needed)
            numeric_columns = df.select_dtypes(include='number').columns.tolist()
            df = self.handle_outliers(df, numeric_columns)

            # Handle nulls (adjust based on dataset)
            columns_with_nulls = ['agent', 'company']
            df = self.handle_null_values(df, columns_with_nulls)

            self.save_data(df)

            logger.info("Data processing pipeline completed successfully")

        except CustomException as ce:
            logger.error(f"Error occurred in data processing pipeline: {str(ce)}")

if __name__ == "__main__":
    processor = DataProcessor()
    processor.run()