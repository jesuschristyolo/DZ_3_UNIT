from User import User


class UserRepository:

    def __init__(self):
        self.__data = []

    def add_user(self, *args):
        for i in args:
            if isinstance(i, User) and i not in self.__data:
                self.__data.append(i)

    def get_data(self):
        return self.__data

    def find_by_name(self, name):
        for i in self.get_data():
            if i.name == name:
                return True
        return False

    def de_logging(self):
        self.__data = list(filter(lambda x: x.is_admin is True, self.__data))


ur = UserRepository()
admin = User('admin', 123)
admin.authentificate()
justuser = User('admin1', 123)
ur.add_user(123, User('moryak', 'qwer'), User('moryak', 'qwer'), User('moryak123', 'qwer4'), admin, justuser)
print(ur.__dict__)

# ur.de_logging()

print(ur.__dict__)
print(len(ur.get_data()))
ur.add_user(234)
print(len(ur.get_data()))
print(ur.find_by_name('admin1'))


