# Vypocetni prostredi Python pro geoinformatiku

**Pozadavky**: 
* Operacni system: GNU/Linux, Unix, Mac, Windows 
* Programovaci/skriptovaci jazyk: Python3 (zpravidla verze 3.9+) 
* Interaktivni prostredi: ipython, Jupyter Notebook nebo JupyeterLab 

Knihovny pro pro praci s geodaty: 
* GDAL/OGR (v prikazove radce) [GDAL](https://gdal.org)
* GDAL-Python (rozsireni GDAL knihovny do prostredi Python) [GDAL-Python](https://gdal.org/api/python_bindings.html)
* TODO: geopandas, rasterio 

Knihovny pro praci s daty v Python: NumPy (maticove pocty) 


**Moznosti pro cviceni v predmetu geoinformatika**: 
1. Varianta: GIS.lab system (klient-server reseni)
2. Varianta: predinstalovany server v OSGeo live (mozno instalovat na vlastnim NTB nebo na PC ve cvicebne K1)
3. Varianta: lokalni instalace (vlastni NTB nebo desktop)


## 1. GIS.lab
[GIS.lab desktop layout](https://gislab.readthedocs.io/en/latest/_images/client-layout.png)

Hlavni panel:
1. pousteni aplikaci 
2. ikonky vybranych 
3. virtualni desktopy
4. spustene aplikace
5. klavesnice 
6. bateria (u notebooku)
7. chat v siti GIS.lab
8. zvuk 
9. cas a kalendar

[GIS.lab system](https://gislab.readthedocs.io/en/latest/client-layout/index.html)

Do GIS.lab klienta se pripojime bootem pres sitvou kartu pri startu PC. 
Je nutne vyvolat vstup do BIOSu (F2 / DEL) a pote Ctrl+Alt+Del 

[Desktop klienta s Qgis](https://gislab.readthedocs.io/en/latest/_images/client-layout-qgis.png) 

- Skriptovani: Python verze 3.x + GDAL-Python 
- CLI aplikace: GDAL/OGR
- Desktop aplikace: QGIS, GRASS
- Text editor: Leafpad
- Linux terminal: $  

[Vice o instalci zde](https://gislab.readthedocs.io/en/latest/client-layout/index.html)


## 2. OSGeo live
K vyuziti OSGeo live je treba instalovat: 
* VirtualBox (Oracle VM VirtualBox) https://www.virtualbox.org 
* OSGeo live, v.9/10 (linux) a vyssi https://live.osgeo.org/en/download.html

Potrebne sw aplikace: 
- Desktop aplikace: QGIS
- Geodatabaze: PostgreSQL/PostGIS server a PgAdmin III, SpatiaLite
- Text editor: Leafpad
- Linux terminal: $  (TODO nazev)

Soubor ../OSGeo/osgeolive-vm-9.0/osgeo-live-9.0.vmdk (nebo jina verze) je treba pripojit do VirtualBoxu.  

VirtualBox: New -> Name: OSGeo9.0, Linux, Ubuntu (64b) -> RAM: napr. 4GB a vice  
-> Use an existing …  Choose a virtual hard disk file (.. /OSGeo/osgeolive-vm-9.0/osgeo-live-9.0.vmdk)
-> Create -> Start


TODO: vlastni lokalni instalace
## 3. Lokalni instalce (localhost) 




### 3.1 Windows 

- [Python3](https://www.python.org/download/releases/3.0/)
```
> python-3.9.2-amd64.exe
```
**DULEZITE**: 

    * pri instalaci nastavte **pip yes** set 
    * a **Python to environment variables** !!!

- Instalace knihoven: 
Pokud pouzivate **PIP** 
```
> pip install numpy 
```
Podobne pro dalsi knihovny. 
```
> pip install ipaython 
```


Pokud jste instalovali Python z kompilace Anaconda, tak musite postupovat dle instrukci 'conda'. Zpravidla: > conda install numpy, atd. 


- Instalace Jupyter notebook

```
> python -m pip install jupyter
```


- GDAL/OGR: https://gdal.org/download.html# 
- GDAL-Python instalace: https://gdal.org/api/python_bindings.html#installation


### 3.2 GNU/Linux 
- [Python3](https://www.python.org/download/releases/3.0/)
```
$ python-3.9.2-amd64.exe
```
**DULEZITE**: 

    * pri instalaci nastavte **pip yes** set 
    * a **Python to environment variables** !!!

- Instalace knihoven: 
Pokud pouzivate **PIP** 
```
> pip install numpy 
```
Podobne pro dalsi knihovny. 
```
> pip install ipaython 
```

- Instalace Jupyter notebook

```
> python -m pip install jupyter
```

- GDAL/OGR: https://gdal.org/download.html# 
- GDAL-Python instalace: https://gdal.org/api/python_bindings.html#installation

