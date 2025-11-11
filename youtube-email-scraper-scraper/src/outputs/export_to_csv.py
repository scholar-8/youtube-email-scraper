thonimport csv

def export_to_csv(data, filename="emails.csv"):
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Email", "Profile URL", "Keyword", "Location", "Country"])
        for row in data:
            writer.writerow(row)

def export_to_excel(data, filename="emails.xlsx"):
    import pandas as pd
    df = pd.DataFrame(data, columns=["Email", "Profile URL", "Keyword", "Location", "Country"])
    df.to_excel(filename, index=False)