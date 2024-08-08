class carta:
    diamante="diamante"
    trebol="trevol"
    corazon="corazon"
    picas="picas"
    def __init__(self,pinta,valor):
        self.valor=valor
        self.pinta=pinta
carta1=carta(carta.corazon,7)
carta2=carta(carta.picas,2)
print(carta1.valor,"de",carta1.pinta)
print(carta2.valor,"de",carta2.pinta)



