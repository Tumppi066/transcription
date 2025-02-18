### Asennusohjeet
1. Paina tältä sivulta vihreästä napista `Code` ja valitse `Download ZIP`. Tai käytä linkkiä [tästä](https://github.com/Tumppi066/transcription/archive/refs/heads/main.zip).
2. Asenna python (3.11 tai 3.12)
3. Asenna openai-whisper (`pip install openai-whisper`)
4. Siirrä .mp3 tiedosto kansioon jossa `main.py` on ja kirjoita konsoliin samassa kansiossa (`python main.py tiedostonimi.mp3`)

### Käyttöohjeet
Sovellus kirjoittaa kaksi eri tiedostoa. 
- `transcription.txt` on yksinkertainen tekstitiedosto josta voi suoraan kopioida ulostulon.
- `transcription.ass` on tekstitys formaatti jonka voi esimerkiksi siirtää VLC:n kautta videon päälle.

### Huomioita
- **Sovellus ei ota yhteyttä internettiin mallin lataamisen jälkeen**. Malli voidaan myös tallentaa kansioon etukäteen, jotta nettiä ei tarvita ollenkaan.
- **Sovellus ei tällä hetkell tiedä kuka puhuu**. Tämän lisään myöhemmin tarpeen vaatiessa.
- **Sovellus ei tällä hetkellä tue äänitteitä, joissa puhutaan monilla eri kielillä.**. Tämänkin voi lisätä myöhemmin.
- Sovellukselle voidaan tehdä käyttöliittymä ja normaalintyylinen .exe tiedosto, jos tätä tarvitsee tehdä pidemmälle.
- **Koska sovellus käyttää Whisper malleja tietokoneella eikä verkossa, toimii se vain tietokoneissa, joissa on yli 8gb RAM muistia.** Riippuen tietokoneen prosessorista aika joka litteroinnin prosessoimiseen menee voi vaihdella. Se voi olla useita kymmeniä minuutteja. Yleisesti aika on äänitteen pituus kertaa kaksi.
