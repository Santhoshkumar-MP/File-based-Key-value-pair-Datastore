import json
import time
import os
import re


# CRD functions:
class Datastore:  # class for various operation to be preformed in datastore
    def create(self, key, value, fd, timeout):  # creating or updating the new value to a json file
        if key in fd:
            print( "error: this key is already in use" )
        else:
            if len( fd ) < (1024 * 1024 * 1024) and value <= (16 * 1024 * 1024):
                if time == 0:
                    wtv = [value, timeout]
                    fd.update( {keyvalue: wtv} )
                    print( "Successfully updated" )
                else:
                    wtv = [value, time.time() + timeout]
                    fd.update( {keyvalue: wtv} )
                    print( "Successfully updated" )
            else:
                print( "Memory limit exceeded..." )

        # create fucntion over
        # Reading

    def read(self, key, fd):  # reading a data from Datastore
        if key in fd:
            print( "Element is present in Datastore" )
            temp = fd[key]
            if temp[1] != 0:
                if time.time() < temp[1]:
                    return key + ":" + temp[0]
                else:
                    print( "error timetolive of key has expired" )
            else:
                return key + ":" + fd[0]
        else:
            print( "Key is invalid or key is not present, \n please the enter valid name " )
        # Reading function over
        # Deletion:-

    def delete(self, key, fd):
        if key in fd:
            temp = fd[key]
            if temp[1] != 0:
                if time.time() < temp[1]:
                    fd.pop( key )
                    print( "deletion completed successfully" )
                else:
                    print( "error timetolive of key has expired" )
            else:
                fd.pop( key )
                print( "key is successfully deleted" )
        else:
            print( "Element is not present" )
        # deleting function over


result = Datastore()
# user request:
print( "1.create \t 2.read \t 3.delete" )  # Getting the user needed operation to be performed

print( "If you want add a new key value pair to existing file then enter yes or else no :" )
choice = input( "yes or no" )
if choice == "yes" or choice == "Yes":
    location = str( input( "Enter the location of the file " ) )  # type: str
    file = open( location, "w+" )  # Opening json file in read and write mode
    data = json.load( file )  # loading json file data in the format of dictionary
else:
    data = {}

user_input = input( "Enter the operation that you want to perform" )

if user_input == '1':

    keyvalue, value_x = input( "Enter the key and value that you want to add" ).split()
    value_x = int( value_x )
    if keyvalue.isalpha():
        result.create( key=keyvalue, value=value_x, fd=data, timeout=0 )
    else:
        print( "Invalid key name\n'Please enter string key as only alphabet'" )
    if choice != "Yes" or choice != "yes":
        json_new = json.dumps( data )
        f = open( input( "Enter the file location to save data in json format" ), "w" )
        f.write( json_new )
        f.close()

elif user_input == '2':

    keyvalue = str( input( "key" ) )
    result.read( keyvalue, data )

elif user_input == '3':

    keyvalue = input( "key" )
    result.delete( keyvalue, data )
