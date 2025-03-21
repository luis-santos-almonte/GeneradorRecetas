class Treatment:
    def __init__(self, description: str, usage: str, quantity: int):
        self.description = description
        self.usage = usage
        self.quantity = quantity
        
class Prescription:
    def __init__(self, treatments: list[Treatment] = None) -> None:
        self.treatments = treatments if treatments else []
        
    def add_treatment(self, treatment: Treatment) -> None:
       self.treatments.append(treatment)

    def __str__(self) -> str:
        return "\n".join([f"{treatment.description} - {treatment.usage} - {treatment.quantity}" for treatment in self.treatments])
    
    def html_list(self) -> str:
        return "\n".join([f"<tr> <th>{treatment.description}</th> <th>{treatment.usage}</th> <th>{treatment.quantity}</th> </th>" for treatment in self.treatments])