class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet_user(self):
        print(f'Привет, {self.name}! Тебе {self.age} лет.')

    def have_birthday(self):
        self.age += 1


if __name__ == '__main__':

    user1 = User('Александр', 25)
    user1.greet_user()
    user1.have_birthday()
    user1.greet_user()

    user2 = User('Маша', 18)
    user2.greet_user()
    user2.have_birthday()
    user2.greet_user()
