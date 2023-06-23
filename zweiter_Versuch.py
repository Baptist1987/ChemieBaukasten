class Stoffe():
    def __init__(self, reinstoff=None, gemisch=None, name=None):
        self.reinstoff = reinstoff
        self.gemisch = gemisch
        self.name = name


class Gemisch(Stoffe):
    def __init__(self, ist_loesung=None, ist_dispersion=None):
        self.ist_loesung = ist_loesung
        self.ist_dispersion= ist_dispersion

    def weise_name_zu(self):
        self.name = input("Name: ")
        Stoffe.__init__(self, name=self.name)


wasser = Gemisch()

wasser.weise_name_zu()

print(wasser.name)
