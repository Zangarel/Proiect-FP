import unittest

from domain.teste import TesteBoxuri
from ui.generate import Generate
from validate.validare_film import ValidatorFilm
from validate.validare_client import ValidatorClient
from service.service_film import ServiceFilmFile
from service.service_client import ServiceClient
from repository.repo_film import RepoFilmFile
from repository.repo_client import RepoClientFile
from ui.consola import UI

if __name__ == "__main__":
    validator_film = ValidatorFilm()
    validator_client = ValidatorClient()
    repo_film = RepoFilmFile("filme.txt")
    repo_client = RepoClientFile("clienti.txt")
    service_film = ServiceFilmFile("filme.txt")
    service_client = ServiceClient(validator_client, repo_client)
    generate_random = Generate(service_film, service_client)
    teste_boxuri = TesteBoxuri()
    # unittest.main()
    consola = UI(service_film, service_client, generate_random, teste_boxuri)
    consola.run()
