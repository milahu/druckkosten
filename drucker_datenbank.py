#!/usr/bin/env python3

"""Manuell gepflegte Laserdrucker-Datenbank.

Alle Eigenschaften eines Modells stehen in einem Eintrag.
Toner-/Drum-Kompatibilität wird nur beim Drucker eingetragen.
Keine Druckkostenberechnung, keine externen Abhängigkeiten.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal


# ============================================================
# Objektklassen
# ============================================================

@dataclass
class Angebot:
    url: str
    haendler: str | None = None
    preis_eur: Decimal | None = None
    anzahl_toner: int | None = None
    reichweite_seiten: int | None = None
    cent_pro_seite: Decimal | None = None
    hinweise: list[str] = field(default_factory=list)


@dataclass
class Toner:
    name: str
    reichweite_seiten: int | None = None
    hinweise: list[str] = field(default_factory=list)
    angebote: list[Angebot] = field(default_factory=list)
    hersteller_url: str | None = None
    artikelnummer: str | None = None


@dataclass
class Drum:
    name: str
    reichweite_seiten: int | None = None
    hinweise: list[str] = field(default_factory=list)
    hersteller_url: str | None = None
    artikelnummer: str | None = None
    preis_eur: Decimal | None = None
    retail_preis_usd: Decimal | None = None


@dataclass
class Drucker:
    name: str
    preisvergleich_url: str | None = None
    hersteller_url: str | None = None
    angebote_anzahl: int | None = None
    preis_ab_eur: Decimal | None = None
    geschwindigkeit_ppm: int | None = None
    nachteile: list[str] = field(default_factory=list)
    hinweise: list[str] = field(default_factory=list)
    verbrauchsmaterial: list[str] = field(default_factory=list)
    toner_ids: list[str] = field(default_factory=list)
    drum_ids: list[str] = field(default_factory=list)
    artikelnummer: str | None = None


PREISVERGLEICH_URL = (
    "https://geizhals.de/?cat=prl&xf=11561_einfarbig"
    "~11501_A4~11514_347*780&pagesize=30&sort=eintr"
    "&promode=true"
)


# ============================================================
# Toner
# ============================================================

TONER = [
    Toner(
        name="Brother TN-3512",
        reichweite_seiten=12_000,
        hinweise=["Reichweite prüfen"],
        angebote=[
            Angebot(
                url="https://www.ebay.de/sch/i.html?_nkw=kompatibel+Brother+TN-3512+10x+-Nachf%C3%BClltinte",
                hinweise=["Suchergebnis"],
            ),
            Angebot(
                url="https://www.ebay.de/itm/158025454203",
                haendler="Eurotone (Berlin)",
                preis_eur=Decimal("326.94"),
                anzahl_toner=30,
                reichweite_seiten=12_000,
                cent_pro_seite=Decimal("0.091"),
                hinweise=[
                    "5 % Deckung; Reichweite prüfen",
                    "Bei 72,5 % tatsächlicher Reichweite: "
                    "0,1255 Cent/Seite",
                ],
            ),
        ],
    ),

    Toner(
        name="Brother TN-3480",
        reichweite_seiten=8_000,
        hinweise=[
            "Reichweite prüfen",
            "Große Mengen verfügbar",
        ],
        angebote=[
            Angebot(
                url="https://www.ebay.de/itm/318623446358?var=616947382603",
                haendler="TemQuilifyh (Krefeld)",
                preis_eur=Decimal("758.28"),
                anzahl_toner=96,
                reichweite_seiten=5_800,
                cent_pro_seite=Decimal("0.136"),
                hinweise=[
                    "12 Toner pro Karton, 8 Kartons",
                    "5 % Deckung; 5.800/8.000 = 0,725",
                    "Alternative Menge: 192 Toner für 1.516,56 EUR",
                ],
            ),
        ],
    ),

    Toner(
        name="Brother TN-3430",
        reichweite_seiten=3_000,
        hinweise=["Reichweite prüfen", "Zu klein"],
    ),

    Toner(
        name="Brother TN-3610XL",
        reichweite_seiten=25_000,
        hinweise=["Reichweite prüfen", "Toner mit Chip"],
        angebote=[
            Angebot(
                url="https://www.ebay.de/itm/366612715117",
                haendler="Conrad Electronic (Hirschau)",
                preis_eur=Decimal("627.75"),
                anzahl_toner=45,
                reichweite_seiten=25_000,
                cent_pro_seite=Decimal("0.0558"),
                hinweise=[
                    "Reichweite prüfen",
                    "Nur kleine Mengen",
                    "Frage nach Palettenmengen offen",
                ],
            ),
            Angebot(
                url="https://www.ebay.de/itm/227083538865",
                haendler="Völkner (Wernberg-Köblitz)",
                preis_eur=Decimal("260.33"),
                anzahl_toner=23,
                reichweite_seiten=25_000,
                cent_pro_seite=Decimal("0.04527"),
                hinweise=[
                    "Reichweite prüfen",
                    "Nur kleine Mengen",
                    "Händler: Nur die auf eBay angezeigte "
                    "Menge verfügbar",
                ],
            ),
            Angebot(
                url="https://www.ebay.de/itm/318230269728",
                haendler="Farbmister / tinte-tone_0 (Heppenheim)",
                preis_eur=Decimal("541.12"),
                anzahl_toner=19,
                reichweite_seiten=25_000,
                cent_pro_seite=Decimal("0.11392"),
                hinweise=[
                    "Reichweite prüfen",
                    "Händler behauptet, auch 100 Stück liefern "
                    "zu können",
                    "Händlerkommunikation widersprüchlich: "
                    "19 Stück für 190 EUR, Preisvorschlag "
                    "10 EUR; 1,57 EUR/Stück abgelehnt",
                ],
            ),
        ],
    ),

    Toner(
        name="Brother TN-3610",
        reichweite_seiten=18_000,
        hinweise=[
            "Reichweite prüfen",
            "Zu klein",
            "Toner mit Chip",
        ],
    ),

    Toner(
        name="Brother TN-3600XXL",
        reichweite_seiten=11_000,
        hinweise=[
            "Reichweite prüfen",
            "Zu klein",
            "Toner mit Chip",
        ],
    ),

    Toner(
        name="Brother TN-3600XL",
        reichweite_seiten=6_000,
        hinweise=[
            "Reichweite prüfen",
            "Zu klein",
            "Toner mit Chip",
        ],
    ),

    Toner(
        name="Brother TN-3600",
        reichweite_seiten=3_000,
        hinweise=[
            "Reichweite prüfen",
            "Zu klein",
            "Toner mit Chip",
        ],
    ),

    Toner(
        name="Lexmark 58D0UA0",
        reichweite_seiten=55_000,
        hinweise=[
            "Reichweite prüfen",
            "MS823/825, MX822, MS/MX725, 826; "
            "55K Toner Cartridge",
            "Original: 796,99 USD Retail; 840 EUR eBay",
        ],
        hersteller_url=(
            "https://www.lexmark.com/en_us/printers/supply/"
            "12488/Lexmark-MS823-825-MX822-MS-MX725-826-"
            "55K-Toner-Cartridge"
        ),
        artikelnummer="58D0UA0",
        angebote=[
            Angebot(
                url="https://www.ebay.de/itm/298062382715",
                haendler="Print-Klex (Reinbek)",
                preis_eur=Decimal("1403.10"),
                anzahl_toner=10,
                reichweite_seiten=15_000,
                cent_pro_seite=Decimal("0.935"),
                hinweise=[
                    "Reichweite prüfen",
                    "140,31 EUR pro Toner",
                ],
            ),
        ],
    ),

    Toner(
        name="HP 159Y",
        reichweite_seiten=26_000,
        hinweise=["Original: 510,99 USD"],
    ),

    Toner(
        name="HP 159X",
        reichweite_seiten=10_000,
        hinweise=["Original: 317,99 USD"],
    ),

    Toner(
        name="HP 159A",
        reichweite_seiten=5_000,
        hinweise=["Original: 207,99 USD"],
    ),

    Toner(
        name="Xerox 006R04670",
        reichweite_seiten=42_000,
        hinweise=["Original: 632,33 EUR"],
    ),

    Toner(
        name="Xerox 006R04668",
        reichweite_seiten=10_000,
        hinweise=["Original: 328,81 EUR"],
    ),
]


# ============================================================
# Trommeln
# ============================================================

DRUMS = [
    Drum(
        name="Brother DR-3600",
        reichweite_seiten=75_000,
        hinweise=["Reichweite prüfen"],
    ),

    Drum(
        name="Brother DR-3400",
        reichweite_seiten=50_000,
        hinweise=["Reichweite prüfen"],
    ),

    Drum(
        name="Lexmark 58D0ZA0",
        reichweite_seiten=150_000,
        hinweise=[
            "150K Imaging Unit",
            "Im Ausgangstext widersprüchliche Reichweiten "
            "15.000/55.000; prüfen",
            "Original eBay: ca. 150 EUR",
        ],
        hersteller_url=(
            "https://www.lexmark.com/en_us/printers/supply/"
            "12504/Lexmark-MS-MX725-822-826-MS821-823-825-"
            "B2865-MB2770-M5255-52"
        ),
        artikelnummer="58D0ZA0",
        retail_preis_usd=Decimal("129.99"),
    ),

    Drum(
        name="Xerox 013R00699",
        reichweite_seiten=150_000,
        preis_eur=Decimal("155.83"),
    ),
]


# ============================================================
# Drucker
# ============================================================

DRUCKER = [
    Drucker(
        name="Brother HL-L6250DN",
        preisvergleich_url="https://geizhals.de/brother-hl-l6250dn-hll6250dng1-a1391294.html",
        hersteller_url="https://store.brother.de/geraete/laser/hl/hll6250dn",
        angebote_anzahl=20,
        preis_ab_eur=Decimal("320"),
        geschwindigkeit_ppm=46,
        toner_ids=[
            "Brother TN-3430",
            "Brother TN-3480",
            "Brother TN-3512",
        ],
        drum_ids=["Brother DR-3400"],
    ),

    Drucker(
        name="Brother HL-L5100DN",
        preisvergleich_url="https://geizhals.de/brother-hl-l5100dn-hll5100dng1-a1409933.html",
        angebote_anzahl=11,
        preis_ab_eur=Decimal("500"),
        geschwindigkeit_ppm=40,
        nachteile=[
            "Kleines Papierfach (250 Blatt)",
            "Teuer",
        ],
        hinweise=[
            "Angebote rückläufig",
            "Discontinued / End of Life",
        ],
        toner_ids=[
            "Brother TN-3430",
            "Brother TN-3480",
        ],
        drum_ids=["Brother DR-3400"],
    ),

    Drucker(
        name="Brother HL-L6410DN",
        preisvergleich_url="https://geizhals.de/brother-hl-l6410dn-hll6410dnre1-a3035862.html",
        hersteller_url="https://store.brother.de/geraete/laser/hl/hll6410dn",
        angebote_anzahl=45,
        preis_ab_eur=Decimal("590"),
        geschwindigkeit_ppm=50,
        nachteile=[
            "Toner mit Chip",
            "Touchscreen unnötig komplex",
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        toner_ids=[
            "Brother TN-3600",
            "Brother TN-3600XL",
            "Brother TN-3600XXL",
            "Brother TN-3610",
            "Brother TN-3610XL",
        ],
        drum_ids=["Brother DR-3600"],
    ),

    Drucker(
        name="HP LaserJet Pro 500 M501dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-pro-500-m501dn-j8h61a-a1406195.html",
        angebote_anzahl=60,
        preis_ab_eur=Decimal("310"),
        geschwindigkeit_ppm=43,
        verbrauchsmaterial=[
            "CF287AS",
            "CF287A",
            "CF287X",
        ],
    ),

    Drucker(
        name="Kyocera Ecosys PA4500x",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa4500x-110c0y3nl0-a2880137.html",
        angebote_anzahl=53,
        preis_ab_eur=Decimal("360"),
        geschwindigkeit_ppm=45,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["TK-3400"],
    ),

    Drucker(
        name="Kyocera Ecosys PA5500x",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa5500x-110c0w3nl0-a2880207.html",
        angebote_anzahl=52,
        preis_ab_eur=Decimal("510"),
        geschwindigkeit_ppm=40,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["TK-3430"],
    ),

    Drucker(
        name="Kyocera Ecosys PA5000x",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa5000x-110c0x3nl0-a2880190.html",
        angebote_anzahl=42,
        preis_ab_eur=Decimal("610"),
        geschwindigkeit_ppm=36,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
            "Langsam",
        ],
        verbrauchsmaterial=["TK-3410"],
    ),

    Drucker(
        name="Kyocera Ecosys PA6000x",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa6000x-110c0t3nl0-a2926312.html",
        angebote_anzahl=37,
        preis_ab_eur=Decimal("730"),
        geschwindigkeit_ppm=43,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["TK-3440"],
    ),

    Drucker(
        name="HP LaserJet Enterprise 5502dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-5502dn-675r6a-a3933816.html",
        angebote_anzahl=31,
        preis_ab_eur=Decimal("620"),
        geschwindigkeit_ppm=50,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=[
            "159A",
            "159X",
            "159Y",
        ],
    ),

    Drucker(
        name="Lexmark MS823dn",
        preisvergleich_url="https://geizhals.de/lexmark-ms823dn-50g0220-a1841772.html",
        hersteller_url="https://www.lexmark.com/en_us/printers/printer/12443/Lexmark-MS823dn",
        angebote_anzahl=30,
        preis_ab_eur=Decimal("590"),
        geschwindigkeit_ppm=61,
        nachteile=[
            "Schwer (25,4 kg)",
            "Kompatibler Toner ca. 10-mal teurer als bei Brother",
        ],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
            "61 ppm A4 prüfen; 65 ppm Letter",
            "Duplex 39 Blatt/min = 78 Seiten/min Letter",
            "Empfohlen: 5.000–75.000 Seiten/Monat",
            "Maximum: 300.000 Seiten/Monat",
        ],
        toner_ids=["Lexmark 58D0UA0"],
        drum_ids=["Lexmark 58D0ZA0"],
    ),

    Drucker(
        name="Lexmark MS826de",
        preisvergleich_url="https://geizhals.de/lexmark-ms826de-50g0330-a1841766.html",
        hersteller_url="https://www.lexmark.com/en_us/printers/printer/12398/Lexmark-MS826de",
        angebote_anzahl=19,
        preis_ab_eur=Decimal("730"),
        geschwindigkeit_ppm=66,
        nachteile=[
            "Schwer (25,6 kg)",
            "Out of stock",
        ],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
        ],
        verbrauchsmaterial=[
            "58D0UA0",
            "58D0ZA0",
        ],
        toner_ids=["Lexmark 58D0UA0"],
        drum_ids=["Lexmark 58D0ZA0"],
        artikelnummer="Lexmark 50G0310",
    ),

    Drucker(
        name="Lexmark MS725dvn",
        preisvergleich_url="https://geizhals.de/lexmark-ms725dvn-50g0630-a1880225.html",
        angebote_anzahl=17,
        preis_ab_eur=Decimal("690"),
        geschwindigkeit_ppm=52,
        nachteile=["Schwer (25,4 kg)"],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
        ],
        verbrauchsmaterial=[
            "58D2000",
            "58D2X00",
            "58D2U00",
            "58D0Z00",
            "58D0ZA0",
        ],
    ),

    Drucker(
        name="HP LaserJet Enterprise 5501dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-5501dn-a29z3a-a3861149.html",
        hersteller_url="https://www.hp.com/us-en/shop/pdp/hp-laserjet-enterprise-5501dn-printer",
        angebote_anzahl=28,
        preis_ab_eur=Decimal("500"),
        geschwindigkeit_ppm=47,
        nachteile=["Kein kompatibler Toner gefunden"],
        toner_ids=[
            "HP 159A",
            "HP 159X",
            "HP 159Y",
        ],
    ),

    Drucker(
        name="Kyocera Ecosys PA4500x/Plus",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa4500x-plus-870b6110c0y3nl3-a3211335.html",
        angebote_anzahl=28,
        preis_ab_eur=Decimal("500"),
        geschwindigkeit_ppm=45,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["TK-3400"],
    ),

    Drucker(
        name="HP LaserJet Enterprise 6501dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-6501dn-675t2a-a3933798.html",
        angebote_anzahl=26,
        preis_ab_eur=Decimal("710"),
        geschwindigkeit_ppm=55,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["160A", "160Y"],
    ),

    Drucker(
        name="Kyocera Ecosys PA5500x Plus",
        preisvergleich_url="https://geizhals.de/kyocera-ecosys-pa5500x-kl3-870b6110c0w3nl0-a2926360.html",
        angebote_anzahl=25,
        preis_ab_eur=Decimal("870"),
        geschwindigkeit_ppm=40,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=["TK-3430"],
    ),

    Drucker(
        name="Lexmark MS632dwe",
        preisvergleich_url="https://geizhals.de/lexmark-ms632dwe-38s0510-a2971133.html",
        angebote_anzahl=25,
        preis_ab_eur=Decimal("370"),
        geschwindigkeit_ppm=24,
        nachteile=[
            "Touchscreen",
            "Langsam",
        ],
        verbrauchsmaterial=[
            "66S2000",
            "66S0HA0",
            "66S2H00",
            "66S2X00",
            "66S0Z00",
            "66S0ZA0",
        ],
    ),

    Drucker(
        name="Lexmark MS821dn",
        preisvergleich_url="https://geizhals.de/lexmark-ms821dn-50g0120-a1841553.html",
        angebote_anzahl=24,
        preis_ab_eur=Decimal("540"),
        geschwindigkeit_ppm=52,
        verbrauchsmaterial=[
            "52D2000",
            "52D2H00",
            "52D200E",
            "52D2H0E",
        ],
    ),

    Drucker(
        name="OKI B512dn",
        angebote_anzahl=23,
        preis_ab_eur=Decimal("420"),
        geschwindigkeit_ppm=45,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=[
            "45807102",
            "45807106",
            "45807111",
            "44574302",
        ],
    ),

    Drucker(
        name="Lexmark MS631dw",
        preisvergleich_url="https://geizhals.de/lexmark-ms631dw-38s0410-a2971157.html",
        angebote_anzahl=20,
        preis_ab_eur=Decimal("460"),
        geschwindigkeit_ppm=24,
        nachteile=["Langsam"],
        verbrauchsmaterial=[
            "66S2000",
            "66S0HA0",
            "66S2H00",
            "66S2X00",
            "66S0Z00",
            "66S0ZA0",
        ],
    ),

    Drucker(
        name="Canon i-SENSYS LBP325x",
        preisvergleich_url="https://geizhals.de/canon-i-sensys-lbp325x-3515c004-a2121604.html",
        angebote_anzahl=18,
        preis_ab_eur=Decimal("430"),
        geschwindigkeit_ppm=43,
        verbrauchsmaterial=[
            "056L",
            "056",
            "056H",
        ],
    ),

    Drucker(
        name="Canon i-SENSYS LBP335dw",
        preisvergleich_url="https://geizhals.de/canon-i-sensys-lbp335dw-7063c007-a3860951.html",
        angebote_anzahl=18,
        preis_ab_eur=Decimal("400"),
        geschwindigkeit_ppm=43,
    ),

    Drucker(
        name="HP LaserJet Enterprise 8501dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-8501dn-9s187a-a3933806.html",
        angebote_anzahl=17,
        preis_ab_eur=Decimal("3200"),
        geschwindigkeit_ppm=70,
        nachteile=[
            "Teuer",
            "Schwer (65,47 kg)",
        ],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
        ],
        verbrauchsmaterial=["176A"],
    ),

    Drucker(
        name="Lexmark MS822de",
        preisvergleich_url="https://geizhals.de/lexmark-ms822de-50g0130-a1841729.html",
        angebote_anzahl=17,
        preis_ab_eur=Decimal("410"),
        geschwindigkeit_ppm=52,
        verbrauchsmaterial=[
            "52D2000",
            "52D2H00",
            "52D200E",
            "52D2H0E",
        ],
    ),

    Drucker(
        name="HP LaserJet Enterprise M507dn",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-m507dn-1pv87a-a2046647.html",
        angebote_anzahl=15,
        preis_ab_eur=Decimal("660"),
        geschwindigkeit_ppm=43,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
        ],
        verbrauchsmaterial=[
            "89A",
            "89X",
        ],
    ),

    Drucker(
        name="Xerox VersaLink B620DN",
        preisvergleich_url="https://geizhals.de/xerox-versalink-b620dn-b620v-dn-a3083685.html",
        hersteller_url="https://www.xerox.de/de-de/office-produkte/drucker/versalink-b620",
        angebote_anzahl=15,
        preis_ab_eur=Decimal("940"),
        geschwindigkeit_ppm=61,
        nachteile=[
            "Hervorstehendes Display (nicht stapelbar)",
            "Touchscreen",
            "Teuer",
            "Schwer (22,3 kg)",
            "Kein kompatibler Toner gefunden",
        ],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
        ],
        verbrauchsmaterial=[
            "106R03940",
            "106R03942",
            "106R03944",
            "101R00582",
        ],
        toner_ids=[
            "Xerox 006R04670",
            "Xerox 006R04668",
        ],
        drum_ids=["Xerox 013R00699"],
    ),

    Drucker(
        name="RICOH P 800",
        preisvergleich_url="https://geizhals.de/ricoh-p-800-418470-a2135136.html",
        angebote_anzahl=13,
        preis_ab_eur=Decimal("650"),
        geschwindigkeit_ppm=55,
    ),

    Drucker(
        name="HP LaserJet Enterprise 8501x",
        preisvergleich_url="https://geizhals.de/hp-laserjet-enterprise-8501x-aj7j3a-a3933821.html",
        angebote_anzahl=12,
        preis_ab_eur=Decimal("4000"),
        geschwindigkeit_ppm=70,
        nachteile=[
            "Teuer",
            "Schwer (93,72 kg)",
        ],
        hinweise=[
            "Gewicht / Tandem-Druckwerk / Single-Pass-Duplex prüfen",
        ],
        verbrauchsmaterial=["176A"],
    ),

    Drucker(
        name="Lexmark M3350",
        preisvergleich_url="https://geizhals.de/lexmark-m3350-38s0960-a2978693.html",
        angebote_anzahl=9,
        preis_ab_eur=Decimal("1000"),
        geschwindigkeit_ppm=24,
        nachteile=["Langsam"],
        verbrauchsmaterial=[
            "66S2000",
            "66S0HA0",
            "66S2H00",
            "66S2X00",
            "66S0Z00",
            "66S0ZA0",
        ],
    ),
]


# ============================================================
# Automatisch erzeugte Indizes
# ============================================================

DRUCKER_BY_NAME = {p.name: p for p in DRUCKER}
TONER_BY_NAME = {t.name: t for t in TONER}
DRUMS_BY_NAME = {d.name: d for d in DRUMS}


# ============================================================
# Beziehungen zwischen den Objekten
# ============================================================

def kompatible_toner(drucker: Drucker) -> list[Toner]:
    return [
        TONER_BY_NAME[name]
        for name in drucker.toner_ids
    ]


def kompatible_drums(drucker: Drucker) -> list[Drum]:
    return [
        DRUMS_BY_NAME[name]
        for name in drucker.drum_ids
    ]


def kompatible_drucker(toner: Toner) -> list[Drucker]:
    return [
        p for p in DRUCKER
        if toner.name in p.toner_ids
    ]


# ============================================================
# Validierung
# ============================================================

def validieren() -> None:
    for name, index, daten in (
        ("Drucker", DRUCKER_BY_NAME, DRUCKER),
        ("Toner", TONER_BY_NAME, TONER),
        ("Drum", DRUMS_BY_NAME, DRUMS),
    ):
        if len(index) != len(daten):
            raise ValueError(f"Doppelte {name}-Namen")

    for p in DRUCKER:
        for name in p.toner_ids:
            if name not in TONER_BY_NAME:
                raise ValueError(
                    f"Unbekannter Toner {name} bei {p.name}"
                )

        for name in p.drum_ids:
            if name not in DRUMS_BY_NAME:
                raise ValueError(
                    f"Unbekannte Trommel {name} bei {p.name}"
                )


# ============================================================
# Beispiel
# ============================================================

if __name__ == "__main__":
    validieren()

    p = DRUCKER_BY_NAME["Brother HL-L6250DN"]

    print(p.name)
    print("Toner:", [
        t.name for t in kompatible_toner(p)
    ])
    print("Drums:", [
        d.name for d in kompatible_drums(p)
    ])

    t = TONER_BY_NAME["Brother TN-3480"]

    print("Drucker für TN-3480:", [
        p.name for p in kompatible_drucker(t)
    ])

    print(
        f"{len(DRUCKER)} Drucker, "
        f"{len(TONER)} Toner, "
        f"{len(DRUMS)} Drums"
    )
