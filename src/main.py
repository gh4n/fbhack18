import pyrebase

class TBA:

    def __init__(self):
        self.config = Config()
        self.db = self.authenticate()
        self.firebase = None
        self.auth = None
        self.listener = self.listen()

    def authenticate(self):
        """
        Handles authentication and connection to firebase
        """
        self.firebase = pyrebase.initialize_app(self.config.config_db())
        self.auth = self.firebase.auth()
        user = self.auth.sign_in_with_email_and_password(self.config.db_email, self.config.db_pwd)
        self.db = self.firebase.database()
        # data = self.config.db_schema()
        # results = self.db.child("users").push(data, user['idToken'])
        return self.db
    
    def sign_in(self, email, password):


    def create_new_user(self, email, password):
        auth.create_user_with_email_and_password(email, password)
    
    
        