import random
from pdfminer import high_level as reader
import PyPDF2


class CMSC132Questions:

    def __init__(self):
        self.PATH = '/Users/loganlach/dailyStudyGuideProject/CMSC132Questions'
        todaysTest = random.randint(1,3)
        options = {1: '/test1.pdf', 2: '/test2.pdf', 3: '/test3.pdf'}
        self.PATH += options.get(todaysTest)

    def getQuestion(self, number):
        thePDF = open(PATH,mode='rb')
        text = reader.extract_text(thePDF)
        questions = []
        currentSubstring = text.find('Problem')
        while(True):
            try:



    def recursiveFind:





thePDF = open(PATH, mode='rb')
text = reader.extract_text(thePDF)

questions = []

try:

except RuntimeError as e:
    PATH = '/Users/loganlach/dailyStudyGuideProject/CMSC132Questions/Test1.pdf'

    # options = {1: '/test1.pdf', 2: '/test2.pdf', 3: '/test3.pdf'}
    # todaysTest = random.randint(1,3)
    # PATH += options.get(todaysTest)

    thePDF = open(PATH, mode='rb')
    text = reader.extract_text(thePDF)

    questions = []

    try:

    except RuntimeError as e:






print(text)




