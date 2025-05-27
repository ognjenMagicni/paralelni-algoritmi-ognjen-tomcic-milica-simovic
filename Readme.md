# Tema
Prikazivanje pristupa paralelizacije na tri različita algoritma (Milicin prvi zadatak) ekvalizacije histograma i (Milicin drugi zadatak).

## Pipeline Segmentation by Region Growing​

Program identifikuje povezane regije koje imaju sličan intenzitet piksela. 

## Ekvalizacija histograma

Histogram ekvalizacije je metoda transformacije slike pomoću kulmulativnog histograma, koji teorijski poboljšava kvalitet slike. Za računanje histograma ekvalizacije koristimo sledeću formulu:

Gdje je T funkcija transformacije, L je najveći intezitet boje, n ukupan broj piksela, h<sub>i</sub> broj piksela inteziteta, a k intezitet piksela koji se razmatra r<sub>k</sub>.

## Global tresholding

Razvijeni algoritam koristi paralelnu obradu slike baziranu na rekurzivnoj podjeli slike (Quad-Tree segmentaciji) i iterativnom globalnom pragovanju piksela u svakoj regiji. ​

# Instalacija
```
git init   
git clone git@github.com:ognjenMagicni/Project001.git   
git pull origin main
cd paralelni-algoritmi-ognjen-tomcic-milica-simovic
python3 -m venv venv_p
source venv_p/bin/activate
pip3 install -r requirements.txt 
```
## Pokretanje Milicinog prvog zad

```
python -u parallelsegmentation.py
```

## Pokretanje histograma ekvalizacije

```
cd ekvalizacija_histogram
python3 alg.py
```

## Pokretanje Milicinog drugog zadatka
```
python -u globaltreshold.py
```
