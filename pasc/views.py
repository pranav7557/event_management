from django.http import HttpResponse
import json
from django.shortcuts import render
import random
import string

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

random = ''.join([random.choice(string.ascii_letters + string.digits)
                  for n in range(20)])

#print (random)

data = {
    'name': 'yash',
    'email': 'pratik@gmail.com',
    'events': ['web', 'fan'],
    'id': 'sgsdf56',
    'att': {'qrovnrio': False}
}

# db.collection(u'cerebro').document(random).set(data)


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
    return render(request, "search.html")


def data(request):
    if request.method == "POST":
        info = request.POST['fname']
    # print(info)
    # print(db.collection('cerebro').get())
    users_ref = db.collection('Combined')
    docs = users_ref.where('id', '==', info).get()
    #docs = users_ref.get()

    for doc in docs:
        print(u'{} => {}'.format(doc.id, doc.to_dict()))
        data = doc.to_dict()
        docid = doc.id
    return render(request, 'attendance.html', {'events': data['events'], 'data': data, 'userid': docid ,'id':data['id']})
