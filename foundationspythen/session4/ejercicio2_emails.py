# 2. Emails only: Construir una lista plana que contenga solo los valores de email[cite: 2].

usuarios = [
    {"name": "Ana", "email": "ana@example.com"},
    {"name": "Luis", "email": "luis@example.com"},
    {"name": "Carlos", "email": "carlos@example.com"}
]

# Comprensión de lista para extraer un campo específico
lista_emails = [usuario["email"] for usuario in usuarios]

print(f"Lista de correos: {lista_emails}")