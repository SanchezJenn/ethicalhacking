# 4. Count by category: Contar cuántas vulnerabilidades pertenecen a cada owasp_category (sin usar librerías)[cite: 2].

vulnerabilidades = [
    {"title": "SQL Injection", "owasp_category": "Injection"},
    {"title": "Cross Site Scripting", "owasp_category": "Injection"},
    {"title": "Insecure Direct Object Reference", "owasp_category": "Broken Access Control"},
    {"title": "Command Injection", "owasp_category": "Injection"}
]

conteo_categorias = {}

for vuln in vulnerabilidades:
    categoria = vuln["owasp_category"]
    # get(categoria, 0) devuelve 0 si la clave no existe, permitiendo sumar 1 de manera segura
    conteo_categorias[categoria] = conteo_categorias.get(categoria, 0) + 1

print("Conteo de vulnerabilidades por categoría:")
for cat, conteo in conteo_categorias.items():
    print(f"- {cat}: {conteo}")