Envoyer des mail (gmail) via python-----------------------------------
Url     : http://codes-sources.commentcamarche.net/source/102473-envoyer-des-mail-gmail-via-pythonAuteur  : thomas.k47200Date    : 23/10/2019
Licence :
=========

Ce document intitul� � Envoyer des mail (gmail) via python � issu de CommentCaMarche
(codes-sources.commentcamarche.net) est mis � disposition sous les termes de
la licence Creative Commons. Vous pouvez copier, modifier des copies de cette
source, dans les conditions fix�es par la licence, tant que cette note
appara�t clairement.

Description :
=============

<pre class="code" data-mode="python">import sys
import smtplib
from email.mime.m
ultipart import MIMEMultipart
from email.mime.text import MIMEText
import email.
message
expmail = input(&quot;votre adresse mail &quot;)
mdp=input(&quot;nvotre 
mot de passe&quot;)
destmail = input(&quot;mail du destinataire&quot;)
objet = i
nput(&quot;objet du mail&quot;)
contenu = input(&quot;contenu du mail(deux espac
e pour sauter une ligne)&quot;).replace(&apos;  &apos;,&apos;&lt;br&gt;&apos;)
t
ruc=contenu.replace(&apos;&lt;br&gt;&apos;,&apos;n&apos;)

print(truc)
import em
ail.message

if input(&quot;envoyer ? (O/N)&quot;)==&quot;O&quot;or&quot;o&quot;
:
    msg = email.message.Message()

    msg.add_header(&apos;Content-Type&apos;
,&apos;text/html&apos;)
    msg.set_payload(&apos;{}&apos;.format(contenu,))

  
  # Send the message via local SMTP server.
    s = smtplib.SMTP(&apos;smtp.gmai
l.com&apos;,587)

    s.starttls()

    try:
        s.login(destmail,
         
   mdp)

        s.sendmail(expmail, destmail, msg.as_string())

        s.quit(
)
        print(&apos;nnnnmessage envoyer avec succés&apos;)
    except:
      
  print(&quot;nnnnERREUR: mauvais mail ou mot de passe nsinon allez sur [https:/
/myaccount.google.com/lesssecureapps] et activer l&apos;option&quot; )
else:
   
 sys.exit()</pre>
