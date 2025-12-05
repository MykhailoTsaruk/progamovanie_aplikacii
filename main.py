from product import Product
from workers import Worker
from read_file import read_file
from save_file import save_file
from get_list import *

if __name__ == "__main__":
    products = []
    workers = []

    read_products = read_file("products.csv")
    if read_products != []:
        for i in range(len(read_products)):
            name = read_products[i][0]

            try:
                price = float(read_products[i][1])
            except ValueError:
                print(f"Product {name}, {i+1} place in file, price must be number!")
                continue

            try:
                quantity = float(read_products[i][2])
            except ValueError:
                print(f"Product {name}, {i+1} place in file, quantity must be number!")
                continue

            products.append(Product(name, price, quantity))

    read_workers = read_file("workers.csv")
    if read_workers != []:
        for i in range(len(read_workers)):
            name = read_workers[i][0]
            position = read_workers[i][1]
            try:
                salary = float(read_workers[i][2])
            except ValueError:
                print(f"Worker {name}, {i+1} place in file, salary must be number!")
                continue

            try:
                experience = int(read_workers[i][3])
            except ValueError:
                print(f"Worker {name}, {i+1} place in file, experience must be integer number!")
                continue

            workers.append(Worker(name, position, salary, experience))

    print('\n\n\n')

    while True:
        print("\n1 - get products list")
        print("2 - get employees list")
        print("3 - add new product")
        print("4 - add new employee")
        print("5 - remove product from list")
        print("6 - remove employee from list")
        
        print("\ngetP - get product count")
        print("getW - get eployee count")

        print("\nsaveP - save products list")
        print("saveW - save empoloyees list")
        print("saveA - save products and empoloyees lists")

        print("\nexit - to exit")
        user_input = input("\nEnter operation: ")

        print("\n\n")
        
        match user_input:
            case '1':
                get_products_list(products)

            case '2':
                get_workers_list(workers)

            case '3':
                user_input_name = input("Enter product name: ")
                try:
                    user_input_price = float(input("Enter product price: "))
                except ValueError:
                    print("\nPrice must be real number!")
                    continue
                try:
                    user_input_quantity = float(input("Enter product quantity: "))
                except ValueError:
                    print("\nQuantity must be real number!")
                    continue
                products.append(Product(user_input_name, user_input_price, user_input_quantity))

            case '4':
                user_input_name = input("Enter employee name: ")
                user_input_position = input("Enter employee position: ")
                try:
                    user_input_salary = float(input("Enter employee salary: "))
                except ValueError:
                    print("\nSalary must be real number!")
                    continue
                try:
                    user_input_experience = int(input("Enter employee experience: "))
                except ValueError:
                    print("\nExperience must be real integer number!")
                    continue
                workers.append(Worker(user_input_name, user_input_position, user_input_salary, user_input_experience))
            
            case "5":
                get_products_list(products)
                if len(products) == 0:
                    continue

                try:
                    user_input = int(input("Enter position in list: "))
                except ValueError:
                    print("\nEnter position must be integer real number!")
                    continue

                if user_input < 0 or user_input > len(products):
                    print(f"\nEntered number must be in the range from 1 to {len(products)}!")
                    continue

                user_input_agree = input(f"Do you want to delete product: {products[user_input-1].get_name()}, {products[user_input-1].get_price()}, {products[user_input-1].get_quantity()}? (Y/N): ")
                match user_input_agree.lower():
                    case 'y':
                        print("\nProduct has been successfully removed.")
                        products.pop(user_input-1)
                        Product.product_remove()
                    case 'n':
                        continue

            case "6":
                get_workers_list(workers)
                if len(workers) == 0:
                    continue

                try:
                    user_input = int(input("Enter position in list: "))
                except ValueError:
                    print("\nEnter position must be integer real number!")
                    continue
                
                if user_input < 0 or user_input > len(workers):
                    print(f"\nEntered number must be in the range from 1 to {len(workers)}!")
                    continue

                user_input_agree = input(f"Do you want to delete product: {workers[user_input-1].get_name()}, {workers[user_input-1].get_position()}, {workers[user_input-1].get_salary()}, {workers[user_input-1].get_experience()}? (Y/N): ")
                match user_input_agree.lower():
                    case 'y':
                        print("\nEmployee has been successfully removed.")
                        workers.pop(user_input-1)
                        Worker.worker_remove()
                    case 'n':
                        continue

            case "getP":
                print(f"Product count: {Product.get_product_range()}")

            case "getW":
                print(f"Worker count: {Worker.get_worker_count()}")

            case "saveP":
                save_list = []
                for product in products:
                    save_list.append(product.get_info())
                if save_file("products.csv", save_list) is True:
                    print("Saved successfully")

            case "saveW":
                save_list = []
                for worker in workers:
                    save_list.append(worker.get_info())
                if save_file("workers.csv", save_list) is True:
                    print("Saved successfully")

            case "saveA":
                save_list_P = []
                for product in products:
                    save_list_P.append(product.get_info())
                if save_file("products.csv", save_list_P) is True:
                    print("Saved successfully")
                    
                save_list_W = []
                for worker in workers:
                    save_list_W.append(worker.get_info())
                if save_file("workers.csv", save_list_W) is True:
                    print("Saved successfully")

            case "exit":
                print("\nExit...")
                break
            
