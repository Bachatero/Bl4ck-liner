
"""
    Blackline report downloader

    - downloads latest completed report from Blackline 

"""


__author__ = 'marcel.kantor'
__date__ = '2019-10-03'



import requests
import json
import csv
import codecs
import shutil
from config import *

import base64
import sys
import os
import time
from dateutil.parser import parse
from dateutil import tz
import argparse



def base64encode(dataString):
    
    try:
        
        encodedBytes = base64.b64encode(dataString.encode("utf-8"))
        encodedStr = str(encodedBytes, "utf-8")
        #print(encodedStr)
        return encodedStr
        
    except:
        
        print('Problem @base64encode')
        print(sys.exc_info())        
        sys.exit(1)



def getReportId(reportName, myList):

    try:
        
        listLength = len(myList)
        myIterator = listLength - 1
        myList = sorted(myList, key = lambda i: i['endTime']) # 
        while myIterator >= 0:
            #print(myList[myIterator])
            if myList[myIterator]['name'] == reportName and myList[myIterator]['status'] == 'Complete':
                return myList[myIterator]['id'], myList[myIterator]['endTime'] 
            myIterator -= 1
            
        raise RuntimeError

    except RuntimeError:
        
        print('Problem @getReportId, invalid report name may have been supplied or no report has been generated yet')
        print(sys.exc_info())        
        sys.exit(1234)
        
    except:
        
        print('Problem @getReportId')
        print(sys.exc_info())        
        sys.exit(1)        



def dbFscte(s,c):

    try:
        
        return(xorWord(''.join(chr(i - c[0]) for i in s), ''.join(chr(j) for j in c)))

    except:
        
        print('Problem @dbFscte')
        print(sys.exc_info())
        sys.exit(1)



def setAuthorizationHeader(myString):

    try:
        
        headers = dict()
        headers['Authorization'] = 'Basic ' + base64encode(myString)
        return headers

    except:
        
        print('Problem @setAuthorizationHeader')
        print(sys.exc_info())        
        sys.exit(1)



def setAuthorizationBearer(myToken):

    try:
        
        headers = dict()
        headers['Authorization'] = 'Bearer ' + myToken
        return headers

    except:
        
        print('Problem @setAuthorizationBearer')
        print(sys.exc_info())        
        sys.exit(1)



def getAccessToken(data, headers):

    try:
        
        r = requests.post(urlAuth, data=data, headers=headers)
        accessToken = r.json()['access_token']
        return accessToken

    except:
        
        print('Problem @getAccessToken, check if API key is valid')
        print(sys.exc_info())        
        sys.exit(4321)        



def getReportList(headers):

    try:
        
        r = requests.get(urlQuery,headers=headers)
        return r.json()
    
    except:
        
        print('Problem @getReportList')
        print(sys.exc_info())        
        sys.exit(1)        



def readConfigData():
    
    try:
        return data

    except:
        
        print('Problem @readConfigData')
        sys.exit(1)



def extractReportData(headers, reportName, reportId, reportType, reportDateTime):

    try:
        
        myUrlDoc = urlDoc.format(reportId, reportType)
        myLocalDateTime = convertTimeZone(reportDateTime)
        filePath = os.path.join(outputDir, reportName + '_reportId_' + str(reportId) + '_' + str(myLocalDateTime.date()) + '_' + str(myLocalDateTime.time()).replace(":","") + "." + reportType)                
        #print(filePath)
        with open(filePath,'wb') as f, \
        requests.get(myUrlDoc, headers=headers, stream=True) as r:
            shutil.copyfileobj(r.raw,f)

        return filePath
    
    except:

        print('Problem @extractReportData')
        print(sys.exc_info())
        sys.exit(1)        



def convertTimeZone(reportDateTime):

    try:
        
        myDateTime = parse(reportDateTime)
        return myDateTime.astimezone(tz.tzlocal())            

    except:
        
        print('Problem @convertTimeZone')
        print(sys.exc_info())
        sys.exit(1)



def parseArguments():

    try:
        
        parser = argparse.ArgumentParser(description='Download report data from Blackline')        
        parser.add_argument("-r","--reportName", help="Enter report name", required=True)
  
        args = parser.parse_args()
                    
        if len(sys.argv) < 2:
            parser.print_help()
            parser.exit(1)

        return args
    
    except:

        #print('Problem @parseArguments')
        #print(sys.exc_info())
        sys.exit(1)



def main():

    try:

        myargs = parseArguments()

        headers = setAuthorizationHeader(dbFscte(s, c))

        myToken = getAccessToken(data, headers)

        headers = setAuthorizationBearer(myToken)

        myList = getReportList(headers)

        myReportId, reportEndtime = getReportId(myargs.reportName, myList)

        #print(extractReportData(headers, myReportId, myType, reportEndtime))
        print(extractReportData(headers, myargs.reportName, myReportId, myType, reportEndtime))

    except:

        print('Problem @main')
        print(sys.exc_info())
        sys.exit(1)
        


if __name__ == '__main__':
    main()
    
       

