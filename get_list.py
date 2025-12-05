def get_products_list(products: list):
    if products != []:
        for i in range(len(products)):
            product = products[i]
            print(f"Product {i+1}: {product.get_name()}, price: {product.get_price()}, quantity: {product.get_quantity()}")
    else:
        print("Products list is empty.")

def get_workers_list(workers: list):
    if workers != []:
        for i in range(len(workers)):
            worker = workers[i]
            print(f"Worker {i+1}: {worker.get_name()}, position: {worker.get_position()}, salary: {worker.get_salary()}, experience: {worker.get_experience()}")
    else:
        print("Workers list is empty.")