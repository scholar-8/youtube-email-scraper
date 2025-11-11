thonimport csv
import pandas as pd

class CSVExporter:
    def export(self, data, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Email', 'Profile URL', 'Keyword', 'Location', 'Country'])
                for item in data:
                    writer.writerow([item['email'], item['profileUrl'], item['keyword'], item['location'], item['country']])
        except Exception as e:
            print(f"Error exporting to CSV: {e}")

class ExcelExporter:
    def export(self, data, filename):
        try:
            df = pd.DataFrame(data)
            df.to_excel(filename, index=False)
        except Exception as e:
            print(f"Error exporting to Excel: {e}")