from tkinter import *
from modell import chat
import pymysql
import time
from datetime import date


#create_products(project[0],project[1],unit_price,units_in_stock,today,today,project[2])
# name  description                                             date_created last_updated  category_name


def create_products( name,description, unit_price ,units_in_stock, category_name):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='full-stack-ecommerce')
    
    #definir le premier cursor
    cursor_1 = conn.cursor()
    
    #definir la premiere requete
    query_1 =  "select id from product_category where category_name = %s"
    
    #executer la premiere requete SQL
    cursor_1.execute(query_1,category_name)
    
    #extrait les données recues
    #data est une table de deux colonnes, id_m et nom_m
    data= cursor_1.fetchall()
        
    #definir le deuxiem cursor
    cursor_2 = conn.cursor()
    
    
    #Definir la deuxieme requete SQL
    query_2 =  "insert into product (NAME, DESCRIPTION ,UNIT_PRICE, UNITS_IN_STOCK, CATEGORY_ID) values (%s,%s,%s,%s,%s);"
    
    
    #Executer la deuxieme requete SQL      
    cursor_2.execute(query_2, (name,description,unit_price,units_in_stock,data[0]))
    
           
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()

def show_projects(titre_p):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée    
    query = "select t.titre_t as 'Titre', t.statut as 'Etat de la tâche', m.nom_m as 'Affectée à' from projet p, tache t, membre m where m.id_m=p.id_m and p.id_p=t.id_p and p.titre_p= %s ;"
    
    #Execute la requete
    cursor.execute(query, titre_p)
    
    #Naviguer dans les données extraites
    data= cursor.fetchall()
    #Afficher les données
    L=''
    for w in data:
        D="\n"+"Tâche        : "+w[0]+"\n"+"Avancement    : "+w[1]+"\n"+"Tâche affectée à : "+w[2]+"\n"+"-------------------------------"
        L=L+D
    return L


def show_projet2(titre_p):
     #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query_1 = "select titre_p, description from projet where titre_p = %s"    
    
    #Execute la requete 1
    cursor.execute(query_1, titre_p)

    
    #Naviguer dans les données extraites
    data= cursor.fetchall()

    return ("\n"+"Titre                   : "+data[0][0]+"\n"+"Description du Projet   : "+data[0][1])      
        


def delete_products(name):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='full-stack-ecommerce')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query =  """delete from product where name= %s """
 
    #Execute la requete
    cursor.execute(query, name)    
        
    #Acccept le changement
    conn.commit()
 
    #Fermer le cursor
    cursor.close()
    
    #Fermer la connection avec la base de donnees
    conn.close()    

def create_tache(titre_t,desc_t,statut,nom_m,titre_p):
    
    #Se connecter à la base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Définir un cursor
    cursor_1 = conn.cursor()
    cursor_2 = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query_1 = " select p.id_p, p.titre_p, m.id_m, m.nom_m from projet p, membre m where m.id_m=p.id_m and nom_m = %s and titre_p = %s ; "
    
    #Executer la requete SQL
    cursor_1.execute(query_1,(nom_m,titre_p))    
    
    
    data= cursor_1.fetchall()
    

    
    query_2 = " insert into tache (titre_t,desc_t,statut,id_m, id_p) values (%s,%s,%s,%s,%s);"
    
    #Executer la requete SQL
    
    cursor_2.execute(query_2, (titre_t,desc_t,statut,data[0][2],data[0][0]))
    
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()
    
def show_products(name):
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='full-stack-ecommerce')
    
    #Definir un cursor
    cursor = conn.cursor()
    cursor2 = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query = "select * from product  where NAME=%s "    
    
    #Execute la requete 1
    cursor.execute(query, (name))
    
    print("Query well executed")
        
    #Naviguer dans les données extraites
    data= cursor.fetchall()
    
    
    
    a=0
    b=''
    L=''
    
    
    #Afficher les données
    for w in data:
        L=L+"\n"   +   "Product           : "   +   w[2]  +  "\n"  +  "Descreption  : "  +  w[3]  +  "\n"  +  "unit price      : "  +  str(w[4])  +  "\n"  +  "unit in stock      : "  +  str(w[7])  +  "\n" 
        a=w[10]
    query2 = "select * from product_category  where id=%s " 
    cursor2.execute(query2, (a))
    data2= cursor2.fetchall()
    for w in data2:
        b=b+w[1]  
    L=L+"Category           : "   + b + "\n"
    return(L)

    
def delete_tache(titre_p,titre_t):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='javaee')
    
    #Définir un cursor
    cursor = conn.cursor()
    
    #Définir la requete SQL souhaitée
    query = """ DELETE tache FROM tache INNER JOIN projet ON projet.id_p = tache.id_p WHERE tache.titre_t = %s and projet.titre_p = %s; """
  
    #Executer la requete
    cursor.execute(query,(titre_t,titre_p))
    
    #Acccepter le changement
    conn.commit()
    
    #Fermer la connexion avec la base de données
    conn.close()
    
    
    
