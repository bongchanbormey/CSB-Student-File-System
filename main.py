import pandas as pd

from school_assessment import SchoolAssessmentSystem
from report_generator import ReportGenerator
from file_processor import FileProcessor

def main():
    try:
        while True:
            print("\nAdministrator Menu:")
            print("1. Look at data in a file and generate a report")
            print("2. Transfer data from one file to another")
            print("3. Fetch data from a website URL")
            print("4. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == '1':
                file_name = input("Enter the file name (with extension): ")
                student_name = input("Enter student name: ")
                
                analyzer = SchoolAssessmentSystem(file_name)
                analyzer.analyze_content(student_name)
                summary = ReportGenerator.generate_summary(analyzer.summary_data)
                print(summary)
                ReportGenerator.save_summary_to_file(summary, f'{student_name}_assessment_report.txt')
            
            elif choice == '2':
                source_file = input("Enter the source file name (with extension): ")
                destination_file = input("Enter the destination file name (with extension): ")
                
                data = pd.read_csv(source_file)
                FileProcessor.data_transfer(data, destination_file)
                print(f"Data has been transferred from {source_file} to {destination_file}")
            
            elif choice == '3':
                url = input("Enter the website URL to fetch data: ")
                
                data = FileProcessor.fetch_web_data(url)
                if data is not None:
                    save_path = input("Enter the file name to save the fetched data (with extension): ")
                    FileProcessor.data_transfer(data, save_path)
                    print(f"Data has been fetched from {url} and saved to {save_path}")
            
            elif choice == '4':
                print("Exiting...")
                break
            
            else:
                print("Invalid choice. Please try again.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()