class Ambient():
    def __init__(self, temp=None, humidity=None, roomvol=None):
        self.temp = temp
        self.humidity = humidity
        self.roomvol = roomvol

    def temperetaur_verändern(self):
        temp_delta = int(input("Bitte geben sie die gewünschte temperaturänderung an: "))
        self.temp = self.temp + temp_delta
        print(f"Temperatur auf {self.temp}°C geändert")


    def temperatur_anzeigen(self):
        print(f"{self.temp}°C")