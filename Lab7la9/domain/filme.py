class Filme:

    def __init__(self, id_film, titlu_film, gen_film):
        """
        :param id_film: id-ul filmului
        :param titlu_film: titlul filmului
        :param gen_film: genul filmului
        """

        '''self.__id_film = id_film
        self.__titlu_film = titlu_film
        self.__gen_film = gen_film
        self.__sters = False'''

        self.__id_film = id_film
        self.__titlu_film = titlu_film
        self.__gen_film = gen_film
        self.__dictionar_filme = {"ID": id_film, "titlul": titlu_film, "gen": gen_film, "disponibil": True, "inchirieri": 0}

    def inc_inchirieri(self):
        """
        Functie de incrementat inchirierile unui film
        :return:
        """
        self.__dictionar_filme["inchirieri"] += 1

    def get_inchirieri(self):
        """
        Functie de get a inchirierilor unui film
        :return:
        """
        return int(self.__dictionar_filme["inchirieri"])

    def set_disponibil_false(self):
        """
        Functie de set pentru un film care nu este disponibil
        :return:
        """
        self.__dictionar_filme["disponibil"] = False

    def set_disponibil_true(self):
        """
        Fucntie de set pentru un film care devine disponibil
        :return:
        """
        self.__dictionar_filme["disponibil"] = True

    def get_disponibil(self):
        """
        Functie de get pentru a determina disponibilitatea unui film
        :return: returneaza True daca un film este disponibil, False altfel
        """
        return self.__dictionar_filme["disponibil"]

    def get_id_film(self):
        """
        Functie de get pentru id-ul filmului
        :return: returneaza id film
        """
        # return self.__id_film
        return self.__dictionar_filme["ID"]

    def get_titlu_film(self):
        """
        Functie de get pentru titlul filmului
        :return: returneaza titlul filmului
        """
        # return self.__titlu_film
        return self.__dictionar_filme["titlul"]

    def get_gen_film(self):
        """
        Functie de get pentru genul filmului
        :return: returneaza genul filmului
        """
        # return self.__gen_film
        return self.__dictionar_filme["gen"]

    def __eq__(self, other):
        """
        Functie de suprascrie functia de egalitate
        :param other:
        :return: returneaza daca doua filme sunt egale
        """
        return self.__dictionar_filme["ID"] == other.__dictionar_filme["ID"]

    def __str__(self):
        """
        Functie care suprascrie functia de str
        :return: returneaza id-ul, titlul si genul filmului
        """
        return f"ID-ul filmului este: {self.__dictionar_filme['ID']}\nTitlul este: {self.__dictionar_filme['titlul']}\nGenul este: {self.__dictionar_filme['gen']}"


'''def test_adauga_film():
    film_test = Filme(12, 'Avatar', 'actiune')
    assert (film_test.get_id_film() == 12)
    assert (film_test.get_titlu_film() == 'Avatar')
    assert (film_test.get_gen_film() == 'actiune')


def all_teste():
    test_adauga_film()


all_teste()'''