def add_category(nom_m):
    
    #se connecter a l a base de donnees
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='full-stack-ecommerce')
    
    #definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query =  """insert into product_category (category_name) values (%s);"""
    
    #Executer la requete SQL
    cursor.execute(query, (nom_m))
    
    #Accepter le changements
    conn.commit()
    
    #Fermer la connection avec la base de donnees
    conn.close()
    
def show_categories():
    
    #Se connecter a l a base de données
    conn = pymysql.connect(host='localhost', user='root', password='1234ABCD????', db='full-stack-ecommerce')
    
    #Definir un cursor
    cursor = conn.cursor()
    
    #Definir la requete SQL souhaitée
    query = "select category_name  from product_category  "    
    
    #Execute la requete 1
    cursor.execute(query)
    
    #Naviguer dans les données extraites
    data= cursor.fetchall()

    L=''
    #Afficher les données
    for w in data:
        D="\n"+"                      category        : "+w[0]
        L=L+D
    L=L+"\n"+"-------------------------------"
    return L




root =Tk()

txt=Text(root,width=70)
txt.grid(row=0,column=0)

e=Entry(root,width=55)
e.grid(row=1,column=0)

txt.insert(END,"-> Start talking with the bot \n-> (type quit to stop)!"+"\n")


    
delete_product=0    
create_product=0
show_product=0
product=[]
unit_price=0
units_in_stock=0


delete_member=0    
create_category=0
show_category=0
category=[]


def quitt(self):
    self.destroy()
    exit()
    
def send():
    global create_product
    global show_product
    global delete_product
    global product
    global unit_price
    global units_in_stock
    

    
    global delete_member
    global create_category
    global show_category
    global member
    
    
    inp=e.get()
    if inp =="quit":
        quitt(root)
    send= "->User :" + inp
    txt.insert(END,send+"\n")
    e.delete(0,END)
    
    chatbot_response=chat(inp)
    
        #################################################################
    
    ###############################  create a new ^product
    if chatbot_response[1]=="create_product":
        create_product=1
        txt.insert(END,"->Ecommerce chatbot  :"+chatbot_response[0]+"\n")
        return 
    
    if create_product==1:        #get the product name and ask for the description 
        txt.insert(END,"->Ecommerce chatbot  :"+"add the descreption of the "+inp+" product"+"\n")
        product.append(inp)
        create_product=2
        return 
    
    if create_product==2:        #get the product descreption and ask for the chef
        txt.insert(END,"->Ecommerce chatbot  :"+"add the  name of category of the "+product[0]+" product"+"\n")
        product.append(inp)
        create_product=3
        return
    if create_product==3:        #get the product descreption and ask for the chef
        txt.insert(END,"->Ecommerce chatbot  :"+"add the unit price of the "+product[0]+" product"+"\n")
        product.append(inp)
        create_product=4
        return
    if create_product==4:        #get the product descreption and ask for the chef
        txt.insert(END,"->Ecommerce chatbot  :"+"add the units in stock of the "+product[0]+" product"+"\n")
        unit_price = inp
        create_product=5
        return
    if create_product==5:
        units_in_stock=inp
        create_products(product[0],product[1],unit_price,units_in_stock,product[2])
        txt.insert(END,"->Ecommerce chatbot  :The product has been added succesfully"+"\n")
        create_product=0
        return

    
        ###############################  show a ^product
    if chatbot_response[1]=="show_product":
        show_product=1
        txt.insert(END,"->Ecommerce chatbot  :"+chatbot_response[0]+"\n")
        return 
    if show_product==1:
        txt.insert(END,"->Ecommerce chatbot  :"+show_products(inp)+"\n")
        show_product=0
        return
       
        ###############################  delete a ^product
    if chatbot_response[1]=="delete_product":
        delete_product=1
        txt.insert(END,"->Ecommerce chatbot  :"+chatbot_response[0]+"\n")
        return 
    if delete_product==1:
        delete_products(inp)
        txt.insert(END,"->Ecommerce chatbot  : Prodect deleted succesfully"+"\n")
        delete_product=0
        return
    
        #################################################################
        
         ###############################  create a new ^category
    if chatbot_response[1]=="create_category":
        create_category=1
        txt.insert(END,"->Ecommerce chatbot  :"+chatbot_response[0]+"\n")
        return 
    
    if create_category==1:
        category.append(inp)
        add_category(category[0])
        txt.insert(END,"->Ecommerce chatbot  :The category has been added succesfully"+"\n")
        create_category=0
        return
    
    ###############################  show a ^category
    if chatbot_response[1]=="show_category":
        txt.insert(END,"->Ecommerce chatbot  : Liste of categories : "+show_categories()+"\n")
        return
    
        
    txt.insert(END,"->Ecommerce chatbot :"+chatbot_response[0]+"\n")

     

    
    
send=Button(root,text="send",fg="red",width=10,command=send).grid(row=1,column=1)


root.title("Ecommerce Chatbot")
root.mainloop()




