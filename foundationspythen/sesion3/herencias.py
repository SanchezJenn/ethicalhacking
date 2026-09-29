# Create Admin(User) that adds a role='admin' attribute and overrides display() to show the role too.

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        return f"Name: {self.name}, Email: {self.email}"

user1 = User("Jennifer", "jennifersanchezvelez@gmail.com")
user2 = User("Carlos", "carlos@gmail.com")
user3 = User("Maria", "mariavelz@gmail.com")
print(user1.display())
print(user2.display())
print(user3.display())


class Admin(User):
    def __init__(self, name, email):
        super().__init__(name, email) # super crea el puente con el construcctor de la clase padre (User)
        self.role = 'admin'

    def display(self):
        return f"Name: {self.name}, Email: {self.email}, Role: {self.role}"

user4 = Admin("Admin", "admin@gmail.com")
user5 = Admin("Admin2", "admin2@gmail.com")
print(user4.display())
print(user5.display())
