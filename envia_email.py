import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

##Classe para envio de e-mails, poderá ser utilizada em vários projetos.
##Feito por Victor Smirnov, uso comercial livre, contanto que deem créditos.
##Contato: philipesan123@hotmail.com

##Classe que realiza envio de e-mails
class enviaEmail:
    def __init__(self, servidor_smtp, porta, conta, senha):
        self.carta = MIMEMultipart()
        self.servidor_smtp = servidor_smtp
        self.porta = porta
        self.carta['From'] = conta
        self.senha = senha


##Este método conecta no servidor SMTP
    def conecta_login(self):
        try:
            self.servidor = smtplib.SMTP(self.servidor_smtp, self.porta)
            self.servidor.starttls()
            self.servidor.login(self.carta['From'], self.senha)
            return True
        except Exception as e:
            print(e)
            return(e)
##Este método envia os E-mails
    def envia_email(self, destinatarios: list, assunto, mensagem, cc = [], cco = []):
        self.carta['To'] = ", ".join(destinatarios)
        if (cc):
            self.carta['CC'] = ", ".join(cc)
        if (cco):
            self.carta['Bcc'] = ", ".join(cco)
        self.carta['Subject'] = assunto
        self.carta.attach(MIMEText(mensagem, 'plain'))
        try:
            self.servidor.sendmail(self.carta['From'], destinatarios, self.carta.as_string())
            return True
        except Exception as e:
            print(e)
            return(e)