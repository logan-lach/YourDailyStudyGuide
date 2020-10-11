import random

from pdfminer import high_level as reader

PATH = '/Users/loganlach/dailyStudyGuideProject/PhilosophyQuestions'

options = {1: '/test1.pdf', 2: '/test2.pdf', 3: '/test3.pdf'}

todaysTest = random.randint(1,3)

PATH += options.get(todaysTest)

print(PATH)

