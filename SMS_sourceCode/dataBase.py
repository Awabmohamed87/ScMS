import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyAQG_KmhFcIzDT90Oj9i9uaKNCE1kM-TqQ",
  "authDomain": "fir-course-eb838.firebaseapp.com",
  "projectId": "fir-course-eb838",
  "storageBucket": "fir-course-eb838.appspot.com",
  "messagingSenderId": "513264369969",
  "appId": "1:513264369969:web:0d0a3123d5e4eb572ab010",
  "databaseURL": "https://fir-course-eb838-default-rtdb.europe-west1.firebasedatabase.app/"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()

def getUser(email):
    user = db.child("USERS").order_by_child("Email").equal_to(email).get()
    for row in user.each():
        if int(row.val()['ROLE']) == 4:
            var = db.child("Students").order_by_child("Email").equal_to(email).get()
            print(var.val())
        elif int(row.val()['ROLE']) == 3:
            var = db.child("TEACHERS").order_by_child("Email").equal_to(email).get()
        break

    return var[0].val()

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(str(email), str(password))
        print("LoggedIn Successfully")
        return True
    except:
        return False

def createUserAccount(email, password):
    try:
        auth.create_user_with_email_and_password(str(email),str(password))
        print("Account Created Successfully")
        return True
    except:
        print("Account already exists")
        return False

