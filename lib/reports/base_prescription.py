from lib.classes.prescription import prescription
from lib.classes.patient import patient

def get_base_prescription(pat: patient, pres: prescription) -> str:
    patient_name = pat.get_fullname()
    patient_age = pat.get_age()
    patient_prescription = ""
    
    for treat in pres.treatments:
        patient_prescription += f"<tr> <th>{treat.description}</th> <th>{treat.usage}</th> <th>{treat.quantity}</th> </th> \n"
    
    base_prescription = """
<!DOCTYPE html>
<html>
<head>
    <title>Reporte 1</title>
</head>
<body>
    <h1>Este es el Reporte 1</h1>
    <p>""" + patient_name + """"</p>
    <p>""" + patient_age + """"</p>
    <table>
        <tr>
            <th>Descripcion</th>
            <th>Uso</th>
            <th>Cantidad</th>
        </tr>
        """ + patient_prescription + """
</body>
</html>
"""
    return base_prescription

