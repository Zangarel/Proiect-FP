from termcolor import colored

from erori.validation_error import ValidError


class ValidatorFilm:

    def __init__(self):
        pass

    @staticmethod
    def valideaza(film):
        """
        Functie care valideaza un film
        :param film: tip lista
        :return: True daca filmul este valid
        :raises: ValidError daca filmul nu este valid
        """
        errors = []
        if film.get_id_film() == "":
            errors.append(colored("Id invalid", 'red'))
        if film.get_titlu_film() == "":
            errors.append(colored("Titlul filmului este invalid", 'red'))
        if film.get_gen_film() == "":
            errors.append(colored("Filmul trebuie sa aiba un gen", 'red'))

        if len(errors) > 0:
            errors = "\n".join(errors)
            raise ValidError(errors)
        return True

    @staticmethod
    def valideaza_film_inchiriere(film):
        """
        Functie care verifica daca filmul este inchiriat
        :param film: filmul verificat
        :return: True daca filmul nu e inchiriat
        :raise: ValidError daca filmul este deja inchiriat
        """
        if film.get_disponibil() is False:
            raise ValidError("Filmul este deja inchiriat")
        return True

    @staticmethod
    def valideaza_film_returnare(film):
        """
        Functie care verifica daca filmul este valid
        :param film: filmul care trebuie validat
        :return: True daca filmul este inchiriat si valid
        :raise: ValidError daca filmul nu a fost inchiriat sau nu este valid
        """
        if film.get_disponibil() is True:
            raise ValidError("Filmul nu a fost inchiriat")
        return True

    @staticmethod
    def valideaza_cheie(key):
        """
        Functie care verifica daca cheia introdusa este valida
        :param key: cheia introdusa
        :return: True
        :raise: ValidError daca cheia nu este valida
        """
        if key != 'id' and key != 'alfabetic' and key != 'inchirieri':
            raise ValidError("Cheia introdusa nu este valida")
        return True
