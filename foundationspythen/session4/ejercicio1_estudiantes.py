# 1. Students who passed: Construir una lista de nombres con grade >= 7 usando una comprensión de listas[cite: 2].

estudiantes = [
    {"name": "Ana", "grade": 9},
    {"name": "Luis", "grade": 6},
    {"name": "Carlos", "grade": 8},
    {"name": "Marta", "grade": 7}
]

# Comprensión de lista para filtrar
aprobados = [estudiante["name"] for estudiante in estudiantes if estudiante["grade"] >= 7]

print(f"Estudiantes aprobados: {aprobados}")