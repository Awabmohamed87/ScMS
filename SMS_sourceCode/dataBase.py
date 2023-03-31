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
            print(row.key())
            var = db.child("Students").child(row.key()).get()
        elif int(row.val()['ROLE']) == 3:
            var = db.child("Teachers").child(row.key()).get()
        elif int(row.val()['ROLE']) == 5:
            continue
        else:
            var = db.child("Managers").child(row.key()).get()
        break

    return var.val(), int(row.val()['ROLE'])

def mapRole(role):
    r = db.child("ROLES").child(role).get()
    return r.val()['ROLE']

def login(email, password):
    try:
        auth.sign_in_with_email_and_password(str(email), str(password))
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

