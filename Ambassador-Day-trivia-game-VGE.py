print("""
Proj: Ambassador

Trivia quiz to see how much you know of different countries
will include language and facts
out of 52 questions, it will choose 10 of them randomly for you to answer. This is so that each time someone plays, they are different questions
Welcome to Know10, [insert name]! This is a trivia quiz to test how much you know of different countries and their culture! You will be tested on the accuracy of fun facts, language, and cultural norms. Good Luck!

--> This is a game made for the Ambassador Focus Day, to test the knowledge of different countries and other culture related questions. You first need to put your name and if you agree to the game 'terms and conditions', and then start playing! Answer each question with just the answer. NO SENTENCES! While playing the game, be sure to record the amount of right and the amount of wrong answers on a piece of paper to compare with your friends!

""")

mylist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def play_game():
    import random
    x= random.choice(mylist)

# this command will slect a random letter from mylist above    
    while x not in mylist:
        x=random.choice(mylist)
    mylist.remove(x)
# so that the same letter will not be selected twice, and we would have the same question repeated accidentally, the selected letter will be removed from the list while the function is running, so that there is no possibility that it is selected twice
    
#while x is in my list choose again, if x not in my list, append x to list 

    if x=="a":
        ans=input("How many countries does Africa have? (type only the number): ")
        if ans== ("54") or ans== ("54."):
            print ("--> Correct! Africa has 54 countries.")
            print ("\n")
        else:
            print("--> :( Incorrect! ANS: Africa has 54 countries.")
            print("\n")
    if x=="b":
        ans=input("Coffee is grown commercially in Hawaii. True or False?: ")
        if ans== ("True") or ans== ("True.") or ans== ("true") or ans== ("true.") or ans== ("TRUE") or ans== ("TRUE."):
            print("--> Correct! Coffee is grown commercially in Hawaii.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: True. Coffee is grown commercially in Hawaii.")
            print ("\n")
    if x=="c":
        ans=input("What is the second largest religion in the U.S.A? (type only the religion as the answer): ")
        if ans== ("Judaism") or ans== ("judaism") or ans== ("Judaism.") or ans== ("judaism.") or ans== ("JUDAISM") or ans== ("JUDAISM.") or ans== ("JUDAISM!"):
            print("--> Correct! Judaism is the second largest religion in the U.S.A.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: After Christianity, Judaism is the 2nd largest Religion in the U.S.A.")
            print ("\n")
    if x=="d":
        ans=input("90% of the world’s fresh water is located in which continent?: ")
        if ans== ("Antarctica") or ans== ("Antarctica.") or ans== ("antarctica") or ans== ("antarctica.") or ans== ("ANTARCTICA") or ans== ("ANTARCTICA.") or ans== ("ANTARCTICA!"):
            print("--> Correct! 90% of the world’s fresh water is located in Antarctica.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: 90% of the world’s fresh water is located in Antarctica. ")
            print ("\n")
    if x=="e":
        ans=input("Over 200 languages are spoken in Europe. True or False?: ")
        if ans== ("True") or ans== ("true") or ans== ("True.") or ans== ("true.") or ans== ("TRUE.") or ans== ("TRUE!") or ans== ("TRUE"):
            print("--> Correct! Over 200 languages are spoken in Europe. ")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: True. Over 200 languages are spoken in Europe.")
            print ("\n")
    if x=="f":
        ans=input("What is Poland’s national symbol? (Hint: it is the white '_____'): ")
        if ans== ("Eagle") or ans== ("Eagle.") or ans== ("eagle") or ans== ("eagle."):
            print("--> Correct! Poland’s national symbol is the White Eagle.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Poland’s national symbol is the White Eagle.")
            print ("\n")
    if x=="g":
        ans=input("What is the smallest country in Europe?: ")
        if ans== ("Vatican") or ans== ("vatican") or ans== ("Vatican.") or ans== ("vatican.") or ans== ("VATICAN") or ans== ("VATICAN.") or ans== ("VATICAN!"):
            print("--> Correct! The smallest country in Europe is Vatican.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The smallest country in Europe is Vatican. ")
            print ("\n")
    if x=="h":
        ans=input("What is the largest island in the world?: ")
        if ans== ("Greenland") or ans== ("greenland") or ans== ("Greenland.") or ans== ("greenland.") or ans== ("GREENLAND") or ans== ("GREENLAND.") or ans== ("GREENLAND!"):
            print("--> Correct! The largest island in the world is Greenland.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The largest island in the world is Greenland. ")
            print ("\n")
    if x=="i":
        ans=input("Which of the 'Seven Wonders' is located in Egypt?: ")
        if ans== ("The pyramid of giza") or ans== ("the pyramid of giza") or ans== ("The pyramid of giza.") or ans== ("the pyramid of giza.") or ans== ("The Pyramid of Giza") or ans== ("The Pyramid of Giza.") or ans== ("The Pyramid Of Giza") or ans== ("The Pyramid Of Giza.") or ans== ("Pyramid Of Giza") or ans== ("Pyramid Of Giza.") or ans== ("Pyramid of Giza") or ans== ("Pyramid of Giza.") or ans== ("Pyramid of giza") or ans== ("Pyramid of giza.") or ans== ("pyramid of giza") or ans== ("pyramid of giza."):
            print("--> Correct! The Pyramid of Giza is one of the 'seven wonders' and is located in Egypt.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The Pyramid of Giza is one of the 'seven wonders' and is located in Egypt. ")
            print ("\n")
    if x=="j":
        ans=input("What is the official animal of Scotland?: ")
        if ans== ("The unicorn") or ans== ("the unicorn") or ans== ("a unicorn") or ans== ("A unicorn") or ans== ("The unicorn.") or ans== ("the unicorn.") or ans== ("Unicorn") or ans== ("unicorn") or ans== ("Unicorn.") or ans== ("unicorn."):
            print("--> Correct! The official animal of Scotland is the unicorn. Wow!")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The official animal of Scotland is the unicorn. ")
            print ("\n")
    if x=="k":
        ans=input("People of which island created the Piña Colada?: ")
        if ans== ("From Puerto Rico") or ans== ("from puerto rico") or ans== ("From puerto rico") or ans== ("from Puerto Rico") or ans== ("puerto rico") or ans== ("Puerto Rico") or ans== ("From Puerto Rico.") or ans== ("from puerto rico.") or ans== ("From puerto rico.") or ans== ("from Puerto Rico.") or ans== ("Puerto Rico.") or ans== ("puerto rico.") or ans== ("Of puerto rico") or ans== ("Of puerto rico.") or ans== ("of puerto rico") or ans== ("of puerto rico.") or ans== ("of Puerto rico") or ans== ("of Puerto rico.") or ans== ("of Puerto Rico") or ans== ("of Puerto Rico.") or ans== ("Of Puerto Rico") or ans== ("Of Puerto Rico.") or ans== ("Of Puerto rico") or ans== ("Of Puerto rico."):
            print("--> Correct! The people of Puerto Rico created the Piña Colada.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The people of Puerto Rico created the Piña Colada. ")
            print ("\n")
    if x=="l":
        ans=input("How many STOP signs are in all of Paris? (enter the number): ")
        if ans== ("1") or ans== ("1.") or ans== ("1 stop sign") or ans== ("1 Stop sign") or ans== ("1 STOP sign") or ans== ("1.") or ans== ("1 stop sign.") or ans== ("1 Stop sign.") or ans== ("1 STOP sign.") or ans== ("one") or ans== ("one.") or ans== ("one stop sign") or ans== ("One stop sign") or ans== ("One STOP sign") or ans== ("one stop sign.") or ans== ("One stop sign.") or ans== ("one STOP sign."):
            print("--> Correct! There is only 1 STOP sign.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: There is only 1 STOP sign. ")
            print ("\n")
    if x=="m":
        ans=input("The tallest building in the world - Burj Khalifa - is located WHERE?: ")
        if ans== ("Dubai") or ans== ("dubai") or ans== ("Dubai.") or ans== ("dubai.") or ans== ("In dubai") or ans== ("In Dubai") or ans== ("in dubai") or ans== ("in Dubai") or ans== ("In dubai.") or ans== ("In Dubai.") or ans== ("in dubai.") or ans== ("in Dubai."):
            print("--> Correct! The tallest building in the world - Burj Khalifa - is located in Dubai, which stands at a towering 2717 feet in height!")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The tallest building in the world - Burj Khalifa - is located in Dubai, which stands at a towering 2717 feet in height. ")
            print ("\n")
    if x=="n":
        ans=input("It is illegal to name your pig Napoleon in France. True or False?: ")
        if ans== ("True") or ans== ("True.") or ans== ("true") or ans== ("true."):
            print("--> Correct! It is, in fact, illegal to name your pig 'Napoleon' in France!")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Truth. It is, in fact, illegal to name your pig 'Napoleon' in France.")
            print ("\n")
    if x=="o":
        ans=input("The Olympic Games originated in which ancient country?: ")
        if ans== ("Greece") or ans== ("Greece.") or ans== ("greece") or ans== ("greece.") or ans== ("Ancient greece") or ans== ("Ancient greece.") or ans== ("ancient greece") or ans== ("ancient greece.") or ans== ("ancient Greece") or ans== ("ancient Greece.") or ans== ("Ancient Greece") or ans== ("Ancient Greece."):
            print("--> Correct! The Olympic Games originated in Ancient Greece.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The Olympic Games originated in Ancient Greece.")
            print ("\n")
    if x=="p":
        ans=input("The two main languages spoken in Canada are English and ______. Fill in the blank: ")
        if ans== ("French") or ans== ("French.") or ans== ("french") or ans== ("french."):
            print("--> Correct! The two main languages spoken in Canada are English and French.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The two main languages spoken in Canada are English and French.")
            print ("\n")
    if x=="q":
        ans=input("What is Pakistan's most popular sport?: ")
        if ans== ("Cricket") or ans== ("Cricket.") or ans== ("cricket.") or ans== ("cricket"):
            print("--> Correct! Cricket is the most popular sport in Pakistan.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Cricket is the most popular sport in Pakistan.")
            print ("\n")
    if x=="r":
        ans=input("The capital and largest city in the Netherlands is ______. Fill in the blank (Hint: This is also the name of an 'Imagine Dragons' song): ")
        if ans== ("Amsterdam") or ans== ("Amsterdam.") or ans== ("amsterdam") or ans== ("amsterdam."):
            print("--> Correct! The capital and largest city in the Netherlands is Amsterdam. Pat yourself on the back if you've listened to the song before :)")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The capital and largest city in the Netherlands is Amsterdam (The song is pretty good too).")
            print ("\n")
    if x=="s":
        ans=input("______ and ______ are popular sports in Turkey. Fill in the blank (Write your full answer in this exact format:'1st answer, 2nd answer'): ")
        if ans== ("Basketball, Volleyball") or ans== ("basketball, volleyball") or ans== ("Volleyball, Basketball") or ans== ("volleyball, basketball") or ans== ("Basketball, Volleyball.") or ans== ("basketball, volleyball.") or ans== ("Volleyball, Basketball.") or ans== ("volleyball, basketball."):
            print("--> Correct! Both basketball and volleyball are popular sports in Turkey.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Both basketball and volleyball are popular sports in Turkey.")
            print ("\n")
    if x=="t":
        ans=input("Siamese cats originated in ______, where they are called 'Wichian Mat'. Fill in the blank: ")
        if ans== ("Thailand") or ans== ("Thailand.") or ans== ("thailand") or ans== ("thailand."):
            print("--> Correct! Siamese cats originated in Thailand, where they are called 'Wichian Mat'.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Siamese cats originated in Thailand, where they are called 'Wichian Mat'.")
            print ("\n")
    if x=="u":
        ans=input("What is the national symbol of Thailand?: ")
        if ans== ("The elephant") or ans== ("The elephant.") or ans== ("The Elephant.") or ans== ("The Elephant") or ans== ("the elephant") or ans== ("the elephant.") or ans== ("Elephant") or ans== ("Elephant.") or ans== ("elephant") or ans== ("elephant.") or ans== ("An elephant") or ans== ("An elephant.") or ans==("An Elephant") or ans==("An Elephant.") or ans==("an elephant") or ans==("an elephant."):
            print("--> Correct! Thailand's national symbol is the elephant. A century ago there were 100,000 elephants in the country, now there are just an estimated 2,000 left in the wild.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Thailand's national symbol is the elephant. A century ago there were 100,000 elephants in the country, now there are just an estimated 2,000 left in the wild.")
            print ("\n")
    if x=="v":
        ans=input("At the Olympics, _____ is Ireland's most successful sport. Fill in the blank: ")
        if ans== ("Boxing") or ans== ("Boxing.") or ans== ("boxing") or ans== ("boxing."):
            print("--> Correct! At the Olympics, boxing is Ireland's most successful sport.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: At the Olympics, boxing is Ireland's most successful sport.")
            print ("\n")
    if x=="w":
        ans=input("The potato is native to the southern area of what is now modern day ______. Fill in the blank: ")
        if ans== ("Peru") or ans== ("Peru.") or ans== ("peru") or ans== ("peru."):
            print("--> Correct! The potato is native to the southern area of what is now modern day Peru.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The potato is native to the southern area of what is now modern day Peru.")
            print ("\n")
    if x=="x":
        ans=input("Which country is one of the most stable and prosperous nations in South America?: ")
        if ans== ("Chile") or ans== ("Chile.") or ans== ("chile") or ans== ("chile."):
            print("--> Correct! Chile is one of the most stable and prosperous nations in South America.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Chile is one of the most stable and prosperous nations in South America.")
            print ("\n")
    if x=="y":
        ans=input("What is the world's most populous island?: ")
        if ans== ("The Island of Java") or ans== ("The Island of Java.") or ans== ("The Island Of Java") or ans== ("The Island Of Java.") or ans== ("the Island of Java") or ans== ("the Island of Java.") or ans== ("the island of java") or ans== ("the island of java.") or ans== ("The island of java") or ans== ("The island of java.") or ans==("The island of Java") or ans==("The island of Java.") or ans==("Island of Java") or ans==("Island of Java.") or ans==("Island of java") or ans==("Island of java.") or ans==("island of java") or ans==("island of java.") or ans==("Java island") or ans==("Java island.") or ans==("Java Island") or ans==("Java Island.") or ans==("java island") or ans==("java island."):
            print("--> Correct! The world's most populous island is Java, which is home to 60% of the country's population (around 130 million people)!")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The world's most populous island is Java, which is home to 60% of the country's population (around 130 million people)!")
            print ("\n")
    if x=="z":
        ans=input("Author and poet Hans Christian Andersen, who wrote notable fairy tales such as 'The Emperor's New Clothes', 'The Little Mermaid' and 'The Ugly Duckling', was from what country?: ")
        if ans== ("Denmark") or ans== ("Denmark.") or ans== ("denmark") or ans== ("denmark."):
            print("--> Correct! Danish author and poet Hans Christian Andersen is from Denmark.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Danish author and poet Hans Christian Andersen is from Denmark.")
            print ("\n")
    if x=="A":
        ans=input("'LEGO' was invented in _____. Fill in the blank (Hint: Legoland and the company headquarters are located in Billund, on the Jutland peninsula): ")
        if ans== ("Denmark") or ans== ("Denmark.") or ans== ("denmark") or ans== ("denmark."):
            print("--> Correct! LEGO was invented in Denmark. Legoland and the company headquarters are located in Billund, on the Jutland peninsula.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: LEGO was invented in Denmark. Legoland and the company headquarters are located in Billund, on the Jutland peninsula.")
            print ("\n")
    if x=="B":
        ans=input("The lemur is only found in the wild in which island?: ")
        if ans== ("Madagascar") or ans== ("Madagascar.") or ans== ("madagascar") or ans== ("madagascar."):
            print("--> Correct! The lemur is only found in the wild in Madagascar. As of 2012, there were 103 living species of lemur in Madagascar, including sub-species.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The lemur is only found in the wild in Madagascar. As of 2012, there were 103 living species of lemur in Madagascar, including sub-species.")
            print ("\n")
    if x=="C":
        ans=input("Finland's nickname for the country is 'Land of the Thousand _____'. Fill in the blank: ")
        if ans== ("Lakes") or ans== ("Lakes.") or ans== ("lakes") or ans== ("lakes."):
            print("--> Correct! Finland's nickname for the country is 'Land of the Thousand Lakes', since it has thousands of lakes (about 188,000) and islands (about 179,500).")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Finland's nickname for the country is 'Land of the Thousand Lakes', since it has thousands of lakes (about 188,000) and islands (about 179,500).")
            print ("\n")
    if x=="D":
        ans=input("The national sport of Finland is called Pesapallo, which is similar to what sport?: ")
        if ans== ("Baseball") or ans== ("Baseball.") or ans== ("baseball") or ans== ("baseball."):
            print("--> Correct! The national sport of Finland, Pesapallo, is similar to baseball.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The national sport of Finland, Pesapallo, is similar to baseball.")
            print ("\n")
    if x=="E":
        ans=input("Is the game of dominoes extremely popular in Cuba? Yes or no: ")
        if ans== ("Yes") or ans== ("Yes.") or ans== ("yes") or ans== ("yes."):
            print("--> Correct! The game of dominoes is extremely popular in Cuba.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The game of dominoes is extremely popular in Cuba.")
            print ("\n")
    if x=="F":
        ans=input("There are three official languages in Belgium. True or False?: ")
        if ans== ("True") or ans== ("True.") or ans== ("true") or ans== ("true."):
            print("--> Correct! There are three official languages in Belgium: Dutch (spoken by just under 60% of the population), French (spoken by around 40% of the population and mainly to the south in the Wallonia region), and there is a small group of German-speakers in eastern Wallonia.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: There are three official languages in Belgium: Dutch (spoken by just under 60% of the population), French (spoken by around 40% of the population and mainly to the south in the Wallonia region), and there is a small group of German-speakers in eastern Wallonia.")
            print ("\n")
    if x=="G":
        ans=input("French fries are believed to have been invented in _______. Fill in the blank: ")
        if ans== ("Belgium") or ans== ("Belgium.") or ans== ("belgium") or ans== ("belgium."):
            print("--> Correct! French fries are believed to have been invented in Belgium, not France.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: French fries are believed to have been invented in Belgium, not France.")
            print ("\n")
    if x=="H":
        ans=input("Belgium has more movie makers per square km than any other country in the world. True or False?: ")
        if ans== ("False") or ans== ("False.") or ans== ("false") or ans== ("false."):
            print("--> Correct! Belgium has more *comic* makers per square km than any other country in the world. Famous comic book series to come out of Belgium include The Adventures of Tintin, The Smurfs, and Asterix (originally a French creation for French-Belgian audiences).")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Belgium has more *comic* makers per square km than any other country in the world. Famous comic book series to come out of Belgium include The Adventures of Tintin, The Smurfs, and Asterix (originally a French creation for French-Belgian audiences).")
            print ("\n")
    if x=="I":
        ans=input("Does Malaysia have a national drink? Yes or No: ")
        if ans== ("Yes") or ans== ("Yes.") or ans== ("yes") or ans== ("yes."):
            print("--> Correct! The national drink of Malaysia is a hot milk tea called Teh tari.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The national drink of Malaysia is a hot milk tea called Teh tari.")
            print ("\n")
    if x=="J":
        ans=input("India has the third largest population in the world. True or False?: ")
        if ans== ("False") or ans== ("False.") or ans== ("false") or ans== ("false."):
            print("--> Correct! India has the *second* largest population in the world, with over 1.2 billion people (1,205,073,612 as of July 2012).")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: India has the *second* largest population in the world, with over 1.2 billion people (1,205,073,612 as of July 2012).")
            print ("\n")
    if x=="K":
        ans=input("Ancient warriors of Japan were known as ______. Fill in the blank: ")
        if ans== ("Samurai") or ans== ("Samurai.") or ans== ("samurai") or ans== ("samurai."):
            print("--> Correct! Ancient warriors of Japan were known as Samurai. They were very skilled fighters and swordsmen. Their main weapon was the Katana, a sharp sword with a slight curve to it.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Ancient warriors of Japan were known as Samurai. They were very skilled fighters and swordsmen. Their main weapon was the Katana, a sharp sword with a slight curve to it.")
            print ("\n")
    if x=="L":
        ans=input("Due to gases produced by power plants, Japan sometimes suffers from ____ rain. Fill in the blank: ")
        if ans== ("Acid") or ans== ("Acid.") or ans== ("acid") or ans== ("acid.") or ans== ("acidic") or ans== ("Acidic") or ans== ("acidic.") or ans== ("Acidic."):
            print("--> Correct! Due to gases produced by power plants, Japan sometimes suffers from acid rain.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Due to gases produced by power plants, Japan sometimes suffers from acid rain.")
            print ("\n")
    if x=="M":
        ans=input("What is the Spanish name for 'Spain'? (spelling and accents need to be correct!): ")
        if ans== ("España") or ans== ("España.") or ans== ("españa") or ans== ("españa."):
            print("--> Correct! The Spanish name for 'Spain' is 'España'.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The Spanish name for 'Spain' is 'España'.")
            print ("\n")
    if x=="N":
        ans=input("Russia is located across how many time zones? (Type just the number!): ")
        if ans== ("nine") or ans== ("nine.") or ans== ("Nine") or ans== ("Nine.") or ans==("9") or ans==("9."):
            print("--> Correct! Russia is located across 9 time zones.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Russia is located across 9 time zones.")
            print ("\n")
    if x=="O":
        ans=input("The world’s second satellite was launched by the Soviet Union. True or False?: ")
        if ans== ("False") or ans== ("False.") or ans== ("false") or ans== ("false."):
            print("--> Correct! The world's *first* satellite, named Sputnik, was launched by the Soviet Union in 1957.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The world's *first* satellite, named Sputnik, was launched by the Soviet Union in 1957.")
            print ("\n")
    if x=="P":
        ans=input("In 1893, _____ became the first country in the world to give all women the right to vote. Fill in the blank: ")
        if ans== ("New Zealand") or ans== ("New Zealand.") or ans== ("new zealand") or ans== ("new zealand.") or ans== ("New zealand") or ans== ("New zealand."):
            print("--> Correct! In 1893, New Zealand became the first country in the world to give all women the right to vote.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: In 1893, New Zealand became the first country in the world to give all women the right to vote.")
            print ("\n")
    if x=="Q":
        ans=input("Which country shares Lake Victoria, the world's second largest freshwater lake, with Tanzania and Uganda? (Hint: it begins with 'k'): ")
        if ans== ("Kenya") or ans== ("Kenya.") or ans== ("kenya") or ans== ("kenya."):
            print("--> Correct! Kenya shares Lake Victoria, the world's second largest freshwater lake, with Tanzania and Uganda.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Kenya shares Lake Victoria, the world's second largest freshwater lake, with Tanzania and Uganda.")
            print ("\n")
    if x=="R":
        ans=input("Argentine cartoonist Quirino Cristiani made and released the world's first or second two animated feature films?: ")
        if ans== ("First") or ans== ("First.") or ans== ("first") or ans== ("first."):
            print("--> Correct! Argentine cartoonist Quirino Cristiani made and released the world's first two animated feature films in 1917 and 1918.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Argentine cartoonist Quirino Cristiani made and released the world's first two animated feature films in 1917 and 1918.")
            print ("\n")
    if x=="S":
        ans=input("Reggae music originated from which island/country?: ")
        if ans== ("Jamaica") or ans== ("Jamaica.") or ans== ("jamaica") or ans== ("jamaica.") or ans== ("From jamaica") or ans== ("From jamaica.") or ans== ("From Jamaica") or ans== ("From Jamaica.") or ans== ("from Jamaica") or ans==("from Jamaica") or ans==("from jamaica") or ans==("from jamaica"):
            print("--> Correct! Reggae music originated from Jamaica, home of well known musician Bob Marley.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Reggae music originated from Jamaica, home of well known musician Bob Marley.")
            print ("\n")
    if x=="T":
        ans=input("Which country is home to the world's longest road tunnel?: ")
        if ans== ("Norway") or ans== ("Norway.") or ans== ("norway") or ans== ("norway."):
            print("--> Correct! Norway is home to the world's longest road tunnel. With a length of 24.5 km's (15.3 miles), the tunnel has become a tourist attraction in itself.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Norway is home to the world's longest road tunnel. With a length of 24.5 km's (15.3 miles), the tunnel has become a tourist attraction in itself..")
            print ("\n")
    if x=="U":
        ans=input("The name 'Argentina' comes from the ______ word for sliver, which is 'argentum'. Fill in the blank (Hint: it's a language): ")
        if ans== ("Latin") or ans== ("Latin.") or ans== ("latin") or ans== ("latin."):
            print("--> Correct! The name Argentina comes from the Latin word for sliver 'argentum'.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The name Argentina comes from the Latin word for sliver 'argentum'.")
            print ("\n")
    if x=="V":
        ans=input("Where was IKEA founded?: ")
        if ans== ("Sweden") or ans== ("Sweden.") or ans== ("sweden") or ans== ("sweden."):
            print("--> Correct! A number of prominent manufacturing and technology company's were founded in Sweden, including IKEA.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: A number of prominent manufacturing and technology company's were founded in Sweden, including IKEA.")
            print ("\n")
    if x=="W":
        ans=input("The official languages of Morocco are Berber and _____. Fill in the blank: ")
        if ans== ("Arabic") or ans== ("Arabic.") or ans== ("arabic") or ans== ("arabic."):
            print("--> Correct! The official languages of Morocco are Berber and Arabic.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The official languages of Morocco are Berber and Arabic.")
            print ("\n")
    if x=="X":
        ans=input("The world's tallest waterfall, Angel Falls, is located in what country?: ")
        if ans== ("Venezuela") or ans== ("Venezuela.") or ans== ("venezuela") or ans== ("venezuela."):
            print("--> Correct! The world's tallest waterfall, Angel Falls, is located in Venezuela.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The worlds tallest waterfall, Angel Falls, is located in Venezuela.")
            print ("\n")
    if x=="Y":
        ans=input("What is Venezuela's most popular sport?: ")
        if ans== ("Baseball") or ans== ("Baseball.") or ans== ("baseball") or ans== ("baseball."):
            print("--> Correct! Baseball is Venezuela's most popular sport. There has been a professional baseball league in the country since 1945.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: Baseball is Venezuela's most popular sport. There has been a professional baseball league in the country since 1945.")
            print ("\n")
    if x=="Z":
        ans=input("The national animal of Bangladesh is the endangered Royal Bengal ______. Fill in the blank: ")
        if ans== ("Tiger") or ans== ("Tiger.") or ans== ("tiger") or ans== ("tiger."):
            print("--> Correct! The national animal of Bangladesh is the endangered Royal Bengal Tiger.")
            print ("\n")
        else: 
            print("--> :( Incorrect! ANS: The national animal of Bangladesh is the endangered Royal Bengal Tiger.")
            print ("\n")
