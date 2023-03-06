from termcolor import colored

from erori.repo_error import RepoError
from erori.validation_error import ValidError


class UI:

    def __init__(self, service_film, service_client, generate_random, teste_boxuri):
        self.__service_film = service_film
        self.__service_client = service_client
        self.__generate_random = generate_random
        self.__teste_boxuri = teste_boxuri
        self.__params = []

    def __meniu_optiuni(self, option):
        if option == 1:
            self.__ui_get_all_filme()

        elif option == 2:
            self.__ui_get_all_clienti()

        elif option == 3:
            id_film = self.__service_film.get_random_id()
            titlu_film = input("Titlul este: ")
            gen_film = input("Genul este: ")
            self.__params = [id_film, titlu_film, gen_film]
            self.__ui_adauga_film()

        elif option == 4:
            id_client = self.__service_client.get_random_id()
            nume_client = input("Numele clientului este: ")
            cnp_client = input("CNP-ul este: ")
            self.__params = [id_client, nume_client, cnp_client]
            self.__ui_adauga_client()

        elif option == 5:
            id_film = input("Id-ul filmului este: ")
            self.__ui_sterge_film(id_film)

        elif option == 6:
            id_client = input("Id-ul clientului este: ")
            self.__ui_sterge_client(id_client)

        elif option == 7:
            id_film = input("Id-ul filmului este: ")
            id_nou = input("Noul ID este: ")
            titlu_nou = input("Noul titlu este: ")
            gen_nou = input("Noul gen este: ")
            self.__params = [id_nou, titlu_nou, gen_nou]
            self.__ui_actualizeaza_film(id_film)

        elif option == 8:
            id_client = input("Id-ul clientului este: ")
            id_nou = input("Noul ID este: ")
            nume_nou = input("Noul nume este: ")
            cnp_nou = input("Noul cnp este: ")
            self.__params = [id_nou, nume_nou, cnp_nou]
            self.__ui_actualizeaza_client(id_client)

        elif option == 9:
            id_film = int(input("ID-ul filmului cautat este: "))
            print(colored(self.__service_film.cauta_film_dupa_id(id_film), 'blue'))

        elif option == 10:
            id_client = int(input("ID-ul clientului cautat este: "))
            client = self.__service_client.cauta_client_dupa_id(id_client)
            print(colored(client, 'blue'))

        elif option == 11:
            self.__ui_get_all_filme_disponibile()
            id_client = int(input("ID-ul dvs. este: "))
            id_film = int(input("ID-ul filmului pe care doriti sa-l inchiriati este: "))
            self.__ui_inchiriaza_film(id_client, id_film)
            print(colored("Film inchiriat cu succes", 'green'))

        elif option == 12:
            id_client = int(input("ID-ul dvs. este: "))
            id_film = int(input("ID-ul filmului pe care doriti sa-l returnati este: "))
            self.__ui_return_film(id_client, id_film)

        elif option == 13:
            self.__ui_get_clienti_cu_filme()

        elif option == 14:
            self.__ui_most_filme_inchiriate()

        elif option == 15:
            self.__ui_get_clienti_cu_filme_procent()

        elif option == 16:
            self.__ui_get_clienti_cu_filme_procent_mai_mare()

        elif option == 17:
            optiune_generare = input("Ce doriti sa generati? >>> ")
            self.__ui_generate_random(optiune_generare)

        elif option == 18:
            exit()
        else:
            print(colored("Comanda invalida", 'red'))

    def __ui_get_all_filme(self):
        filme = self.__service_film.get_all_filme()
        if len(filme) == 0:
            print(colored("Nu exista filme", 'red'))
            return
        for film in filme:
            print(colored(film, "blue"))
            print()

    def __ui_get_all_clienti(self):
        clienti = self.__service_client.get_all_clienti()
        if len(clienti) == 0:
            print(colored("Nu exista clienti", 'red'))
            return
        for client in clienti:
            print(colored(client, "blue"))
            print()

    def __ui_adauga_film(self):
        id_film = self.__params[0]
        titlu_film = self.__params[1]
        gen_film = self.__params[2]
        try:
            self.__service_film.adauga_film(id_film, titlu_film, gen_film)
        except ValueError as msg:
            print(colored(str(msg), 'red'))

    def __ui_adauga_client(self):
        id_client = self.__params[0]
        nume_client = self.__params[1]
        cnp_client = self.__params[2]
        try:
            self.__service_client.adauga_client(id_client, nume_client, cnp_client)
        except ValueError as msg:
            print(colored(str(msg), 'red'))

    def __ui_sterge_film(self, id_film):
        if self.__service_film.sterge_film(id_film):
            print(colored("Film sters", 'green'))
        else:
            return

    def __ui_sterge_client(self, id_client):
        if self.__service_client.sterge_client(id_client):
            print(colored("Client sters", 'green'))
        else:
            return

    def __ui_actualizeaza_film(self, id_film):
        if self.__service_film.actualizeaza_film(id_film, self.__params):
            print(colored("Film actualizat", 'green'))
        else:
            return

    def __ui_actualizeaza_client(self, id_client):
        if self.__service_client.actualizeaza_client(id_client, self.__params):
            print(colored("Client actualizat", 'green'))
        else:
            return

    def __ui_get_all_filme_disponibile(self):
        filme_disponibile = self.__service_film.get_all_filme_disponibile()
        try:
            for film in filme_disponibile:
                print(colored(film, 'blue'))
                print()
        except ValueError:
            print(colored("Nu exista filme disponibile", 'red'))

    def __ui_inchiriaza_film(self, id_client, id_film):
        try:
            film = self.__service_film.cauta_film_dupa_id(id_film)
            self.__service_client.inchiriaza_film(id_client, film)
            self.__service_film.inchiriaza_film(id_film)
        except ValidError as msg:
            print(colored(str(msg), 'red'))

    def __ui_get_clienti_cu_filme(self):
        clienti = self.__service_client.get_clienti_cu_filme()
        if len(clienti) == 0:
            print(colored("Nu exista clienti ce au filme inchiriate", 'red'))
        else:
            for client in clienti:
                print(colored(client, 'blue'))
                print(colored("Numarul de filme inchiriate este:", 'blue'), colored(str(len(client.get_filme_inchiriate())), 'blue'))
                print()

    def __ui_return_film(self, id_client, id_film):
        try:
            self.__service_film.return_film(id_film)
        except ValidError as msg:
            print(colored(str(msg), 'red'))

        film = self.__service_film.cauta_film_dupa_id(id_film)

        try:
            self.__service_client.return_film(id_client, film)
            print(colored("Film returnat cu succes", 'green'))
        except RepoError as msg:
            print(colored(str(msg), 'red'))

    def __ui_generate_random(self, optiune_generare):
        contor = 0
        try:
            contor = int(input("Contorul este: "))
            print()
        except ValueError:
            print(colored("Valoarea nu este valida", 'red'))
        if optiune_generare == 'filme':
            self.__generate_random.generate_filme(contor)
        elif optiune_generare == 'clienti':
            self.__generate_random.generate_clienti(contor)
        else:
            print(colored("Optiune invalida", 'red'))

    def __ui_most_filme_inchiriate(self):
        key = lambda x: (x.get_inchirieri(), x.get_titlu_film())
        _reversed = input("Sortarea va fi crescatoare?(True or False): ")
        if _reversed == 'True':
            _reversed = True
        else:
            _reversed = False
        try:
            lista_filme = self.__service_film.most_filme_inchiriate(key, _reversed)
            if len(lista_filme) == 0:
                raise ValueError("Nu exista filme inchiriate")
            else:
                for film in lista_filme:
                    print(colored(film, 'blue'),
                          colored(f"Numarul de inchirieri este: {film.get_inchirieri()}", 'blue'))
                    print()
        except ValidError as msg:
            print(colored(str(msg), 'red'))

    def __ui_get_clienti_cu_filme_procent(self):
        clienti = self.__service_client.get_clienti_cu_filme()
        if len(clienti) == 0:
            print(colored("Nu exista clienti ce au filme inchiriate", 'red'))
        else:
            lungime = 30 * len(clienti) / 100
            i = 0
            i = int(i)
            for client in clienti:
                if i <= lungime:
                    print(colored(client, 'blue'))
                    print()
                i += 1

    def __ui_get_clienti_cu_filme_procent_mai_mare(self):
        clienti = self.__service_client.get_clienti_cu_filme()
        if len(clienti) == 0:
            print(colored("Nu exista clienti ce au filme inchiriate", 'red'))
        else:
            self.__service_film.get_clienti_cu_filme_procent_mai_mare(clienti, 0)

    def run(self):
        while True:
            meniu()
            print()
            option = input("Introduceti comanda: ")
            print()
            try:
                self.__meniu_optiuni(int(option))
            except ValueError as msg:
                print(colored(str(msg), 'red'))
            except ValidError as msg:
                print(colored(str(msg), 'red'))
            except RepoError as msg:
                print(colored(str(msg), 'red'))


def meniu():
    print()
    print("1. Tipareste lista de filme disponibile")
    print("2. Tipareste lista de clienti")
    print("3. Adauga un film in lista")
    print("4. Adauga un client in lista")
    print("5. Sterge un film din lista de filme")
    print("6. Sterge un client din lista de client")
    print("7. Modifica lista de filme")
    print("8. Modifica lista de clienti")
    print("9. Cauta un film dupa id")
    print("10. Cauta un client dupa id")
    print("11. Inchiriaza un film")
    print("12. Returneaza un film")
    print("13. Tipareste lista de clienti ce au filme inchiriate si numarul acestora")
    print("14. Tipareste cele mai inchiriate filme")
    print("15. Tipareste primii 30% clienti ce au cele mai multe filme inchiriate")
    print("16. Tipareste primii 50% clienti ce au cele mai multe filme inchiriate")
    print("17. Genereaza filme sau clienti random")
    print("18. Iesire din aplicatie")
