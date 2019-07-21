from django.http import HttpResponse
import json
from django.shortcuts import render
import random
import string
import pyrebase

# my database
'''import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("/home/pk/Downloads/event19.json")
firebase_admin.initialize_app(cred)
db = firestore.client()'''

# pasc demo database
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("/home/pk/Downloads/pascdemo.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


config = {
    'apiKey': "AIzaSyAgNOnXoSPWipURDip7ff_wDX7Bq3s1pls",
    'authDomain': "pascregistrationappdemo.firebaseapp.com",
    'databaseURL': "https://pascregistrationappdemo.firebaseio.com",
    'projectId': "pascregistrationappdemo",
    'storageBucket': "pascregistrationappdemo.appspot.com",
    'messagingSenderId': "100193450230",
    'appId': "1:100193450230:web:45bcd71bc8cc1506"
  };

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

#random = ''.join([random.choice(string.ascii_letters + string.digits)
#                 for n in range(20)])

#print (random)

data = {
    'name': 'yash',
    'email': 'pratik@gmail.com',
    'events': ['web', 'fan'],
    'id': 'sgsdf56',
    'att': {'qrovnrio': False}
}

# db.collection(u'cerebro').document(random).set(data)


def signIn(request):
    return render(request, "login.html")


def postsign(request):

    email = request.POST.get('email')
    passw = request.POST.get("pass")
    try:
        user = authe.sign_in_with_email_and_password(email, passw)
    except:
        message = "Invalid Credentials"
        return render(request, "login.html", {"messg": message})
    return render(request, "menu.html")
    #return render(request, "welcome.html", {"e": email})


def update_att(req):
    print(req.POST['id'])
    #db.collection('Combined').document(req.POST['userid']).update({'attendance.' + req.POST['event']: req.POST['val']})
    #db.collection('Combined').where('id' ,'==', req.POST['id']).update({'attendance.' + req.POST['event']: req.POST['val']})
    
    temp1=db.collection('Combined').where('id', '==', req.POST['id']).get()
    for temp2 in temp1:
        uid1=temp2.id

    db.collection('Combined').document(uid1).update({'attendance.' + req.POST['event']: req.POST['val']})
    print(uid1)

    temp3=db.collection(req.POST['event']).where('id', '==', req.POST['id']).get()
    for temp4 in temp3:
        uid2=temp4.id

    print(uid2)
    db.collection(req.POST['event']).document(uid2).update({'attendance' : req.POST['val']})
    
    #temp.update({'attendance.' + req.POST['event']: req.POST['val']})
    #db.collection(req.POST['event']).document(req.POST['userid']).update({'attendance' : req.POST['val']})
    #print(req.POST['event'])
    print(req.POST['event'] + "\n" + req.POST['val'])
    return HttpResponse("")

# Event wise display contestants


def func(req):
    # print(db.collection('cerebro').get())
    users_ref = db.collection('Combined')
    docs = users_ref.where('events', 'array_contains', 'dex').get()
    #docs = users_ref.get()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    return HttpResponse("c")


def search(request):
    return render(request, "page1.html")

def events(request):
    return render(request, "pulzion.html")

def data(request):
    if request.method == "POST":
        info = request.POST['fname']
    # print(info)
    # print(db.collection('cerebro').get())
    try:
        users_ref = db.collection('Combined')
        docs = users_ref.where('id', '==', info).get()
        #docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
            data = doc.to_dict()
            docid = doc.id
        return render(request, 'page2.html', {'events': data['events'], 'data': data, 'userid': docid ,'id':data['id']})
    except:
        message = "Invalid Credentials"
        return render(request, "page1.html", {"messg": message})

    