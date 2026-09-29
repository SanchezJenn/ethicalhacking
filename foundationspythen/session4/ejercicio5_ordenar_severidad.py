# 5. Highest severity first: Ordenar una lista de diccionarios por el campo 'severity', usando sorted()[cite: 2].

vulnerabilidades = [
    {"title": "Information Exposure", "severity": 3},
    {"title": "Remote Code Execution", "severity": 10},
    {"title": "Cross Site Scripting", "severity": 6},
    {"title": "Path Traversal", "severity": 8}
]

# sorted() con key=lambda para definir el criterio de ordenamiento y reverse=True para orden descendente
vulns_ordenadas = sorted(vulnerabilidades, key=lambda x: x["severity"], reverse=True)

print("Vulnerabilidades ordenadas por mayor severidad:")
for v in vulns_ordenadas:
    print(v)