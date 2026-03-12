import csv

file1 = "r-m-c.csv"
file2 = "random-michaels.csv"
result_file = "result_kursov.csv"

unique_rows = set()

with open(file1, "r", newline="", encoding="utf-8") as f1:
    reader = csv.reader(f1)
    for row in reader:
        unique_rows.add(tuple(row))

with open(file2, "r", newline="", encoding="utf-8") as f2:
    reader = csv.reader(f2)
    for row in reader:
        unique_rows.add(tuple(row))

with open(result_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in unique_rows:
        writer.writerow(row)

print("Файл створено:", result_file)