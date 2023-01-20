import csv
import datetime

with open('categorii.txt' ,'a' ) as file:
    while True:
        categorie = input('Introduceti o categorie de taskuri.Tastati enter pentru a incheia')
        if categorie == '':
         break
        else:
            file.write(categorie +'\n')


lista_categorii=[]
with open('categorii.txt', 'r') as file:
    while True:
        line=file.readline().replace('\n',"")
        if not line:
         break
        lista_categorii.append(line)

def validate_categorii(categorie):
    global lista_categorii
    if categorie not in lista_categorii:
        # return False
     print('Categoria nu exista.Introduceti alta categorie :')
    print(lista_categorii)
    return False

    return True

    # return False

def validate_date(date_string):
    try:
        date= datetime.datetime.strptime('date_string, %Y-%m-%d')
    except Exception as e :
        print('Data introdusa nu este in formatul corect(yyyy-ll-dd)!')
    return False
    # False
    else :
     return True

# def validate_category(categorie):
#     global lista_categorii
#         if categorie not in lista_categorii
#             return False
#     print('categoria nu exista, alegeti din categpriile de mai jos')
#     print(lista_categprii)
#         return True
# return False

with open('taskuri.csv ,a') as file:
    while True:
     tasks =input("Introduceti un task.Tastati enter pentru a incheia")
    if task == '':
        break
    while True:
     end_date=('Introduceti data limita:')
    if validate_date(end_date):
        # break
    # if end_date=='':
    #     break
    responsible= input('Introduceti o persoana responsabila:')
    if responsible=='':
        break
    while True:
     categorie=input('Introduceti o categorie:')
    if validate_categorii(categorie):
        break
    next_category=input('Introduceti alta categorie?(Y/N):')
    csv.writer=csv.writer(file , delimiter= ',')
    csv_writer.writerow([tasks,end_date,resposible,category])
    if next_category.lower!='Y':
        break
    end_date=datetime.datetime.strptime(input('Introduceti o data limita(YYYY-MM-DD):'), '%Y-%m-%m')

    # next_task =input('Introduceti un alt task Y/N')
