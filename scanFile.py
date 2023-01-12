"""
    Scans downloaded csv for error code 422

"""


__author__ = 'marcel.kantor'
__date__ = '2021-05-06'


import os
import sys

stringToSpot = '"code":422'


def readFile(inputFile):

    try:

        if os.stat(inputFile).st_size == 0:
            #print('file is empty')
            return "ko"
        
        with open(inputFile,'r',encoding='utf-8') as myFile:
            head = [next(myFile) for x in range(1)]
            if any(stringToSpot in s for s in head):
                #print('yes it sucks')
                return "ko"
            else:
                #print('is is ok')
                return "ok"
            
    except:

        print("Problem reading input file")
        print(str(sys.exc_info()))        
        sys.exit(1)

        
def main(inputFile):
    print(readFile(inputFile))


if __name__ == '__main__':
    inputFile = sys.argv[1]
    main(inputFile)        
