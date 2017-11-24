import Serie

serie1 = Serie.Serie("Serie 1", 7, False, "Género 1", "Autor 1")
serie2 = Serie.Serie("Serie 2", 12, False, "Género 2", "Autor 2")
serie3 = Serie.Serie("Serie 3", 45, False, "Género 3", "Autor 3")
serie4 = Serie.Serie("Serie 4", 9, False, "Género 4", "Autor 4")
serie5 = Serie.Serie("Serie 5", 10, False, "Género 5", "Autor 5")

juego1 = Serie.Videojuego("Juego 1", 4, False, "Género 1", "Compañia 1")
juego2 = Serie.Videojuego("Juego 2", 34, False, "Género 2", "Compañia 2")
juego3 = Serie.Videojuego("Juego 3", 34, False, "Género 3", "Compañia 3")
juego4 = Serie.Videojuego("Juego 4", 67, False, "Género 4", "Compañia 4")
juego5 = Serie.Videojuego("Juego 5", 90, False, "Género 5", "Compañia 5")

juego5.entregar()
serie1.entregar()
serie3.entregar()
serie2.entregar()

listaSeries = [serie1, serie2, serie3, serie4, serie5]
listaJuegos = [juego1, juego2, juego3, juego4, juego5]

seriesEntregadas=0
juegosEntregados=0
nTemporadas=0
nHoras=0
serieConMasTemporadas=""
juegoConMasHoras=""

for e in listaSeries:

    if e.entregado is True:
        seriesEntregadas=seriesEntregadas+1
        print(e.getTitulo()+" entregada.")

    if e.getNTemporadas() > nTemporadas:
        nTemporadas=e.getNTemporadas()
        serieConMasTemporadas=e.getTitulo()


for e in listaJuegos:

    if e.entregado is True:
        juegosEntregadas=juegosEntregados+1
        print(e.getTitulo()+" entregado.")

    if e.getHorasEstimadas() > nHoras:
        nHoras=e.getHorasEstimadas()
        juegoConMasHoras=e.getTitulo()

print("El juego con mas horas es: "+juegoConMasHoras+" con "+str(nHoras)+" horas.")
print("La serie con mas temporadas es: "+serieConMasTemporadas+" con "+str(nTemporadas)+" temporadas.")