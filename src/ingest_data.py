import os
import zipfile
from abc import ABC, abstractmethod

import pandas as pd

# Define an abstract class for Data Ingestor
class DataIngestor(ABC):
    @abstractmethod
    def ingest(self, file_path: str) -> pd. DataFrame:
        """Abstract method to ingest data from a given file."""
        pass

# Implement a concrete class for ZIP Ingestion
class ZipDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Extracts a .zip file and returns the content as a pandas DataFrame."""
        # Ensure the file is a .zip
        if not file_path.endswith(".zip"):
            raise ValueError("The provided file is not a .zip file.")
        
        # Extract the zip file
        with zipfile.ZipFile(file_path, "r") as zip_ref:
            zip_ref.extractall("extracted data")

        # Find th extracted CSV (assuming there is one CSV file inside the zip)
        extracted_files= os.listdir("extracted_data")
        csv_files = [f for f in extracted_files if f.endswith(".csv")]

        if len(csv_files) == 0:
            raise FileNotFoundError("No CSV file found in the extracted data.")
        if len(csv_files)>1:
            raise ValueError("Multiple CSV files found. Please specify which one to use.")
        
        # Read the CSV into a DataFrame
        csv_file_path = os.path.join("extracted_data", csv_files[0])
        df = pd.read_csv(csv_file_path)

        # Return the Dataframe
        return df
    
# Implement a concrete class for Excel Ingestion
class ExcelDataIngestor(DataIngestor):
    def ingest(self, file_path: str) -> pd.DataFrame:
        """Reads an Excel (.xlsx) file and returns the content as a pandas DataFrame."""
        if not file_path.endswith(".xlsx"):
            raise ValueError("The provided file is not a .xlsx file.")

        # Load the Excel file into a DataFrame
        try:
            df = pd.read_excel(file_path)
        except ValueError as e:
            raise ValueError(f"Error reading Excel file: {e}")

        return df

    
# Implement a Factory to create DataIngestors
class DataIngestorFactory:
    @staticmethod
    def get_data_ingestor(file_extension: str)-> DataIngestor:
        """Returns the appropriate DataIngestor based on file extension."""
        if file_extension == ".zip":
            return ZipDataIngestor()
        elif file_extension == ".xlsx":
            return ExcelDataIngestor()
        else:
            raise ValueError(f"No ingestor available for file extension: {file_extension}")
        
# Example usage:
if __name__ == "__main__":
    # Specify the file path
    # file_path = "C:\Users\40107588\Desktop\HOUSE-PRICE-END-TO-END\src\ingest_data.py"     
    
    # Determine the file extension
    # file_extension = os.path.splitext(file_path)[1]
    
    # Get the appropriate DataIngestor
    # data_ingestor = DataIngestorFactory.get_data_ingestor(file_extension)
    
    # Ingest the data and load it in a DataFrame
    # df = data_ingestor.ingest(file_path)                        
    
    # Now df contains the DataFrame from the extracted CSV
    # print(df.head())
    pass           