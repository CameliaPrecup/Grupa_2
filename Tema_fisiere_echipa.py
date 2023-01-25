import csv
import datetime


def validate_date(date_string): #Camelia
    """
    Functie care valideaza daca un string este o data valida

    :param date_string: string - textul care trebuie validat
    :return: boolean - True sau False in functie daca string-ul poate fi interpretat ca o data sau nu
    """
    try:
        date = datetime.datetime.strptime(date_string, '%Y-%m-%d')
    except Exception as e:
        print('Data introdusa nu este in formatul corect(yyyy-ll-dd)!', str(e))
        return False
    else:
        return True


def add_categories(category_list, categories_file): #Camelia
    """
    Functie care citeste de la tastatura un set de categorii pe care le adauga intr-o lista si le salveaza
    intr-un fisier. Verifica daca o categorie exista deja si afiseaza un mesaj de eroare

    :param category_list: list - lista cu categoriile existenta la care se adauga cele introduse de la tastatura
    :param categories_file: string - numele fisiserului cu categoriile existente la care se adauga cele introduse
    de la tastatura

    :return: list - lista completa cu toate categoriile (cele existente + cele introduse de la tastatura)
    """
    with open(categories_file, 'a')as file :
        while True:
            category=input('Introduceti o categorie de task-uri.Tastati enter pentru a  incheia:')
            if category=='':
                break
            else:
                if category in category_list:
                    print('Categoria exista deja:!')
                    continue
                else:
                    file.write(category+'\n')
                    category_list.append(category)
                    print(category_list)
    return category_list




#am pus mai jos un eemplu de implementare al functiei.

# def add_categories(category_list, categories_file):
#     """
#     Functie care citeste de la tastatura un set de categorii pe care le adauga intr-o lista si le salveaza
#     intr-un fisier. Verifica daca o categorie exista deja si afiseaza un mesaj de eroare
#
#     :param category_list: list - lista cu categoriile existenta la care se adauga cele introduse de la tastatura
#     :param categories_file: string - numele fisiserului cu categoriile existente la care se adauga cele introduse
#     de la tastatura
#
#     :return: list - lista completa cu toate categoriile (cele existente + cele introduse de la tastatura)
#     """
#     with open(categories_file, 'a') as file:
#         while True:
#             category = input('Introduceti o categorie de task-uri. Tastati enter pentru a incheia: ')
#             if category == '':
#                 break
#             else:
#                 if category in category_list:
#                     print("Categoria exista deja!")
#                     continue
#                 else:
#                     file.write(category + "\n")
#                     category_list.append(category)
#     return category_list


def add_tasks(task_list, tasks_file): #Camelia
    """
    Functie care citeste un task de la tastatura si pe care il adauga intr-o lista existenta si il salveaza intr-un
    fisier

    :param task_list: list - lista cu task-urile existente la care se adauga cele introduse de la tastatura
    :param category_list: list - lista de categorii folosita pentru validarea categoriei introduse de utilzator
    :param tasks_file: string - fisierul cu task-urile existente la care se adauga cele introduse de la tastatura

    :return: list - lista completa cu toate task-urile (cele existente + cele introduse de la tastatura)
    """
    with open(tasks_file, "a") as file:
        while True:
            while True:
                descriere = input("Introduceti un task.Tastati enter pentru a incheia:")
                filtered_list = list(filter(lambda x: x[0] == descriere, task_list))
                if filtered_list:
                    print("Taskul exista deja!")
                else:
                    break
                if descriere == "":
                    break

            if descriere == "":
                break

            while True:
                end_date = input("Introduceti data limita. Tastati enter pentru a incheia:")
                if validate_date(end_date) or end_date == "":
                    break

            if end_date == "":
                break

            responsible = input("Introduceti o persoana responsabila. Tastati enter pentru a incheia:")
            if responsible == "":
                break

            while True:
                category = input("Introduceti o categorie. Tastati enter pentru a incheia:")
                if category == "":
                    break
                elif category not in category_list:
                    print("Categoria nu exista in lista. Trebuie sa introduci una din categoriile de mai jos:")
                    print(category_list)
                else:
                    break
            if category == "":
                break

            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow([descriere, end_date, responsible, category])
            task_list.append([descriere, end_date, responsible, category])

            next_category = input('Introduceti alt task? (Y/N): ')
            if next_category.lower() != 'y':
                break
    return task_list





