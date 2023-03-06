import random
from termcolor import colored

from domain.client import Client
from erori.repo_error import RepoError


class RepoClient:

    def __init__(self):
        self.__clienti = {}

    def adauga_client(self, client):
        """
        Functie care adauga un nou client la lista de clienti
        :param client: obiectul client
        :return:
        """
        if client.get_id_client() in self.__clienti:
            raise ValueError(colored("Client existent"))
        self.__clienti[client.get_id_client()] = client
        return self.__clienti[client.get_id_client()]

    def sterge_client(self, id_client):
        """
        Functie care sterge un client din lista de clienti
        :param id_client: id-ul clientului dat ca parametru
        :return:
        """
        if id_client not in self.__clienti:
            raise ValueError(colored("Client inexistent", 'red'))
        client_sters = self.__clienti[id_client]
        del self.__clienti[id_client]
        return client_sters

    @staticmethod
    def get_random_id():
        """
        Functie care genereaza un id random
        :return: id-ul random al filmului
        """
        id_random = random.randint(1, 9999999)
        return id_random

    @staticmethod
    def get_random_nume():
        """
        Functie care genereaza un nume random
        :return: nume random
        """
        lista_nume = ['Helēna Mitre', 'Ofira Uno', 'Ajeet Palle', 'Leila Hreiðunn', 'Girish Jojo', 'Ejder Uju',
                      'Marilou Naïma', 'Ben Menodora', 'Ntombi Bastian', 'Voitsekh Melvyn', 'Letha Séamus',
                      'Verginius Yamikani', 'Jarmo Bianka', 'Veselin Laverna', 'Kelemen Mihăiță', 'Beatrice Akiba',
                      'Widad Bragi', 'Pafnutiy Gomes', 'Drahomír Sancha', 'Ælfweard Mark']
        nume_random = random.choice(lista_nume)
        return nume_random

    @staticmethod
    def get_random_cnp():
        """
        Functie care genereaza un cnp random
        :return: cnp random
        """
        cnp_random = random.randint(1000000000, 5000000000)
        return cnp_random

    def cauta_client_dupa_id(self, id_client):
        """
        Functie care cauta un client dupa id
        :param id_client: id-ul clientului dorit
        :return: toate datele clientului daca acesta exista in lista
        :raises: RepoError daca clientul nu exista
        """
        def cauta_client_dupa_id_recursiv(lista, id_client_cautat):
            if int(lista[0].get_id_client()) == id_client_cautat:
                return self.__clienti[lista[0].get_id_client()]
            else:
                return cauta_client_dupa_id_recursiv(lista[1:], id_client_cautat)
        try:
            client = cauta_client_dupa_id_recursiv(self.get_all_clienti(), id_client)
            return client
        except IndexError:
            raise RepoError("Client inexistent")

        '''if id_client not in self.__clienti:
            raise ValueError(colored("Client inexistent"))
        return self.__clienti[id_client]'''

    def actualizeaza_client(self, id_client, client_nou):
        """
        Functie care actualizeaza datele unui client
        :param id_client: obiectul client
        :param client_nou: clientul actualizat
        :return:
        """
        if id_client not in self.__clienti:
            raise ValueError(colored("Client inexistent"))
        self.__clienti[id_client] = client_nou
        return self.__clienti[id_client]

    def get_all_clienti(self):
        """
        Functie care stocheaza intr-o lista toti clientii
        :return: lista de clienti
        """
        clienti = []
        for id_client in self.__clienti:
            clienti.append(self.__clienti[id_client])
        return clienti

    def inchiriaza_film(self, id_client, film):
        """
        Functie de repo care salveaza filmele inchiriate de client
        :param id_client: id-ul clientului care a inchiriat filmul
        :param film: filmul care a fost inchiriat
        :return:
        """
        client = self.cauta_client_dupa_id(id_client)
        client.set_filme_inchiriate(film)

    def return_film(self, id_client, film):
        """
        Functie de repo pentru a returna un film inchiriat
        :param id_client: id-ul clientului
        :param film: filmul care urmeaza a fi returnat
        :return:
        """
        client = self.cauta_client_dupa_id(id_client)
        client.del_filme_inchiriate(film)

    def get_clienti_cu_filme(self):
        """
        Functie care returneaza lista cu clienti ce au filme inchiriate
        :return: lista de clienti
        """
        clienti = []
        for id_client in self.__clienti:
            client = self.__clienti[id_client]
            if client.get_filme_inchiriate():
                clienti.append(client)
        return clienti


