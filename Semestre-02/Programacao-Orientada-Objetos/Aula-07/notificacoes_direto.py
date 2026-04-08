class NotificacaoEmail:
    def enviar(self, mensagem):
        print(f"📧 [E-mail] Enviando para paula@designer.com: {mensagem}")

class NotificacaoSMS:
    def enviar(self, mensagem):
        print(f"📱 [SMS] Enviando para (11) 99999-9999: {mensagem}")

# O AlertaUrgente herda das duas!
class AlertaUrgente(NotificacaoEmail, NotificacaoSMS):
    def enviar(self, mensagem):
        print("🚨 --- ALERTA DE SEGURANÇA ---")
        
        # Aqui o MRO entra em ação:
        # 1. Ele vai no NotificacaoEmail e executa.
        # 2. Como o Email não tem super(), a corrente pararia aqui...
        # MAS, para o sistema ser perfeito, o ideal é que todos usem super()!
        
        NotificacaoEmail.enviar(self, mensagem)
        NotificacaoSMS.enviar(self, mensagem)
        print("🚨 ---------------------------")

# --- TESTE ---
if __name__ == '__main__':
    aviso = AlertaUrgente()
    aviso.enviar("Alguém tentou acessar sua conta de um novo dispositivo!")