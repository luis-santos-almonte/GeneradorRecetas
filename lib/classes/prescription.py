class treatment:
    def __init__(self, description: str, usage: str, quantity: int):
        self.description = description
        self.usage = usage
        self.quantity = quantity
        
class prescription:
    def __init__(self, treatments: list[str]) -> None:
        self.treatments = treatments
        
    def add_treatment(self, treatment: treatment) -> None:
       self.treatments.append(treatment)
       