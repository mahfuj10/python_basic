from pathlib import Path

# path = Path('emails')
path = Path()

# print(path.exists()) to check directory exist
# print(path.mkdir()) create directory
# print(path.rmdir())  delete directory

for file in path.glob('*.py'):  # get all .py file
    print(file)
