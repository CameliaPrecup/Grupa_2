import csv
import datetime


def validate_date(date_string):
    """
    Functie care valideaza daca un string este o data valida

    :param date_string: string - textul care trebuie validat
    :return: boolean - True sau False in functie daca string-ul poate fi interpretat ca o data sau nu
    """

    return False


def add_categories(category_list, categories_file):
    """
    Functie care citeste de la tastatura un set de categorii pe care le adauga intr-o lista si le salveaza
    intr-un fisier. Verifica daca o categorie exista deja si afiseaza un mesaj de eroare

    :param category_list: list - lista cu categoriile existenta la care se adauga cele introduse de la tastatura
    :param categories_file: string - numele fisiserului cu categoriile existente la care se adauga cele introduse
    de la tastatura

    :return: list - lista completa cu toate categoriile (cele existente + cele introduse de la tastatura)
    """

    return []


def add_tasks(task_list, category_list, tasks_file):
    """
    Functie care citeste un task de la tastatura si pe care il adauga intr-o lista existenta si il salveaza intr-un
    fisier

    :param task_list: list - lista cu task-urile existente la care se adauga cele introduse de la tastatura
    :param category_list: list - lista de categorii folosita pentru validarea categoriei introduse de utilzator
    :param tasks_file: string - fisierul cu task-urile existente la care se adauga cele introduse de la tastatura

    :return: list - lista completa cu toate task-urile (cele existente + cele introduse de la tastatura)
    """
    return []


def load_categories(filename):
    """
    Functie care citeste o lista de categorii dintr-un fisier dat (fiecare linie reprezinta o categorie)

    :param filename: string - numele fisiserului din care se citesc categoriile
    :return: list - lista cu categoriile citite sau o lista goala daca fisiserul nu exista sau e gol
    """
    return []


def load_tasks(filename):
    """
    Functie care citeste o lista cu task-uri dintr-un fisier dat (fiecare linie reprezinta un task)

    :param filename: string - numele fisierului din care se citesc task-urile
    :return: list - lista cu task-urile citite sau o lista goala daca fisierul nu exista sau e gol
    """
    return []


def list_tasks(task_list, sort_field="", reverse=False):
    """
    Functie care ordoneaza si afiseaza o lista de taskuri

    :param task_list: list - Lista de task-uri care trebuie sortata si afisata
    :param sort_field: string - campul folosit pentru sortare (in cazul in care acest parametru este un string gol
    lista nu va fi sortata)
    :param reverse: boolean - True sau False in cazul in care sortarea se va face descendent sau nu

    :return: None - nu intoarce nimi
    """

    return


def update_tasks(task_list, filename):
    """
    Functie care scrie o lista de task-uri intr-un fisier csv. Rescrie fisiserul in cazul in care acesta exista deja.
    Creaza fisiserul in cazul in care acesta nu exista

    :param task_list: list - lista de task-uri care va fi scrisa in fisiser
    :param filename: string - numele fisierului in care vor fi scrise task-urile

    :return: None - nu intoarce nimic
    """

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
    return False


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
    return False


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
    return False, False


def show_edit_menu(task_list, category_list):
    """
    Functie care afiseaza submeniu de editare si modifica un task ales de utilizator dintr-o lista existenta
    Editeaza detaliilor referitoare la task, dată, persoană sau categorie dintr-un anumit task ales de utilizator de la
    tastatură (când se cere această opțiune, se va lista lista de taskuri cu un identificator unic pe rand, astfel încât
    să se știe ce informație urmează să editeze utilizatorul)

    :param task_list: list - lista de task-uri pe care utilizatorul le va putea edita
    :param category_list: list - lista de categorii folosita pentru validarea categoriei introduse de utilzator
    :return: task_list: list - lista de task-uri cu task-ul modificat de utilizator
    """

    return task_list


def show_delete_menu(task_list):
    """
    Functie care afiseaza submeniul de stergere si sterge un task ales de utilizator dintr-o lista existenta

    :param task_list: list - lista de task-uri pe care utilizatorul le va putea sterge
    :return: list - lista de task-uri ramase
    """

    return task_list

# -------------------------------------------------------------------------------------------------------------
# ---------------------------------------  END OF FUNCTIONS DEFINITIONS ---------------------------------------
# -------------------------------------------------------------------------------------------------------------


task_fields = ('descriere', 'data', 'persoana', 'categorie')
categories_file = "categorii.txt"
tasks_file = "taskuri.csv"

category_list = load_categories(categories_file)
add_categories(category_list, categories_file)
task_list = load_tasks(tasks_file)
add_tasks(task_list, category_list, tasks_file)

while True:
    menu_choice = show_menu()
    if menu_choice is False:
        break
    if menu_choice == 1:
        list_tasks(task_list, "categorie")
    elif menu_choice == 2:
        submenu_choice = show_sort_menu()
        if submenu_choice == 1:
            list_tasks(task_list, "descriere")
        elif submenu_choice == 2:
            list_tasks(task_list, "descriere", True)
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
            continue #listeaza lista filtrata in functie de filter_text si filter_index
    elif menu_choice == 4:
        add_tasks(task_list, category_list, tasks_file)
    elif menu_choice == 5:
        task_list = show_edit_menu(task_list, category_list)
        update_tasks(task_list, tasks_file)
    elif menu_choice == 6:
        task_list = show_delete_menu(task_list)
        update_tasks(task_list, tasks_file)