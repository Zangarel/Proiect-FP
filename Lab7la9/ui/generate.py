"""
Trebuie sa generez random x filme sau clienti cu nume si id random
din generate apelez functia de service care va face toata treaba
"""
from termcolor import colored

from domain.client import Client
from domain.filme import Filme


class Generate:

    def __init__(self, service_film, service_client):
        self.__service_film = service_film
        self.__service_client = service_client

    def generate_filme(self, x):
        """
        Functie care genereaza random x filme
        :param x: numarul de filme
        :return:
        """
        for i in range(x):
            id_film = self.__service_film.get_random_id()
            titlu_film = self.__service_film.get_random_titlu()
            gen_film = self.__service_film.get_random_gen()
            film = Filme(id_film, titlu_film, gen_film)
            print(colored(str(film), 'blue'), '\n')

    def generate_clienti(self, x):
        """
        Functie care genereaza random x clienti
        :param x: numarul de clienti
        :return:
        """
        for i in range(x):
            id_client = self.__service_client.get_random_id()
            nume_client = self.__service_client.get_random_nume()
            cnp_client = self.__service_client.get_random_cnp()
            client = Client(id_client, nume_client, cnp_client)
            print(colored(str(client), 'blue'), '\n')