#all these 'if statements' are to associate the selected letter with a question; converting it into a variable, in a way. So if the selected letter is 'a' for example, it would be associated with a certain question. If it was 'b' then it would be a different question.
#in the 'if statements', there is another if/else statement, to check if the input is the correct answer. 
#this is all first since it's all part of a function (play_game ())
name= input("Welcome to Know10! Enter your name: ")
print("Welcome to Know10,",name,"! This is a trivia quiz to test how much you know of different countries and their culture! You will be tested on the accuracy of fun facts, language, and cultural norms. Be sure to have a piece of paper with you to keep score of how many questions you get right. Good Luck!")
print("RULES: Be a good team player. Do not cheat when taking this quiz; this is just for fun. There will be some questions that you will not know the answer to, so just guess! The most important thing about this game is to learn more about other countries. When answering the questions, DO NOT PUT IT IN COMPLETE SENTENCES. Just answer the question with the precise answer. Lastly, take this quiz in a respectful manner!")
#these are the rules. If they comply, then they can continue the game. If not, then the game will stop entirely. 
agr= input("Do you agree with these terms? Yes or No: ")
if agr==("Yes") or agr==("yes") or agr==("Yes.") or agr==("yes."):
    print ("Good answer!")
    print ("\n")
    for i in range(10):
       play_game ()
    print ("\n")
    print("Thanks for playing! Make sure to count up your correct answers, write them down, and compare them with your friends! Hope you had fun playing Know10 :)")
#the for loop is for the function process to happen 10 times, hence the name (Know10). Clever, right? And after ten random questions are printed, the game ends with a nice conclusion and a happy face :) 
else:
    print ("\n")
    print (":(")

#sources: https://www.uselessdaily.com/world/23-interesting-facts-about-different-countries/#.XeHqv-dKiqB; https://www.omniglot.com/language/articles/10culturaldifferences.htm; https://www.holidayguru.ie/travel-magazine/fun-facts-about-countries/; http://www.sciencekids.co.nz/sciencefacts/countries.html

