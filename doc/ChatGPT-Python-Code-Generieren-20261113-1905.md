# Python Code Generieren

**User:** Anonymous  
**Created:** 2026/11/13 15:51:13  
**Updated:** 2026/11/13 19:02:13  
**Exported:** 2026/11/13 19:05:08  
**Link:** [<https://chatgpt.com/c/6af723e0-e6e8-83ed-beca-cf5ed1cda0f8>](https://chatgpt.com/c/6af723e0-e6e8-83ed-beca-cf5ed1cda0f8)

## Prompt:

11/13/2026, 3:57:19 PM

generiere python-code aus diesem pseudo-YAML-code

der python-code soll die verschiedenen typen von objekten (drucker, toner, drums) als verschiedene objekte darstellen, die miteinander verbunden sind (ein drucker funktioniert nur mit bestimmten tonern und drums)

code zur "auswertung" (abschätzung der druckkosten) brauche ich erstmal nicht, dafür ist die datenbank zu klein (also das kann man locker "per hand" auswerten)

mein pseudo-YAML-code ist eine kleine "datenbank" für druckkosten von laserdruckern. mich interessieren dabei vor allem die druckkosten mit "compatible toner", weil der deutlich billiger sein kann als der original toner. mein trauriges fazit ist mal wieder: nur der hersteller "Brother" ist interessant für mich als privatkunde, und davon nur der drucker "Brother HL-L6250DN"

``` yaml
- Preisvergleich:
    - Drucker: https://geizhals.de/?cat=prl&xf=11561_einfarbig~11501_A4~11514_347*780&pagesize=30&sort=eintr&promode=true
- Drucker
    - Brother HL-L6250DN
        - Preisvergleich: https://geizhals.de/brother-hl-l6250dn-hll6250dng1-a1391294.html
            - Angebote: 20
            - Preis: ab 320 Euro
        - Hersteller: https://store.brother.de/geraete/laser/hl/hll6250dn
        - Print speed: 46 ppm
        - Toner: TN-3430, TN-3480, TN-3512
        - Drums: DR-3400
    - Brother HL-L5100DN
        - Preisvergleich: https://geizhals.de/brother-hl-l5100dn-hll5100dng1-a1409933.html
            - Angebote: 11 (Tendenz fallend, discontinued, "end of life")
            - Preis: ab 500 Euro
        - Nachteile: kleines Papierfach (250 Blatt), teuer
        - Print speed: 40 ppm
        - Toner: TN-3430, TN-3480
        - Drums: DR-3400
    - Brother HL-L6410DN
        - Preisvergleich: https://geizhals.de/brother-hl-l6410dn-hll6410dnre1-a3035862.html
            - Angebote: 45
            - Preis: ab 590 Euro
        - Hersteller: https://store.brother.de/geraete/laser/hl/hll6410dn
        - Nachteile:
            - Chipped Toner
            - Touchscreen-Display (unnötig komplex)
            - Display steht raus (nicht stapelbar)
        - Print speed: 50 ppm
        - Toner: TN-3600, TN-3600XL, TN-3600XXL, TN-3610, TN-3610XL
        - Drums: DR-3600
    - HP LaserJet Pro 500 M501dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-pro-500-m501dn-j8h61a-a1406195.html
            - Angebote: 60
            - Preis: ab 310 Euro
        - Print speed: 43 ppm
        - Verbrauchsmaterial: CF287AS, CF287A, CF287X
        - Toner: 
        - Drums: 
    - Kyocera Ecosys PA4500x
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa4500x-110c0y3nl0-a2880137.html
            - Angebote: 53
            - Preis: ab 360 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 45 ppm
        - Verbrauchsmaterial: TK-3400
        - Toner: 
        - Drums: 
    - Kyocera Ecosys PA5500x
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa5500x-110c0w3nl0-a2880207.html
            - Angebote: 52
            - Preis: ab 510 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 40 ppm
        - Verbrauchsmaterial: TK-3430
        - Toner: 
        - Drums: 
    - Kyocera Ecosys PA5000x
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa5000x-110c0x3nl0-a2880190.html
            - Angebote: 42
            - Preis: ab 610 Euro
        - Nachteile:
            - Display steht raus (nicht stapelbar)
            - langsam
        - Print speed: 36 ppm
        - Verbrauchsmaterial: TK-3410
        - Toner: 
        - Drums: 
    - Kyocera Ecosys PA6000x
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa6000x-110c0t3nl0-a2926312.html
            - Angebote: 37
            - Preis: ab 730 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 43 ppm
        - Verbrauchsmaterial: TK-3440
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise 5502dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-5502dn-675r6a-a3933816.html
            - Angebote: 31
            - Preis: ab 620 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 50 ppm
        - Verbrauchsmaterial: 159A, 159X, 159Y
        - Toner: 
        - Drums: 
    - Lexmark MS823dn
        - Preisvergleich: https://geizhals.de/lexmark-ms823dn-50g0220-a1841772.html
            - Angebote: 30
            - Preis: ab 590 Euro
        - Hersteller: https://www.lexmark.com/en_us/printers/printer/12443/Lexmark-MS823dn
        - Nachteile:
            - schwer (25.4kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
            - "Compatible Toner" ist zu teuer, circa 10 Mal teurer bei Brother
        - Print speed: 61 ppm (TODO A4?)
            - Print Speed: 65 ppm (pages per minute) (Letter)
            - Print Speed Duplex: 39 spm (sheets per minute) (Letter) (78 pages per minute)
        - Print volume:
            - Recommended Page Volume: 5_000 - 75_000 pages per month
            - Maximum Duty Cycle: 300_000 pages per month
        - Toner: 
            - Lexmark 58D0UA0
                - Lexmark MS823, 825, MX822, MS/MX725, 826 55K Toner Cartridge
                - Hersteller: https://www.lexmark.com/en_us/printers/supply/12488/Lexmark-MS823-825-MX822-MS-MX725-826-55K-Toner-Cartridge
                - Part Number: 58D0UA0
                - Reichweite: 55_000 A4-Seiten (TODO verify)
                - Retail Price: $796.99
                - Ebay: 840 Euro (Original)
        - Compatible Toner:
            - https://www.ebay.de/itm/298062382715
                - Händler: Print-Klex aus Reinbek bei Hamburg
                - Reichweite: 15_000 A4-Seiten (TODO verify)
                - Preis: EUR 1_403.10 Euro / 10 Toner = 140.31 / 1 Toner = 0.935 Cent / A4-Seite
        - Drums: 
            - Lexmark 58D0ZA0
                - Lexmark MS/MX725, 822, 826, MS821, 823, 825, B2865, MB2770, M5255, 5270, XM5355, 5370, 7355, 7365, 7370 150K Imaging Unit
                - Hersteller: https://www.lexmark.com/en_us/printers/supply/12504/Lexmark-MS-MX725-822-826-MS821-823-825-B2865-MB2770-M5255-52
                - Part Number: 58D0ZA0
                - Reichweite: 15_000 A4-Seiten (TODO verify)
                    - Original Reichweite: 55_000 A4-Seiten
                - Retail Price: $129.99
                - Ebay: 150 Euro (Original)
    - Lexmark MS826de
        - Preisvergleich: https://geizhals.de/lexmark-ms826de-50g0330-a1841766.html
            - Angebote: 19
            - Preis: ab 730 Euro
        - Hersteller: https://www.lexmark.com/en_us/printers/printer/12398/Lexmark-MS826de
        - Part Number: Lexmark 50G0310
        - Nachteile:
            - schwer (25.6kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
            - Out of Stock
        - Print speed: 66 ppm
        - Verbrauchsmaterial: 58D0UA0, 58D0ZA0
        - Toner:
            - Lexmark 58D0UA0
        - Drums:
            - Lexmark 58D0ZA0
    - Lexmark MS725dvn
        - Preisvergleich: https://geizhals.de/lexmark-ms725dvn-50g0630-a1880225.html
            - Angebote: 17
            - Preis: ab 690 Euro
        - Nachteile: schwer (25.4kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
        - Print speed: 52 ppm
        - Verbrauchsmaterial: 58D2000, 58D2X00, 58D2U00, 58D0Z00, 58D0ZA0
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise 5501dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-5501dn-a29z3a-a3861149.html
            - Angebote: 28
            - Preis: ab 500 Euro
        - Hersteller: https://www.hp.com/us-en/shop/pdp/hp-laserjet-enterprise-5501dn-printer
        - Nachteile:
            - kein "Compatible Toner"
        - Print speed: 47 ppm
        - Toner:
            - HP 159Y: 26_000 pages, $510.99
            - HP 159X: 10_000 pages, $317.99
            - HP 159A: 5_000 pages, $207.99
        - Drums: 
    - Kyocera Ecosys PA4500x/Plus
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa4500x-plus-870b6110c0y3nl3-a3211335.html
            - Angebote: 28
            - Preis: ab 500 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 45 ppm
        - Verbrauchsmaterial: TK-3400
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise 6501dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-6501dn-675t2a-a3933798.html
            - Angebote: 26
            - Preis: ab 710 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 55 ppm
        - Verbrauchsmaterial: 160A, 160Y
        - Toner: 
        - Drums: 
    - Kyocera Ecosys PA5500x Plus
        - Preisvergleich: https://geizhals.de/kyocera-ecosys-pa5500x-kl3-870b6110c0w3nl0-a2926360.html
            - Angebote: 25
            - Preis: ab 870 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 40 ppm
        - Verbrauchsmaterial: TK-3430
        - Toner: 
        - Drums: 
    - Lexmark MS632dwe
        - Preisvergleich: https://geizhals.de/lexmark-ms632dwe-38s0510-a2971133.html
            - Angebote: 25
            - Preis: ab 370 Euro
        - Nachteile:
            - Touchscreen
            - langsam
        - Print speed: 24 ppm
        - Verbrauchsmaterial: 66S2000, 66S0HA0, 66S2H00, 66S2X00, 66S0Z00, 66S0ZA0
        - Toner: 
        - Drums: 
    - Lexmark MS821dn
        - Preisvergleich: https://geizhals.de/lexmark-ms821dn-50g0120-a1841553.html
            - Angebote: 24
            - Preis: ab 540 Euro
        - Nachteile: 
        - Print speed: 52 ppm
        - Verbrauchsmaterial: 52D2000, 52D2H00, 52D200E, 52D2H0E
        - Toner: 
        - Drums: 
    - OKI B512dn
        - Preisvergleich: 
            - Angebote: 23
            - Preis: ab 420 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 45 ppm
        - Verbrauchsmaterial: 45807102, 45807106, 45807111, 44574302
        - Toner: 
        - Drums: 
    - Lexmark MS631dw
        - Preisvergleich: https://geizhals.de/lexmark-ms631dw-38s0410-a2971157.html
            - Angebote: 20
            - Preis: ab 460 Euro
        - Nachteile: langsam
        - Print speed: 24 ppm
        - Verbrauchsmaterial: 66S2000, 66S0HA0, 66S2H00, 66S2X00, 66S0Z00, 66S0ZA0
        - Toner: 
        - Drums: 
    - Canon i-SENSYS LBP325x
        - Preisvergleich: https://geizhals.de/canon-i-sensys-lbp325x-3515c004-a2121604.html
            - Angebote: 18
            - Preis: ab 430 Euro
        - Nachteile: 
        - Print speed: 43 ppm
        - Verbrauchsmaterial: 056L, 056, 056H
        - Toner: 
        - Drums: 
    - Canon i-SENSYS LBP335dw
        - Preisvergleich: https://geizhals.de/canon-i-sensys-lbp335dw-7063c007-a3860951.html
            - Angebote: 18
            - Preis: ab 400 Euro
        - Nachteile: 
        - Print speed: 43 ppm
        - Verbrauchsmaterial: 
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise 8501dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-8501dn-9s187a-a3933806.html
            - Angebote: 17
            - Preis: ab 3200 Euro
        - Nachteile:
            - teuer
            - schwer (65.47kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
        - Print speed: 70 ppm
        - Verbrauchsmaterial: 176A
        - Toner: 
        - Drums: 
    - Lexmark MS822de
        - Preisvergleich: https://geizhals.de/lexmark-ms822de-50g0130-a1841729.html
            - Angebote: 17
            - Preis: ab 410 Euro
        - Nachteile: 
        - Print speed: 52 ppm
        - Verbrauchsmaterial: 52D2000, 52D2H00, 52D200E, 52D2H0E
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise M507dn
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-m507dn-1pv87a-a2046647.html
            - Angebote: 15
            - Preis: ab 660 Euro
        - Nachteile: Display steht raus (nicht stapelbar)
        - Print speed: 43 ppm
        - Verbrauchsmaterial: 89A, 89X
        - Toner: 
        - Drums: 
    - Xerox VersaLink B620DN
        - Preisvergleich: https://geizhals.de/xerox-versalink-b620dn-b620v-dn-a3083685.html
            - Angebote: 15
            - Preis: ab 940 Euro
        - Hersteller: https://www.xerox.de/de-de/office-produkte/drucker/versalink-b620
        - Nachteile:
            - Display steht raus (nicht stapelbar)
            - Touchscreen
            - teuer
            - schwer (22.3kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
            - kein "Compatible Toner"
        - Print speed: 61 ppm
        - Verbrauchsmaterial: 106R03940, 106R03942, 106R03944, 101R00582
        - Toner:
            - Xerox 006R04670
                - Reichweite: 42_000 A4-Seiten
                - Preis: € 632,33
            - Xerox 006R04668
                - Reichweite: 10_000 A4-Seiten
                - Preis: € 328,81
        - Drums:
            - Xerox 013R00699
                - Reichweite: 150_000 A4-Seiten
                - Preis: € 155,83
    - RICOH P 800
        - Preisvergleich: https://geizhals.de/ricoh-p-800-418470-a2135136.html
            - Angebote: 13
            - Preis: ab 650 Euro
        - Nachteile: 
        - Print speed: 55 ppm
        - Verbrauchsmaterial: 
        - Toner: 
        - Drums: 
    - HP LaserJet Enterprise 8501x
        - Preisvergleich: https://geizhals.de/hp-laserjet-enterprise-8501x-aj7j3a-a3933821.html
            - Angebote: 12
            - Preis: ab 4000 Euro
        - Nachteile:
            - teuer
            - schwer (93.72kg) (TODO warum so schwer? Tandem-Druckwerk? = Single-Pass Duplex?)
        - Print speed: 70 ppm
        - Verbrauchsmaterial: 176A
        - Toner: 
        - Drums: 
    - Lexmark M3350
        - Preisvergleich: https://geizhals.de/lexmark-m3350-38s0960-a2978693.html
            - Angebote: 9
            - Preis: ab 1000 Euro
        - Nachteile: langsam
        - Print speed: 24 ppm
        - Verbrauchsmaterial: 66S2000, 66S0HA0, 66S2H00, 66S2X00, 66S0Z00, 66S0ZA0
        - Toner: 
        - Drums: 
- Toner
    - Brother TN-3512
        - Drucker: Brother HL-L6250DN
        - Reichweite: 12_000 A4-Seiten (TODO verify)
        - Compatible Toner:
            - https://www.ebay.de/sch/i.html?_nkw=kompatibel+Brother+TN-3512+10x+-Nachf%C3%BClltinte
            - https://www.ebay.de/itm/158025454203
                - Händler: Eurotone aus Berlin
                - Reichweite: 12_000 A4-Seiten bei 5% Deckung (TODO verify)
                - Preis: 326.94 Euro / (3x 10 Toner) = 10.898 Euro / 1 Toner = 0.091 Cent / A4-Seite
                    - 0.1255 Cent / A4-Seite bei 0.725 tatsächlicher Reichweite
    - Brother TN-3480
        - Drucker: Brother HL-L6250DN, Brother HL-L5100DN
        - Reichweite: 8_000 A4-Seiten (TODO verify)
        - Vorteile: Große Mengen verfügbar
        - Compatible Toner:
            - https://www.ebay.de/itm/318623446358?var=616947382603
                - Händler: TemQuilifyh aus Krefeld bei Düsseldorf
                - Packung: 12 Toner pro Karton
                - Reichweite: 5_800 A4-Seiten bei 5% Deckung
                    - 5_800 / 8_000 = 0.725 von der angeblichen Reichweite
                - Preis: 758.28 Euro / (12x 8 Toner) = 7.89875 Euro / 1 Toner = 0.136 Cent / A4-Seite
                - Preis: 1_516.56 Euro / (24x 8 Toner) = 7.89875 Euro / 1 Toner = 0.136 Cent / A4-Seite
    - Brother TN-3430
        - Reichweite: 3_000 A4-Seiten (TODO verify)
        - Drucker: Brother HL-L6250DN, Brother HL-L5100DN
        - Nachteile: Zu Klein
    - Brother TN-3610XL
        - Drucker: Brother HL-L6410DN
        - Reichweite: 25_000 A4-Seiten (TODO verify)
        - Nachteile: Chipped Toner
        - Compatible Toner:
            - https://www.ebay.de/itm/366612715117
                - Händler: Conrad Electronic aus Hirschau bei Traunstein bei München
                - Reichweite: 25_000 A4-Seiten (TODO verify)
                - Preis: 627.75 Euro / 45 Toner = 13.95 Euro / 1 Toner = 0.0558 Cent / A4-Seite
                - Nachteile: Nur kleine Mengen
                - Frage: kann ich davon auch größere mengen kaufen? also palettenweise...? aktuell kann ich ja nur 45 stück kaufen, das reicht mir vielleicht für 2 wochen...
            - https://www.ebay.de/itm/227083538865
                - Händler: Völkner aus Wernberg-Köblitz bei Nürnberg
                - Reichweite: 25_000 A4-Seiten (TODO verify)
                - Preis: 260.33 Euro / 23 Toner = 11.3186 Euro / 1 Toner = 0.04527 Cent / A4-Seite
                - Nachteile: Nur kleine Mengen
                - Frage: kann ich davon auch größere mengen kaufen? also palettenweise...? aktuell kann ich ja nur 23 stück kaufen, das reicht mir vielleicht für eine woche...
                    - Antwort: Leider haben wir nur die auf eBay angezeigte Menge verfügbar.
            - https://www.ebay.de/itm/318230269728
                - Händler: Farbmister (tinte-tone_0) aus Heppenheim bei Frankfurt
                - Reichweite: 25_000 A4-Seiten (TODO verify)
                - Preis: 541.12 Euro / 19 Toner = 28.48 Euro / 1 Toner = 0.11392 Cent / A4-Seite
                - Nachteile: Nur kleine Mengen
                - Frage: kann ich davon auch größere mengen kaufen? also palettenweise...? aktuell kann ich ja nur 19 stück kaufen, das reicht mir vielleicht für eine woche...
                    - Antwort: Ja natürlich können Sie das
                    - Frage: aha, warum dann nur "19 verfügbar", und auch sonst gibt es keinen händler der diese "compatible toner" in größeren mengen verkauft...? das ist ein "chipped toner", also scheinbar nicht so leicht zu fälschen...
                    - Antwort: 19 Stück x 10,00 EURO = 190,00 EURO inkl. Versand
                    - Antwort: Sie können auch 100 Stück bekommen
                    - Antwort: 19 Stück für 190,00 € wie kommen Sie auf 29,98 € für 19 Stück ich glaube Sie sollten mal eine Schule besuchen
                    - Antwort: tinte-tone_0 hat einen Preisvorschlag gesendet: EUR 10,00
                    - Antwort: Für 1,57 € verkaufen wir keine TN-3610
    - Brother TN-3610
        - Drucker: Brother HL-L6410DN
        - Reichweite: 18_000 A4-Seiten (TODO verify)
        - Nachteile: Zu Klein, Chipped Toner
    - Brother TN-3600XXL
        - Drucker: Brother HL-L6410DN
        - Reichweite: 11_000 A4-Seiten (TODO verify)
        - Nachteile: Zu Klein, Chipped Toner
    - Brother TN-3600XL
        - Drucker: Brother HL-L6410DN
        - Reichweite: 6_000 A4-Seiten (TODO verify)
        - Nachteile: Zu Klein, Chipped Toner
    - Brother TN-3600
        - Drucker: Brother HL-L6410DN
        - Reichweite: 3_000 A4-Seiten (TODO verify)
        - Nachteile: Zu Klein, Chipped Toner
- Drums
    - Brother DR-3600
        - Drucker: Brother HL-L6410DN
        - Reichweite: 75_000 A4-Seiten (TODO verify)
    - Brother DR-3400
        - Reichweite: 50_000 A4-Seiten (TODO verify)
```

## Response:

11/13/2026, 3:58:07 PM

> **Defining Printer Supplies Database Models**
>
> **Fixing Printer Database Iteration Error**
>
> **Defined printer supply models and fixed database iteration errors**
>
> Worked for 53s

Ich würde deine Drucker-Datenbank in Python mit **`dataclasses` und echten Objektreferenzen** umsetzen. Damit bekommst du eine kleine, übersichtliche Objektdatenbank, ohne SQL, ORM, YAML-Parser oder externe Bibliotheken.

Die wichtigsten Eigenschaften:

- **`Drucker`, `Toner` und `Drum`** sind eigenständige Python-Klassen.
- **Kompatibilität über Objektreferenzen:** Ein Drucker kennt seine kompatiblen Toner und Trommeln. Derselbe Toner kann mehreren Druckern zugeordnet sein.
- **`Angebot`** als eigene Klasse für Original- und kompatible Toner, inklusive Händler, Preis, Menge, Reichweite und URL.
- **Keine automatische Druckkostenberechnung.** Deine bereits recherchierten Cent-pro-Seite-Werte können als Daten gespeichert werden.
- **Unbekannte Werte bleiben `None`.** Fehlende Informationen werden nicht geraten.
- **Kommentare, TODOs, Nachteile und Händlerantworten** bleiben erhalten, soweit sie für deine Recherche relevant sind.

Ich würde außerdem zwischen einem Tonermodell (z. B. `Brother TN-3480`) und einem konkreten Angebot eines Händlers unterscheiden. Das ist gerade für deinen Schwerpunkt auf kompatiblen Tonern wichtig.

Beispielsweise kannst du später direkt auf die Beziehungen zugreifen:

Hier ist die Umsetzung als vollständiges Python-Skript mit deinen Daten.

## Vollständiger Python-Code

<row align="center" gap={3}>
  <box background="surface-secondary" radius="lg" padding={3}>
    <icon name="file-code" size="2xl"/>
  </box>
  <box flex="1" gap={1}>
    **drucker_datenbank.py**

    <text color="secondary" size="xs">Python 3.10+ · Standardbibliothek · ausführbar und getestet</text>

  </box>
  <button color="primary" onClick={() => GenUI.openUrl("sandbox:/mnt/data/drucker_datenbank.py")}>Datei öffnen</button>
</row>

[Python-Datei herunterladen](sandbox:/mnt/data/drucker_datenbank.py)

Die Datei enthält deine 29 Druckermodelle, 14 explizit erfasste Tonermodelle, 4 Trommelmodelle sowie die recherchierten Angebote. Die übrigen Verbrauchsmaterialnummern bleiben vorerst als Listen erhalten, solange ihre genaue Zuordnung zu Toner oder Trommel nicht geklärt ist.

## So sind die Objekte miteinander verbunden

<box border radius="xl" padding={3} gap={2}>
  <svg viewBox="0 0 340 220" width="100%" xmlns="http://www.w3.org/2000/svg">
    <rect x="73" y="8" width="194" height="48" rx="9" fill="#2563eb" fillOpacity=".14" stroke="#3b82f6"/>
    <text x="170" y="27" textAnchor="middle" fontSize="12" fontWeight="600" fill="currentColor">Brother HL-L6250DN</text>
    <text x="170" y="44" textAnchor="middle" fontSize="10" fill="currentColor">Drucker</text>
    {#each [57,170,283] as x}
      <path d={`M170 56 V76 H${x} V98`} stroke="#64748b" strokeWidth="1.5" fill="none"/>
    {/each}
    {#each [{x:8,t:"TN-3430"},{x:121,t:"TN-3480"},{x:234,t:"TN-3512"}] as item}
      <rect x={item.x} y="98" width="98" height="41" rx="7" fill="#16a34a" fillOpacity=".12" stroke="#16a34a"/>
      <text x={item.x+49} y="114" textAnchor="middle" fontSize="11" fontWeight="600" fill="currentColor">{item.t}</text>
      <text x={item.x+49} y="128" textAnchor="middle" fontSize="10" fill="currentColor">Toner</text>
    {/each}
    <path d="M170 139 V167" stroke="#64748b" strokeWidth="1.5" strokeDasharray="4 3"/>
    <rect x="112" y="168" width="116" height="40" rx="7" fill="#d97706" fillOpacity=".12" stroke="#d97706"/>
    <text x="170" y="184" textAnchor="middle" fontSize="11" fontWeight="600" fill="currentColor">Angebote</text>
    <text x="170" y="198" textAnchor="middle" fontSize="10" fill="currentColor">Händler / Preise</text>
  </svg>
  <caption>Vereinfachter Ausschnitt: Die DR-3400-Trommel ist ebenfalls direkt mit dem Drucker verknüpft. Angebote gehören jeweils zu einem Tonermodell.</caption>
</box>

Ein weiterer wichtiger Punkt: Die Beziehungen funktionieren **in beide Richtungen**.

Das ist eine echte Objektstruktur und keine Sammlung voneinander unabhängiger Dictionaries.

**Wichtig:** Die Preise, Reichweiten und Kompatibilitäten wurden aus deinem Ausgangstext übernommen, nicht extern verifiziert. Offene TODOs und widersprüchliche Angaben sind entsprechend gekennzeichnet.

Für deine derzeitige Datenbankgröße halte ich diese Lösung für ausreichend. Du kannst neue Drucker, Toner, Trommeln und Händlerangebote ergänzen, ohne bereits jetzt eine SQL-Datenbank oder eine Auswertungslogik einführen zu müssen.

## Prompt:

11/13/2026, 4:01:04 PM

nein, das ist hässlicher code.  
wenn ich da einen neuen drucker eintragen will, dann muss ich gefühlt an 10 verschiedenen stellen die neuen daten eintragen...  
nein, die struktur sollte ähnlich sein wie in meiner pseudo-YAML-datenbank, also alle eigenschaften von einem objekt (zum beispiel von einem drucker) sollten an einer stelle sein. ich brauche nur deswegen verschiedene typen von objekten (drucker, toner, drums), weil ein toner-modell kann kompatibel sein mit mehreren drucker-modellen (deduplikation)

## Response:

11/13/2026, 4:01:05 PM

Ja, dann war mein vorheriger Ansatz unnötig kompliziert. Du willst im Grunde **deine bisherige YAML-Struktur beibehalten**, aber mit Python-Objekten und Referenzen zwischen diesen Objekten.

Ich würde dafür `dataclasses` verwenden und die Daten **direkt bei der Definition des jeweiligen Objekts** eintragen.

Ein neuer Drucker benötigt dann genau einen Eintrag. Die Toner und Trommeln werden über ihre Modellnummer referenziert.

## 1. Die Objektklassen

``` python
from dataclasses import dataclass, field

@dataclass
class Angebot:
    url: str
    haendler: str
    preis_eur: float | None = None
    anzahl: int | None = None
    reichweite: int | None = None
    kosten_cent_pro_seite: float | None = None
    notizen: list[str] = field(default_factory=list)

@dataclass
class Toner:
    name: str
    reichweite: int | None = None
    nachteile: list[str] = field(default_factory=list)
    vorteile: list[str] = field(default_factory=list)
    compatible_toner: list[Angebot] = field(default_factory=list)

@dataclass
class Drum:
    name: str
    reichweite: int | None = None
    notizen: list[str] = field(default_factory=list)

@dataclass
class Drucker:
    name: str
    preisvergleich: str | None = None
    hersteller_url: str | None = None
    angebote: int | None = None
    preis_ab_eur: float | None = None
    print_speed_ppm: int | None = None
    toner: list[str] = field(default_factory=list)
    drums: list[str] = field(default_factory=list)
    nachteile: list[str] = field(default_factory=list)
    notizen: list[str] = field(default_factory=list)
```

## 2. Die eigentliche Datenbank

Die Daten stehen jetzt zusammenhängend an jeweils einer Stelle, ähnlich wie in deinem Pseudo-YAML.

Die Toner werden separat definiert, weil dieselben Tonermodelle in mehreren Druckern verwendet werden können.

Und die Trommeln:

## 3. Referenzen auflösen

Du brauchst nicht einmal eine zusätzliche Datenbankklasse.

Die Modellnummern dienen als Schlüssel. Damit kannst du die gemeinsamen Objekte direkt nachschlagen:

Ausgabe:

Das ist bereits Deduplication: Der TN-3480 existiert nur einmal, obwohl ihn mehrere Drucker verwenden.

Wenn du unbedingt echte Python-Objektreferenzen statt String-IDs möchtest, kannst du die Referenzen auch einmalig nach dem Anlegen aller Objekte auflösen. Für eine kleine, manuell gepflegte Datenbank würde ich das aber nicht unbedingt machen.

## 4. Noch eine Vereinfachung

Die redundante Angabe `name="Brother ..."` innerhalb eines Dictionaries mit demselben Schlüssel würde ich sogar entfernen.

Du könntest die Objekte stattdessen als einfache Listen anlegen:

Und bei Bedarf einen Index erzeugen:

**Meine Empfehlung für deine Anwendung:** Eine einzige Python-Datei mit drei Datenabschnitten (`drucker`, `toner`, `drums`), `dataclasses` für die Typdefinitionen und Modellnummern als Referenzen. Keine Registrierungsfunktionen, keine mehrfachen Kompatibilitätslisten, keine komplizierte Initialisierung.

Damit bleibt der Pflegeaufwand praktisch genauso gering wie bei deiner Pseudo-YAML-Datenbank.

## Prompt:

11/13/2026, 4:03:51 PM

# Selected text:

## Selection 1

Du könntest die Objekte stattdessen als einfache Listen anlegen:

## My request:

ja, so würde ich das auch machen, dann gibt es keine duplikation zwischen dem "dict key" und dem "drucker.name"

bitte generiere meine drucker-datenbank als python-code

## Response:

11/13/2026, 4:03:54 PM

> **Inspecting printer database script**
>
> ------------------------------------------------------------------------
>
> **Generating structured printer database code**
>
> Worked for 24s

Ich habe deine Drucker-Datenbank als Python-Datei umgesetzt - mit **Listen statt Dictionaries** und ohne doppelte Pflege von Modellnamen.

<row align="center" gap={3}>
  <icon name="file-code-2" size="2xl" color="secondary"/>
  <box flex="1" gap={1}>
    **drucker_datenbank.py**

    <text color="secondary" size="xs">547 Zeilen · Python 3.10+ · keine externen Bibliotheken</text>

  </box>
</row>

[Python-Datei herunterladen](sandbox:/mnt/data/drucker_datenbank.py)

Die Datei enthält:

- 29 Druckermodelle
- 14 Tonermodelle
- 4 Trommelmodelle
- Deine recherchierten Händlerangebote, Preise, Reichweiten, Nachteile und TODOs

## Aufbau

Die Daten stehen in drei einfachen Listen:

Jeder Toner wird nur einmal definiert. Händlerangebote stehen direkt beim jeweiligen Toner.

Die Referenzen lassen sich über einfache Funktionen auflösen:

Die Indizes (`DRUCKER_BY_NAME` usw.) werden automatisch aus den Listen erzeugt. Du musst sie nicht selbst pflegen.

**Getestet:** Das Skript lässt sich ausführen, und die Kompatibilitätsbeziehungen für den Brother HL-L6250DN funktionieren.

Die ursprünglichen Rechercheangaben habe ich übernommen, ohne Preise oder Reichweiten neu zu verifizieren.

## Prompt:

11/13/2026, 6:27:16 PM

ich kann die datei nicht runterladen: drucker_datenbank.py

> Failed to download file. Please try again later.

kannst du mir die datei hier in den chat schreiben?

## Response:

11/13/2026, 6:27:19 PM

> **Inspecting Drucker database script**
>
> **Displaying Full Python File Content**
>
> **Extracting Middle 200 Script Lines**
>
> **Inspected Drucker database script and extracted its full content**
>
> Worked for 10s

Ja. Ich schreibe dir die vollständige Datei direkt hier in den Chat, damit du sie ohne Download als `drucker_datenbank.py` speichern kannst.

Der Code enthält die drei Listen `DRUCKER`, `TONER` und `DRUMS`, die zugehörigen `dataclasses` sowie die Funktionen zum Auflösen der Kompatibilitätsbeziehungen. Es ist dieselbe 547 Zeilen lange Datei, die ich zuvor erstellt habe.

<CodeBlock language="python" editable>
"""Manuell gepflegte Laserdrucker-Datenbank.

Alle Eigenschaften eines Modells stehen in einem Eintrag.  
Toner-/Drum-Kompatibilität wird nur beim Drucker eingetragen.  
Keine Druckkostenberechnung, keine externen Abhängigkeiten.  
"""

from **future** import annotations

from dataclasses import dataclass, field  
from decimal import Decimal

# ============================================================

# Objektklassen

# ============================================================

@dataclass  
class Angebot:  
url: str  
haendler: str \| None = None  
preis_eur: Decimal \| None = None  
anzahl_toner: int \| None = None  
reichweite_seiten: int \| None = None  
cent_pro_seite: Decimal \| None = None  
hinweise: list\[str\] = field(default_factory=list)

@dataclass  
class Toner:  
name: str  
reichweite_seiten: int \| None = None  
hinweise: list\[str\] = field(default_factory=list)  
angebote: list\[Angebot\] = field(default_factory=list)  
hersteller_url: str \| None = None  
artikelnummer: str \| None = None

@dataclass  
class Drum:  
name: str  
reichweite_seiten: int \| None = None  
hinweise: list\[str\] = field(default_factory=list)  
hersteller_url: str \| None = None  
artikelnummer: str \| None = None  
preis_eur: Decimal \| None = None  
retail_preis_usd: Decimal \| None = None

@dataclass  
class Drucker:  
name: str  
preisvergleich_url: str \| None = None  
hersteller_url: str \| None = None  
angebote_anzahl: int \| None = None  
preis_ab_eur: Decimal \| None = None  
geschwindigkeit_ppm: int \| None = None  
nachteile: list\[str\] = field(default_factory=list)  
hinweise: list\[str\] = field(default_factory=list)  
verbrauchsmaterial: list\[str\] = field(default_factory=list)  
toner_ids: list\[str\] = field(default_factory=list)  
drum_ids: list\[str\] = field(default_factory=list)  
artikelnummer: str \| None = None

PREISVERGLEICH_URL = (  
"<https://geizhals.de/?cat=prl&xf=11561_einfarbig>"  
"~11501_A4~11514_347\*780&pagesize=30&sort=eintr"  
"&promode=true"  
)

# ============================================================

# Toner

# ============================================================

TONER = \[  
Toner(  
name="Brother TN-3512",  
reichweite_seiten=12_000,  
hinweise=\["Reichweite prüfen"\],  
angebote=\[  
Angebot(  
url="<https://www.ebay.de/sch/i.html?_nkw=kompatibel+Brother+TN-3512+10x+-Nachf%C3%BClltinte>",  
hinweise=\["Suchergebnis"\],  
),  
Angebot(  
url="<https://www.ebay.de/itm/158025454203>",  
haendler="Eurotone (Berlin)",  
preis_eur=Decimal("326.94"),  
anzahl_toner=30,  
reichweite_seiten=12_000,  
cent_pro_seite=Decimal("0.091"),  
hinweise=\[  
"5 % Deckung; Reichweite prüfen",  
"Bei 72,5 % tatsächlicher Reichweite: "  
"0,1255 Cent/Seite",  
\],  
),  
\],  
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

\]

# ============================================================

# Trommeln

# ============================================================

DRUMS = \[  
Drum(  
name="Brother DR-3600",  
reichweite_seiten=75_000,  
hinweise=\["Reichweite prüfen"\],  
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

\]

# ============================================================

# Drucker

# ============================================================

DRUCKER = \[  
Drucker(  
name="Brother HL-L6250DN",  
preisvergleich_url="<https://geizhals.de/brother-hl-l6250dn-hll6250dng1-a1391294.html>",  
hersteller_url="<https://store.brother.de/geraete/laser/hl/hll6250dn>",  
angebote_anzahl=20,  
preis_ab_eur=Decimal("320"),  
geschwindigkeit_ppm=46,  
toner_ids=\[  
"Brother TN-3430",  
"Brother TN-3480",  
"Brother TN-3512",  
\],  
drum_ids=\["Brother DR-3400"\],  
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
            "Empfohlen: 5.000-75.000 Seiten/Monat",
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

\]

# ============================================================

# Automatisch erzeugte Indizes

# ============================================================

DRUCKER_BY_NAME = {p.name: p for p in DRUCKER}  
TONER_BY_NAME = {t.name: t for t in TONER}  
DRUMS_BY_NAME = {d.name: d for d in DRUMS}

# ============================================================

# Beziehungen zwischen den Objekten

# ============================================================

def kompatible_toner(drucker: Drucker) -\> list\[Toner\]:  
return \[  
TONER_BY_NAME\[name\]  
for name in drucker.toner_ids  
\]

def kompatible_drums(drucker: Drucker) -\> list\[Drum\]:  
return \[  
DRUMS_BY_NAME\[name\]  
for name in drucker.drum_ids  
\]

def kompatible_drucker(toner: Toner) -\> list\[Drucker\]:  
return \[  
p for p in DRUCKER  
if toner.name in p.toner_ids  
\]

# ============================================================

# Validierung

# ============================================================

def validieren() -\> None:  
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

if **name** == "**main**":  
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

</CodeBlock>

Die Datei ist vollständig und benötigt nur die Python-Standardbibliothek. Speichere den Code als `drucker_datenbank.py` und starte ihn mit `python drucker_datenbank.py`.

Die noch nicht eindeutig als Toner oder Trommel klassifizierten Artikelnummern stehen weiterhin in `verbrauchsmaterial`. So bleiben deine recherchierten Informationen erhalten, ohne zusätzliche Objekte mit erfundenen Eigenschaften anzulegen.

------------------------------------------------------------------------

Powered by [ChatGPT Exporter](https://www.chatgptexporter.com)
