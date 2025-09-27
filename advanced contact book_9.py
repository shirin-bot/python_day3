#برای دخیره کردن داده ها 
import json
#برای بررسی وجود فایل 
import os
if os.path.exists("contacts.json"):
    with open("contacts.json","r") as f:
        contacts = json.load(f)
else:
    contacts=[]
def save():
    with open("contacts.json","w") as f:
        json.dump(contacts,f,indent=4)
#اضافه کردن مخاطبین 
def add_contact():
    name = input("name:")
    phone = input("phone:")
    contacts.append({"name":name,"phone":phone})
    save()
    print(f"{name} added successfully\n") 
# نمایش لیست مخاطبین 
def show_contact():
    contacts.sort(key=lambda x:x["name"])
    if contacts:
        for i in contacts:
            print(f"name : {i['name']},phone : {i['phone']}")
            print()
    else:
        print("no contacts found")  
#جستجو در لیست
def search_contacts():
    s = input("name?")
    x=0
    for c in contacts:
        if s in c["name"]:
            print(f"{c['name']} phone : {c['phone']}\n")
            print()
            x+=1
    if x==0:
        print("not found") 
#حذف مخاطب
def del_contacts():
    d = input("name?")
    for c in contacts:
        if c["name"]== d:
            contacts.remove(c)
            save()
            print("deleted")
            return
        print("not found")
while True:
    ch=input("what do you want to do?(add/show/search/delete/exit):")
    if ch=="add":
        add_contact()
    elif ch =="show":
        show_contact()
    elif ch =="search":
        search_contacts()
    elif ch =="delete":
        del_contacts()
    elif ch =="exit":
        print("end")
        break
    else:
        print("try again")