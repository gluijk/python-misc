# -*- coding: utf-8 -*-

# Checks Navigation

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '8_Navigation/FASTLOAD_17CAMPOS_20191107/')

path = ('C:/_Analisis Ad-hoc_TMP/FASTLOAD_17CAMPOS_20200312/')


fichero = path + 'Navigation_KM_20191107.csv'
dest_filename = path + 'Navigation_KM_20191107_412555.csv'

fichero = path + 'Consumptions_KM_20200312_23.csv'
dest_filename = path + 'Consumptions_KM_20200312_23_NLINES.csv'


lines = []
n = 0

# Leer solo unas pocas filas del fichero
with open(fichero, 'r', encoding='utf-8') as infile:
    for i in range(1000):
        lines.append(infile.readline())

# Guardar con open
fout = open(dest_filename, 'w', encoding='utf-8')
fout.writelines(lines)
fout.close()


# Guardar con with open
with open(dest_filename, 'w', encoding='utf-8') as outfile:
    outfile.writelines(lines)

# Lo siguiente lee todas las filas del fichero (OJO: TARDA)
with open(fichero, 'r', encoding='utf-8') as infile:
    lines = infile.readlines()
    firstline = lines[0]
    print(firstline)
