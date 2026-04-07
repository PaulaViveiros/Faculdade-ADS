class ContaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        # Dois sublinhados = PRIVADO (Só a mãe mexe na gaveta)
        self.__saldo = saldo_inicial 

    def depositar(self, valor):
        self.__saldo += valor
        print(f"💰 Depósito de R$ {valor} feito para {self.titular}.")

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor
            print(f"✅ Saque de R$ {valor} realizado. Saldo atual: R$ {self.__saldo}")
            return True
        else:
            print(f"❌ Saldo insuficiente para {self.titular}!")
            return False

# AGORA O POLIMORFISMO: A Conta Investimento é "especial"
class ContaInvestimento(ContaBancaria):
    def __init__(self, titular, saldo_inicial, taxa_saque):
        # Chama a mãe para guardar o básico
        super().__init__(titular, saldo_inicial)
        self.taxa_saque = taxa_saque

    # SOBRESCRITA: Vamos mudar o comportamento do saque!
    def sacar(self, valor):
        valor_com_taxa = valor + self.taxa_saque
        print(f"--- Verificando taxas de investimento (R$ {self.taxa_saque}) ---")
        
        # Como o saldo é PRIVADO (__saldo), a filha não pode fazer contas com ele.
        # Ela precisa "pedir" para o método da mãe fazer o serviço:
        return super().sacar(valor_com_taxa)

# --- TESTANDO TUDO ---
if __name__ == '__main__':
    conta_comum = ContaBancaria("Paula", 1000)
    conta_comum.sacar(100)
    
    print("\n" + "="*30 + "\n")
    
    # A conta investimento tem uma taxa de R$ 10 por saque
    conta_inv = ContaInvestimento("Paula Investimentos", 1000, 10)
    conta_inv.sacar(100) # Vai tirar 110 do saldo total!

    # Teste de Saldo Insuficiente
conta_comum = ContaBancaria("Paula", 1000)
conta_comum.sacar(1500) # Tentando sacar mais do que tem!