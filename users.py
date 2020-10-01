class Users:
    n_active = 0
    users = []

    def __init__(self, active, user_name):
        self.active = active
        self.user_name = user_name        

enrique = Users(True, 'fenriquegimenez')

print(enrique.user_name)
print(Users.users)
print(Users.sumer(enrique))