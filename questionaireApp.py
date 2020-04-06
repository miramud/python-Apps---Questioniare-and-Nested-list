# NUMBER OF QUESTIONS TO ASK
numQuestions = input("How many questions do you want to ask: ")

# CHECK FOR ALPHABETS AND ASK FOR A NUMBER
while not numQuestions.isdigit():
    numQuestions = input("Please input a digit and not an alphabet: ")
numQuestions = int(numQuestions)

# NUMBER OF PERSONS TO ASK THESE QUESTIONS
numPersons = input("How any number of persons do you want to ask these questions: ")
# CHECK FOR ALPHABETS AND ASK FOR A NUMBER
while not numPersons.isdigit():
    numPersons = input("Please input a number and not an alphabet: ")
numPersons = int(numPersons)
print(" ")

# DEFINE THE QUESTIONAIRE FUNCTION THAT TAKES IN THE TWO VARIABLES ABOVE AS PARAMETERS
def questionaire(numQuestions, numPersons):
    
    # DECLARE EMPTY LISTS FOR THE QUESTIONS, ANSWERS AND NAMES, AND EMPTY DICTIONARIES FOR THE NAME AND ANSWERS PAIRS, AND THE FINAL NAME
    # QUESTION AND ANSWER PAIRS
    quests = list()
    answersDB = []
    names = []
    nameAndAnswers = dict()
    finalNameQuesAndAnsDB = {}

    # DECLARE THE COUNTER TO LOOP THROUGH QUESTS LIST USING THE NUMBER OF QUESTIONS
    i = 0
    user = input("Hello, What is your Username: ")
    print("Hello {}, Please Type your questions".format(user))

    while i < numQuestions:
        tempQuest = i + 1
        print("Type Question {}".format(tempQuest))
        ask = input("")
        quests.append(ask)
        i += 1

    # DECLARE THE COUNTER TO LOOP THROUGH THE NAMES LIST USING THE NUMBER OF PERSONS
    j = 0
    print(" ")
    while j < numPersons:
        print("Please input your name.")
        name = input(" ")
        print(" ")
        print("Hello {}, Please give the correct answers to the questions that follow".format(name))
        print(" ")
        names.append(name)
        
        # DECLARE A TEMPORARY ANSWERS EMPTY LIST FOR STORING THE ANSWERS TO THE QUESTIONS FROM EACH PERSON
        answers = []

        # DECLARE THE COUNTER TO LOOP THROUGH THE QUESTS LIST, AND ALSO APPEND THE ANSWERS INTO THE ANSWERS LIST
        x = 0
        while x < numQuestions:
            temp = x + 1
            print("Question {}".format(temp))
            print(quests[x])
            answer = input("")
            print(" ")
            answers.append(answer)        # APPEND THE ANSWER INTO THE ANSWERS LIST
            x += 1
        answersDB.append(answers)         # APPEND THE ANSWERS LIST INTO THE GENERAL ANSWERSDB LIST
            # print(quests, answers)

        # CREATE THE DICTIONARY nameAndAnswers TO HAVE THE NAME OF RESPONDER AS KEY AND ANSWER FROM answersDB AS VALUE  
        nameAndAnswers[name] = answersDB[j]       
        j += 1
    
    # LOOP THROUGH THE nameAndAnswers DICTIONARY USING THE KEYS (NAMES OF REPONDERS)
    for key in nameAndAnswers:
        counter = 0             # DECLARE A COUNTER FOR LOOPING THROUGH THE VALUES IN THE nameAndAnswers DICTIONARY
        listQnA = {}            # DECLARE A TEMPORARY listQnA DICTIONARY FOR HOLDING THE QUESTION/ANSWER PAIRS IN THE WHILE LOOP BELOW

        while counter < len(quests):
            # LET THE TEMPORARY listQnA DICTIONARY HAVE QUESTIONS AS KEYS, AND CORRESPONDING ANSWERS BY EACH RESPONDER AS VALUES
            listQnA[quests[counter]] = nameAndAnswers[key][counter]  

            # THEN FINALLY TAKE THE KEY FROM THE nameAndAnswers DICTIONARY(NAMES OF RESPONDERS), AS THE KEYS, 
            # WHILE THE TEMPORARY listQnA DICTIONARY (NOW HAVING THE QUESTION/ANSWER PAIRS FOR EACH RESPONDER), AS THE VALUES
            finalNameQuesAndAnsDB[key] = listQnA   
            counter += 1
    
    # PRINT OR RETURN THE NECESSARY DICTIONARIES, AND SENTENCES NEEDED.
    print("The Following questions were asked by {}".format(user))
    print(quests)
    print(" ")
    print("Below is a dictionary of answers given by various persons")
    print(nameAndAnswers)    # DICTIONARY OF NAME/ANSWERS PAIR
    print(" ")
    print("Below is a Nested Dictionary of the names of users who answered your questions, and their Question/Answer pairs")
    print(finalNameQuesAndAnsDB)    # THE MAIN DICTIONARY OF NAME/QUESTION/ANSWER PAIR
       
questionaire(numQuestions, numPersons)



''' 

# HOW TO LOOP THROUGH A LIST AND A DICTIONARY CONTAINING A LIST, 
# SO AS TO PAIR THE VALUES OF THE LIST, WITH THE VALUES OF THE DATA IN THE DICTIONARY VALUES

quest = ['age?', 'school?']

nameQnA = {
    'jane': ['23', 'uniben'], 
    'jude': ['21', 'unilag'], 
    'Jakes': ['31', 'uniPort'], 
    'Bejay': ['28', 'UniJos'], 
    'Success': ['32', 'AAU']
}


db = {}
finalDB = []

for key in nameQnA:
    j = 0 
    listQnA = {}
    while j < len(quest):
        
        listQnA[quest[j]] = nameQnA[key][j]
        # listQnA.append([])
        db[key] = listQnA        
        j += 1
print(db)
# print(nameQnA)
    # finalDB.append(db)

# print(finalDB) '''