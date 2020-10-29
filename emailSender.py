import random
import smtplib
from pdfminer import high_level as reader
from datetime import date as day
import os
import requests
from bs4 import BeautifulSoup
import lxml

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

PATH = "/Users/loganlach/Developer/chromedriver"


def linAlgQuestions():
    text = getTest('LinearAlgebraTest1')
    return findQuestion(reader.extract_text(text))


def getTest(path):
    # Pulls a random test from my projects folder
    PATH = '/Users/loganlach/dailyStudyGuideProject/' + path
    # Gets a random test, out of the three put in there
    todaysTest = random.randint(1, 3)
    options = {1: '/test1.pdf', 2: '/test2.pdf', 3: '/test3.pdf'}
    PATH += options.get(todaysTest)

    text = open(PATH, mode='rb')
    return text


def findQuestion(text):
    constant = 1
    currentIndex = 0
    list = []
    while currentIndex != -1:
        for i in range(currentIndex, len(text)):
            currentIndex = text.find('Problem ' + str(constant))
            list.append(currentIndex)
            constant += 1
            break
    randomQuestion = random.randint(0, len(list) - 1)
    packet = text[int(list[randomQuestion]):int(list[randomQuestion + 1])]
    return packet


def csQuestions():
    text = getTest('CMSC132Questions')
    thePacket = reader.extract_text(text)

    # Constant refers to the current problem we are on, like looking for
    # Problem 1, then problem 2, etc.
    constant = 1
    # Current index is self explanatory, it shows which char we are it in relation to the
    # Entire size of the list
    currentIndex = 0
    list = []
    while currentIndex != -1:
        for i in range(currentIndex, len(thePacket)):
            currentIndex = thePacket.find('Problem ' + str(constant))
            list.append(currentIndex)
            constant += 1
            break

    # This part here is for picking a random question out of our available questions
    randomQuestion = random.randint(0, len(list) - 1)
    packet = thePacket[int(list[randomQuestion]):int(list[randomQuestion + 1])]
    return packet


# Run it from the top, test 2 has a ton of questions and answers included so some unique work has
# To be done on them

def pythonQuestions():
    PATH = '/Users/loganlach/dailyStudyGuideProject/Python Questions/PythonTest1.txt'
    text = open(PATH, mode='r', encoding='utf-8')

    ranNum = random.randint(1, 45)

    other = text.readlines()
    print(other)
    while (other.__contains__('\n')):
        other.remove('\n')

    i = 0
    while(i < other.__len__()):
        string = other[i]
        if string[0].isdigit():
            i = i + 1
            continue
        else:
            other.remove(string)
            i = i-1

    return other[ranNum-1]


def javaQuestions():
    PATH = '/Users/loganlach/dailyStudyGuideProject/JavaQuestions'
    todaysTest = random.randint(1, 2)
    options = {1: '/test1.txt', 2: '/test2.txt'}
    PATH += options.get(todaysTest)
    text = open(PATH, mode='r').readlines()

    str = ''
    for t in text:
        str += t

    print(str)






# Done for now, will come back when machine is working
# to fix everything else.
def emailWork():
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Your coding review guide' + " " + day.strftime(day.today(), '%m/%d')
        body = 'Hello! \n\n\n This is your daily coding guide \n\n\n Your Java Question \n\n\n' + javaQuestions() + '\n\n\n\n\n Your CMSC132 Question\n\n' + csQuestions()

        msg = f'Subject: {subject}\n\n{body} '

        try:
            smtp.sendmail(EMAIL_ADDRESS, 'lwlach123@gmail.com', msg)
        except:
            subject = 'Your coding review guide' + " " + day.strftime(day.today(), '%m/%d')
            body = 'Hello! \n\n\n This is your daily coding guide \n\n\n Your Java Question \n\n\n' + javaQuestions() + '\n\n\n\n\n Your CMSC132 Question\n\n' + csQuestions().replace(
                '"', '\'') + '\n\n\n' + 'Your Python Question' + '\n\n\n' + pythonQuestions()

            msg = f'Subject: {subject}\n\n{body} '

            smtp.sendmail(EMAIL_ADDRESS, 'lwlach123@gmail.com', msg)



javaQuestions()



