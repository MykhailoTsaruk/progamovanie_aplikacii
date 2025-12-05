import os

def read_file(file_name: str) -> list:
    result = []
    if os.path.exists(file_name):
        file = open(file_name, 'r')
        for string in file.readlines():
            result.append(string.strip().split(';'))
    else:
        file = open(file_name, 'x')
        print(f"File products.csv was not found, and was created")

    # print(result)

    file.close()
    return result