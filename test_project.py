from project import fjern, regnut_t, få_handling

def test_fjern(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: 1)
    sjokolade = [{"Nummer": 1,"Navn": "Freia","Pris i NOK": 27,"Butikk": "Meny",}]
    fjern(sjokolade)
    assert sjokolade == []


def test_regnut_t():
    sjokolade = [{"Nummer": 1,"Navn": "Freia","Pris i NOK": 27,"Butikk": "Meny",}]
    assert regnut_t(sjokolade) == f"\nTotal pris er 27 kroner."


def test_få_handling(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "l")
    assert få_handling() == "L"
