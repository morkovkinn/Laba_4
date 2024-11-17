import json

def task(filename) -> float:
    current_sum = 0

    for pair in filename:
        current_sum += pair['score'] * pair['weight']

    otvet = round(current_sum, 3)
    return otvet

with open('input.json') as file:
    task_data = json.load(file)

print(task(task_data))
