class treatment:
    def __init__(self, description: str, usage: str, quantity: int):
        self.description = description
        self.usage = usage
        self.quantity = quantity
        
class prescription:
    def __init__(self, treatments: list[treatment] = None) -> None:
        self.treatments = treatments if treatments else []
        
    def add_treatment(self, treatment: treatment) -> None:
       self.treatments.append(treatment)

    def __str__(self) -> str:
        return "\n".join([f"{treatment.description} - {treatment.usage} - {treatment.quantity}" for treatment in self.treatments])