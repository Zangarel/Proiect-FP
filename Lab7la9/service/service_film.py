from termcolor import colored

from domain.filme import Filme
from erori.repo_error import RepoError
from repository.repo_film import RepoFilm
from validate.validare_film import ValidatorFilm


class ServiceFilm:

    def __init__(self, validator_film, repo_film):
        self.__validator_film = validator_film
        self.__repo_film = repo_film

    def adauga_film(self, id_film, titlu_film, gen_film):
        """
        Functie de service care se asigura ca datele filmului sunt valide si apeleaza functia de repo pentru a adauga filmul in lista
        :param id_film: id-ul clientului
        :param titlu_film: numele clientului
        :param gen_film: cnp-ul clientului
        :return:
        """
        film = Filme(id_film, titlu_film, gen_film)
        self.__validator_film.valideaza(film)
        self.__repo_film.adauga_film(film)
        return film

    def sterge_film(self, id_film):
        """
        Functie de service care apeleaza functia de repo
        :param id_film: id-ul  filmului cautat
        :return: True daca repo nu ridica erori
        """
        return self.__repo_film.sterge_film(id_film)

    def actualizeaza_film(self, id_film, params):
        """
        Functie de service care citeste noile date si apeleaza functia de repo
        :param params: lista de parametrii
        :param id_film: id-ul filmului cautat
        :return: True daca repo nu ridica erori
        """
        film_nou = Filme(params[0], params[1], params[2])
        self.__validator_film.valideaza(film_nou)
        return self.__repo_film.actualizeaza_film(id_film, film_nou)

    def get_random_id(self):
        """
        Functie care apeleaza functia din repo care genereaza un id random
        :return: id-ul random
        """
        return self.__repo_film.get_random_id()

    def get_random_titlu(self):
        """
        Functie care genereaza un titlu random
        :return: titlul random
        """
        return self.__repo_film.get_random_titlu()

    def get_random_gen(self):
        """
        Functie care genereaza un gen random
        :return: gen random
        """
        return self.__repo_film.get_random_gen()

    def cauta_film_dupa_id(self, id_film):
        """
        Functie de service care apeleaza functia de repo
        :param id_film: id-ul filmului cautat
        :return: filmul daca acesta exista
        """
        return self.__repo_film.cauta_film_dupa_id(id_film)

    def get_all_filme(self):
        """
        Functie de service care extrage lista de filme
        :return: lista de filme
        """
        return self.__repo_film.get_all_filme()

    def get_all_filme_disponibile(self):
        """
        Functie care apeleaza functia de repo pentru a gasi filmele disponibile si verifica daca exista filme
        :return:
        """
        filme_disponibile = self.__repo_film.get_all_filme_disponibile()
        if len(filme_disponibile) > 0:
            return filme_disponibile
        else:
            raise RepoError("Toate filmele sunt inchiriate")

    def inchiriaza_film(self, id_film):
        """
        Functie care se asigura ca filmul nu este deja inchiriat si apeleaza repo sa faca atribuirea
        :param id_film: id-ul filmului dorit sa fie inchiriat
        :return:
        """
        film = self.__repo_film.cauta_film_dupa_id(id_film)
        self.__validator_film.valideaza_film_inchiriere(film)
        self.__repo_film.inchiriaza_film(id_film)

    def return_film(self, id_film):
        """
        :param id_film: id-ul filmului returnat
        :return:
        """
        film = self.__repo_film.cauta_film_dupa_id(id_film)
        self.__validator_film.valideaza_film_returnare(film)
        self.__repo_film.return_film(id_film)

    def most_filme_inchiriate(self, key, _reversed):
        """
        Gaseste filmele inchiriate
        :param _reversed: True daca lista se va sorta descrescator, False crescator
        :return: lista de filme sortate
        """
        lista_filme = self.__repo_film.most_filme_inchiriate()
        lista_filme_sortat = self.__repo_film.merge_sort(lista_filme, key, _reversed)
        return lista_filme_sortat

    def get_clienti_cu_filme_procent_mai_mare(self, clienti, index):
        """
        Raportul care trebuia creat de noi
        :param clienti:
        :param index:
        :return:
        """
        lungime = 50 * len(clienti) / 100
        if index >= lungime:
            return 0
        else:
            print(colored(clienti[index], 'blue'))
            self.print_in_file(clienti[index])
            self.get_clienti_cu_filme_procent_mai_mare(clienti, index+1)

    @staticmethod
    def print_in_file(client):
        """
        Functie care adauga un client in fisier pentru raportul creat de mine
        :param client:
        :return:
        """
        fh = open("raport.txt", "w")
        client_fisier = str(str(client.get_id_client()) + " " + client.get_nume_client() + " " + str(client.get_cnp_client()))
        fh.write(client_fisier)
        fh.write("\n")
        fh.close()


