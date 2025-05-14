import csv
import json
import os

csv_filename = "students.csv"
json_filename = "students.json"

# Дані для запису в CSV
students_data = [
    {"id": 1, "name": "Іван", "grade": 90},
    {"id": 2, "name": "Марія", "grade": 85},
    {"id": 3, "name": "Петро", "grade": 78}
]

# Створення та запис у CSV файл
def write_csv_file(filename, data):
    try:
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            fieldnames = ["id", "name", "grade"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"CSV файл '{filename}' успішно створено.")
    except Exception as e:
        print(f"Помилка при записі CSV: {e}")

# Читання CSV та запис у JSON
def convert_csv_to_json(csv_file, json_file):
    try:
        with open(csv_file, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            data = [dict(row) for row in reader]
            # Перетворення чисел з рядків
            for row in data:
                row["id"] = int(row["id"])
                row["grade"] = int(row["grade"])
        
        with open(json_file, mode="w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        print(f"JSON файл '{json_file}' успішно створено.")
    except FileNotFoundError:
        print("Файл CSV не знайдено.")
    except json.JSONDecodeError:
        print("Помилка при перетворенні в JSON.")
    except Exception as e:
        print(f"Інша помилка: {e}")

# Виконання
write_csv_file(csv_filename, students_data)
convert_csv_to_json(csv_filename, json_filename)

