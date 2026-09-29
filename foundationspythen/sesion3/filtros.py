# From a list of {name, grade} dicts, build a list of names with grade >= 7 using a comprehension.
user=list()
user.append({ "id": 1, "name": "Jennifer", "grade": 8, "email": "jennifer@gmail.com", "role": "admin" })
user.append({"id": 2, "name": "John", "grade": 6, "email": "john@gmail.com", "role": "admin"})
user.append({"id": 3, "name": "Alice", "grade": 9, "email": "alice@gmail.com", "role": "user"})
user.append({"id": 4, "name": "Bob", "grade": 5, "email": "bob@gmail.com", "role": "user"})

#utillizar for loop para filtrar por role

# counter=list()
# for u in user:
#     if u["role"] == "admin":
#         print(f"Admin: {u['name']}, Email: {u['email']}, Grade: {u['grade']}")
#         counter.append(u)
# print(f"Total Admins: {len(counter)}")

# # as a list comprehesion
# counter = [u for u in user if u["role"] == "admin"]
# print(f"Total Admins: {len(counter)}")

# # the use of next
# finalUser=next((u for u in user if u['role'] == "admin"), None)
# print(f"Final User: {finalUser['name'] if finalUser else None}")

#  crear una lista que va a tener elementos diccionarios dentros de esos elementos va a haber items y esos intems van a ser puertos y el datos va a ser status, al menos  puertos, en status se define si esta abierto o cerrado, Solo filtrar los de estado open 

# puertos = [
#     {"port": 21, "status": "closed"},
#     {"port": 22, "status": "open"},
#     {"port": 80, "status": "open"},
#     {"port": 443, "status": "open"},
#     {"port": 3306, "status": "closed"}
# ]

# counter2 = [port for port in puertos if port["status"] == "open"]
# print(f"Total Open Ports: {len(counter2)}") 


# Sort a list of vulnerability dicts by a numeric 'severity' field, highest first, using sorted().
vulnerabilidades = [
    {"id": 1, "name": "SQL Injection", "severity": 9},
    {"id": 2, "name": "Cross-Site Scripting", "severity": 7},
    {"id": 3, "name": "Insecure Direct Object References", "severity": 8},
    {"id": 4, "name": "Security Misconfiguration", "severity": 6},
    {"id": 5, "name": "Sensitive Data Exposure", "severity": 5}
]  
vulnerabilidades_ordenadas = sorted(vulnerabilidades, key=lambda x: x["severity"], reverse=True)
print("Vulnerabilidades ordenadas por severidad (mayor a menor):")
for v in vulnerabilidades_ordenadas:
    print(f"ID: {v['id']}, Name: {v['name']}, Severity: {v['severity']}")



