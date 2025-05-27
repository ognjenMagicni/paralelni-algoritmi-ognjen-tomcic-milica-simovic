# Tema
Prikazivanje pristupa paralelizacije na tri različita algoritma (Milicin prvi zadatak) ekvalizacije histograma i (Milicin drugi zadatak).

## Pipeline Segmentation by Region Growing

Koristimo region growing algoritam za segmentaciju slika​ kako bi identifikovali povezane regije koje imaju sličan intenzitet piksela.
## Ekvalizacija histograma

Histogram ekvalizacije je metoda transformacije slike pomoću kulmulativnog histograma, koji teorijski poboljšava kvalitet slike. Za računanje histograma ekvalizacije koristimo sledeću formulu:

Gdje je T funkcija transformacije, L je najveći intezitet boje, n ukupan broj piksela, h<sub>i</sub> broj piksela inteziteta, a k intezitet piksela koji se razmatra r<sub>k</sub>.

## Milicin drugi zadatak

Nesto malo teksta

## Link do prezentacije
https://onedrive.live.com/personal/b543137be827fddd/_layouts/15/Doc.aspx?sourcedoc=%7B9b9eaca9-b843-4e45-9695-e78d54f52f6a%7D&action=default&redeem=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy9iNTQzMTM3YmU4MjdmZGRkL0VhbXNucHREdUVWT2xwWG5qVlQxTDJvQlFFa2pFdUhYcW5GNGo3a2dVTHpYQ0E_ZT1yalczMkM&slrid=0c46a2a1-001a-d000-0a30-9ced02a27b07&originalPath=aHR0cHM6Ly8xZHJ2Lm1zL3AvYy9iNTQzMTM3YmU4MjdmZGRkL0VhbXNucHREdUVWT2xwWG5qVlQxTDJvQlFFa2pFdUhYcW5GNGo3a2dVTHpYQ0E_cnRpbWU9cVd1SEJTMmQzVWc&CID=d8f7ba69-1244-465b-a26f-3c13106227ad&_SRM=0:G:39&file=Presentation%203.pptx

## Link do seminarskog rada
https://docs.google.com/document/d/1K3PjI8WkhNKjmkOtjc5ZXpXpEWLNtI2VRQDlZ90S2mI/edit?tab=t.0

# Instalacija
```
git init   
git clone git@github.com:ognjenMagicni/Project001.git   
git pull origin main
cd paralelni-algoritmi-ognjen-tomcic-milica-simovic
```
## Pokretanje Pipeline segmentation
```
python -u parallelsegmentation.py
```
## Pokretanje histograma ekvalizacije

```
cd ekvalizacija_histogram
python3 alg.py
```

## Pokretanje Tresholding
```
python -u globaltreshold.py
```
