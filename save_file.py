import os

def save_file(file_name: str, save_list: list) -> bool:
    if os.path.exists(file_name):
        file = open(file_name, 'w')
        for s_list in save_list:
            file.write(s_list)
    else:
        file = open(file_name, 'x')
        for s_list in save_list:
            file.write(s_list)
    
    file.close()
    return True