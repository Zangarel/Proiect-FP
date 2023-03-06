from termcolor import colored

from erori.validation_error import ValidError


class ValidatorClient:

    def __init__(self):
        pass

    @staticmethod
    def valideaza(client):
        errors = []
        if client.get_id_client() == "":
            errors.append(colored("Id invalid", 'red'))
        if client.get_nume_client() == "":
            errors.append(colored("Numele introdus este invalid", 'red'))
        if len(client.get_cnp_client()) < 10:
            errors.append(colored("CNP introdus este invalid", 'red'))

        if len(errors) > 0:
            errors = '\n'.join(errors)
            raise ValidError(errors)
