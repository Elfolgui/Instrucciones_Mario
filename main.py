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

Puntos = Palabra(150, 10, Colores["Blanco"], "ayuda  a  mario  a  llegar  al  poli", 0)

reloj = Controlador.iniciar_reloj()

Lista_Primer_Horacion = ["a", "g", "a", "r", "r", "a", "  ", "l", "a", "s", "  ", "m", "o", "n", "e", "d", "a", "s",
                         "  ", "q", "u", "e", "  ", "p", "u", "e", "d", "a", "s"]

Lista_Segunda_Horacion = ["s", "e", "  ", "e", "l", "  ", "m", "a", "s", "  ", "r", "a", "p", "i", "d", "o",
                          "  ", "e", "n", "  ", "l", "l", "e", "g", "a", "r"]

Lista_Tercera_Horacion = ["m", "a", "t", "a", "  ", "t", "o", "d", "o", "  ", "l", "o", "  ",
                          "q", "u", "e", "  ", "s", "e", "  ", "m", "u", "e", "v", "a"]

Primer_Horacion_texto = ""

Segunda_Horacion_texto = ""

Tercera_Horacion_texto = ""

frames_totales = 0

frames_aux = 0

Primer_Horacion = Palabra(100, 300, Colores["Blanco"], Primer_Horacion_texto, 50)

Segunda_Horacion = Palabra(100, 400, Colores["Blanco"], Segunda_Horacion_texto, 50)

Tercera_Horacion = Palabra(100, 500, Colores["Blanco"], Tercera_Horacion_texto, 50)

posicion_h1 = 0

posicion_h2 = 0

posicion_h3 = 0

frames_escritura = 0

crecimiento = 0

Primera = False

Segunda = False

Tercera = False

aux = True

# Mostrador_Puntos_Habilidad = Palabra(340, 395, Colores["Blanco"], str(Sumador), 60)
#
# Puntuacion_Total = Palabra(740, 45, Colores["Blanco"], str(Puntos_Totales), 80)

while True:
    Controlador.set_fps(reloj, FPS)
    Controlador.buscar_eventos()
    Controlador.rellenar_pantalla(ventana, Colores)
    Base.Grupo.draw(ventana)

    if frames_aux + 1 < frames_totales and crecimiento < 80:
        frames_aux = frames_totales
        Puntos.Aparecer(crecimiento, Colores["Blanco"])
        crecimiento += 1

    if aux and crecimiento >= 80:
        Primera = True
        frames_escritura = frames_totales
        aux = False

    if Primera and frames_escritura + 7 < frames_totales:
        frames_escritura = frames_totales
        Primer_Horacion_texto += Lista_Primer_Horacion[posicion_h1]
        Primer_Horacion.Escritura(Colores["Blanco"], Primer_Horacion_texto)
        posicion_h1 += 1

    if Primera and posicion_h1 >= 29:
        frames_escritura = frames_totales
        Segunda = True
        Primera = False

    if Segunda and frames_escritura + 7 < frames_totales:
        frames_escritura = frames_totales
        Segunda_Horacion_texto += Lista_Segunda_Horacion[posicion_h2]
        Segunda_Horacion.Escritura(Colores["Blanco"], Segunda_Horacion_texto)
        posicion_h2 += 1

    if Segunda and posicion_h2 >= 26:
        frames_escritura = frames_totales
        Segunda = False
        Tercera = True

    if Tercera and frames_escritura + 7 < frames_totales:
        frames_escritura = frames_totales
        Tercera_Horacion_texto += Lista_Tercera_Horacion[posicion_h3]
        Tercera_Horacion.Escritura(Colores["Blanco"], Tercera_Horacion_texto)
        posicion_h3 += 1

    if posicion_h3 >= 25:
        frames_escritura = frames_totales
        Tercera = False

    ventana.blit(Primer_Horacion.Palabra, (Primer_Horacion.posX, Primer_Horacion.posY))
    ventana.blit(Segunda_Horacion.Palabra, (Segunda_Horacion.posX, Segunda_Horacion.posY))
    ventana.blit(Tercera_Horacion.Palabra, (Tercera_Horacion.posX, Tercera_Horacion.posY))
    ventana.blit(Puntos.Palabra, (Puntos.posX, Puntos.posX))
    pygame.display.update()
    frames_totales += 1