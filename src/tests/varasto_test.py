import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_negatiivinen_tavaraa(self):
        self.assertAlmostEqual(self.varasto.lisaa_varastoon(-10), None)

    def test_otetaan_negatiivinen_varastosta(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-10), 0)

    def test_varasto_negatiivinen_varasto_luo_tyhjan_varaston(self):
        uusi_varasto = Varasto(-10)
        self.assertAlmostEqual(uusi_varasto.tilavuus,0)

    def test_varasto_negatiivinen_alkusaldo_luoo_tyhjan_alkusaldon(self):
        uusi_varasto = Varasto(-10,-10)
        self.assertAlmostEqual(uusi_varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_varastoon_lisataan_liian_paljon_tavaraa(self):
        self.varasto.lisaa_varastoon(121)
        self.assertAlmostEqual(self.varasto.tilavuus, self.varasto.saldo)

    def test_varastosta_otetaan_liian_paljon(self):
        self.varasto.lisaa_varastoon(6)
        self.assertAlmostEqual(self.varasto.ota_varastosta(10),6)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_str_toimii(self):
        self.assertEqual(print(str(self.varasto)), "saldo = 0, vielä tilaa 10")

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(),2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(2)
        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
