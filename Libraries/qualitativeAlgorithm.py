from Libraries import polyskel
from Libraries.euclid import *
import matplotlib.pyplot as plt
import numpy as np
import networkx as nx
from Libraries.buffer import Buffer_LineSegment2
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from random import *

nodes_room = []
totalpath = []
a = []
b = []
ufficiSuperati = []
coordinateStanze = []
window = Tk()
window.geometry("%dx%d+%d+%d" % (300, 350, 600, 200))
window.wm_iconbitmap("Icons\corsa.ico")


# function for insert the map
def inserisciMappa():
    room1 = [[(2, 0), (2, 5), (0, 5), (0, 0)]]
    room2 = [[(5, 0), (5, 3), (2, 3), (2, 0)]]
    room3 = [[(8, 0), (8, 3), (5, 3), (5, 0)]]
    room4 = [[(9.5, 0), (9.5, 4), (8, 4), (8, 0)]]
    room5 = [[(11.5, 0), (11.5, 4), (9.5, 4), (9.5, 0)]]
    room6 = [[(14, 0), (14, 4), (11.5, 4), (11.5, 0)]]
    room7 = [[(16, 0), (16, 4), (14, 4), (14, 0)]]
    room8 = [[(2, 5), (2, 8), (0, 8), (0, 5)]]
    room9 = [[(2, 8), (2, 11), (0, 11), (0, 8)]]
    room10 = [[(2, 11), (2, 16), (0, 16), (0, 11)]]
    room11 = [[(5, 12), (5, 16), (2, 16), (2, 12)]]
    room12 = [[(8, 12), (8, 16), (5, 16), (5, 12)]]
    room13 = [[(10, 12), (10, 16), (8, 16), (8, 12)]]
    room14 = [[(10, 10.5), (16, 10.5), (16, 16), (10, 16)]]
    room15 = [[(10, 7), (16, 7), (16, 10.5), (10, 10.5)]]
    # room16=[[(3.5,10.5),(3.5,7),(10,7),(10,10.5)]]
    room16 = [[(16, 10.5), (21, 10.5), (21, 16), (16, 16)]]
    room17 = [[(16, 0), (18.5, 0), (18.5, 4), (16, 4)]]
    room18 = [[(18.5, 0), (21, 0), (21, 5), (18.5, 5)]]
    room19 = [[(21, 0), (23.5, 0), (23.5, 5), (21, 5)]]
    room20 = [[(23.5, 0), (26, 0), (26, 4), (23.5, 4)]]
    room21 = [[(26, 0), (28, 0), (28, 4), (26, 4)]]
    room22 = [[(28, 0), (31, 0), (31, 4), (28, 4)]]
    room23 = [[(31, 0), (33, 0), (33, 4), (31, 4)]]
    room24 = [[(33, 0), (35.5, 0), (35.5, 4), (33, 4)]]
    room25 = [[(35.5, 0), (38, 0), (38, 5), (35.5, 5)]]
    room26 = [[(38, 0), (40.5, 0), (40.5, 5), (38, 5)]]
    room27 = [[(40.5, 0), (45.5, 0), (45.5, 4), (40.5, 4)]]
    room28 = [[(45.5, 0), (48, 0), (48, 4), (45.5, 4)]]
    room29 = [[(48, 0), (50, 0), (50, 4), (48, 4)]]
    room30 = [[(50, 0), (53, 0), (53, 3), (50, 3)]]
    room31 = [[(53, 0), (56, 0), (56, 3), (53, 3)]]
    room32 = [[(56, 0), (58, 0), (58, 5), (56, 5)]]
    room33 = [[(56, 5), (58, 5), (58, 8), (56, 8)]]
    room34 = [[(56, 8), (58, 8), (58, 11), (56, 11)]]
    room35 = [[(56, 11), (58, 11), (58, 16), (56, 16)]]
    room36 = [[(56, 16), (53.5, 16), (53.5, 12), (56, 12)]]
    room37 = [[(53.5, 12), (53.5, 16), (51, 16), (51, 12)]]
    room38 = [[(51, 12), (51, 16), (48, 16), (48, 12)]]
    # room39=[[(48,10.5),(48,6.5),(53.5,6.5),(53.5,10.5)]]
    room40 = [[(48, 10.5), (41, 10.5), (41, 7), (48, 7)]]
    # room41=[[(39.5,7),(39.5,10.5),(28,10.5),(28,8.5),(33,8.5),(33,7)]]
    room42 = [[(26, 16), (26, 12), (28, 12), (28, 10.5), (43, 10.5), (43, 16)]]
    # room43=[[(16,10.5),(16,7),(23,7),(23,10.5)]]
    room44 = [[(21, 16), (21, 12), (26, 12), (26, 16)]]
    room45 = [[(43, 16), (43, 10.5), (48, 10.5), (48, 16)]]
    hallway1 = [
        [(2, 12), (2, 3), (3.45, 3), (3.45, 5.5), (6.5, 5.5), (6.5, 3), (8, 3), (8, 4), (16, 4), (16, 7), (3.5, 7),
         (3.5, 10.5), (10, 10.5), (10, 12)]]
    hallway2 = [[(23, 10.5), (23, 7), (28, 7), (28, 12), (21, 12), (21, 10.5)]]
    hallway3 = [[(48, 4), (50, 4), (50, 3), (51.5, 3), (51.5, 5.5), (54.5, 5.5), (54.5, 3), (56, 3), (56, 12), (48, 12),
                 (48, 10.5), (54.45, 10.5), (54.45, 7), (48, 7)]]
    hallway4 = [[(33, 7), (33, 6), (28, 6), (28, 7), (16, 7), (16, 4), (18.5, 4), (18.5, 5),
                 (23.5, 5), (23.5, 4), (35.5, 4), (35.5, 5), (40.5, 5), (40.5, 4), (48, 4), (48, 7)]]
    hallway5 = [[(39.5, 10.5), (39.5, 7), (41, 7), (41, 10.5)]]
    wc = [[(28, 6), (33, 6), (33, 8.5), (28, 8.5)]]
    rooms = [room1, room2, room3, room4, room5, room6, room7, room8, room9, room10, room11, room12, room13, room14,
             room15, room16, room17, room18, room19, room20, room21,
             room22, room23, room24, room25, room26, room27, room28, room29, room30, room31,
             room32, room33, room34, room35, room36, room37, room38, room40,
             room42, room44, room45, hallway1, hallway2, hallway3, hallway4, hallway5, wc]
    return rooms


