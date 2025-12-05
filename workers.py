class Worker:
    worker_count = 0

    def __init__(self, name: str, position: str, salary: float, experience: int):
        self.name = name
        self.position = position
        self.salary = salary
        self.experience = experience
        Worker.worker_count += 1
    
    def change_name(self, new_name: str) -> bool:
        if type(new_name) != str:
            print("New name must be string!")
            return False
        else:
            self.name = new_name
            print(f"New name: {self.name}")
            return True

    def change_position(self, new_position: str) -> bool:
        if type(new_position) != str:
            print("New position must be string!")
            return False
        else:
            self.position = new_position
            print(f"New position: {self.position}")
            return True

    def change_slary(self, new_salary: float) -> bool:
        if type(new_salary) != float or type(new_salary) != int:
            print("Salary must be real number!")
            return False
        
        if new_salary < 0:
            print("Salary cannot be less than 0!")
            return False
        else:
            self.salary = new_salary
            print(f"New salary: {self.salary}")
            return True
        
    def change_experience(self, new_experience: int) -> bool:
        if type(new_experience) != int:
            print("New experience must be integer number!")
            return False
        
        if new_experience < 0:
            print("Experience cannot be less than 0!")
            return False
        else:
            self.experience = new_experience
            print(f"New experience: {self.experience}")

    def get_name(self) -> str:
        return self.name
    
    def get_position(self) -> str:
        return self.position
    
    def get_salary(self) -> float:
        return self.salary
    
    def get_experience(self) -> int:
        return self.experience
    
    def get_info(self) -> str:
        return f"{self.name};{self.position};{self.salary};{self.experience}\n"
        
    @classmethod
    def get_worker_count(cls) -> int:
        return cls.worker_count
    
    @classmethod
    def worker_remove(cls):
        cls.worker_count -= 1