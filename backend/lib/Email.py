import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def envoie_email(destinataire, sujet, corp):
    # Paramètres Gmail
    email_sender = 'bloodjens32@gmail.com'
    email_password = 'Jessy123@'
    email_receiver = destinataire

    # Création du message
    message = MIMEMultipart()
    message['From'] = email_sender
    message['To'] = email_receiver
    message['Subject'] = sujet

    # Corps du message
    body = corp
    message.attach(MIMEText(body, 'html'))

    # Connexion au serveur SMTP de Gmail
    server = smtplib.SMTP('smtp.gmass.co', 25)
    server.starttls()
    server.login("gmass", "41fe8d90-f331-43c7-a07f-ed5f260c1eaa")

    # Envoi de l'e-mail
    text = message.as_string()
    server.sendmail(email_sender, email_receiver, text)

    # Fermeture de la connexion
    server.quit()
