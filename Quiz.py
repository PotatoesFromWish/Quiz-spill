#Lists storing the question info
question_1 = ["Første spørsmål: Hva er hovedstaden i Norge? ","oslo"] 
question_2 = ["Hva heter Norges nest største by? ","bergen"]
question_3 = ["Hva heter det beste fotballaget i Bergen? ","brann"]

#List storing the responses
respsons = ["Det er riktig! Godt jobbet :)", "Beklager, men det er feil svar."]

poeng = 0

#Handles what happens when the answer is right
def right_answer():
    print(respsons[0])
    poeng +=1

#Handles what happens when the answer is wrong
def wrong_answer():
    print(respsons[1])

def start_spill():
    """"
    Kjører quiz spillet
    """

    #Sier hei til deg
    print("Velkommen til dette Quiz-spillet!")
    #Ber brukeren om navnet
    navn = input("Hva heter du? ")
    print("Så kjekt at du vil være med " + navn + "!")
    poeng = 0

    #Stiller første spørsmål
    svar1 = input(question_1[0])
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar1.lower() == question_1[1]:
        right_answer()
    else:
        wrong_answer()

    #Stiller andre spørsmål
    svar2 = input(question_2[0])
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar2.lower() ==question_2[1]:
        right_answer()
    else:
        wrong_answer()

    #Stiller andre spørsmål
    svar3 = input(question_3[0])
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar3.lower() == question_3[1]:
        right_answer()
    else:
        wrong_answer()

    #Sier hvordan du gjorde det
    print(f"Gratulerer {navn}! Du fikk {poeng} poeng!")
    #Sjekker hvor mange poeng du fikk og gir deg en rett respons
    if poeng == 3:
        print("Godt jobbet! Du fikk full pott :)")
    elif poeng == 2:
        print("Nokså bra jobbet. Nesten alt riktig :)")
    elif poeng == 1:
        print("Du fikk 1 poeng riktig. Neste gang klarer du nok mer :)")
    elif poeng == 0:
        print("Du fikk ingen riktige, men du har forhåpetligvis lært litt :)")


#Gjør at spillet starter på nytt etter du er ferdig
while True:
    start_spill()