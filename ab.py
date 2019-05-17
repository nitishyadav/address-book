#!/usr/bin/python
import os
import json
import pickle

class Contact:
    def __init__(self,fname,lname,street,city,state,pincode):
        self.name=name
        self.fname=fname
        self.lname=lname
        self.street=street
        self.city=city
        self.state=state
        self.pincode=pincode
        
    def __str__(self):
        return "Name:{0}\nFirst Name:{1}\nLast Name:{2}\nStreet address:{3}\nCity:{4}\nState:{5}\nArea Code:{6}".format(self.name,self.fname,self.lname,self.street,self.city,self.state,self.pincode)
        
    def change_fname(self,fname):
        self.fname=fname
        
    def change_lname(self,lname):
        self.lname=lname
        
    def change_street(self,street):
        self.street=street
        
def add_contact():
    address_file=open("address_file","r")
    is_file_empty=os.path.getsize("address_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_file)
    else:
        list_contacts=[]
    try:
        contact=get_contact_info_from_user()
        address_book_file=open("address_file","w")
        list_contacts.append(contact)
        pickle.dump(list_contacts,address_book_file)
        print "Contact added"
    except KeyboardInterrupt:
        print "Contact not added"
    except EOFError:
        print "Contact not added"
    finally:
        address_book_file.close()
    
def get_contact_info_from_user():
    try:
        contact_fname=input("Enter contact First name\n")
        contact_lname=input("Enter contact Lat Name\n")
        contact_street=input("Enter street address\n")
        contact_city=input("Enter city\n")
        contact_state=input("Enter state\n")
        contact_area=input("Enter street address\n")
        contact=Contact(contact_name,contact_email,contact_phone)
        return contact
    except EOFError as e:
        #print "You entered end of file. Contact not added"
        raise e
    except KeyboardInterrupt as e:
        #print "Keyboard interrupt. Contact not added"
        raise e
    
def display_contacts():
    address_book_file=open("address_file","r")
    is_file_empty=os.path.getsize("address_file")==0
    if not is_file_empty:
        list_contacts=pickle.load(address_book_file)
        for each_contact in list_contacts:
            print each_contact
    else:
        print "No contacts in address book"
        return
    address_book_file.close()
    
def search_contact():
    #search_name=input("Enter the name\n")
    address_file=open("address_file","r")
    is_file_empty=os.path.getsize("address_file")==0
    if not is_file_empty:
        search_name=input("Enter the name\n")
        is_contact_found=False
        list_contacts=pickle.load(address_file)
        for each_contact in list_contacts:
            contact_name=each_contact.name
            search_name=search_name.lower()
            contact_name=contact_name.lower()
            if(contact_name==search_name):
                print each_contact
                is_contact_found=True
                break
        if not is_contact_found:
            print "No contact found with the provided search name"
    else:
        print "Address book empty. No contact to search"
    address_book_file.close()
      
print "Enter 'a' to add a contact, 'b' to browse through contacts, 's' to search for contact and 'q' to quit"
while True:
    choice=input("Enter your choice\n")
    if choice == 'q':
        break
    elif(choice=='a'):
        add_contact()
    elif(choice=='b'):
        display_contacts()
    elif(choice=='s'):
        search_contact()
    else:
        print "Incorrect choice. Need to enter the choice again"