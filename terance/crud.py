#TOUT D ABORD ON IMPORTE LES MODULES
from tkinter import *
import mysql.connector as db
from tkinter import ttk
from tkinter import messagebox
def database():
    global conn,cursor
    conn=db.connect(host="localhost",user="berenger",password="bg236",database="banquepython")
    cursor=conn.cursor()
   # if conn:
    #    print("connexion reusie")
    #else:
     #   print("echec de connexion")

database()

#def lire():
#    sql="select * from comptes"
#    database()
#    cursor.execute(sql)
#    tab=cursor.fetchall()
#    return(tab)
#resultat=lire()
#print(resultat)

def lire():
    sql="select id,prenom,nom,numcompte,code,solde from comptes"
    database()
    cursor.execute(sql)
    tab=cursor.fetchall()
    x = dataTreeview.get_children()
    for item in x:
        dataTreeview.delete(item)
    for item in tab:
        dataTreeview.insert("", 1, text="", values=item)

def inserer(id,prenom,nom,numcompte,code,solde):
    sql="insert into comptes(id,prenom, nom, numcompte,code,solde) values(%s, %s, %s, %s, %s, %s)"
    database()
    val = (id,prenom, nom, numcompte,code,solde)
    cursor.execute(sql, val)
    conn.commit()
#inserer("Latyr","ndiaye","909140","2023","700000")
#resultat=lire()
#print(resultat)

#def update(id,prenom,nom,numcompte,code,solde):
#    sql="update comptes set prenom=%s, nom=%s, numcompte=%s, code=%s, solde=%s where id=%s"
#    database()
#    val = (prenom, nom, numcompte, code, solde,id)
#    cursor.execute(sql, val)
#    conn.commit()
#update(3,"Mr","bessan","909140","2023","990000")
#resultat=lire()
#print(resultat)

def update(id,prenom,nom,numcompte,code,solde):
    sql="update comptes set prenom=%s, nom=%s, numcompte=%s, code=%s, solde=%s where id=%s"
    database()
    val = (id,prenom, nom, numcompte, code, solde)
    cursor.execute(sql, val)
    conn.commit()

#def delete(id,):
#    sql="delete from comptes where id=%s"
#    database()
#    val = (id,)
#    cursor.execute(sql, val)
#    conn.commit()
#delete(3)
#resultat=lire()
#print(resultat)

def delete(id):
    sql="delete from comptes where id=%s"
    database()
    val = (id,)
    cursor.execute(sql, val)
    conn.commit()

#CREATION DES LABELS
fen=Tk()
fen.geometry('700x1000')
fen.title("Logiciel EC2LT")
Label(fen, text="Id:").place(relx=0, rely=0.05, relwidth=0.1)
Label(fen, text="Prenom:").place(relx=0.5, rely=0.05, relwidth=0.1)
Label(fen, text="Nom:").place(relx=0, rely=0.1, relwidth=0.1)
Label(fen, text="Numcompte:").place(relx=0.5, rely=0.1, relwidth=0.1)
Label(fen, text="Code:").place(relx=0, rely=0.15, relwidth=0.1)
Label(fen, text="Solde:").place(relx=0.5, rely=0.15, relwidth=0.1)

#CREONS Les Champs De Saisie En Leur Attribuant Des Noms
id= IntVar()
prenom= StringVar()
nom= StringVar()
numcompte= StringVar()
code= StringVar()
solde= StringVar()
Entry(fen, textvariable=id).place(relx=0.1, rely=0.05, relwidth=0.37, height=25)
Entry(fen, textvariable=prenom).place(relx=0.6, rely=0.05, relwidth=0.37, height=25)
Entry(fen, textvariable=nom).place(relx=0.1, rely=0.1, relwidth=0.37, height=25)
Entry(fen, textvariable=numcompte).place(relx=0.6, rely=0.1, relwidth=0.37, height=25)
Entry(fen, textvariable=code).place(relx=0.1, rely=0.15, relwidth=0.37, height=25)
Entry(fen, textvariable=solde).place(relx=0.6, rely=0.15, relwidth=0.37, height=25)
Label(fen, text='LOGICIEL DE GESTION D UNE BANQUE TEG', bg='white', fg='blue', font=(' ',15)).pack(side=TOP, fill='x')

#CREATION DES 4 Boutons De Commande
Button(fen, text="Voir Tout", command=lire).place(relx=0.2, rely=0.2, width=100)
Button(fen, text="Ajout utilisateur", command=lambda:
inserer(prenom.get(),nom.get(),numcompte.get(),code.get(),solde.get())).place(relx=0.4, rely=0.2, width=120)
Button(fen, text="Suppression user", command=lambda:delete(id.get())).place(relx=0.6,rely=0.2, width=120)
Button(fen, text="Mise a jour user", command=lambda:update(id.get(),prenom.get(),nom.get(),numcompte.get(),code.get(),solde.get())).place(relx=0.8, rely=0.2, width=120)

#CREATION DU Treeview Nommé DataTreeview Ayant 4 Colonnes
dataTreeview = ttk.Treeview(fen, show='headings', column=(id,'prenom', 'nom', 'numcompte', 'code','solde'))

#ICI On Definit La Largeur Des Colonnes De Notre Datatreeview
dataTreeview.column(id, width=150, anchor="center")
dataTreeview.column('prenom', width=150, anchor="center")
dataTreeview.column('nom', width=150, anchor="center")
dataTreeview.column('numcompte', width=150, anchor="center")
dataTreeview.column('code', width=150, anchor="center")
dataTreeview.column('solde', width=150, anchor="center")

#ICI On Renseigne Les Noms A Afficher Des Colonnes De DataTreeview
dataTreeview.heading(id, text='ID')
dataTreeview.heading('prenom', text='PRENOM')
dataTreeview.heading('nom', text='NOM')
dataTreeview.heading('numcompte', text='NUM COMPTE')
dataTreeview.heading('code', text='CODE')
dataTreeview.heading('solde', text='SOLDE')

#Là On Affiche DataTreeview
dataTreeview.place(rely=0.3, relwidth=0.97)

fen.mainloop()