# function for insert doors
def inserisciPorte():
    doors = [(2, -4), (2.75, -3), (7.25, -3), (9, -4), (11, -4), (12.75, -4), (15.5, -4), (2, -7.5), (2, -8.5),
             (2, -11.5), (3.5, -12), (5.5, -12), (8.5, -12), (12.5, -7), (50, -12), (52, -12), (54, -12), (56, -11.5),
             (56, -8.5), (56, -7.5), (56, -4.5), (55.25, -3), (50.75, -3), (48, -2), (47.5, -4),
             (44, -4), (40.5, -4.5), (35.5, -4.5), (34, -4), (32, -4), (29, -4), (27.5, -4), (24.5, -4),
             (22, -5), (20, -5), (17.5, -4), (28, -6.25), (33, -6.25), (40.25, -6.5), (40.25, -10.5), (48, -11.5),
             (28, -11.5), (25, -12), (25.5, -7), (16, -11.25), (46, -6.5), (16, -6.5), (48, -6.5), (5.5, -5.5),
             (52.5, -5.5), (23, -8),
             (40.25, -7), (46, -7), (21, -11.25)]
    return doors


def startPoint():
    window.title("Indoor Navigation")
    lbl = Label(window, text="Select source:", font=("Arial Bold", 12))
    lbl.place(relx=0.5, rely=0.1, anchor=CENTER)
    comboStart = comboStartEnd(window)
    comboStart.place(relx=0.5, rely=0.2, anchor=CENTER)
    comboStart.bind("<<ComboboxSelected>>", callbackFunc1)
    lb2 = Label(window, text="Select destination:", font=("Arial Bold", 12))
    lb2.place(relx=0.5, rely=0.4, anchor=CENTER)
    comboEnd = comboStartEnd(window)
    comboEnd.place(relx=0.5, rely=0.5, anchor=CENTER)
    comboEnd.bind("<<ComboboxSelected>>", callbackFunc2)
    button = Button(window, text="Calculate Route", command=lambda: test())
    button.place(relx=0.5, rely=0.7, anchor=CENTER)
    auth = Label(window, text="Valentina DOrazio & Andrea Pagliaro", font=("Arial", 4))
    auth.place(relx=0.5, rely=0.9, anchor=CENTER)
    window.mainloop()


