class patient:
    def __init__(self, name: str, lastname: str, age: int):
        self.name = name
        self.lastname = lastname
        self.age = age
    
    def get_fullname(self) -> str:
        return f"{self.name} {self.lastname}"
    
    def get_age(self) -> int:
        return f"{self.age} años"