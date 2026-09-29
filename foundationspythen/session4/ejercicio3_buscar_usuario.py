# 3. Find by email: Escribir la función find_user_by_email() usando next(), retornando None si no se encuentra[cite: 2].

usuarios = [
    {"name": "Ana", "email": "ana@example.com"},
    {"name": "Luis", "email": "luis@example.com"}
]

def find_user_by_email(users, email):
    # next() busca el primer elemento que coincida, si no, devuelve el valor por defecto (None)
    return next((u for u in users if u.get("email") == email), None)

usuario_encontrado = find_user_by_email(usuarios, "luis@example.com")
usuario_inexistente = find_user_by_email(usuarios, "carlos@example.com")

print(f"Búsqueda exitosa: {usuario_encontrado}")
print(f"Búsqueda fallida: {usuario_inexistente}")