def load_categories(filename):
    """
    Functie care citeste o lista de categorii dintr-un fisier dat (fiecare linie reprezinta o categorie)

    :param filename: string - numele fisiserului din care se citesc categoriile
    :return: list - lista cu categoriile citite sau o lista goala daca fisiserul nu exista sau e gol
    """

    with open(filename, "r") as file:
        category = file.readlines()
    category = list(map(lambda x: x.replace("\n", ""), category))
    return category



def load_tasks(filename):
    """
    Functie care citeste o lista cu task-uri dintr-un fisier dat (fiecare linie reprezinta un task)

    :param filename: string - numele fisierului din care se citesc task-urile
    :return: list - lista cu task-urile citite sau o lista goala daca fisierul nu exista sau e gol
    """

    with open(filename, "r") as file:
        return list(csv.reader(file, delimiter=","))


def list_tasks(tasks, sortby="", reverse=False):
    """
    Functie care ordoneaza si afiseaza o lista de taskuri

    :param tasks: list - Lista de task-uri care trebuie sortata si afisata
    :param sortby: string - campul folosit pentru sortare (in cazul in care acest parametru este un string gol
    sau nu exista in lista de campuri predefinita - task_fields - lista nu va fi sortata)
    :param reverse: boolean - True sau False in cazul in care sortarea se va face descendent sau nu

    :return: None - nu intoarce nimi
    """
    if sortby in task_fields:
        tasks.sort(key=lambda x: x[task_fields.index(sortby)], reverse=reverse)

    for i in range(len(tasks)):
        print(f"{i+1}. Task: {tasks[i][0]}, data: {tasks[i][1]}, persoana responsabila: {tasks[i][2]}, categoria: {tasks[i][3]}.")
    return


def update_tasks(task_list, filename):
    """
    Functie care scrie o lista de task-uri intr-un fisier csv. Rescrie fisiserul in cazul in care acesta exista deja.
    Creaza fisiserul in cazul in care acesta nu exista

    :param task_list: list - lista de task-uri care va fi scrisa in fisiser
    :param filename: string - numele fisierului in care vor fi scrise task-urile

    :return: None - nu intoarce nimic
    """
    with open(filename, "w") as file:
        csv_writer = csv.writer(file, delimiter=",")
        csv_writer.writerows(task_list)

    return


def show_menu():
    """
    Functie care afiseaza meniu principal
    Se afișează un meniu din care utilizatorul poate alege să realizeze următoarele operații:
1. Listare date: în afișarea inițială a datelor se realizează o sortare în funcție de categorie.
2. Sortare: se alege o opțiune din cele 8 de mai jos
3. Filtrare date: filtrarea datelor reprezintă de fapt o listare a datelor în funcție de anumite detalii date
de la tastatură.
4. Adăugarea unui nou task în lista inițiala
5. Editarea detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la
tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât să
se știe ce informație urmează să editeze utilizatorul)
6. Ștergerea unui task din lista inițială.

    :return: int - numarul optiunii introduse de utilzator sau False in cazul in care utilizatorul introduce un text gol
    """
    print('[1] - Listare ordonata date ')
    print('[2] - Sortare date')
    print('[3] - Filtrare date ')
    print('[4] - Adaugare task nou ')
    print('[5] - Editare detalii ')
    print('[6] - Stergere task ')

    while True:
        main_option = input('Introduceti optiunea. Tastati enter pentru a incheia: ')
        if main_option == '':
            return False
        elif not main_option.isdigit():
            print("Nu ai introdus un numar!")
            continue
        elif int(main_option) < 1 or int(main_option) > 6:
            print("Optiunea introdusa nu exista!")
            continue
        else:
            break
    return int(main_option)


