import json

def task(filename) -> float:

    current_sum = sum([pair['score'] * pair['weight'] for pair in filename])

    otvet = round(current_sum, 3)
    return otvet

with open('input.json') as file:
    task_data = json.load(file)

print(task(task_data))
