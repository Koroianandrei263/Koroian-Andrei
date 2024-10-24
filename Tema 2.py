import string
# Declarația unui șir copiat dintr-un articol de știri
sir_articol = """Poliţiştii din cadrul Inspectoratului Judeţean de Poliţie Prahova au fost sesizaţi la data de 16 octombrie a.c. despre faptul că în staţiunea Buşteni, judeţul Prahova, un bărbat de 58 de ani, care îndeplineşte o funcţie de autoritatea publică (primarul Mircea Corbu- n.r.), aflat în exercitarea atribuţiilor de serviciu, a agresat fizic şi verbal o femeie de 36 de ani, ce are calitatea de administrator al unei societăţi comerciale. În continuarea cercetărilor efectuate de către poliţiştii Serviciului de Investigaţii Criminale Prahova sub directa supraveghere şi coordonare a Parchetului de pe lângă Judecătoria Sinaia, referitoare la situaţia prezentată, faţa de bărbatul în cauză a fost dispusă, la data de 24 octombrie a.c., continuarea cercetărilor sub aspectul săvârşirii infracţiunilor de purtare abuzivă, precum şi pentru săvârşirea infracţiunilor de influenţarea declaraţiilor şi instigare la mărturie mincinoasă", informează Inspectoratul Judeţean de Poliţie (IJP) Prahova."""
# Împărțirea șirului în două părți egale
jumatate = len(sir_articol) // 2
prima_parte = sir_articol[:jumatate]
a_doua_parte = sir_articol[jumatate:]
# Procesare prima parte:
# Transformă toate literele în majuscule
prima_parte = prima_parte.upper()
# Elimină toate spațiile goale de la începutul și finalul șirului
prima_parte = prima_parte.strip()
# Procesare a doua parte:
# Inversează ordinea caracterelor
a_doua_parte = a_doua_parte[::-1]
# Transformă prima literă în majusculă
a_doua_parte = a_doua_parte.capitalize()
# Elimină toate caracterele de punctuație (., ,, !, ?) din această parte
a_doua_parte = a_doua_parte.translate(str.maketrans('', '', string.punctuation))
# Combinarea celor două părți
rezultat = prima_parte + a_doua_parte
# Afișarea rezultatului
print(rezultat)
