from User import User
from UserRepository import UserRepository
from unittest import TestCase, main

class TestUsers(TestCase):

    def setUp(self) -> None:
        admin = User('admin_name', 123)
        admin.authentificate()
        admin1 = User('admin_name1', 1234)
        admin1.authentificate()
        self.userrepo = UserRepository()
        self.userrepo.add_user(User('moryak', 'qwer'), User('moryak123', 'qwer4'), admin, admin1)


    def test_add_user(self):
        data_len = len(self.userrepo.get_data())

        self.userrepo.add_user(User('moryak', 'qwer'))
        self.assertEqual(len(self.userrepo.get_data()), data_len)

        self.userrepo.add_user(User('new_person', '123'))
        self.assertNotEqual(len(self.userrepo.get_data()), data_len)

        data_len = len(self.userrepo.get_data())

        self.userrepo.add_user(123)
        self.assertEqual(len(self.userrepo.get_data()), data_len)

    def test_get_data(self):
        self.assertTrue(type(self.userrepo.get_data()) == list, True)


    def test_find_by_name(self):
       self.assertEqual(self.userrepo.find_by_name('moryak'), True)
       self.assertEqual(self.userrepo.find_by_name(123), False)
       self.assertTrue(self.userrepo.find_by_name('admin_name'))

    def test_de_logging(self):
        self.userrepo.de_logging()
        self.assertEqual(len(self.userrepo.get_data()), 2)

        admin3 = User('admin_3', 890)
        self.userrepo.add_user(User('casual_man', 123), User('rare_man', 12345), admin3)
        admin3.authentificate()
        self.userrepo.de_logging()
        self.assertEqual(len(self.userrepo.get_data()), 3)

















if __name__ == '__main__':
    main()