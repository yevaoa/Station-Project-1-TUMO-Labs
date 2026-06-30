import random
choice = int(input("Choose a storyline (type 0 for first, 1 for second, 2 for third)"))
end = ["what a unique story!","so mysterious!","wow! you are an incredible story teller!"]
template = [1,2,3]

for i in template:
    if choice == 0:
        num = input("Write a number: ")
        time = input("Input a measure of time(days/months/years etc.): ")
        move = input("Input a method of transportation: ")
        adj = input ("Write an adjective: ")
        adj1 = input("And another one right here: ")
        noun = input("Think of any noun: ")
        color = input("Your favourite color: ")
        body = input("Input a body part: ")
        num1 = input("Input a different number now: ")
        noun1 = input("Input a different noun: ")
        noun2 = input("And another one: ")
        body1 = input("Input an other body part: ")
        verb = input("Think of a verb and input here: ")
        noun3 = input("We are not done with nouns yet, type another one again: ")
        adj2 = input("Anotherrrrrrrrrrrrr adjective please: ")
        silly = input("Write down a silly word: ")
        print("\n")
        print("This is the story you've created!\n")
        print(f"It was about {num} {time} ago when I arrived at the hospital in a {move}. The hospital is a/an {adj} place, there are a lot of {adj1} {noun} here. There are nurses here who have {color} {body}. If someone wants to come into my room I told them that they have to {verb} first. I’ve decorated my room with {num1} {noun1}. Today I talked to a doctor and they were wearing a {noun2} on their {body1}. I heard that all doctors {verb} {noun3} every day for breakfast. The most {adj2} thing about being in the hospital is the {silly} {noun} ! ")
        print(random.choice(end))
        break

    elif choice == 1:
        name = input("Input a name: ")
        noun4 = input("Think of a noun: ")
        adj3 = input("Write a feeling: ")
        animal = input("Input any animal: ")
        verb1 = input("Input a verb: ")
        adj4 = input("Write down another feeling: ")
        color1 = input("Input color: ")
        verb2 = input("Now input a verb with -ing ending: ")
        adv = input("An adverb + ly: ")
        num2 = input("Enter a number: ")
        time1 = input("Enter a measure of time(days/weeks/months etc.): ")
        silly1 = input("Enter a silly word: ")
        noun5 = input("Input a noun: ")

        print("\n")
        print("This is the story you've created!\n")
        print(f"This weekend I am going camping with {name}. I packed my lantern, sleeping bag, and {noun4}. I am so {adj3} to {verb1} in a tent. I am {adj4} we might see a(n) {animal}, I hear they’re kind of dangerous. While we’re camping, we are going to hike, fish, and {verb1}. I have heard that the {color1} lake is great for {verb2}. Then we will {adv} hike through the forest for {num2} {time1}. If I see a {color1} {animal} while hiking, I am going to bring it home as a pet! At night we will tell {num2} {silly1} stories and roast {noun5} around the campfire!! ")
        print(random.choice(end))
        break

    elif choice == 2:
        name1 = input("Input a name: ")
        adj5 = input("Write an adjective: ")
        color2 = input("Input a color: ")
        animal1 = input("Input an animal: ")
        place= input("Input a place: ")
        adj6= input("Input a name: ")
        creature= input("Think of a magical creature in plural form: ")
        adj7= input("Input a name: ")
        creature1= input("Input a different magical creature in plural form: ")
        room= input("Enter a room: ")
        noun6= input("Input a noun: ")
        noun7= input("Now enter another noun but in plural form: ")
        noun8= input("And another one (in plural, again): ")
        adj8= input("Input an adjective ")
        noun9= input("Input another noun in plural (yeah, i know): ")
        num3= input("Enter a numberrrrr: ")
        time2= input("Input a measure of time (hours/days/weeks and etc.): ")
        verb3= input("Input a verb with -ing ending: ")
        adj9= input("Input an adjective: ")
        noun10= input("Input the last noun (i promise): ")

        print("\n")
        print("This is the story you've created!\n")
        print (f"Dear {name1}, I am writing to you from a {adj5} castle in an enchanted forest. I found myself here one day after going for a ride on a {color2} {animal1} in {place}. There are {adj6} {creature} and (Adjective3) {creature1} here! In the {room} there is a pool full of {noun6}. I fall asleep each night on a {noun7} of {noun8} and dream of (Adjective4) ( Noun (Plural)4). It feels as though I have lived here for {num3} {time2}. I hope one day you can visit, although the only way to get here now is {verb3} on a {adj7} {noun10}!!")
        print(random.choice(end))
        break


