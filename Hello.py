print ("Hello You!, ik ben Ties Hogenboom")
print ("Wie ben jij?")
naam = input ()
print("Hello, " + naam)
print("Hier zijn wat vragen over mij:")

ans = input ("In welk jaar ben ik geboren? A 2002 B 2003 C 2004")

if ans == "B":
    print("Dat is correct ik kom uit 2003!")
else :
    print("dit is niet juist")

ans = input ("Welk van deze anime is mijn favoriet? A One Piece B Naruto C God of Highschool")

if ans == "B":
    print("Dat klopt Naruto is mijn favoriet!")
else :
    print("dit is niet juist")

ans = input ("Wat drink ik liever? A Redbull B IceTea C Appelsap")

if ans == "A":
    print("Jup Redbull is erg lekker")
    ans = input("Vind ik de normale RedBull beter dan de andere RedBull smaken? A Ja! B Nee C Even goed")
    if ans == "A":
        print("Natuurlijk!")
    else :
        print("dit is niet juist")
        
elif ans == "B":
    print("Jup IceTea is erg lekker")
    ans = input("Vind ik IceTea beter dan normale thee? A Ja! B Nee C Even goed")
    if ans == "A":
        print("Natuurlijk!")
    else :
        print("dit is niet juist")
else :
    print("dit is niet juist")

