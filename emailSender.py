import random
import smtplib
from pdfminer import high_level as reader
from selenium import webdriver
PATH = "/Users/loganlach/Developer/chromedriver"





def linAlgQuestions():
    text = getTest('LinearAlgebraTest1')
    thePacket = reader.extract_text(text)
    return thePacket

def getTest(path):
    PATH = '/Users/loganlach/dailyStudyGuideProject/' + path
    todaysTest = random.randint(1, 3)
    options = {1: '/test1.pdf', 2: '/test2.pdf', 3: '/test3.pdf'}
    PATH += options.get(todaysTest)

    text = open(PATH, mode='rb')
    return text


def csQuestions():
    text = getTest('CMSC132Questions')
    thePacket = reader.extract_text(text)

    constant = 1
    currentIndex = 0
    list = []
    while currentIndex != -1:
        for i in range (currentIndex, len(thePacket)):
            currentIndex = thePacket.find('Problem ' + str(constant))
            list.append(currentIndex)
            constant += 1
            break

    return thePacket[int(list[0]),int(list[1])]






print(csQuestions())










