class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite


class Cliente:

   def __init__(self, nome):
       self.__nome = nome

   @property
   def nome(self): 
       print("chamando @property nome()")
       return self .__nome.title()
   
   def nome(self, nome):
    print("chamando setter nome()")
    self.__nome = nome

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome


'''>>> from conta import Conta
>>> conta = Conta(123, "Nico", 55.5, 1000.0)
Construindo objeto ... <conta.Conta object at 0x7f82af89d048>
>>> conta2 = Conta(321, "Marcos", 100.0, 1000.0)
Construindo objeto ... <conta.Conta object at 0x7f82af89d400>
>>> conta.transfere(10.0, conta2)
>>> conta.extrato()
Saldo de 45.5 do titular Nico
>>> conta2.extrato()
Saldo de 110.0 do titular Marcos'''