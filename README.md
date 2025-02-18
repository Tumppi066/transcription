### Asennusohjeet
1. Asenna python (3.11 tai 3.12)
2. Asenna openai-whisper (`pip install openai-whisper`)
3. Siirrä .mp3 tiedosto tähän kansioon ja kirjoita (`python main.py tiedostonimi.mp3`)

### Käyttöohjeet
Sovellus kirjoittaa kaksi eri tiedostoa. 
- `transcription.txt` on yksinkertainen tekstitiedosto josta voi suoraan kopioida ulostulon.
- `transcription.ass` on tekstitys formaatti jonka voi esimerkiksi siirtää VLC:n kautta videon päälle.

### Huomioita
- Sovellus ei ota yhteyttä internettiin mallin lataamisen jälkeen. Malli voidaan myös tallentaa kansioon etukäteen, jotta nettiä ei tarvita ollenkaan.
- Sovellus ei tällä hetkellä ota äänistä puhujaa, mutta sen voi lisätä.
- Sovellus ei tällä hetkellä tue tiedostoja joissa puhutaan monilla eri kielillä, tämänkin voi lisätä myöhemmin.
- Sovelluksella tulee olemaan käyttöliittymä ja normaalintyylinen .exe tiedosto jos tätä tarvitsee tehdä pidemmälle.