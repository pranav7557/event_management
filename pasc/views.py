from django.http import HttpResponse
import json
from django.shortcuts import render
import random
import string
import pyrebase

# pasc demo database
# from google.cloud import firestore
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
}

firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
database = firebase.database()

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
    # return render(request, "welcome.html", {"e": email})


def update_att(req):
    print(req.POST['id'])
    # db.collection('Combined').document(req.POST['userid']).update({'attendance.' + req.POST['event']: req.POST['val']})
    # db.collection('Combined').where('id' ,'==', req.POST['id']).update({'attendance.' + req.POST['event']: req.POST['val']})

    temp1 = db.collection('Combined').where('id', '==', req.POST['id']).get()
    for temp2 in temp1:
        uid1 = temp2.id

    db.collection('Combined').document(uid1).update(
        {'attendance.' + req.POST['event']: req.POST['val']})
    print(uid1)

    temp3 = db.collection(req.POST['event']).where(
        'id', '==', req.POST['id']).get()
    for temp4 in temp3:
        uid2 = temp4.id

    print(uid2)
    db.collection(req.POST['event']).document(
        uid2).update({'attendance': req.POST['val']})

    # temp.update({'attendance.' + req.POST['event']: req.POST['val']})
    # db.collection(req.POST['event']).document(req.POST['userid']).update({'attendance' : req.POST['val']})
    # print(req.POST['event'])
    print(req.POST['event'] + "\n" + req.POST['val'])
    return HttpResponse("")

# Event wise display contestants


def func(req):
    # print(db.collection('cerebro').get())
    users_ref = db.collection('Combined')
    docs = users_ref.where('events', 'array_contains', 'dex').get()
    # docs = users_ref.get()
    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
    return HttpResponse("c")


def search(request):
    return render(request, "page1.html")


def events(request):
    return render(request, "pulzion.html")


def register(request):
    return render(request, "new_reg.html")


def menu(request):
    return render(request, "menu.html")


def data(request):
    if request.method == "POST":
        info = request.POST['fname']
    # print(info)
    # print(db.collection('cerebro').get())
    try:
        users_ref = db.collection('Combined')
        docs = users_ref.where('id', '==', info).get()
        # docs = users_ref.get()

        for doc in docs:
            print(u'{} => {}'.format(doc.id, doc.to_dict()))
            data = doc.to_dict()
            docid = doc.id
        return render(request, 'page2.html', {'events': data['events'], 'data': data, 'userid': docid, 'id': data['id']})
    except:
        message = "Invalid Credentials"
        return render(request, "page1.html", {"messg": message})


def add_data(request):
    x = []

    if request.method == 'POST':
        name1 = request.POST.get('participant1')
        name2 = request.POST.get('participant2')
        college = request.POST.get('collegeName')
        vol = request.POST.get('volunteer')
        emailid = request.POST.get('mail')
        cont = request.POST.get('contact')

        dex = request.POST.get('Dextrous')
        qb = request.POST.get('Quiz2Bid')
        rc = request.POST.get('Recode_It')
        cer = request.POST.get('Cerebro')
        jc = request.POST.get('JustCoding')
        cb = request.POST.get('Code_Buddy')
        bg = request.POST.get('Bug_Off')
        eq = request.POST.get('ElectroQuest')
        dq = request.POST.get('DataQuest')
        wa = request.POST.get('Web_and_App_Development')
        fan = request.POST.get('Fandom')
        ins = request.POST.get('Insight')
        pr = request.POST.get('Photoshop_Royale')

    if dex == 'on':
        x.append('Dextrous')

    if qb == 'on':
        x.append('Quiz2Bid')

    if rc == 'on':
        x.append('Recode_It')

    if jc == 'on':
        x.append('JustCoding')

    if cb == 'on':
        x.append('Code_Buddy')

    if bg == 'on':
        x.append('Bug_Off')

    if eq == 'on':
        x.append('ElectroQuest')

    if dq == 'on':
        x.append('DataQuest')

    if wa == 'on':
        x.append('Web_and_App_Development')

    if fan == 'on':
        x.append('Fandom')

    if ins == 'on':
        x.append('Insight')

    if pr == 'on':
        x.append('Photoshop_Royale')

    if cer == 'on':
        x.append('Cerebro')

    random1 = ''.join([random.choice(string.ascii_letters + string.digits)
                       for n in range(20)])

    random2 = ''.join([random.choice(string.ascii_letters + string.digits)
                       for n in range(8)])
    random2 = random2.upper()
    print(x)
    print(name1)
    print(random1)

    d1 = {
        'participant1': name1,
        'participant2': name2,
        'mail': emailid,
        'events': x,
        'id': random2,
        'contact': cont,
        'collegeName': college,
        'volunteer': vol,
    }

    print(d1)
    db.collection(u'Combined').document(random1).set(d1)

    d2 = {
        'participant1': name1,
        'participant2': name2,
        'mail': emailid,
        'id': random2,
        'contact': cont,
        'collegeName': college,
        'score': '0',
        'volunteer': vol,
    }

    for y in x:
        random3 = ''.join([random.choice(string.ascii_letters + string.digits)
                           for n in range(20)])
        print(y)
        print(random3)
        print(d2)
        db.collection(y).document(random3).set(d2)

    return render(request, "page3.html", {"id": random2})


def rep(req):
    # eventname=req.POST['event']
    users_ref = db.collection(req.POST['event'])
    docs = users_ref.where('attendance', '==', 'true').get()
    # docs1=users_ref.where(not 'attendance').get()
    print('hihiello')
    # docs = users_ref.get()
    # data = docs.to_dict()
    # print(docs)
    global data1
    data1 = []
    for i in docs:
        # print(u'{} => {}'.format(doc.id, doc.to_dict()))
        data1.append(i.to_dict())
    return HttpResponse("")


def rep_(req):
    print(data1)
    return render(req, 'rep.html', {'db': data1})
