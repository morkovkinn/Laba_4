# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task(filename) -> None:

    with open(filename) as file:
        reader = csv.DictReader(file)
        task_data = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w') as otvet:
        json.dump(task_data, otvet, indent=4)

if __name__ == '__main__':
    # Нужно для проверки
    task(INPUT_FILENAME)

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
