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
    svar1 = input("Første spørsmål: Hva er hovedstaden i Norge? ")
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar1.lower() == "oslo":
        print("Det er riktig! Godt jobbet :)")
        poeng +=1
    else:
        print("Beklager, men det er feil svar.")

    #Stiller andre spørsmål
    svar2 = input("Hva heter Norges nest største by? ")
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar2.lower() =="bergen":
        print("Det er riktig! Godt jobbet :)")
        poeng +=1
    else:
        print("Beklager, men det er feil svar.")

    #Stiller andre spørsmål
    svar3 = input("Hva heter det beste fotballaget i Bergen? ")
    #Sjekker om det er rett og gir 1 poeng hvis det er det
    if svar3.lower() == "brann":
        print("Det er riktig! Godt jobbet :)")
        poeng +=1
    else:
        print("Beklager, men det er feil svar.")

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