sir_articol="""O șefă dintr-o mare companie de telefonie mobilă nu doar că a scotocit în istoricul convorbirilor telefonice purtate de o clientă, dar le-a și divulgat iubitului acesteia, care încerca să afle astfel dacă este înșelat.

Ilegalitățile au fost descoperite întâmplător, într-un alt caz scandalos de corupție. Angajata companiei și-a recunoscut fapta pentru a scăpa de detenție."""
jumatate = len(sir_articol) // 2
prima_parte = sir_articol[:jumatate]
a_doua_parte = sir_articol[jumatate:]
prima_parte = prima_parte.upper()
prima_parte = prima_parte.strip()
a_doua_parte = a_doua_parte[::-1]
a_doua_parte = a_doua_parte.capitalize()
rezultat = prima_parte + a_doua_parte