def show_sort_menu():
    """
    Functie care afiseaza submeniul de sortare
    Sortare: se alege o opțiune din cele 8 de mai jos:
Criteriile disponibile sunt:
1. sortare ascendentă task
2. sortare descendentă task
3. sortare ascendentă data
4. sortare descendentă data
5. sortare ascendentă persoana responsabilă
6. sortare descendentă persoană responsabilă
7. sortare ascendentă categorie
8. sortare descendentă categorie

    :return: int - numarul optiunii introduse de utilzator sau False in cazul in care utilizatorul introduce un text gol
    """

    while True:
        print('[1] - Sortare ascendentă task ')
        print('[2] - Sortare descendentă task ')
        print('[3] - Sortare ascendentă data ')
        print('[4] - Sortare desscendentă data ')
        print('[5] - Sortare ascendentă persoana responsabilă ')
        print('[6] - Sortare descendentă persoană responsabilă ')
        print('[7] - Sortare ascendentă categorie! ')
        print('[8] - Sortare descendentă categorie ')


        submenu_choice = input("Alege una din optiunile de mai sus (1-8). "
                               "Tasteaza enter pentru a te intoarce la meniul anterior: ")
        if submenu_choice == '':
            return False
        elif not submenu_choice.isdigit():
            print("Trebuie sa introduceti o cifra de la 1 la 8!")
            continue
        elif int(submenu_choice) < 1 or int(submenu_choice) > 8:
            print("Trebuie sa introduceti o cifra de la 1 la 8!")
            continue
        else:
            break

    return int(submenu_choice)

def show_filter_menu(task_fields):
    """
    Functie care afiseaza submeniul de filtrare
-       se cere de la tastatură câmpul după care se realizeaza filtrarea:
1.     Task
2.     Dată
3.     Persoană responsabilă
4.     Categorie
-       după alegerea campului de la tastatură se cere introducerea unui string utilizat pentru filtrarea în lista
inițială de date, astfel încât din lista inițială să rămână doar datele care conțin / încep cu valoarea introdusă

    :param task_fields: lista care contine campurile unui task (se foloseste pentru a valida campul introdus de la
    tastatura

    :return: intoarce 2 variabile
    filter_index - index-ul campului (din task_fields) dupa care se va face filtrarea
    filter_text - textul care va fi folosit pentru filtrarea datelor
    intoarce False, False in cazul in care utilizatorul introduce un text gol

    """
    while True:
        print('[1] - Task ')
        print('[2] - Dată ')
        print('[3] - Persoană responsabilă ')
        print('[4] - Categorie ')
        filter_field = input("Alegeti campul dupa care vreti sa filtrati: ")

        if filter_field == '':
            return False, False
        elif not filter_field.isdigit():
            print("Trebuie sa introduceti o cifra de la 1 la 4!")
            continue
        elif int(filter_field) < 1 or int(filter_field) > 4:
            print("Optiunea nu exista!")
            continue
        else:
            break

    filter_text = input("Introduceti textul dupa care se va face filtrarea!. Enter pentru a va intoarce la meniul anterior: ")
    if filter_field == '':
        return False, False

    return int(filter_field)-1, filter_text


