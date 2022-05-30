
import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import email.message
expmail = input("votre adresse mail ")
mdp=input("\nvotre mot de passe")
destmail = input("mail du destinataire")
objet = input("objet du mail")
contenu = input("contenu du mail(deux espace pour sauter une ligne)").replace('  ','<br>')
truc=contenu.replace('<br>','\n')

print(truc)
import email.message

if input("envoyer ? (O/N)")=="O"or"o":
    msg = email.message.Message()

    msg.add_header('Content-Type','text/html')
    msg.set_payload('{}'.format(contenu,))

    # Send the message via local SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)

    s.starttls()

    try:
        s.login(destmail,
            mdp)

        s.sendmail(expmail, destmail, msg.as_string())

        s.quit()
        print('\n\n\n\nmessage envoyer avec succés')
    except:
        print("\n\n\n\nERREUR: mauvais mail ou mot de passe \nsinon allez sur https://myaccount.google.com/lesssecureapps et activer l'option" )
else:
    sys.exit()