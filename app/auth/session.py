class Session:

    def __init__(self):

        self.current_user = None


    def login(self, user):

        self.current_user = user


    def logout(self):

        self.current_user = None


    def get_user(self):

        return self.current_user


session = Session()