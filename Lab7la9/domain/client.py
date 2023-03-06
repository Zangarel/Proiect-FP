class Client:

    def __init__(self, id_client, nume_client, cnp_client):
        """

        :param id_client: id-ul clientului
        :param nume_client: numele clientului
        :param cnp_client: cnp-ul clientului
        """
        '''self.__id_client = id_client
        self.__nume_client = nume_client
        self.__cnp_client = cnp_client
        self.__sters = False'''
        self.__id_client = id_client
        self.__nume_client = nume_client
        self.__cnp_client = cnp_client
        self.__sters = False
        self.__dictionar_clienti = {"ID": id_client, "nume": nume_client, "cnp": cnp_client, "filme": []}

    def set_filme_inchiriate(self, film):
        """
        Functie de set pentru lista de filme inchiriate
        :return:
        """
        self.__dictionar_clienti["filme"].append(film)

    def del_filme_inchiriate(self, film):
        """
        Functie care sterge filmul inchiriat din contul clientului
        :param film: filmul care urmeaza a fi returnat
        :return:
        """
        liste_filme = self.__dictionar_clienti["filme"]
        noua_lista = [filme for filme in liste_filme if filme != film]
        self.__dictionar_clienti["filme"] = noua_lista

    def get_filme_inchiriate(self):
        """
        Functie de get pentru toate filmele inchiriate de un client
        :return: lista de filme inchiriate
        """
        return self.__dictionar_clienti["filme"]

    def get_id_client(self):
        """
        Functie de get pentru id-ul clientului
        :return: returneaza id client
        """
        # return self.__id_client
        return self.__dictionar_clienti["ID"]

    def get_nume_client(self):
        """
        Functie de get pentru numele clientului
        :return: returneaza numele clientului
        """
        # return self.__nume_client
        return self.__dictionar_clienti["nume"]

    def get_cnp_client(self):
        """
        Functie de get pentru cnp-ul clientului
        :return: returneaza cnp-ul clientului
        """
        # return self.__cnp_client
        return self.__dictionar_clienti["cnp"]

    def __eq__(self, other):
        """
        Functie de suprascrie functia de egalitate
        :param other:
        :return: returneaza daca doi clienti au acelasi id
        """
        return self.__dictionar_clienti["ID"] == other.__dictionar_clienti["ID"]

    def __str__(self):
        """
        Functie care suprascrie functia de str
        :return: returneaza id-ul, numele si cnp-ul clientului
        """
        return f"ID-ul clientului este: {self.__dictionar_clienti['ID']} \nNumele clientului este: {self.__dictionar_clienti['nume']} \nCNP-ul clientului este: {self.__dictionar_clienti['cnp']}"
