import pandas as pd
from tabulate import tabulate


def save_to_excel(data, file_name="leads.xlsx"):
    df = pd.DataFrame(data)
    df.to_excel(file_name, index=False)
    print(f"[+] Excel file saved: {file_name}")


def save_to_txt_table(data, file_name="leads.txt"):
    df = pd.DataFrame(data)
    table = tabulate(df, headers="keys", tablefmt="grid")
    with open(file_name, "w") as f:
        f.write(table)
    print(f"[+] Text table saved: {file_name}")
