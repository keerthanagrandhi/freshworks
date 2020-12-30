import threading

from threading import*
import time

dt={} 


def create(key,value,timeout=0):
    if key in dt:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dt)<(1024*1024*1024) and value<=(16*1024*1024): #since value less than 16KB 
                if timeout==0:
                    l=[value,timeout]
                else:
                    l=[value,time.time()+timeout]
                if len(key)<=32: 
                    dt[key]=l
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalid key!! key must contain only alphabets and no special characters or numbers")#error message3


            
def read(key):
    if key not in dt:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: #comparing the present time with expiry time
                stri=str(key)+":"+str(b[0]) #to return the value in the format of JasonObject i.e.,"key:value"
                return stri
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            stri=str(key)+":"+str(b[0])
            return stri

#for delete operation
#use syntax "delete(key)"

def delete(key):
    if key not in dt:
        print("error: given key does not exist in database. Please enter a valid key") #error message4
    else:
        b=dt[key]
        if b[1]!=0:
            if time.time()<b[1]: 
                del dt[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") #error message5
        else:
            del dt[key]
            print("key is successfully deleted")



def modify(key,value):
    b=dt[key]
    if b[1]!=0:
        if time.time()<b[1]:
            if key not in dt:
                print("error: given key does not exist in database. Please enter a valid key") #error message6
            else:
                l=[]
                l.append(value)
                l.append(b[1])
                dt[key]=l
        else:
            print("error: time-to-live of",key,"has expired") #error message5
    else:
        if key not in dt:
            print("error: given key does not exist in database. Please enter a valid key") #error message6
        else:
            l=[]
            l.append(value)
            l.append(b[1])
            dt[key]=l
