class Heroi:

    def __init__(self, voa, possui_arma, lanca_teia, frase_comum):
        self.voa = voa
        self.possui_arma = possui_arma
        self.lanca_teia = lanca_teia
        self.frase_comum = frase_comum

    def falar(self):
        print(self.frase_comum)

    def detalhar(self):
        if self.voa:
            print("Esse herói voa")
        if self.possui_arma:
            print("Esse herói possui arma")
        if self.lanca_teia:
            print("Esse herói lança teia")


