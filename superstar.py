#zadeklarovanie premennej, zoznamu a slovnika
hlasy = 0
vypadnuti = []
sutaziaci = {"5220":0,"5221":0,"5222":0,"5223":0,"5224":0,"5225":0,"5226":0,"5227":0,"5228":0,"5229":0}

#otvorenie suborov
subor = open("hlasovanie_1.txt","r")
subor1 = open("hlasovanie_vypadnuti.txt","r")

for riadok in subor: #cyklus na spocitanie hlasov v subore
    hlasy += 1
    riadocek = riadok.strip()
    
    #podmienka na pocitanie hlasov
    if str(riadocek) == "5220":
        sutaziaci["5220"] += 1
    if str(riadocek) == "5221":
        sutaziaci["5221"] += 1
    if str(riadocek) == "5222":
        sutaziaci["5222"] += 1
    if str(riadocek) == "5223":
        sutaziaci["5223"] += 1
    if str(riadocek) == "5224":
        sutaziaci["5224"] += 1
    if str(riadocek) == "5225":
        sutaziaci["5225"] += 1
    if str(riadocek) == "5226":
        sutaziaci["5226"] += 1
    if str(riadocek) == "5227":
        sutaziaci["5227"] += 1
    if str(riadocek) == "5228":
        sutaziaci["5228"] += 1
    if str(riadocek) == "5229":
        sutaziaci["5229"] += 1

#vypisanie pozadovanych hodnot
print("Hlasy:",hlasy,"\n")
print("Súťažiaci 5220 dostal", sutaziaci["5220"], "hlasov.")
print("Súťažiaci 5221 dostal", sutaziaci["5221"], "hlasov.")
print("Súťažiaci 5222 dostal", sutaziaci["5222"], "hlasov.")
print("Súťažiaci 5223 dostal", sutaziaci["5223"], "hlasov.")
print("Súťažiaci 5224 dostal", sutaziaci["5224"], "hlasov.")
print("Súťažiaci 5225 dostal", sutaziaci["5225"], "hlasov.")
print("Súťažiaci 5226 dostal", sutaziaci["5226"], "hlasov.")
print("Súťažiaci 5227 dostal", sutaziaci["5227"], "hlasov.")
print("Súťažiaci 5228 dostal", sutaziaci["5228"], "hlasov.")
print("Súťažiaci 5229 dostal", sutaziaci["5229"], "hlasov.","\n")

#zistenie vypadajuceho a vypisanie
najmensie = min(sutaziaci, key=sutaziaci.get)
print("Najmenej hlasov dostal súťažiaci",najmensie,"\n")

for riadok1 in subor1: #cyklus na vyhodenie vypadnutych zo slovnika
    riadocek1 = riadok1.strip()
    vypadnuti.append(riadocek1)
    del sutaziaci[str(riadocek1)]

#vypisanie vypadnutych
print("Vypadnutí sú súťažiaci:",*vypadnuti,"\n")

#zistenie vypadajuceho a vypisanie bez uz vypadnutych
najmensie1 = min(sutaziaci, key=sutaziaci.get)
print("Najmenej hlasov dostal nevypadnutý súťažiaci",najmensie1,"a vypadáva.")

#zatvorenie suborov
subor.close()
subor1.close()


