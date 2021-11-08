
import sqlite3
import datetime
from django.shortcuts import redirect
import time
import os
import threading

lock = threading.Lock()

db = sqlite3.connect('db.sqlite3',check_same_thread=False)
cur = db.cursor()

def read_booking(message):
    lock.acquire(True)
    try:
        read('home_booking',message)
    finally:
        lock.release()
def read_device(message):
    print("thuan")
    lock.acquire(True)
    try:
        read('home_device',message)
    finally:
        lock.release()

def read_information(message):
    lock.acquire(True)
    try:
        read('home_information',message)
    finally:
        lock.release()


def read(db_tbl,message):
    print("+++++++++++",message)
    list_id = getAllID(db_tbl)
    data=message["data"]
    if (type(data)==list):
        data=message["data"][1:len(data)]
        for i in range(0,len(data)):
            elm=data[i]
            if elm != None:
                if int(elm['id'])  not in list_id:
                    create(elm,db_tbl)
                else:
                    update(elm,db_tbl)
    elif data !=None:
        id = message["path"].split('/')
        elm=data
        if type(data) == dict:
            if id not in list_id:
                create(elm,db_tbl)
            else:
                update(elm,db_tbl)
        else:
            updatefield(elm,db_tbl,id[2],id[1])

def create(elm, db_tbl):
    date = datetime.datetime.now()
    elm['date'] = date
    placeholders = ':'+', :'.join(elm.keys())
    print(placeholders)
    if (db_tbl == 'home_device'):
        columns = "date, device_name, hospital_id, id, role_id"
    elif (db_tbl == 'home_booking'):
        columns = "check_in_id, check_out_id, confirm_id, date, id, info_id, note, qrcode, showed, slot_id"
    else:
        columns = "address, birthdate, bluetooth, city, date, district, gender_id, id, name, national, phone_number, ward"
        #print(columns)
    query = 'INSERT INTO '+db_tbl+' (%s) VALUES (%s)' % (columns, placeholders)
    cur.execute(query, elm)
    db.commit()

def update(elm, db_tbl):
    val=""
    if (db_tbl == 'home_device'):
        val = "role_id = " + str(elm['role'] )
    elif (db_tbl == 'home_booking'):
        val += "confirm_id =" + str(elm['confirm'])
        val += ", check_in_id =" + str(elm['check_in'])
        val += ", check_out_id =" + str(elm['check_out'])
    else:
        #print(elm['name'])
        val += "name = \"" + str(elm['name'])+"\""
        val += ", gender_id = \"" + str(elm['gender'])+"\""
        val += ", birthdate = \"" + str(elm['birthdate'])+"\""
        val += ", address = \"" + str(elm['address'])+"\""
        val += ", ward = \"" + str(elm['ward'])+"\""
        val += ", district = \"" + str(elm['district'])+"\""
        val += ", city = \"" + str(elm['city'])+"\""
        val += ", national = \"" + str(elm['national'])+"\""
        #print(val)
    cond="id = " + str(elm['id'])
    query = 'UPDATE ' + db_tbl + ' SET ' + val + ' WHERE ' + cond
    cur.execute(query)
    db.commit()

def getAllID(table):
    query="SELECT id FROM " + table
    id = cur.execute(query)
    list_id=[]
    for i in id:
        list_id.append(i[0])
    return list_id

def updatefield(elm,db_tbl,field,id):
    val = swith(field) +" = \""+str(elm)+"\""
    cond="id = " + str(id)
    query = 'UPDATE ' + db_tbl + ' SET ' + val + ' WHERE ' + cond
    print(query)
    cur.execute(query)
    db.commit()
def swith(argument):
    switcher = {
        "role": "role_id",
        "confirm": "confirm_id",
        "check_in": "check_in_id",
        "check_out": "check_out_id",
        "gender": "gender_id"
    }
    return switcher.get(argument, argument)