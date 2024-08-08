class cuenta_bancaria:
    def __init__(self,numero_cuenta,propietarios,balance):
        self.numero_cuenta=numero_cuenta
        self.propietarios=propietarios
        self.balance=balance
    def depositar(self,monto):
        self.balance+=monto
    def retirar(self,retiro):
        if self.balance>retiro:
            self.balance -= retiro
    def aplicar_cuota_manejo(self):
        self.balance-= 0.02*self.balance
    def mostrar_detalles(self):
        print("numero de cuenta:",self.numero_cuenta)
        print("propietarios:",self.propietarios)
        print("su balance es:",self.balance)

cuenta_bancaria=cuenta_bancaria(1334,644,6543)
cuenta_bancaria.mostrar_detalles()