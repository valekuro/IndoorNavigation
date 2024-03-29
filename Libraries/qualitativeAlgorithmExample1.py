#file relativo alla piantina iniziale

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

def inserisciMappa():
    room1 = [[(0, 0), (1, 0), (1, 1), (0, 1)]]
    room2 = [[(1, 3), (0, 3), (0, 1), (1, 1)]]
    room3 = [[(1, 3), (1, 5), (0, 5), (0, 3)], [(0.35, 3.35), (0.35, 3.65), (0.65, 3.65), (0.65, 3.35), ]]
    room4 = [[(1, 5), (1, 0), (8, 0), (8, 2),
              (6, 1), (6, 3), (6, 5), (4, 5), (4, 1), (2, 2), (2, 3),
              (2, 5)]]
    room5 = [[(4, 5), (2, 5), (2, 3), (4, 3)]]
    room6 = [[(4, 3), (2, 3), (2, 2), (4, 1)]]
    room7 = [[(6, 3), (6, 1), (8, 2), (8, 3)]]
    room8 = [[(8, 3), (8, 5), (6, 5), (6, 3)], [(6.75, 4.75), (7.25, 4.75), (7.25, 3.25), (6.75, 3.25)]]
    rooms = [room1, room2, room3, room4, room5, room6, room7, room8]

    # room4 = [[(3, 0), (6, 0), (6, 1), (4, 1), (4, 2), (8, 2), (8, 4), (4, 4), (4, 5), (3, 5)]]
    # room1 = [[(6, 0), (8, 0), (8, 2), (6, 2)]]
    #
    # room2 = [[(8, 4), (8, 5), (7, 5), (7, 4)]]
    # room3 = [[(7, 4), (7, 5), (4, 5), (4, 4)]]
    # room5 = [[(1, 2), (3, 2), (3, 5), (1, 5)]]
    # room6 = [[(4, 1), (6, 1), (6, 2), (4, 2)]]
    # room7 = [[(1, 0), (3, 0), (3, 2), (1, 2)]]
    #
    # rooms = [room4, room1, room2, room3, room5, room7, room6]
    return rooms


#function for insert doors
def inserisciPorte():
    doors = [(1.5, -5), (1, -2), (1, -0.5), (1, -4), (4, -4), (4, -2), (6, -4), (6, -2)]
    # doors = [(5, -1), (7, -2), (8, -3), (7.5, -4), (5.5, -4), (3, -3), (3, -1)]
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
    for stanza in nodes_room:
        if len(nodes_room[stanza]) > 1:
            # se ho due elementi è una porta
            num = num + 1
            coordinateStanze.append([stanza, 'Office ' + str(num)])
            plt.text(stanza[0], -stanza[1] + 0.2, 'Office' + str(num), ha="center", va="center", size=10)


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
            #print(p1, p2, p3)
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

                if distanzaCentroCirconferenzaNodo < 1.5 and distanzaCentroCirconferenzaNodo > 0:
                    for nomeStanza in coordinateStanze:
                        if nomeStanza[0] == stanza and stanza != b[0][0] and stanza != a[0][0]:
                            angoloEsegno2 = calcoloAngoloOrientamentoEsegno(p2, p3, stanza)


                            if angoloEsegno2[1] > 0:
                                indicazione = nomeStanza[1] + " on your right"
                            elif angoloEsegno2[1] < 0:
                                indicazione = nomeStanza[1] + " on your left"



                            if angoloEsegno2[0] >= 90:

                                try:
                                    indice = ufficiSuperati.index(nomeStanza[1])
                                    testoNomeStanza = []

                                except ValueError:
                                    ufficiSuperati.append(nomeStanza[1])
                                    if (i < (len(minPath) - 2)):
                                        testoNomeStanza.append(indicazione)
                                break

                            elif angoloEsegno2[0] < 90:
                                mem_next = TRUE;
            textSinonimi = randint(0, 2)
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

            elif angolo > 67.5 and angolo <= 147:
                acc_angolo = angolo
                if segno > 0:
                    aux = ['turn right ', 0, ['']]

                elif segno < 0:
                    aux = ['turn left ', 0, ['']]

            if i == 0:

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

                else:
                    #listaIndicazioni.append(aux)
                    print(angolo)
                    listaIndicazioni = gestioneRettilineiContinui(aux, listaIndicazioni, idx, testoNomeStanza, sinonimiPercorsoLungoDritto, sinonimiPercorsoBreveDritto, textSinonimi)
                    dest = []
                    dest.append(searchOfficeFromPoint(b[0][0]))
                    if angolo > 22.5 and angolo <= 67.5 and mtDec<2:
                        if segno > 0:
                            aux = [dest[0]+' will be on the slightly right', 0, ['']]
                        else:
                            aux = [dest[0]+' will be on the slightly left', 0, ['']]
                    elif angolo > 67.5 and angolo <= 210:
                        if segno > 0:
                            aux = [dest[0]+' will be on the right', 0, ['']]
                        else:
                            aux = [dest[0]+' will be on the left', 0, ['']]
                    else:
                        aux = ['you will find the '+ dest[0] +' in front of you', 0, ['']]

                    listaIndicazioni.append(aux)
    graficaIndicazioni(listaIndicazioni)


def gestioneRettilineiContinui(aux, listaIndicazioni, idx, testoNomeStanza, sinonimiPercorsoLungoDritto, sinonimiPercorsoBreveDritto, textSinonimi):
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
    else:
        listaIndicazioni.append(aux)
    return listaIndicazioni

def graficaIndicazioni(listaIndicazioni):
    # finestra percorso
    window.destroy()
    windowPath = Tk()
    windowPath.title("Route")
    # finestra.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, X, Y))  # anche posizione
    windowPath.geometry("%dx%d+%d+%d" % (600, 400, 800, 200))  # anche posizione
    windowPath.wm_iconbitmap("Icons\corsa.ico")
    Label(windowPath, text='start navigation...', font=("Arial Bold", 15)).grid(row=0, column=1, sticky='nw')
    str_test = ""
    i=0
    for element in listaIndicazioni:
        canv = Canvas(windowPath, width=10, height=10, bg='#FFFFFF')  # (10)
        i=i+1
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
    #plt.plot(b[0][0].x, b[0][0].y, color="red", marker="o", linewidth=1)
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
    office = np.array([['Entrance', Point2(1.50, -5.00)], ['Office1', Point2(1.00, -2.00)],
                       ['Office2', Point2(1.00, -0.50)], ['Office3', Point2(1.00, -4.00)],
                       ['Office4', Point2(4.00, -4.00)], ['Office5', Point2(4.00, -2.00)],
                       ['Office6', Point2(6.00, -4.00)], ['Office7', Point2(6.00, -2.00)]])
    # office = np.array([['Stairs', Point2(5.00, -1.00)], ['room1', Point2(7.00, -2.00)],
    #                    ['Entrance', Point2(8.00, -3.00)], ['Elevator', Point2(7.50, -4.00)],
    #                    ['room2', Point2(5.50, -4.00)], ['room3', Point2(3.00, -3.00)],
    #                    ['room4', Point2(3.00, -1.00)]])
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

def searchOfficeFromPoint(pointOffice):
    print(pointOffice)
    offPos = officePosition()
    for row in offPos:
        if row[1] == pointOffice:
            return row[0]