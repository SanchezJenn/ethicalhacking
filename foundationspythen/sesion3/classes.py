class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

        # print("User created")
    def mostrar_information(self):
        return f"Name: {self.name}, Email: {self.email}"

user1 = User("Jennifer", "jennifer@gmail.com")
user2 = User("John", "jhon@gmail.com")
user3 = User("Alice", "alice@gmail.com")


# tmp=user1.mostrar_information()
# print(tmp)

print(user1.mostrar_information())
print(user2.mostrar_information())
print(user3.mostrar_information())a