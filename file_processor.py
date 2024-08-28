import pandas as pd
from urllib.request import urlopen
class FileProcessor:
    @staticmethod
    def process_file(file_path):
        try:
            if file_path.endswith('.csv'):
                return pd.read_csv(file_path)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                return pd.read_excel(file_path)
            elif file_path.endswith('.txt'):
                return pd.read_txt(file_path, sep='\t')
            else:
                raise ValueError("Unsupported file format")
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An error occurred while processing the file: {e}")


    @staticmethod
    def data_transfer(data, file_path):
        try:
            if file_path.endswith('.csv'):
                data.to_csv(file_path, index=False)
            elif file_path.endswith('.xlsx') or file_path.endswith('.xls'):
                data.to_excel(file_path, index=False)
            elif file_path.endswith('.txt'):
                data.to_csv(file_path, index=False, sep='\t')
            else:
                raise ValueError("Unsupported file format")
        except Exception as e:
            print(f"An error occurred while transferring the data: {e}")


    @staticmethod
    def fetch_web_data(url):
        try:
            # Fetching the CSV content from the URL
            response = urlopen(url)
            csv_data = response.read().decode('utf-8')
            
            # Convert the CSV data to a Pandas DataFrame
            from io import StringIO
            data = pd.read_csv(StringIO(csv_data))
            
            # Optionally, you can print or return specific columns or rows
            print(data.head())  # Displaying the first few rows
            
            return data

        except Exception as e:
            print(f"An error occurred while fetching web data: {e}")
            return None

    
