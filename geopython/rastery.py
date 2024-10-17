#!/usr/bin/env python3

# Skriptovani procesu s rastery v Python
# 1. otevreni datasetu
# 2. cteni metadat rasteru
# 3. cteni dat rasteru do pole NumPy (numericky Python)
# 4. mapova algebra pomoci NumPy
# 5. zapis vysledku do noveho souboru

# Rasterio dokumentace
# https://rasterio.readthedocs.io

# knihovny
import numpy as np
import os
import rasterio

### DATA ###
# cesta = './'
cesta = '/Users/lukas/Work/prfuk/vyuka/geoinformatika/src/geoinformatika/geodata/raster/'
# Muzete vyuzit i jiny soubor, nejlepe vyrez multispektralniho snimku
soubor = 'S2A_T33UVR_20180703T101029.tif'

### PRUZKUM RASTERU ###
# 1. Otevreni datasetu
# Funkce open() přijímá řetězec cesty a vrací otevřený objekt datové sady.
# Rasterio otevře data pomocí ovladače GDAL.
ds = rasterio.open(os.path.join(cesta, soubor))
print(f'Dataset: {ds}')
print(f'Typ datasetu: {type(ds)}')

# 2. Stavove attributy otevreneho objektu dataset
# Objekty datových sad mají některé stejné atributy jako objekty souborů Pythonu.
print(f'Stav datasetu, uzavreny?: {ds.closed}')
print(f'Jmeno otevreneho souboru/datasetu: {ds.name}')
print(f'Mod otevreneho datasetu: {ds.mode}')

# 3. Metadata (vlastnosti) datasetu - take atributy objektu
print(f'Pocet pasem datasetu: {ds.count}')
print(f'Sirka: {ds.width}')
print(f'Vyska: {ds.height}')

# atribut meta
meta = ds.meta
print(type(meta))
print('Metadata datasetu: ...')
for k in meta:
    print(k, meta[k])

# Indexy pasem
print(f'Indexy pasem datasetu: {ds.indexes}')
print(f'... a jejich datove typy: {ds.dtypes}')
bands_dtypes = {i: dtype for i, dtype in zip(ds.indexes, ds.dtypes)}
bands_dtypes

# 4. Georeferencovani rasteru
print(f'Minimalni ohranicujici obdelnik (Bbox): {ds.bounds}')
print(f'Souradnice X leveho horniho rohu: {ds.bounds.left}')
# Bbox je ziskan z geoprostorovych transformacnich atributu
# ... afinní transformační matice, která mapuje umístění pixelů v souřadnicích (col, row) na prostorové pozice (x, y)
print(f'Atributy geo transformace: {ds.transform}')
# Součin této matice a (0, 0), souřadnic sloupce a řádku levého horního rohu datové sady,
# je prostorová poloha levého horního rohu.

# Souradnice leveho horniho bodu
print(f'Souradnice leveho hodniho bodu: {ds.transform * (0,0)}')
# Souradnice praveho dolniho bodu
print(f'Souradnice praveho dolniho bodu: {ds.transform * (ds.width, ds.height)}')

# CRS: Coordinate Reference System
print(f'CRS datasetu: {ds.crs}')
# ds.crs.to_string()
# ds.crs.to_wkt()

### CTENI DAT RASTERU ###
# index pasma: 1
B1 = ds.read(1)
# Rasterio metoda .read() vrati pole hodnot typu NumPy
print(f'Typ pole hodnot: {type(B1)}')
B1
B1.dtype

# adresovani hodnot NumPy pole: B1[vyska, sirka]
x_ix = 100; y_ix = 150
print(f'Hodnota pole B1 v souradnicih x: {x_ix} a y: {y_ix} je {B1[y_ix, x_ix]}')

# Indexovani pomoci souradnice
# Datové sady mají metodu DatasetReader.index() pro získání indexů pole odpovídajících bodům
# v georeferencovaném prostoru. Chcete-li získat hodnotu pro pixel 10 km východně a 5 km jižně
# od levého horního rohu datové sady, postupujte takto.
x, y = (ds.bounds.left + 10000, ds.bounds.top - 5000)
radek, sloupec = ds.index(x, y)
print(f'Hodnota pole pro vybrany pixel je: {B1[radek, sloupec]}')

# Chceme-li získat prostorové souřadnice pixelu, použijte metodu DatasetReader.xy() datové sady.
# Souřadnice středu pole (obrazu) lze vypočítat takto.
print(f'Souradnice x, y stredu obrazovych dat: {ds.xy(ds.height // 2, ds.width // 2)}')

### OPTIONAL ###
# Okna pro cteni dat
# ((první_řádek, poslední_řádek), (první_sloupec, poslední_sloupec))
# Window(první_sloupec, první_řádek, šířka, výška)
with rasterio.open(os.path.join(cesta, soubor)) as cervene:
    B3 = cervene.read(1, window=((0, 100), (0, 200)))
print(f'Velikost  pole kanalu 3: {B3.shape}')

### MAPOVA ALGEBRA ###
# Vypocet NDVI
RED = ds.read(3).astype(np.float32)
NIR = ds.read(4).astype(np.float32)
print(f'Datovy typ cerveno pasma: {RED.dtype}')

NDVI = (NIR - RED) / (NIR + RED)
print(type(NDVI))
print(NDVI.min(), NDVI.max())

# prazdan matice dane velikosti
# pole_nul = np.zeros((500, 1000))
# print(f'Velikost pole: {pole_nul.shape}')
# pole_nul

### ZAPIS RASTERU DO SOUBORU ###
# zapis https://rasterio.readthedocs.io/en/latest/topics/writing.html
# with rasterio.open(
#     './data/new.tif',
#     'w',
#     driver='GTiff',
#     height=pole.shape[0],
#     width=pole.shape[1],
#     count=1,
#     dtype=pole.dtype,
#     crs='+proj=latlong',
#     transform=transform,
# ) as dst:
#     dst.write(1, pole)

# priprava
meta = ds.meta
print(f'Metadata datasetu: {meta}')
# vystup: 32-bitova data
meta["dtype"] = "float32"
# pocet kanalu = 1
meta['count'] = 1
# komprese dat
# Rasterio pouziva GDAL jake 'backend'. Jake kompresni metody jsou implementovany pod kterymi zkratkami?
meta['compress'] = 'lzw'

with rasterio.open(os.path.join(cesta, 'ndvi.tif'), 'w', **meta) as dst:
   dst.write_band(1, NDVI.astype(rasterio.float32))

if os.path.isfile(os.path.join(cesta, 'ndvi.tif')):
    print('Soubor ndvi.tif je zapsan na disk.')
    print(f"Velikost souboru je: {os.path.getsize(os.path.join(cesta, 'ndvi.tif')) / 1000000} MB.")

###