def show_edit_menu(tasks):
    """
    Functie care afiseaza submeniu de editare si modifica un task ales de utilizator dintr-o lista existenta
    Editeaza detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la
    tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât
    să se știe ce informație urmează să editeze utilizatorul)

    :param tasks: list - lista de task-uri pe care utilizatorul le va putea edita
    :param category_list: list - lista de categorii folosita pentru validarea categoriei introduse de utilzator
    :return: task_list: list - lista de task-uri cu task-ul modificat de utilizator
    """
    list_tasks(tasks)

    while True:
        task_id = input("introduceti id-ul task-ului pe care vreti sa il editati!. Tastati enter pentru a va intoarce la meniul anterior: ")

        if task_id == '':
            return False
        elif not task_id.isdigit():
            print(f"Trebuie sa introduceti o cifra de la 1 la {len(tasks)}!")
            continue
        elif int(task_id) < 1 or int(task_id) > len(tasks):
            print("Task-ul cu id-ul introdus nu exista!")
            continue
        else:
            break

    task_id = int(task_id)

    descriere = input(f"Introduceti noua descriere! Tastati enter pentru a lasa lafel ({tasks[task_id-1][0]}): ")
    if descriere != "":
        tasks[task_id - 1][0] = descriere

    while True:
        data_limita = input(f"Introduceti noua data limita! Tastati enter pentru a lasa lafel ({tasks[task_id - 1][1]}): ")
        if data_limita == "":
            break
        elif validate_date(data_limita):
            tasks[task_id - 1][1] = data_limita
            break
        else:
            continue

    persoana = input(f"Introduceti noua persoana responsabila! Tastati enter pentru a lasa lafel ({tasks[task_id-1][2]}): ")
    if persoana != "":
        tasks[task_id - 1][2] = persoana

    while True:
        categorie = input(f"Introduceti noua categorie! Tastati enter pentru a lasa lafel ({tasks[task_id - 1][3]}): ")
        if categorie == "":
            break
        elif categorie in category_list:
            tasks[task_id - 1][3] = categorie
            break
        else:
            print("Categoria nu se afla in lista. Introduceti una din categoriile de mai jos:")
            print(category_list)
            continue

    return task_list


def show_delete_menu(tasks: list):
    """
    Functie care afiseaza submeniul de stergere si sterge un task ales de utilizator dintr-o lista existenta

    :param tasks: list - lista de task-uri pe care utilizatorul le va putea sterge
    :return: list - lista de task-uri ramase
    """

    list_tasks(tasks)

    while True:
        taskName = input("introduceti numele task-ului pe care vreti sa il stergeti!: ")
        if taskName == "":
            return tasks
        filtered_list = list(filter(lambda x: x[0] == taskName, tasks))
        if not filtered_list:
            print("Taskul nu exista!")
            continue
        else:
            tasks.remove(filtered_list[0])
            print("Taskul a fost sters cu succes!")
            return tasks

# -------------------------------------------------------------------------------------------------------------
# ---------------------------------------  END OF FUNCTIONS DEFINITIONS ---------------------------------------
# -------------------------------------------------------------------------------------------------------------


task_fields = ('task', 'data', 'persoana', 'categorie')
categories_file = "categorii.txt"
tasks_file = "taskuri.csv"

category_list = load_categories(categories_file)
add_categories(category_list, categories_file)

task_list = load_tasks(tasks_file)
add_tasks(task_list, tasks_file)

while True:
    menu_choice = show_menu()
    if menu_choice is False:
        break
    if menu_choice == 1:
        list_tasks(task_list, "categorie")
    elif menu_choice == 2:
        submenu_choice = show_sort_menu()
        if submenu_choice == 1:
            list_tasks(task_list, "task")
        elif submenu_choice == 2:
            list_tasks(task_list, "task", True)
        elif submenu_choice == 3:
            list_tasks(task_list, "data")
        elif submenu_choice == 4:
            list_tasks(task_list, "data", True)
        elif submenu_choice == 5:
            list_tasks(task_list, "persoana")
        elif submenu_choice == 6:
            list_tasks(task_list, "persoana", True)
        elif submenu_choice == 7:
            list_tasks(task_list, "categorie")
        elif submenu_choice == 8:
            list_tasks(task_list, "categorie", True)
        else:
            continue
    elif menu_choice == 3:
        filter_index, filter_text = show_filter_menu(task_fields)
        if filter_index is not False:
            list_tasks(list(filter(lambda x: filter_text in x[filter_index], task_list)))
    elif menu_choice == 4:
        add_tasks(task_list, tasks_file)
    elif menu_choice == 5:
        task_list = show_edit_menu(task_list)
        update_tasks(task_list, tasks_file)
    elif menu_choice == 6:
        task_list = show_delete_menu(task_list)
        update_tasks(task_list, tasks_file)
