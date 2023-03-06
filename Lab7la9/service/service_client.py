from termcolor import colored

from domain.client import Client
from erori.repo_error import RepoError
from repository.repo_client import RepoClient
from validate.validare_client import ValidatorClient


class ServiceClient:

    def __init__(self, validator_client, repo_client):
        self.__validator_client = validator_client
        self.__repo_client = repo_client

    def adauga_client(self, id_client, nume_client, cnp_client):
        """
        Functie de service care se asigura ca datele clientului sunt valide si apeleaza functia de repo pentru a adauga clientul in lista
        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param cnp_client: cnp-ul clientului
        :return:
        """
        client = Client(id_client, nume_client, cnp_client)
        self.__validator_client.valideaza(client)
        try:
            return self.__repo_client.adauga_client(client)
        except RepoError as msg:
            print(colored(str(msg), 'red'))

    def sterge_client(self, id_client):
        """
        Functie de service care apeleaza functia de repo
        :param id_client: id-ul  clientului cautat
        :return:
        """
        return self.__repo_client.sterge_client(id_client)

    def get_random_id(self):
        """
        Functie care apeleaza functia din repo care genereaza un id random
        :return: id-ul random
        """
        return self.__repo_client.get_random_id()

    def get_random_nume(self):
        """
        Functie care genereaza un nume random
        :return: nume random
        """
        return self.__repo_client.get_random_nume()

    def get_random_cnp(self):
        """
        Functie care genereaza un cnp random
        :return: cnp random
        """
        return self.__repo_client.get_random_cnp()

    def cauta_client_dupa_id(self, id_client):
        """
        Functie de service care apeleaza functia de repo
        :param id_client: id-ul clientului cautat
        :return: clientul daca acesta exista
        """
        return self.__repo_client.cauta_client_dupa_id(id_client)

    def actualizeaza_client(self, id_client, params):
        """
        Functie de service care citeste noile date si apeleaza functia de repo
        :param params: lista de parametrii
        :param id_client: id-ul clientului cautat
        :return: True daca repo nu ridica erori
        """
        film_nou = Client(params[0], params[1], params[2])
        return self.__repo_client.actualizeaza_client(id_client, film_nou)

    def get_all_clienti(self):
        """
        Functie de service care extrage lista de clienti
        :return: lista de clienti
        """
        return self.__repo_client.get_all_clienti()

    def inchiriaza_film(self, id_client, film):
        """
        Fucntie care se asigura ca id-ul este valid si apeleaza functia de repo
        :param id_client: id-ul clientului
        :param film: filmul care se inchiriaza
        :return:
        """
        client = self.__repo_client.cauta_client_dupa_id(id_client)
        self.__validator_client.valideaza(client)
        self.__repo_client.inchiriaza_film(id_client, film)

    def return_film(self, id_client, film):
        """
        Functie care se asigura ca id-ul clientului este valid si apeleaza functia de repo
        :param id_client: id-ul clientului
        :param film: filmul care urmeaza sa fie returnat
        :return:
        """
        client = self.__repo_client.cauta_client_dupa_id(id_client)
        self.__validator_client.valideaza(client)
        self.__repo_client.return_film(id_client, film)

    def get_clienti_cu_filme(self):
        """
        Functie care gaseste toti clientii ce au filme inchiriate
        :return: lista de clienti si nuamrul filmelor inchiriate
        """
        clienti = self.__repo_client.get_clienti_cu_filme()
        return clienti


class ServiceClientFile(ServiceClient):

    def __init__(self, filename):
        ServiceClient.__init__(self, validator_client=ValidatorClient(), repo_client=RepoClient())
        self.__filename = filename
        self.__load_from_file()

    @staticmethod
    def __creaza_client_line(line):
        """
        Functie care face rost de parametrii de pe o linie din fisier
        :param line:
        :return:
        """
        params = line.split(" ")
        return int(params[0]), params[1], params[2]

    def __load_from_file(self):
        """
        Functie care ia toate datele din fisier
        :return:
        """
        fh = open(self.__filename, "r")
        for line in fh:
            if line.strip() == "":
                continue
            id_client, nume_client, cnp_client = self.__creaza_client_line(line)
            ServiceClient.adauga_client(self, id_client, nume_client, cnp_client)
        fh.close()

    def adauga_client(self, id_client, nume_client, cnp_client):
        """
        Functie care adauga un client in lista
        :param id_client:
        :param nume_client:
        :param cnp_client:
        :return:
        """
        client = ServiceClient.adauga_client(self, id_client, nume_client, cnp_client)
        self.__append_to_file(client)

    def __append_to_file(self, client):
        """
        Functie care adauga un client in fisier
        :param client:
        :return:
        """
        fh = open(self.__filename, "a")
        line = str(client.get_id_client() + " " + client.get_nume_client() + " " + client.get_cnp_client())
        fh.write("\n")
        fh.write(line)

    def cauta_client_dupa_id(self, id_client):
        """
        Functie care cauta un client dupa id
        :param id_client:
        :return:
        """
        return ServiceClient.cauta_client_dupa_id(self, id_client)

    def actualizeaza_client(self, id_client, params):
        """
        Functie care actualizeaza un client
        :param id_client:
        :param params:
        :return:
        """
        ServiceClient.actualizeaza_client(self, id_client, params)
        self.__actualizeaza_file()

    def __actualizeaza_file(self):
        """
        Functie care actualizeaza fisierul
        :return:
        """
        fh = open(self.__filename, "w")
        clienti = ServiceClient.get_all_clienti(self)
        for client in clienti:
            line = str(client.get_id_client() + " " + client.get_nume_client() + " " + client.get_cnp_client())
            fh.write(line)
            fh.write("\n")
        fh.close()

    def sterge_client(self, id_client):
        """
        Functie care sterge un client
        :param id_client:
        :return:
        """
        ServiceClient.sterge_client(self, id_client)
        self.__actualizeaza_file()


'''def test_adauga_client():
    validator_client = ValidatorClient()
    repo_client = RepoClient()
    test_srv = ServiceClient(validator_client, repo_client)
    assert test_srv.adauga_client(12, 'Tony', '32341414953')


def test_sterge_client():
    validator_client = ValidatorClient()
    repo_client = RepoClient()
    test_srv = ServiceClient(validator_client, repo_client)
    test_srv.adauga_client(12, 'Tony', '32341414953')

    client_sters = test_srv.sterge_client(12)
    assert (client_sters.get_id_client() == 12)
    assert (client_sters.get_nume_client() == 'Tony')
    assert (client_sters.get_cnp_client() == '32341414953')

    try:
        test_srv.sterge_client(1)
        assert False
    except ValueError:
        assert True


def test_actualizeaza_client():
    validator_client = ValidatorClient()
    repo_client = RepoClient()
    test_srv = ServiceClient(validator_client, repo_client)
    test_srv.adauga_client(12, 'Tony', '12323123124')

    params = [1, 'Tony', '111111111111']
    client_test = test_srv.actualizeaza_client(12, params)
    assert (client_test.get_id_client() == 1)
    assert (client_test.get_nume_client() == 'Tony')
    assert (client_test.get_cnp_client() == '111111111111')


def all_teste():
    test_adauga_client()
    test_sterge_client()
    test_actualizeaza_client()


all_teste()'''