# assegnaNomeStanze() -> function that associates the points of the doors with the name of the room corresponding to that door.
# In the following function you assign a random number to the ports.
# If you prefer to enter the name manually for each port, uncomment the next function assegnaNomeStanze() and comment this one
# Edit also officePosition()
def assegnaNomeStanze():
     num = 0
     array_nome_stanza = ['L', 'A','B','C','D','E','F','G','H','I','L','M','N','O','P','Q','R','S','T','U','V','Z','AA','AB','AC','AD','AE','AF',
                          'AG','AH','AI','AL','AM','AN','AO','AP','AQ','AR','AS','AV','AZ','BA','BB','BC','BE','BG','BH','BN','BA','BD','BI','BL','BM',
                          'BF']
     for stanza in nodes_room:
         if len(nodes_room[stanza]) > 1:
             # se ho due elementi è una porta
             num = num + 1
             coordinateStanze.append([stanza, array_nome_stanza[num]])
             plt.text(stanza[0], -stanza[1] + 0.2, array_nome_stanza[num], ha="center", va="center", size=10)


def plotMinPath(minPath, *args):
    if len(minPath) < 2:
        pass
    else:
        for i in range(len(minPath) - 1):
            xs = [minPath[i][0], minPath[i + 1][0]]
            ys = [-minPath[i][1], -minPath[i + 1][1]]
            plt.plot(xs, ys, *args)


