"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vojtěch Vaněk
email: vojtech.vanek007@gmail.com
discord: Vojtech V.#7369
"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

users={"bob" : "123" , "ann " : "pass123" , "mike" : "password123" , "liz" : "pass123"}
password_correct=False

while not password_correct:
    login_name=input("Insert your name: ")
    password=input("Insert your password: ")

    if users.get(login_name)==password:
        password_correct=True
        print(f"Correct, Hi {login_name}")
        text_type=input("Please select your Text (1-3)")
        if not text_type.isnumeric() or int(text_type) > 3 or int(text_type)<1 :
            print("Worng choice")
            quit()
        else:
            analyze_text=(TEXTS[int(text_type)-1])
            analyze_text=analyze_text.replace("\n"," ")
            analyze_text=analyze_text.lstrip()
            analyze_text=analyze_text.rstrip()
            print(analyze_text)
            word_counter=(analyze_text.split(" "))
            print(f"Number of words in text is: {len(word_counter)}")
            istittle_counter=0
            isupper_counter = 0
            islower_counter = 0
            isdecimal_counter = 0
            sum_list=[]
            word_len=[]
            for word in word_counter:
                word_len.append(len(word))
                if word.istitle():
                    istittle_counter+=1
                if word.isupper():
                    isupper_counter+=1
                if word.islower():
                    islower_counter+=1
                if word.isdecimal():
                    isdecimal_counter += 1
                    sum_list.append(int(word))
            print(f"Number of title words in text is: {istittle_counter}")
            print(f"Number of upper words in text is: {isupper_counter}")
            print(f"Number of lower words in text is: {islower_counter}")
            print(f"Number of decimal words in text is: {isdecimal_counter}")
            print(f"Number of sum of all numbers in text is: {sum(sum_list)}")

            unique_numbers=set(word_len)
            unique_numbers_list=list(unique_numbers)
            for value in (unique_numbers_list):
                amount=word_len.count(value)
                print(f"Len: {value} ","*"*amount)

    else:
        print("Incorrect, Login name or password is wrong.\n Please try it again")