class ServiceFilmFile(ServiceFilm):

    def __init__(self, filename):
        ServiceFilm.__init__(self, validator_film=ValidatorFilm(), repo_film=RepoFilm())
        self.__filename = filename
        self.__load_from_file()

    @staticmethod
    def __creaza_film_line(line):
        """
        Functie care scoate toti parametrii de pe o linie din fisier
        :param line:
        :return:
        """
        params = line.split(" ")
        return int(params[0]), params[1], params[2]

    def __load_from_file(self):
        """
        Incarca toate datele in fisier
        :return:
        """
        fh = open(self.__filename, "r")
        for line in fh:
            if line.strip() == "":
                continue
            id_film, titlu_film, gen_film = self.__creaza_film_line(line)
            ServiceFilm.adauga_film(self, id_film, titlu_film, gen_film)
        fh.close()

    def adauga_film(self, id_film, titlu_film, gen_film):
        """
        Functie care adauga un film
        :param id_film: id_ul filmului
        :param titlu_film: titlul
        :param gen_film: gen
        :return:
        """
        film = ServiceFilm.adauga_film(self, id_film, titlu_film, gen_film)
        self.__append_to_file(film)

    def __append_to_file(self, film):
        """
        Functie care adauga un film in fisier
        :param film:
        :return:
        """
        fh = open(self.__filename, "a")
        line = str(str(film.get_id_film()) + " " + film.get_titlu_film() + " " + film.get_gen_film())
        fh.write("\n")
        fh.write(line)

    def cauta_film_dupa_id(self, id_film):
        """
        Functie care cauta un film dupa id
        :param id_film:
        :return:
        """
        return ServiceFilm.cauta_film_dupa_id(self, id_film)

    def actualizeaza_film(self, id_film, params):
        """
        Functie care actualizeaza un film
        :param id_film:
        :param params: datele cu care se va actualiza filmul
        :return:
        """
        ServiceFilm.actualizeaza_film(self, id_film, params)
        self.__actualizeaza_file()

    def inchiriaza_film(self, id_film):
        ServiceFilm.inchiriaza_film(self, id_film)
        self.__actualizeaza_file()

    def __actualizeaza_file(self):
        """
        Functie care actualizeaza cu totul fisierul
        :return:
        """
        fh = open(self.__filename, "w")
        filme = ServiceFilm.get_all_filme(self)
        for film in filme:
            if film.get_disponibil() is True:
                line = str(str(film.get_id_film()) + " " + film.get_titlu_film() + " " + film.get_gen_film())
                fh.write(line)
                fh.write("\n")
        fh.close()

    def sterge_film(self, id_film):
        """
        Functie care sterge un film dupa id
        :param id_film:
        :return:
        """
        ServiceFilm.sterge_film(self, id_film)
        self.__actualizeaza_file()

    def most_filme_inchiriate(self, key, _reversed):
        """
        Functie care gaseste cele mai inchiriate filme de pana acum
        :param key:
        :param _reversed:
        :return:
        """
        return ServiceFilm.most_filme_inchiriate(self, key, _reversed)


'''def test_adauga_film():
    validator_film = ValidatorFilm()
    repo_film = RepoFilm()
    test_srv = ServiceFilm(validator_film, repo_film)
    assert test_srv.adauga_film(12, 'Avatar', 'actiune')


def test_sterge_film():
    validator_film = ValidatorFilm()
    repo_film = RepoFilm()
    test_srv = ServiceFilm(validator_film, repo_film)
    test_srv.adauga_film(12, 'Avatar', 'actiune')

    film_sters = test_srv.sterge_film(12)
    assert (film_sters.get_id_film() == 12)
    assert (film_sters.get_titlu_film() == 'Avatar')
    assert (film_sters.get_gen_film() == 'actiune')

    try:
        test_srv.sterge_film(1)
        assert False
    except ValueError:
        assert True


def test_actualizeaza_film():
    validator_film = ValidatorFilm()
    repo_film = RepoFilm()
    test_srv = ServiceFilm(validator_film, repo_film)
    test_srv.adauga_film(12, 'Avatar', 'actiune')

    params = [1, 'Roma', 'drama']
    film_test = test_srv.actualizeaza_film(12, params)
    assert (film_test.get_id_film() == 1)
    assert (film_test.get_titlu_film() == 'Roma')
    assert (film_test.get_gen_film() == 'drama')


def all_teste():
    test_adauga_film()
    test_sterge_film()
    test_actualizeaza_film()


all_teste()
'''
