import unittest

from domain.client import Client
from domain.filme import Filme
from erori.repo_error import RepoError
from erori.validation_error import ValidError
from repository.repo_client import RepoClient
from repository.repo_film import RepoFilm
from service.service_client import ServiceClient
from service.service_film import ServiceFilm
from validate.validare_client import ValidatorClient
from validate.validare_film import ValidatorFilm


class TesteBoxuri(unittest.TestCase):

    def setUp(self):
        self.controller = ServiceFilm(ValidatorFilm(), RepoFilm())
        self.controller_client = ServiceClient(ValidatorClient(), RepoClient())
        self.repo_film = RepoFilm()
        self.repo_client = RepoClient()
        self.controller.adauga_film(1, 'avatar', 'actiune')
        self.controller_client.adauga_client(1, 'Tony', '12321323222')

    def test_film_get_id(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_id_film() == 1)

    def test_film_get_titlu(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_titlu_film() == 'avatar')

    def test_film_get_gen(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_gen_film() == 'actiune')

    def test_film_get_disp(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_disponibil() is True)

    def test_film_set_disp_true(self):
        film = self.controller.cauta_film_dupa_id(1)
        film.set_disponibil_true()
        self.assertTrue(film.get_disponibil() is True)

    def test_film_set_disp_false(self):
        film = self.controller.cauta_film_dupa_id(1)
        film.set_disponibil_false()
        self.assertTrue(film.get_disponibil() is False)

    def test_film_get_inchirieri(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_inchirieri() == 0)

    def test_film_inc_inchrieri(self):
        film = self.controller.cauta_film_dupa_id(1)
        film.inc_inchirieri()
        self.assertTrue(film.get_inchirieri() == 1)

    def test_create(self):
        self.assertTrue(len(self.controller.get_all_filme()) == 1)

    def test_sterge(self):
        film_test = self.controller.cauta_film_dupa_id(1)
        film_sters = self.controller.sterge_film(1)
        self.assertTrue(len(self.controller.get_all_filme()) == 0)
        self.assertTrue(film_test.get_id_film() == film_sters.get_id_film())
        self.assertTrue(film_test.get_titlu_film() == film_sters.get_titlu_film())
        self.assertTrue(film_test.get_gen_film() == film_sters.get_gen_film())
        try:
            self.assertFalse(film_test.get_id_film() != film_sters.get_id_film())
        except ValueError:
            assert True
        try:
            self.assertFalse(film_test.get_titlu_film() != film_sters.get_titlu_film())
        except ValueError:
            assert True
        try:
            self.assertFalse(film_test.get_gen_film() != film_sters.get_gen_film())
        except ValueError:
            assert True

    def test_actualizeaza_film(self):
        params = [2, 'Roma', 'actiune']
        film_act = self.controller.actualizeaza_film(1, params)
        lista_filme = self.controller.get_all_filme()
        self.assertTrue(len(lista_filme) == 1)
        self.assertTrue(film_act.get_id_film() == 2)
        self.assertTrue(film_act.get_titlu_film() == 'Roma')
        self.assertTrue(film_act.get_gen_film() == 'actiune')
        try:
            params = [3, 'Avatar', 'drama']
            self.controller.actualizeaza_film(2, params)
            assert False
        except ValueError:
            assert True
        try:
            params = [3, '', 'drama']
            self.controller.actualizeaza_film(2, params)
            assert False
        except ValueError and ValidError:
            assert True
        try:
            params = [3, 'Avatar', '']
            self.controller.actualizeaza_film(2, params)
            assert False
        except ValueError and ValidError:
            assert True

    def test_adauga_film(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.repo_film.adauga_film(film)
        self.assertTrue(self.repo_film.cauta_film_dupa_id(1) == film)

    def test_sterge_film(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.repo_film.adauga_film(film)
        film_sters = self.repo_film.sterge_film(1)
        try:
            self.repo_film.sterge_film(1)
            assert False
        except ValueError:
            assert True
        self.assertTrue(film_sters == film)

    def test_cauta_film(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.repo_film.adauga_film(film)
        self.assertTrue(self.repo_film.cauta_film_dupa_id(1) == film)
        try:
            self.repo_film.cauta_film_dupa_id(2)
            assert False
        except ValueError:
            assert True

    def test_actualizeaza_film_repo(self):
        film = Filme(1, 'Avatar', 'actiune')
        film_nou = Filme(2, 'Roma', 'drama')
        self.repo_film.adauga_film(film)
        self.assertTrue(self.repo_film.actualizeaza_film(1, film_nou) == film_nou)
        self.repo_film.actualizeaza_film(1, film_nou)
        try:
            self.repo_film.actualizeaza_film(2, film_nou)
            assert False
        except ValueError:
            assert True

    def test_get_all_filme(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        lista = self.repo_film.get_all_filme()
        self.assertTrue(lista == [film])

    def test_get_all_filme_disp(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        lista = self.repo_film.get_all_filme_disponibile()
        self.assertTrue(lista == [film])
        film.set_disponibil_false()
        lista = self.repo_film.get_all_filme_disponibile()
        self.assertTrue(lista == [])

    def test_inchiriaza_film(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        self.repo_film.inchiriaza_film(1)
        lista = self.repo_film.get_all_filme_disponibile()
        self.assertTrue(lista == [])
        self.assertTrue(film.get_inchirieri() == 1)

    def test_return_filme(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        self.repo_film.inchiriaza_film(1)
        self.repo_film.return_film(1)
        lista = self.repo_film.get_all_filme_disponibile()
        self.assertTrue(lista == [film])

    def test_sort_lista_filme(self):
        film = Filme(1, 'Avatar', 'actiune')
        film2 = Filme(2, 'Roma', 'drama')
        film3 = Filme(3, 'Asdd', 'comedie')
        self.repo_film.adauga_film(film)
        self.repo_film.adauga_film(film2)
        self.repo_film.adauga_film(film3)
        self.repo_film.inchiriaza_film(2)
        self.repo_film.inchiriaza_film(3)
        self.repo_film.return_film(2)
        self.repo_film.inchiriaza_film(2)
        lista_filme = [film, film2, film3]
        lista_filme = self.repo_film.bingo_sort(lista_filme, len(lista_filme))
        self.assertEqual(lista_filme, [film, film2, film3])

    def test_cauta_film_dupa_id(self):
        film = self.controller.cauta_film_dupa_id(1)
        self.assertTrue(film.get_id_film() == 1)
        self.assertTrue(film.get_titlu_film() == 'avatar')
        self.assertTrue(film.get_gen_film() == 'actiune')
        try:
            self.controller.cauta_film_dupa_id(0)
            assert False
        except ValueError:
            assert True
        try:
            self.assertFalse(film.get_id_film() == 0)
        except ValueError:
            assert True
        try:
            self.assertFalse(film.get_titlu_film() == "")
        except ValueError:
            assert True
        try:
            self.assertFalse(film.get_gen_film() == "")
        except ValueError:
            assert True

    def test_cauta_film_dupa_id_blackbox(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.assertTrue(self.controller.cauta_film_dupa_id(1) == film)

    def test_client_get_id(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.assertTrue(client.get_id_client() == 1)

    def test_client_get_nume(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.assertTrue(client.get_nume_client() == 'Tony')

    def test_client_get_cnp(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.assertTrue(client.get_cnp_client() == '12321323222')

    def test_client_get_filme_inchiriate(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.assertTrue(client.get_filme_inchiriate() == [])

    def test_client_del_filme_inchriate(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        film = self.controller.cauta_film_dupa_id(1)
        client.del_filme_inchiriate(film)
        self.assertTrue(client.get_filme_inchiriate() == [])

    def test_client_set_filme_inchiriate(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        film = self.controller.cauta_film_dupa_id(1)
        client.set_filme_inchiriate(film)
        self.assertTrue(client.get_filme_inchiriate() == [film])

    def test_adauga_client(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.repo_client.adauga_client(client)
        self.assertTrue(self.repo_client.cauta_client_dupa_id(1) == client)

    def test_sterge_client(self):
        client = self.controller_client.cauta_client_dupa_id(1)
        self.repo_client.adauga_client(client)
        client_sters = self.repo_client.sterge_client(1)
        try:
            self.repo_client.sterge_client(1)
            assert False
        except ValueError:
            assert True
        self.assertTrue(client_sters == client)

    def test_cauta_client(self):
        client = Client(1, 'Tony', '23123123123212')
        self.repo_client.adauga_client(client)
        self.assertTrue(self.repo_client.cauta_client_dupa_id(1) == client)
        try:
            self.repo_client.cauta_client_dupa_id(2)
            assert False
        except RepoError:
            assert True

    def test_actualizeaza_client_repo(self):
        client = Client(1, 'Tony', '2321312321222')
        client_nou = Client(2, 'Victor', '4399989898999')
        self.repo_client.adauga_client(client)
        self.assertTrue(self.repo_client.actualizeaza_client(1, client_nou) == client_nou)
        self.repo_client.actualizeaza_client(1, client_nou)
        try:
            self.repo_client.actualizeaza_client(2, client_nou)
            assert False
        except ValueError:
            assert True

    def test_get_all_clienti(self):
        client = Client(1, 'Tony', '2132312322222')
        self.repo_client.adauga_client(client)
        lista = self.repo_client.get_all_clienti()
        self.assertTrue(lista == [client])

    def test_inchiriaza_film_client(self):
        client = Client(1, 'Tony', '2132312322222')
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_client.adauga_client(client)
        self.repo_film.adauga_film(film)
        self.repo_client.inchiriaza_film(1, film)
        self.assertTrue(client.get_filme_inchiriate() == [film])

    def test_return_film_client(self):
        client = Client(1, 'Tony', '2132312322222')
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_client.adauga_client(client)
        self.repo_film.adauga_film(film)
        self.repo_client.inchiriaza_film(1, film)
        self.repo_client.return_film(1, film)
        self.assertEqual(client.get_filme_inchiriate(), [])

    def test_get_clienti_cu_filme(self):
        client = Client(1, 'Tony', '2132312322222')
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_client.adauga_client(client)
        self.repo_film.adauga_film(film)
        self.repo_client.inchiriaza_film(1, film)
        clienti_filme = self.repo_client.get_clienti_cu_filme()
        self.assertTrue(clienti_filme == [client])
        try:
            self.assertTrue(clienti_filme == [])
            assert False
        except AssertionError:
            assert True

    def test_validate_client(self):
        client = Client('', 'Tony', '21231231231222')
        try:
            ValidatorClient.valideaza(client)
            assert False
        except ValidError:
            assert True
        client = Client('1', '', '21231231231222')
        try:
            ValidatorClient.valideaza(client)
            assert False
        except ValidError:
            assert True
        client = Client('1', 'Tony', '')
        try:
            ValidatorClient.valideaza(client)
            assert False
        except ValidError:
            assert True

    def test_validate_film(self):
        film = Filme('', 'Avatar', 'actiune')
        try:
            ValidatorFilm.valideaza(film)
            assert False
        except ValidError:
            assert True
        film = Filme(1, '', 'actiune')
        try:
            ValidatorFilm.valideaza(film)
            assert False
        except ValidError:
            assert True
        film = Filme(1, 'Avatar', '')
        try:
            ValidatorFilm.valideaza(film)
            assert False
        except ValidError:
            assert True

    def test_validate_inchiriere(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        film.set_disponibil_false()
        try:
            ValidatorFilm.valideaza_film_inchiriere(film)
            assert False
        except ValidError:
            assert True

    def test_validate_return(self):
        film = Filme(1, 'Avatar', 'actiune')
        self.repo_film.adauga_film(film)
        try:
            ValidatorFilm.valideaza_film_returnare(film)
            assert False
        except ValidError:
            assert True

    def test_bingo_sort(self):
        film = Filme(1, 'Avatar', 'actiune')
        film2 = Filme(2, 'Roma', 'drama')
        self.repo_film.adauga_film(film)
        self.repo_film.adauga_film(film2)
        self.repo_film.inchiriaza_film(1)
        lista_filme = [film, film2]
        self.assertTrue(self.repo_film.bingo_sort(lista_filme, len(lista_filme)) == [film, film2])

    def test_merge_sort(self):
        film = Filme(1, 'Avatar', 'actiune')
        film2 = Filme(2, 'Roma', 'drama')
        film.inc_inchirieri()
        film.inc_inchirieri()
        film2.inc_inchirieri()
        lista_filme = [film, film2]
        key = 'inchirieri'
        _reversed = False
        lista_sortata = self.repo_film.merge_sort(lista_filme, key, _reversed)
        self.assertTrue(lista_sortata == lista_filme)
