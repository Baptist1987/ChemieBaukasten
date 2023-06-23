import Ambient

# class Ambient():
#     def __init__(self, temp=None, humidity=None, roomvol=None):
#         self.temp = temp
#         self.humidity = humidity
#         self.roomvol = roomvol
#
#     def temperetaur_verändern(self):
#         temp_delta = int(input("Bitte geben sie die gewünschte temperaturänderung an: "))
#         self.temp = self.temp + temp_delta
#         print(f"Temperatur auf {self.temp}°C geändert")
#         if self.temp <= 0:
#
#     def temperatur_anzeigen(self):
#         print(f"{self.temp}°C")

class Element(Ambient):
    def __init__(self, temp=None, humidity=None,roomvol=20, agrzustand=None, schmelzpunkt=None, siedepunkt=None):
        super().__init__(temp, humidity, roomvol)
        self.agrzustand     =   agrzustand
        self.schmelzpunkt   =   schmelzpunkt
        self.siedepunkt     =   siedepunkt

    def temperetaur_verändern(self):
        x = None
        temp_delta = int(input("Bitte geben sie die gewünschte temperaturänderung an: "))
        self.temp = self.temp + temp_delta
        print(f"Temperatur auf {self.temp}°C geändert")
        if self.temp < x:
            pass


wasser = Element(temp=22,humidity=20,siedepunkt=10)

print(wasser.temp, wasser.humidity)
wasser.temperatur_anzeigen()

wasser.temperetaur_verändern()











''''class Ambient():
    def __init__(self, temp=None, humidity=None, roomvol=None):
        self.temp = temp
        self.humidity = humidity
        self.roomvol = roomvol

class Element(Ambient):
    def __init__(self, temp=20, humidity=40, agrzustand=None, schmelzpunkt=None, siedepunkt=None, dichte=None, eleiter=None, magnetisch=None, radioaktiv=None, roomvol=None):
        super(). __init__(temp=20, humidity=40, agrzustand=None, schmelzpunkt=None, siedepunkt=None, dichte=None, eleiter=None, magnetisch=None, radioaktiv=None, roomvol=None)
        self.agrzustand     =   agrzustand
        self.schmelzpunkt   =   schmelzpunkt
        self.siedepunkt     =   siedepunkt
        self.dichte         =   dichte
        self.eleiter        =   eleiter
        self.magnetisch     =   magnetisch
        self.radioaktiv     =   radioaktiv
        self.roomvol        =   roomvol

    def temp(self, chg_agregatzustand):

        if self.temp < self.schmelzpunkt:
            self.agrzustand = "fest"

Umgebung = Ambient(20,40)
wasser = Element(agrzustand="Flüssig", schmelzpunkt="95")

######
## Ausgabe

print(f"Die Umgebungstemperatur ist {Umgebung.temp}°C und die relative Luftfeuchte beträgt {Umgebung.humidity}%.")
print(f"Der Agregatszustand ist {wasser.agrzustand}.")'''