class RepoClientFile(RepoClient):

    def __init__(self, filename):
        RepoClient.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    @staticmethod
    def __creaza_client_line(line):
        params = line.split(" ")
        client = Client(int(params[0]), params[1], params[2])
        return client

    def __load_from_file(self):
        fh = open(self.__filename)
        for line in fh:
            if line.strip() == "":
                continue
            client = self.__creaza_client_line(line)
            RepoClient.adauga_client(self, client)
        fh.close()

    def adauga_client(self, client):
        RepoClient.adauga_client(self, client)
        self.__append_to_file(client)

    def __append_to_file(self, client):
        fh = open(self.__filename, "a")
        line = str(str(client.get_id_client()) + " " + client.get_nume_client() + " " + str(client.get_cnp_client()))
        fh.write("\n")
        fh.write(line)
        fh.close()

    def cauta_client_dupa_id(self, id_client):
        return RepoClient.cauta_client_dupa_id(self, id_client)

    def actualizeaza_client(self, id_client, client_nou):
        RepoClient.actualizeaza_client(self, id_client, client_nou)
        self.__actualizeaza_file()

    def __actualizeaza_file(self):
        fh = open(self.__filename, "w")
        clienti = RepoClient.get_all_clienti(self)
        for client in clienti:
            line = str(client.get_id_client() + " " + client.get_nume_client() + " " + client.get_cnp_client())
            fh.write(line)
            fh.write("\n")
        fh.close()

    def sterge_client(self, id_client):
        RepoClient.sterge_client(self, id_client)
        self.__actualizeaza_file()


'''@staticmethod
   def test_adauga_client():
       repo_client = RepoClient()
       client = Client(1, 'Tony', '231231231232')
       repo_client.adauga_client(client)

       client = repo_client.cauta_client_dupa_id(1)
       assert (client.get_id_client() == 1)
       assert (client.get_nume_client() == 'Tony')
       assert (client.get_cnp_client() == '231231231232')

   @staticmethod
   def test_actualizeaza_client():
       repo_client = RepoClient()
       client = Client(1, 'Tony', '231231231232')
       repo_client.adauga_client(client)

       client_nou = Client(22, 'Marian', '231231231232')
       repo_client.adauga_client(client_nou)
       client_actualizat = repo_client.actualizeaza_client(1, client_nou)
       assert (client_actualizat == client_nou)

   @staticmethod
   def test_get_all_clienti():
       repo_client = RepoClient()
       client1 = Client(1, 'Tony', '231231231232')
       client2 = Client(2, 'Marian', '93809809899')
       repo_client.adauga_client(client1)
       repo_client.adauga_client(client2)

       lista_clienti = repo_client.get_all_clienti()
       assert (lista_clienti[0] == client1)
       assert (lista_clienti[1] == client2)

   @staticmethod
   def test_inchiriaza_film():
       repo_client = RepoClient()
       repo_film = RepoFilm()
       client = Client(1, 'Tony', '231231231232')
       film = Filme(1, 'Avatar', 'actiune')
       repo_client.adauga_client(client)
       repo_film.adauga_film(film)

       repo_client.inchiriaza_film(1, film)
       film_inch = client.get_filme_inchiriate()
       assert (film_inch[0] == film)

   @staticmethod
   def test_return_film():
       repo_client = RepoClient()
       repo_film = RepoFilm()
       client = Client(1, 'Tony', '231231231232')
       film = Filme(1, 'Avatar', 'actiune')
       repo_client.adauga_client(client)
       repo_film.adauga_film(film)

       repo_client.inchiriaza_film(1, film)
       repo_client.return_film(1, film)
       film_inch = client.get_filme_inchiriate()
       assert (film_inch == [])

   @staticmethod
   def test_clienti_cu_filme():
       repo_client = RepoClient()
       repo_film = RepoFilm()
       client = Client(1, 'Tony', '231231231232')
       film = Filme(1, 'Avatar', 'actiune')
       repo_client.adauga_client(client)
       repo_film.adauga_film(film)

       repo_client.inchiriaza_film(1, film)
       lista_clienti = repo_client.get_clienti_cu_filme()
       assert (lista_clienti[0] == client)


def all_teste():
   repo_client = RepoClient()
   repo_client.test_adauga_client()
   repo_client.test_actualizeaza_client()
   repo_client.test_get_all_clienti()
   repo_client.test_inchiriaza_film()
   repo_client.test_return_film()
   repo_client.test_clienti_cu_filme()


all_teste()'''
