import json
import random
import os

#Основные комманды
print("Commands:\n",
      "stop = STOP the words,\n",
      "all = print ALL words in lesson,\n",
      "new = chooses another BOOK with LESSON,\n",
      "add = ADDs difficult words to review,\n",
      "clear = CLEARS the review list,\n",
      "'s' = SKIP the word.\n")

print("From OB L 11 every word is DIFFICULT!\n")

#Открывает JSON
with open(os.getcwd() + "\\Triple_main_shit_book.json", "r+", encoding="utf-8") as f:
    words = json.load(f)

#Переменные
book = ""
lesson = ""

#Для new цикла книг
def choosbook():
    x = str(input("What book: "))
    global book
    if x.upper() == "O" or x.upper() == "ORANGE" or x.upper() == "ORANGE BOOK":
        book = "Orange book"        
    elif x.upper() == "B" or x.upper() == "BLUE" or x.upper() == "BLUE BOOK":
        book = "Blue book"        
    elif x.upper() == "G" or x.upper() == "GREEN" or x.upper() == "GREEN BOOK":
        book = "Green book"
    elif x.upper() == "DF" or x.upper() == "DIFFICULT WORDS" or x.upper() == "D":
        book = "Difficult words"
    elif x.upper() == "H" or x.upper() == "HSK":
        book = "HSK"

#Для new цикла книг
def chooslesson():
    x = str(input("What lesson: "))
    x = x.upper() + " "
    global book, lesson
    for i in words[book].keys():
        if x in i:
            lesson = i
        elif x == "EXTRA " or x == "E ":
            lesson = "Extra"

#Меню выбора, отсек для трех книг
for book in words.keys():
    print(book,"\n")

#Начальный цикл
choosbook()

#Меню выбора, отсек для глав
try:
    for lesson in words[book].keys():
        print(lesson)
    #Начальный цикл
    chooslesson()
except:
    print("Ok")

def add(new):
    global words
    if new not in words["Difficult words"]:
        words["Difficult words"].append(new)
        with open(os.getcwd() + "\\Triple_main_shit_book.json", "w", encoding="utf-8") as f:
            json.dump(words, f, ensure_ascii=False, indent=4)
        print("Shit was added\n")
    else:
        print("Already there\n")

#Для оценки ответа
def right(chosen_book, key, answer, chosen_lesson = ""):
    if answer == "stop":
        global cont
        cont = False
        exit()
    elif answer == "all":
        try:
            for key, value in words[chosen_book][chosen_lesson].items():
                print(key, ":", value)
            print("\n")
        except:
            for dfwords in words["Difficult words"]:
                for key, value in dfwords.items():
                    print(f"{key}: {value}")
    elif answer == "new":
        global book, lesson
        choosbook()
        try:
            for lesson in words[book].keys():
                print(lesson,"\n")
            chooslesson()
        except:
            print("Ok")
        print(f"New book: {book}, New lesson: {lesson}\n")
        pick(book, lesson)
    elif answer == "add" and chosen_lesson != "":
        add({str(key): str(words[chosen_book][chosen_lesson][key])})
    elif answer == "clear":
        words["Difficult words"] = []
        print("Have been cleared")
        with open(os.getcwd() + "\\Triple_main_shit_book.json", "w", encoding="utf-8") as f:
            json.dump(words, f, ensure_ascii=False, indent=4)
    elif answer == str(key[ : key.find(" (")]) or answer == "s":
        print("Correct\n" + str(key) + "\n")
    else:
        print("Wrong\n" + str(key) + "\n")
        answer = str(input("- "))
        right(chosen_book, key, answer, chosen_lesson)

#Основная функция для цикла
def pick(book, lesson):    
    key = random.choice(list(words[book][lesson].keys()))
    print(words[book][lesson][key])
    answer = str(input("- "))
    right(book, key, answer, lesson)

def dfpick():
    dictionary = random.choice(words["Difficult words"])
    key = list(dictionary.keys())[0]
    print(dictionary[key])
    answer = str(input("- "))
    right(book, key, answer)

#Цикл для постоянного подбора вопроса
cont = True
while cont:
    try:
        pick(book, lesson)
    except:
        dfpick()
