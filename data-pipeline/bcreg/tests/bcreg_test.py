
from bcreg.bcregistries import BCRegistries
from bcreg.tests.bcregistries_baseline import BCRegistriesBaseline


def test_connect_bcreg():
    with BCRegistries() as bcreg:
	    assert True

def test_connect_bcreg_baseline():
    with BCRegistriesBaseline() as bcreg:
	    assert True

