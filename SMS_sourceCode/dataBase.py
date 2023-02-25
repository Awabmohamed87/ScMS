import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyA8cAWq-4TfLMhJkrr0M865S8ua8ms2DKQ",
    "authDomain": "scms-f6376.firebaseapp.com",
    "databaseURL": "https://scms-f6376-default-rtdb.firebaseio.com/",
    "projectId": "scms-f6376",
    "storageBucket": "scms-f6376.appspot.com",
    "messagingSenderId": "90321163000",
    "appId": "1:90321163000:web:ca87e7c9647573e947a10d",
    "measurementId": "G-1W55SEG7XJ"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(str(email),str(password))
        print("LoggedIn Successfully")
        return True
    except:
        print("Invalid userName or password")
        return False

def createUserAccount(email, password):
    try:
        auth.create_user_with_email_and_password(str(email),str(password))
        print("Account Created Successfully")
        return True
    except:
        print("Account already exists")
        return False

