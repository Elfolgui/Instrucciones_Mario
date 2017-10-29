from Clases import *

Controlador.iniciar()

Colores = {'Negro': (0, 0, 0), "Blanco": (255, 255, 255), "Verde": (50, 205, 50),
           "Rojo": (178, 34, 34), "Naranja": (255, 165, 0), "Amarillo": (255, 215, 0),
           "Celeste": (0, 255, 255), "Azul": (0, 0, 255)}
#(255, 0, 0)}

ancho, alto = 1360, 720

FPS = 120

ventana = Controlador.configurar_pantalla(ancho, alto)

Controlador.rellenar_pantalla(ventana, Colores)

reloj = Controlador.iniciar_reloj()

Lista_Ayuda = ["a", "y", "u", "d", "a", "  ", "a", "  ", "m", "a", "r", "i","o","  ","a",
                "  ","l","l","e","g","a","r","  ","a","l","  ","p","o","l","i",]

Lista_Primer_Horacion = ["a", "g", "a", "r", "r", "a", "  ", "l", "a", "s", "  ", "m", "o", "n", "e", "d", "a", "s",
                         "  ", "q", "u", "e", "  ", "p", "u", "e", "d", "a", "s"]

Lista_Segunda_Horacion = ["s", "e", "  ", "e", "l", "  ", "m", "a", "s", "  ", "r", "a", "p", "i", "d", "o",
                          "  ", "e", "n", "  ", "l", "l", "e", "g", "a", "r"]

Lista_Tercera_Horacion = ["c", "u", "i", "d", "a", "d", "o", "  ", "c", "o", "n", "  ", "l",
                          "o", "s", "  ", "e", "n", "e", "m", "i", "g", "o", "s"]

Ayuda_Texto = ""

Primer_Horacion_texto = ""

Segunda_Horacion_texto = ""

Tercera_Horacion_texto = ""

frames_totales = 0

frames_aux = 0

Ayuda = Palabra(80, 100, Colores["Blanco"], Ayuda_Texto, 80)

Primer_Horacion = Palabra(80, 300, Colores["Blanco"], Primer_Horacion_texto, 50)

Segunda_Horacion = Palabra(80, 400, Colores["Blanco"], Segunda_Horacion_texto, 50)

Tercera_Horacion = Palabra(80, 500, Colores["Blanco"], Tercera_Horacion_texto, 50)

posicion_Ayuda = 0

posicion_h1 = 0

posicion_h2 = 0

posicion_h3 = 0

frames_escritura = 0

crecimiento = 0

Titulo = True

Primera = False

Segunda = False

Tercera = False

aux = True

while True:
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.rellenar_pantalla(ventana, Colores)

    if Titulo and frames_escritura + 5 < frames_totales:
        frames_escritura = frames_totales
        Ayuda_Texto += Lista_Ayuda[posicion_Ayuda]
        Ayuda.Escritura(Colores["Blanco"], Ayuda_Texto, True)
        posicion_Ayuda += 1

    if posicion_Ayuda >= 30 and aux:
        Primera = True
        frames_escritura = frames_totales
        Titulo = False
        aux = False

    if Primera and frames_escritura + 5 < frames_totales:
        frames_escritura = frames_totales
        Primer_Horacion_texto += Lista_Primer_Horacion[posicion_h1]
        Primer_Horacion.Escritura(Colores["Blanco"], Primer_Horacion_texto, False)
        posicion_h1 += 1

    if Primera and posicion_h1 >= 29:
        frames_escritura = frames_totales
        Segunda = True
        Primera = False

    if Segunda and frames_escritura + 5 < frames_totales:
        frames_escritura = frames_totales
        Segunda_Horacion_texto += Lista_Segunda_Horacion[posicion_h2]
        Segunda_Horacion.Escritura(Colores["Blanco"], Segunda_Horacion_texto, False)
        posicion_h2 += 1

    if Segunda and posicion_h2 >= 26:
        frames_escritura = frames_totales
        Segunda = False
        Tercera = True

    if Tercera and frames_escritura + 5 < frames_totales:
        frames_escritura = frames_totales
        Tercera_Horacion_texto += Lista_Tercera_Horacion[posicion_h3]
        Tercera_Horacion.Escritura(Colores["Blanco"], Tercera_Horacion_texto, False)
        posicion_h3 += 1

    if posicion_h3 >= 24:
        frames_escritura = frames_totales
        Tercera = False

    ventana.blit(Ayuda.Palabra, (Ayuda.posX, Ayuda.posY))
    ventana.blit(Primer_Horacion.Palabra, (Primer_Horacion.posX, Primer_Horacion.posY))
    ventana.blit(Segunda_Horacion.Palabra, (Segunda_Horacion.posX, Segunda_Horacion.posY))
    ventana.blit(Tercera_Horacion.Palabra, (Tercera_Horacion.posX, Tercera_Horacion.posY))
    pygame.display.update()
    frames_totales += 1