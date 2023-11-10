
class User:

    def __init__(self, name, password):
        self.name = name
        self.password = password
        self.is_admin = False

    def authentificate(self):
        self.is_admin = True

    def __hash__(self):
        return hash((self.name, self.password))

    def __eq__(self, other):
        return hash(self) == hash(other)

