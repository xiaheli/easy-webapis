#This is a moudel can help you to get the json file very easily.
#To use this model , please NOTE to follow the GPLv3 License
#I will tell you how to use this model , so , followme!
import json
import urllib.request
#This model build on the json model and the urllib.request model.
#We just support pure English Address now.
#We support the internet address (IP or Domain)
def getjson_local(jsons):       #This is for puretxt json in your program
    gotcha = json.loads(jsons)  #This is for load json
    return gotcha               #Return the list(Datatype = list)
def getjson_file(jsons):                    #This is for json file in your computer
    file = open(jsons, encoding='utf-8')    #This is for open the file
    gotcha = file.read()                    #This is for read the file
    return gotcha                           #Return the list(Datatype = list)
def getjson_remote(jsons):                    #This is for the json file on the internet
    file = urllib.request.urlopen(jsons)    #This is for to download the file form the internet
    result = file.read()                    #This is for to read and open the txt
    gotcha = json.loads(result)             #This is for to load the file and make the json to the list
    return gotcha                           #Return the list(Datatype = list)
def autojson(jsons , keys , requests):
    geturl = jsons + '?key=' + keys + '&' + requests #You should and must transform the key to your requests target
    file = urllib.request.urlopen(geturl)
    result = json.loads(file.read())
    return result
#Thank you for your watch , to know how to use the Easy Web Apis more easily.You can visit the offical site www.xiahe.tk(Do Not Forgot the www)