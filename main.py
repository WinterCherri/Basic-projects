import random

flashcards = []

textfile = input("Which text file would you like to use?: ")

#Student created function lets the user import a 
#text file to use for vocabulary list and so that 
#the data can be sifted

def textfilechooser(textfile):
  wordlistfile = open(textfile, "r")
  wordlist = wordlistfile.read()
  global flashcards 
  flashcards = wordlist.split("\n")

textfilechooser(textfile)

flashcards_dict = []
subcount = int(input(("How many words would you like in your sublist?: ")))
cardrepeat = int(input(("How many times would you like the card to repeat?: ")))
sublist = int(input(("How many sublists would you like?: ")))

#A loop that sifts through data in the list and puts it into dictionary format

for i in range(int(len(flashcards)/2)):
  object = {
"word": flashcards[i*2], "definition": flashcards 
[(i*2)+1], "frequency": cardrepeat, "checker": 0
}
  flashcards_dict.append(object)
  random.shuffle(flashcards_dict)

#This splits the dictionaries in the list into 
#sublists of 5 elements
chunking_list = [flashcards_dict[subcount*i:subcount*(i+1)] for i in range(0, sublist)]

#The student developed function below changes 
#the checker value back to 0 and the frequency 
#back to 1 upon the completion of the second set. 
#This is so that the program returns back to the 
#first chunk/flashcard set without the checker 
#holding a value that is indicative of a mastered 
#word [In this case, that value would be 1.]

def list_clear(chunk):
  back_checker = 0
  while True:
    #print("!")
    choice = chunking_list[chunk][random.randrange(len(chunking_list[chunk]))]
    frequency = choice.get("frequency")
    checker = choice.get("checker")
    #print(choice)
    if frequency == 0 and checker == 1:
      checker = 0
      frequency = cardrepeat
      back_checker += 1
      choice.update ({"checker": checker})
      choice.update ({"frequency": frequency})
      print(choice)
    if back_checker == len(chunking_list[chunk]):
      back_checker = 0
      print("Done")
      break
#This student developed function helps set all 
#the terms in the chunk back to original 
#frequency and checker value in order to repeat 
#the entire flashcard set.

def list_clear_clear():
  global chunk
  for i in range(len(chunking_list)):
      chunk = i
      list_clear(chunk)
      
chunk = 0
master_checker = 0
last_master_checker = 0
#print(chunking_list)

#The implementation of Ebbinghaus' fundamental 
#memory curve principles are coded below. Upon 
#the completion of a set, the next set will be 
#started. Upon the completion of that second set, 
#the program will return to the first set. Upon 
#the second completion of that first set, the 
#program will skip to the third set and so on. 

def masterfunction(chunk):
  global master_checker
  global last_master_checker
  global sublist
  global frequency
  global cardrepeat
  global checker
  while True:
    #print("!")
    #print(chunk)
    while not(master_checker == subcount + 1):
      #print("!!")
      #print(master_checker)
      if chunk <= (sublist - 1):
        if master_checker == len(chunking_list[chunk]): 
        #and #frequency == 0:
          #print("!!!")
          master_checker = 0
          print("This Set is Officially Complete")
          print(last_master_checker)
          print(chunk)
          if last_master_checker == 0:
            last_master_checker += 2
            chunk += 1
            #list_clear()
          elif last_master_checker == 1:
            last_master_checker += 1
            chunk += 2
          elif last_master_checker == 2: 
            last_master_checker -= 1
            chunk -=1
            print(chunk)
            list_clear(chunk)
      elif chunk >= (sublist - 1):
        print("You have completed these flashcards!")
        break
      if chunk < sublist: 
        choice = chunking_list[chunk][random.randrange(len(chunking_list[chunk]))]
        #print(choice)
        word = choice.get("word")
        definition = choice.get("definition")
        frequency = choice.get("frequency")
        checker = choice.get("checker")
      if frequency > 0:
        #print("!!!!")
        break
    if frequency > 0: 
      question = str.lower(input("What is the definition of " + word + "?: "))

#selection: checks the frequency of correct 
#questions and quizes the user. Also lets the #
#user restart the learning process

    if chunk < sublist: 
      if question == str.lower(definition):
        print("Correct!")
        if frequency > 0:
          frequency -= 1
          choice.update ({"frequency": frequency})
          #print(master_checker)
      else: 
        print("Incorrect, it is " + "[" + definition + "].")
        if 0 < frequency < cardrepeat:
          frequency += 1
          choice.update ({"frequency": frequency})
      if frequency == 0 and checker == 0:
        #print("!!")
        checker += 1
        master_checker += 1
        choice.update ({"checker": checker})
    if chunk >= (sublist):
      restart = str(input("Would you like to restart this list? (Y/N): "))
      if restart == "Y":
        print("YESSSSSSS")
        chunk = 0 
        master_checker = 0
        last_master_checker = 0
        list_clear_clear()
        #print(chunking_list)
      elif restart == "N":
        print("NOOOO")
        quit()

masterfunction(chunk)
