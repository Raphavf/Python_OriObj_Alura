

class Conta:

    def __init__(self, numero, titular, saldo, limite=1000):
        print("Construindo Objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_para_saque = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_para_saque

    def saca(self, valor_a_sacar):
        if self.__pode_sacar(valor_a_sacar):
            self.__saldo -= valor_a_sacar
        else:
            print("Valor excede o limite!")

    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_numero(self):
        return self.__numero

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite
    @limite.setter
    def limite(self, limite):
        self.__limite = limite
    @staticmethod
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {"bb":"001", 'Caixa':'104', 'Bradesco':'237'}