def indicazioni(minPath):
    acc_angolo = 0
    mem_next = FALSE
    #print(minPath)
    mem_svolta_stanza = []
    # per trovare l'angolo si utilizza la formula tra vettori: cos(teta)=(uv)/|u|*|v|
    listaIndicazioni = []
    sinonimiPercorsoLungoDritto = ['go straight on for about ', 'still advances for about ', 'still walks for ']
    sinonimiPercorsoBreveDritto = ['take a few steps ', 'advance a little ', 'continue a little ']

    if len(minPath) > 1:

        aux = []
        idx = 0
        if len(minPath) == 2:
            for i in range(len(minPath) - 1):
                xmedio = (minPath[i - 1][0] + minPath[i][0]) / 2
                ymedio = (minPath[i - 1][1] + minPath[i][1]) / 2
                minPath.insert(1, Point2(xmedio, ymedio))

        for i in range(len(minPath) - 2):
            p1 = Point2(minPath[i][0], minPath[i][1])
            p2 = Point2(minPath[i + 1][0], minPath[i + 1][1])
            p3 = Point2(minPath[i + 2][0], minPath[i + 2][1])
            # print("punti")
            print(p1, p2, p3)
            angoloEsegno = calcoloAngoloOrientamentoEsegno(p1, p2, p3)
            angolo = angoloEsegno[0]
            segno = angoloEsegno[1]
            if i == 0 and (angolo >= 0 and angolo <= 67.5):
                mt1 = np.sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2)
                mt2 = np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)
                mt = mt1 + mt2
            else:
                mt = np.sqrt((p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2)

            # arrotondo per togliere misure piccole
            mtDec = int(mt)

            testoNomeStanza = []
            sub = 0
            # raggio della circonferenza = 1 --> valore da impostare a mano
            if mem_next:
                sub = 1
                mem_next = FALSE
            for stanza in nodes_room:
                distanzaCentroCirconferenzaNodo = np.sqrt(
                    (minPath[i + 2 - sub].x - stanza.x) ** 2 + (minPath[i + 2 - sub].y - stanza.y) ** 2)

                if distanzaCentroCirconferenzaNodo < 1.8 and distanzaCentroCirconferenzaNodo > 0:
                    for nomeStanza in coordinateStanze:
                        if nomeStanza[0] == stanza and stanza != b[0][0] and stanza != a[0][0]:
                            angoloEsegno2 = calcoloAngoloOrientamentoEsegno(p2, p3, stanza)
                            if angoloEsegno2[1] > 0:
                                indicazione = nomeStanza[1] + " on your right"
                            elif angoloEsegno2[1] < 0:
                                indicazione = nomeStanza[1] + " on your left"

                            if angoloEsegno2[0] >= 90:
                                # se il nome della stanza già esiste lo mette in indice e non si deve fare l'append.
                                # se indice non esiste, mi torna un'errore con il value errore aggiungo alla lista
                                # delle stanxe da sorpassare, il nome stanza da sorpassare e questo per non far ripetere
                                # le stanze. In pratica faccio l'append solo se va in errore

                                try:

                                    indice = ufficiSuperati.index(nomeStanza[1])
                                    testoNomeStanza = []
                                except ValueError:
                                    ufficiSuperati.append(nomeStanza[1])
                                    if (i < (len(minPath) - 4)):
                                        testoNomeStanza.append(indicazione)
                                break
                            elif angoloEsegno2[0] < 90:
                                mem_next = TRUE;
            textSinonimi = randint(0, 2)
            # print("ANGOLO", angolo)
            if angolo > 22.5:
                angolo = angolo + acc_angolo
            if angolo >= 0 and angolo <= 22.5:
                if angolo != 0:
                    acc_angolo = 0

                if mtDec >= 1.0:
                    aux = [str(sinonimiPercorsoLungoDritto[textSinonimi]), mt, [testoNomeStanza]]
                else:
                    aux = [str(sinonimiPercorsoBreveDritto[textSinonimi]), mt, [testoNomeStanza]]
            elif angolo > 22.5 and angolo <= 67.5:
                acc_angolo = angolo
                if segno > 0:
                    aux = ['turn slightly right ', 0, [testoNomeStanza]]

                elif segno < 0:

                    aux = ['turn slightly left ', 0, [testoNomeStanza]]

            elif angolo > 67.5 and angolo <= 136:
                acc_angolo = angolo
                #print("angolo", angolo)
                #print("acc angolo", acc_angolo)
                if segno > 0:
                    aux = ['turn right ', 0, ['']]

                elif segno < 0:
                    aux = ['turn left ', 0, ['']]

            if i == 0:

                #listaIndicazioni.append(aux)
                #idx = 1
                aux1 = aux
                if ('turn slightly left ' == aux[0]) or (
                        'turn slightly right ' == aux[0]) or ('turn right ' == aux[0]) or (
                        'turn left ' == aux[0]):
                    if mtDec >= 1.0:
                        aux = [str(sinonimiPercorsoLungoDritto[textSinonimi]), mt, [testoNomeStanza]]
                    else:
                        aux = [str(sinonimiPercorsoBreveDritto[textSinonimi]), 0, [testoNomeStanza]]
                    listaIndicazioni.append(aux)
                    idx = 1
                listaIndicazioni.append(aux1)
                idx = idx + 1
            else:
                if i != (len(minPath) - 3):
                    #print(aux)
                    if ((listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto) and (
                            aux[0] in sinonimiPercorsoLungoDritto)) or (
                            (listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and (
                            aux[0] in sinonimiPercorsoBreveDritto)) or (
                            (listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto) and (
                            aux[0] in sinonimiPercorsoBreveDritto)) or (
                            (listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and (
                            aux[0] in sinonimiPercorsoLungoDritto)
                    ):
                        listaIndicazioni[idx - 1][1] = listaIndicazioni[idx - 1][1] + aux[1]
                        if ((listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and (
                                aux[0] in sinonimiPercorsoLungoDritto)) or listaIndicazioni[idx - 1][1] > 1:
                            listaIndicazioni[idx - 1][0] = str(sinonimiPercorsoLungoDritto[textSinonimi])
                        if len(testoNomeStanza) > 0:
                            if len(listaIndicazioni[idx - 1][2][0]) == 0:
                                listaIndicazioni[idx - 1][2] = [testoNomeStanza]
                            else:
                                listaIndicazioni[idx - 1][2].append(testoNomeStanza)
                    elif (aux[0] == 'turn slightly left ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                              0] == 'turn left ') or (
                            aux[0] == 'turn left ' and (listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and
                            listaIndicazioni[idx - 2][0] == 'turn slightly left ') or (
                            aux[0] == 'turn left ' and (listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and
                            listaIndicazioni[idx - 2][0] == 'turn left ') or (
                            aux[0] == 'turn slightly left ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                                0] == 'turn slightly left ') or (
                            aux[0] == 'turn right ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                                0] == 'turn right ') or (
                            aux[0] == 'turn slightly right ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                                0] == 'turn slightly right ') or (
                            aux[0] == 'turn slightly right ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                                0] == 'turn right ') or (
                            aux[0] == 'turn right ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoBreveDritto) and listaIndicazioni[idx - 2][
                                0] == 'turn slightly right '):
                        if mtDec >= 1.0:

                            listaIndicazioni[idx - 1] = [str(sinonimiPercorsoLungoDritto[textSinonimi]), mt,
                                                         [testoNomeStanza]]
                        else:
                            listaIndicazioni[idx - 1] = [str(sinonimiPercorsoBreveDritto[textSinonimi]), mt,
                                                         [testoNomeStanza]]
                        acc_angolo = angolo

                    elif (aux[0] == 'turn slightly left ' and (
                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto)) or (
                            (aux[0] == 'turn left ' and (
                                    listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto)) or (
                                    (aux[0] == 'turn slightly right ' and (
                                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto))) or (
                                    (aux[0] == 'turn right ' and (
                                            listaIndicazioni[idx - 1][0] in sinonimiPercorsoLungoDritto)))
                    ):
                        if mtDec >= 1.0:
                            idx = idx + 1
                            listaIndicazioni.append(
                                      [str(aux[0] + "and " + sinonimiPercorsoLungoDritto[textSinonimi]), mt, [testoNomeStanza]])


                    else:

                        listaIndicazioni.append(aux)
                        idx = idx + 1
                        if ('turn slightly left ' == aux[0]) or ('turn slightly right ' == aux[0]) or (
                                'turn right ' == aux[0]) or ('turn left ' == aux[0]):

                            if mtDec >= 1.0:

                                aux = [str(sinonimiPercorsoLungoDritto[textSinonimi]), mt, [testoNomeStanza]]
                            else:
                                aux = [str(sinonimiPercorsoBreveDritto[textSinonimi]), mt, [testoNomeStanza]]
                            listaIndicazioni.append(aux)
                            idx = idx + 1

                    # qui

                else:
                    listaIndicazioni.append(aux)
                    #print(aux)
                    #print("min - 3")
                    if angolo > 40 and mtDec<2:
                        if segno > 0:
                            aux = ['your destination will be on the right', 0, ['']]
                        else:
                            aux = ['your destination will be on the left', 0, ['']]
                    else:
                        aux = ['you will find the destination in front of you', 0, ['']]

                    listaIndicazioni.append(aux)

    graficaIndicazioni(listaIndicazioni)


def graficaIndicazioni(listaIndicazioni):
    # finestra percorso
    window.destroy()
    windowPath = Tk()
    windowPath.title("Route")
    # finestra.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, X, Y))  # anche posizione
    windowPath.geometry("%dx%d+%d+%d" % (600, 400, 800, 200))  # anche posizione
    windowPath.wm_iconbitmap("Icons\corsa.ico")
    Label(windowPath, text='start navigation... \n', font=("Arial Bold", 15)).grid(row=0, column=1, sticky='nw')
    str_test = ""
    i=0
    for element in listaIndicazioni:
        canv = Canvas(windowPath, width=10, height=10, bg='#FFFFFF')  # (10)
        i=i+1
        print(i)
        newElement = int(element[1])
        if newElement >= 1:
            testoRicostruito = element[0] + str(newElement) + ' mt'
        else:
            testoRicostruito = element[0]

        if element[2][0]:
            for office in range(len(element[2])):
                if office == 0:
                    testoRicostruito = testoRicostruito + ' overcoming ' + str(element[2][office][0])
                else:
                    testoRicostruito = testoRicostruito + ' and ' + str(element[2][office][0])

        str_test = str_test + testoRicostruito
        if element == listaIndicazioni[-1]:
            canv.create_line((10, 0, 10, 400), fill="green", width=10)  # (32)
            canv.grid(row=i, column=0, sticky='w')
            Label(windowPath, text=testoRicostruito + "!", font=("Arial Bold", 15)).grid(row=i, column=1, sticky='nw')
        else:
            canv.create_line((10,0, 10, 400), fill="green", width=10)  # (32)
            canv.grid(row=i, column=0, sticky='w')
            Label(windowPath, text=testoRicostruito, font=("Arial Bold", 10)).grid(row=i, column=1, sticky='nw')
    plt.show()
    windowPath.mainloop()



def calcoloAngoloOrientamentoEsegno(p1, p2, p3):
    v1 = Point2(p2.x - p1.x, p2.y - p1.y)
    u1 = Point2(p3.x - p2.x, p3.y - p2.y)
    dp = v1.x * u1.x + v1.y * u1.y
    n1 = np.sqrt(u1.x * u1.x + u1.y * u1.y)
    n2 = np.sqrt(v1.x * v1.x + v1.y * v1.y)
    calcolo_angolo = dp / (n1 * n2)
    angolo = np.degrees(np.arccos(calcolo_angolo))
    # é la regola della mano destra, si fa il prodotto vettoriale
    # con il segno è possibile capire se il vettore prodotto "esce dal foglio o entra"
    # e quindi in che direzione il vettore è stato ruotato di quei tot gradi
    # Se in senso antiorario è +, in senso orario è -
    segno = v1.x * u1.y - v1.y * u1.x
    return angolo, segno


def test():
    percorso = []
    percorso_2 = []
    if a == b:
        messagebox.showerror("ERROR: ",
                             "The starting point and the arrival point are the same! Unable to calculate a route!")
    else:
        assegnaNomeStanze()
        percorso1 = nx.dijkstra_path(totalpath, a[0][0], b[0][0])

        for u in range(len(percorso1) - 1):
            xP1 = round(percorso1[u].x, 2)
            xP2 = round(percorso1[u + 1].x, 2)
            yP1 = round(percorso1[u].y, 2)
            yP2 = round(percorso1[u + 1].y, 2)
            if xP1 == xP2 and yP1 == yP2:
                pass
            else:
                percorso.append(percorso1[u])
                dst = np.sqrt((xP2 - xP1) ** 2 + (yP2 - yP1) ** 2)
                if dst > 0.2:
                    percorso_2.append(percorso1[u])

                if (len(percorso1) - 2 == u):
                    percorso.append((percorso1[u + 1]))
                    percorso_2.append(percorso1[u + 1])

        plotMinPath(percorso, "r-")
        indicazioni(percorso_2)


def officePosition():
    office = np.array([['A', Point2(2, -4)], ['B',Point2(2.75, -3)], ['C',Point2(7.25, -3)], ['D', Point2(9, -4)], ['E',Point2(11, -4)], ['F',Point2(12.75, -4)],
                       ['G',Point2(15.5, -4)], ['H',Point2(2, -7.5)],
                       ['I',Point2(2, -8.5)], ['L',Point2(2, -11.5)], ['M',Point2(3.5, -12)], ['N',Point2(5.5, -12)], ['O',Point2(8.5, -12)], ['P',Point2(12.5, -7)],
                       ['Q',Point2(50, -12)],
                       ['R',Point2(52, -12)], ['S',Point2(54, -12)], ['T',Point2(56, -11.5)], ['U',Point2(56, -8.5)], ['V',Point2(56, -7.5)],
                       ['Z',Point2(56, -4.5)], ['AA',Point2(55.25, -3)],
                       ['AB',Point2(50.75, -3)], ['AC',Point2(48, -2)], ['AD',Point2(47.5, -4)], ['AE',Point2(44, -4)], ['AF',Point2(40.5, -4.5)],
                       ['AG',Point2(35.5, -4.5)], ['AH',Point2(34, -4)], ['AI',Point2(32, -4)],
                       ['AL',Point2(29, -4)], ['AM',Point2(27.5, -4)], ['AN',Point2(24.5, -4)],['AO',Point2(22, -5)], ['AP',Point2(20, -5)], ['AQ',Point2(17.5, -4)],
                       ['AR',Point2(28, -6.25)], ['AS',Point2(33, -6.25)],
                       ['AT',Point2(40.25, -6.5)], ['AU',Point2(40.25, -10.5)], ['AV',Point2(48, -11.5)],['AZ',Point2(28, -11.5)], ['BA',Point2(25, -12)],
                       ['BB',Point2(25.5, -7)], ['BC',Point2(16, -11.25)],
                       ['BD',Point2(46, -6.5)], ['BE',Point2(16, -6.5)], ['BF',Point2(48, -6.5)], ['BG',Point2(5.5, -5.5)], ['BH',Point2(52.5, -5.5)],
                       ['BI',Point2(23, -8)],['BL',Point2(40.25, -7)], ['BM',Point2(46, -7)],
                       ['BN',Point2(21, -11.25)]])

    return office


def comboStartEnd(window):
    combo = Combobox(window)
    officep = officePosition()
    office = [row[0] for row in officep]
    combo['values'] = (office)
    # combo.current('')  # set the selected item
    return combo


# funzione legata al primo combobox"
def callbackFunc1(event):
    if event:
        startChoose = []
        startChoose.append(searchPointOfOffice(event.widget.get()))
    del a[:]
    a.append(startChoose)


# funzione legata al secondo combobox
def callbackFunc2(event):
    if event:
        endChoose = []
        endChoose.append(searchPointOfOffice(event.widget.get()))
    del b[:]
    b.append(endChoose)


def searchPointOfOffice(officeNumber):
    offPos = officePosition()
    for row in offPos:
        if row[0] == officeNumber:
            return row[1]
