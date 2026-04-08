class NotificacaoEmail:
    def enviar(self, mensagem):
        print(f"📧 Enviando E-mail: {mensagem}")
        super().enviar(mensagem) # "Próximo da fila, sua vez!"

class NotificacaoSMS:
    def enviar(self, mensagem):
        print(f"📱 Enviando SMS: {mensagem}")
        super().enviar(mensagem) # "Próximo da fila, sua vez!"

class AlertaUrgente(NotificacaoEmail, NotificacaoSMS):
    def enviar(self, mensagem):
        print("🚨 ALERTA DE SEGURANÇA DETECTADO!")
        super().enviar(mensagem)

# --- BLOCO DE TESTE (A "CHAVE" PARA LIGAR O CÓDIGO) ---
if __name__ == '__main__':
    # 1. Criamos o objeto
    meu_alerta = AlertaUrgente()
    
    # 2. Chamamos o método que dispara tudo
    meu_alerta.enviar("Tentativa de login suspeita!")