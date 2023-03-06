import random

from termcolor import colored

from domain.filme import Filme


class RepoFilm:

    def __init__(self):
        self.__filme = {}

    def adauga_film(self, film):
        """
        Functie care adauga un film in lista de filme
        :param film: obiectul film
        :return:
        :raises: RepoError daca filmul nu exista
        """
        if film.get_titlu_film() == self.__filme:
            raise ValueError("Un film cu acest titlu exista deja")
        self.__filme[film.get_id_film()] = film

    def sterge_film(self, id_film):
        """
        Functie care sterge un film din lista
        :param id_film: id-ul filmului dorit
        :return:
        :raises: RepoError daca filmul nu exista
        """
        if id_film not in self.__filme:
            raise ValueError(colored("Film inexistent", 'red'))
        film_sters = self.__filme[id_film]
        del self.__filme[id_film]
        return film_sters

    @staticmethod
    def get_random_id():
        """
        Functie care genereaza un id random
        :return: id-ul random al filmului
        """
        id_random = random.randint(1, 9999999)
        return id_random

    @staticmethod
    def get_random_titlu():
        """
        Functie care imi genereaza un titlu random
        :return: titlul random
        """
        lista_filme = ['Avatar', 'Roma', 'Bleeding At My Past', 'Punished By My Wife', 'Call To The River', 'Shelter At The World', 'Hiding My Future', 'Arriving At The Champions', 'Visiting The Shadows', 'Invited By The Mist', 'Hurt By History', 'Screams At History', 'Life At The Commander', 'Life At Eternity', 'Signs Of The City']
        titlu_random = random.choice(lista_filme)
        return titlu_random

    @staticmethod
    def get_random_gen():
        """
        Functie care genereaza un gen random
        :return: gen random
        """
        lista_genuri = ['actiune', 'comedie', 'drama', 'horror', 'thriller', 'aventura']
        gen_random = random.choice(lista_genuri)
        return gen_random

    def cauta_film_dupa_id(self, id_film):
        """
        Functie care cauta un film dupa id
        :param id_film: id-ul filmului cautat
        :return: filmul cautat daca acesta exista
        :raises: RepoError daca filmul nu exista
        """
        if id_film not in self.__filme:
            raise ValueError(colored("Film inexistent"))
        return self.__filme[id_film]

    def actualizeaza_film(self, id_film, film_nou):
        """
        Functie care actualizeaza un film
        :param id_film: id film cautat
        :param film_nou: filmul actualizat
        :return:
        :raises: RepoError daca filmul nu exista
        """
        if id_film not in self.__filme:
            raise ValueError(colored("Film inexistent"))
        self.__filme[id_film] = film_nou
        return self.__filme[id_film]

    def get_all_filme(self):
        """
        Functie care stocheaza toate filmele intr-o lista
        :return: lista de filme
        """
        filme = []
        for id_film in self.__filme:
            filme.append(self.__filme[id_film])
        return filme

    def get_all_filme_disponibile(self):
        """
        Functie care gaseste toate filmele disponibile
        :return: lista de filme disponibile
        """
        new_list = []
        for id_film in self.__filme:
            film = self.__filme[id_film]
            if film.get_disponibil() is True:
                new_list.append(self.__filme[id_film])
        return new_list

    def inchiriaza_film(self, id_film):
        """
        Functie care atribuie filmul inchiriat unui client
        :param id_film:
        :return:
        """
        film = self.__filme[id_film]
        film.set_disponibil_false()
        film.inc_inchirieri()

    def return_film(self, id_film):
        """
        Functie pentru returnarea unui film
        :return:
        """
        film = self.__filme[id_film]
        film.set_disponibil_true()

    def most_filme_inchiriate(self):
        """
        Functie ce afla numarul de inchirieri al unui film
        :return: lista de filme inchiriate
        """
        lista_filme = []
        for id_film in self.__filme:
            film = self.__filme[id_film]
            if film.get_inchirieri() != 0:
                lista_filme.append(film)
        return lista_filme

    @staticmethod
    def cmp(film1, film2, key):
        """
        Functie care compara dupa cheie
        :param film1:
        :param film2:
        :param key1:
        :param key2:
        :return:
        """

        if key(film1)[0] < key(film2)[0]:
            return True
        elif key(film1)[0] == key(film2)[0]:
            if key(film1)[1] < key(film2)[1]:
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def merge_sort_final(start, finish, key, _reversed, cmp):
        """
        Functie de merge pentru doua jumatati
        :param cmp:
        :param key:
        :param start: punctul de inceput
        :param finish: punctul de final
        :param _reversed: True daca lista va fi sortata descrescator, False crescator
        :return: cele doua jumatati sortate
        """
        i = 0
        j = 0
        rez = []

        if _reversed is True:
            while i < len(start) and j < len(finish):
                '''if start[i].key(key) <= finish[j].key(key):'''
                if cmp(start[i], finish[j], key) is True:
                    rez.append(start[i])
                    i += 1
                else:
                    rez.append(finish[j])
                    j += 1

            while i < len(start):
                film1 = start[i]
                rez.append(film1)
                i += 1

            while j < len(finish):
                film2 = finish[j]
                rez.append(film2)
                j += 1
        else:
            while i < len(start) and j < len(finish):
                if cmp(start[i], finish[j], key) is False:
                    rez.append(start[i])
                    i += 1
                else:
                    rez.append(finish[j])
                    j += 1

            while i < len(start):
                film1 = start[i]
                rez.append(film1)
                i += 1

            while j < len(finish):
                film2 = finish[j]
                rez.append(film2)
                j += 1

        return rez

    def merge_sort(self, lista_filme, key, _reversed):
        """
        Functie de mergesort pentru lista de filme
        :param cmp:
        :param key:
        :param lista_filme: lista de filme iniante de sortare
        :param _reversed: True daca lista va fi sortata descrescator, False crescator
        :return: lista sortata
        caz favorabil: complexitate timp O(n * logn)
        caz nefavorabil: complexitate timp O(n * logn)
        caz mediu/general: complexitate timp O(n * logn)
        """
        if not lista_filme:
            return []
        else:
            if len(lista_filme) == 1:
                return [lista_filme[0]]
            else:
                return self.merge_sort_final(self.merge_sort(lista_filme[:len(lista_filme) // 2], key, _reversed), self.merge_sort(lista_filme[len(lista_filme) // 2:], key, _reversed), key, _reversed, self.cmp)

    @staticmethod
    def min_max(lista_filme, bingo, next_bingo):
        """
        Functie care gaseste filmul cu cele mai putine inchirieri
        :param lista_filme: lista de filme curenta
        :param bingo: elementul cel mai mic
        :param next_bingo: elementul urmator cel mai mic
        :return: bingo si next_bingo
        """
        for film in lista_filme:
            if bingo.get_inchirieri() < film.get_inchirieri():
                bingo = film
            if next_bingo.get_inchirieri() > film.get_inchirieri():
                next_bingo = film
        return bingo, next_bingo

    def bingo_sort(self, lista_filme, lungime):
        """
        Functie de bingo sort pentru lista de filme
        :param lista_filme: lista de filme inainte de sortare
        :param lungime: lungimea listei de filme
        :return:
        """
        bingo = lista_filme[0]
        next_bingo = lista_filme[0]
        bingo, next_bingo = self.min_max(lista_filme, bingo, next_bingo)
        largest_elem = next_bingo
        next_elem_pos = 0
        while bingo.get_inchirieri() < next_bingo.get_inchirieri():
            start_pos = next_elem_pos
            for i in range(start_pos, lungime):
                if lista_filme[i].get_inchirieri() == bingo.get_inchirieri():
                    aux = lista_filme[i]
                    lista_filme[i] = lista_filme[next_elem_pos]
                    lista_filme[next_elem_pos] = aux
                    next_elem_pos += 1
                elif lista_filme[i].get_inchirieri() < next_bingo.get_inchirieri():
                    next_bingo = lista_filme[i]
            bingo = next_bingo
            next_bingo = largest_elem
        return lista_filme


'''@staticmethod
    def sort_lista_filme(lista_filme):
        """
        Functie de sortare a unei liste de filme
        :param lista_filme: lista de filme inainte de sortare
        :return: lista de filme sortate
        """
        new_list = []
        ind_max = 0
        while len(lista_filme) > 0:
            for ind in range(len(lista_filme)):
                film = lista_filme[ind]
                maxim = 0
                ind_max = 0
                if film.get_inchirieri() > maxim:
                    maxim = film.get_inchirieri()
                    ind_max = ind
            new_list.append(lista_filme[ind_max])
            del lista_filme[ind_max]
        return new_list'''


class RepoFilmFile(RepoFilm):

    def __init__(self, filename):
        RepoFilm.__init__(self)
        self.__filename = filename
        self.__load_from_file()

    @staticmethod
    def __creaza_film_linie(line):
        params = line.split(" ")
        film = Filme(int(params[0]), params[1], params[2])
        return film

    def __load_from_file(self):
        fh = open(self.__filename)
        for line in fh:
            if line.strip() == "":
                continue
            film = self.__creaza_film_linie(line)
            RepoFilm.adauga_film(self, film)
        fh.close()

    def adauga_film(self, film):
        RepoFilm.adauga_film(self, film)
        self.__append_to_file(film)

    def __append_to_file(self, film):
        fh = open(self.__filename, "a")
        line = str(str(film.get_id_film()) + " " + film.get_titlu_film() + " " + str(film.get_gen_film()))
        fh.write("\n")
        fh.write(line)
        fh.close()

    def cauta_film_dupa_id(self, id_film):
        return RepoFilm.cauta_film_dupa_id(self, id_film)

    def actualizeaza_film(self, id_film, film_nou):
        RepoFilm.actualizeaza_film(self, id_film, film_nou)
        self.__actualizeaza_file()

    def inchiriaza_film(self, id_film):
        RepoFilm.inchiriaza_film(self, id_film)
        self.__actualizeaza_file()

    def __actualizeaza_file(self):
        fh = open(self.__filename, "w")
        filme = RepoFilm.get_all_filme(self)
        for film in filme:
            if film.get_disponibil is True:
                line = str(film.get_id_film() + " " + film.get_titlu_film() + " " + film.get_gen_film())
                fh.write(line)
                fh.write("\n")
        fh.close()

    def sterge_film(self, id_film):
        RepoFilm.sterge_film(self, id_film)
        self.__actualizeaza_file()

    def most_filme_inchiriate(self):
        """
        Functie care creeaza lista de filme inchiriate cel mai des pana acum
        :return:
        """
        return RepoFilm.most_filme_inchiriate(self)

    def merge_sort(self, lista_filme, key, _reversed):
        """
        Functie care sorteaza lista de filme folosind metoda merge sort
        :param lista_filme:
        :param _reversed:
        :return:
        """
        lista_finala = RepoFilm.merge_sort(self, lista_filme, key, _reversed)
        return lista_finala


'''    @staticmethod
    def test_adauga_film():
        film = Filme(12, 'Avatar', 'actiune')
        repo_film = RepoFilm()
        repo_film.adauga_film(film)

        filme = repo_film.cauta_film_dupa_id(12)
        assert (filme.get_id_film() == 12)
        assert (filme.get_titlu_film() == 'Avatar')
        assert (filme.get_gen_film() == 'actiune')

    @staticmethod
    def test_sterge_film():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        film_sters = repo_film.sterge_film(12)
        assert (film_sters.get_id_film() == 12)
        assert (film_sters.get_titlu_film() == 'Avatar')
        assert (film_sters.get_gen_film() == 'actiune')

        try:
            repo_film.sterge_film(1)
            assert False
        except ValueError:
            assert True

    @staticmethod
    def test_actualizeaza_film():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        film_nou = Filme(1, 'Roma', 'drama')
        repo_film.adauga_film(film_nou)
        film_test = repo_film.actualizeaza_film(12, film_nou)
        assert (film_test.get_id_film() == 1)
        assert (film_test.get_titlu_film() == 'Roma')
        assert (film_test.get_gen_film() == 'drama')

    @staticmethod
    def test_get_all_filme():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        lista_filme = repo_film.get_all_filme()
        for filme in lista_filme:
            assert (film == filme)

    @staticmethod
    def test_get_all_filme_disponibile():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)
        film.set_disponibil_false()

        lista_disp = repo_film.get_all_filme_disponibile()
        assert (lista_disp == [])

    @staticmethod
    def test_inchiriaza_film():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        repo_film.inchiriaza_film(film.get_id_film())
        assert (film.get_disponibil() is False)

    @staticmethod
    def test_return_film():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        repo_film.inchiriaza_film(film.get_id_film())
        repo_film.return_film(film.get_id_film())
        assert (film.get_disponibil() is True)

    @staticmethod
    def test_most_filme_inchiriate():
        repo_film = RepoFilm()
        film = Filme(12, 'Avatar', 'actiune')
        repo_film.adauga_film(film)

        repo_film.inchiriaza_film(film.get_id_film())
        lista_filme = repo_film.most_filme_inchiriate()
        assert (lista_filme == [film])


def all_teste():
    repo_film = RepoFilm()
    repo_film.test_adauga_film()
    repo_film.test_sterge_film()
    repo_film.test_actualizeaza_film()
    repo_film.test_get_all_filme()
    repo_film.test_get_all_filme_disponibile()
    repo_film.test_inchiriaza_film()
    repo_film.test_return_film()
    repo_film.test_most_filme_inchiriate()


all_teste()
'''