import os

print("Vai result.json eksistē?", os.path.exists('result.json'))
print("Vai result.json rakstāms?", os.access('result.json', os.W_OK))