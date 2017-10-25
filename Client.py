import socket
from threading import Thread

TCP_IP = 'localhost'
TCP_PORT = 25565
BUFFER_SIZE = 1024


id = ""

def addEnergyEngine(nb):
    global w, id
    w.msg.append("SendPengine,"+id+","+str(nb))

def addEnergyShield(nb):
    global w, id
    w.msg.append("SendPShield,"+id+","+str(nb))

def addEnergyShootSpeed(nb):
    global w, id
    w.msg.append("SendPShoot,"+id+","+str(nb))

def addEnergyShootPower(nb):
    global w, id
    w.msg.append("SendPpuissance,"+id+","+str(nb))


def turn(nb):
    global w, id
    w.msg.append("SendRotate," + id + "," + str(nb))

def shoot():
    global w, id
    w.msg.append("SendShoot,"+id)

def stay():
    global w, id
    w.msg.append("SendStay,"+id)



t = 100
em = 5

def play(game): # codé l'ia dans cette fonction
    global t, em
    if em > 0:
        addEnergyEngine(1)
        addEnergyShootSpeed(1)
        addEnergyShootSpeed(1)
        em -=1
        return
    else:
        if t <= 0:
            turn(5)
            t = 4
        elif t == 1:
            shoot()
            t -=1
        else:
            t-=1
            stay()

    stay()
    stay()




def read(msg):
    global id
    data = msg.split(",")
    if data[0] == "SendPlayerId":
        id = data[1]
    elif data[0] == "SendPlayers":
        playersdata = data[1].split("/")
        players = {}
        missiles = []
        for e in playersdata:
            info = e.split(":")
            if len(info) == 2:
                vd = info[1].split(";")
                vais = (float(vd[0]), float(vd[1]), int(vd[2]) , int(vd[3]), int(vd[4]), int(vd[5]), (float(vd[6]), float(vd[7])), (float(vd[8]), float(vd[9])))
                players[info[0]] = vais

        if len(data) >= 3 and data[2] != "":
            md = data[2].split("/")
            for e in md:
                if e != "":
                    vd = e.split(";")
                    m = ((float(vd[0]), float(vd[1])), (float(vd[2]), float(vd[3])), float(vd[4]))
                    missiles.append(m)
        game = [players,missiles]
        play(game)

class reader(Thread):


    """Thread chargé simplement d'afficher une lettre dans la console."""


    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
        self.stop = False
        self.msg = ""

    def run(self):

        while not self.stop:
            data = self.s.recv(BUFFER_SIZE)
            data = data.decode()
            self.msg += data
            if "\n" in self.msg:
                self.msg = self.msg.replace("\n","")
                read(self.msg)
                self.msg = "";


class writer(Thread):


    """Thread chargé simplement d'afficher une lettre dans la console."""


    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
        self.stop = False
        self.msg = []

    def run(self):

        while not self.stop:
            if len(self.msg) > 0:
                data = self.msg[0]
                self.msg = self.msg[1:]
                data += "\n"
                s.send(data.encode())


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))


w = writer(s)
r = reader(s)

r.start()
w.start()



