# Concatenar 24 ficheros Consumptions/User_Entitlement de un día...
# Necesario en ficheros: Consumptions y User_Entitlement

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/3_Consumptions/' +
        'FASTLOAD_17CAMPOS_20200108/')

source_filename = path + 'Consumptions_KM_20200108'
dest_filename = path + 'Consumptions_KM_20200108_ALL.csv'


lines = []
n = 0

for i in range(24):
    sufijo = str(i)
    if i < 10:
        sufijo = '0' + sufijo
    fichero = source_filename + '_' + sufijo + '.csv'
    print('Processing:', fichero)
    with open(fichero, 'r', encoding='utf-8') as infile:
        for linea in infile:
            if n % 100000 == 0:
                print('Lines processed so far:', n)
            n += 1
            lines.append(linea)

print('Total lines processed:', n)

# Abrimos el fichero y escribimos las lineas
fout = open(dest_filename, 'w', encoding='utf-8')
fout.writelines(lines)
fout.close()
print('File saved.')



######################
# Version que lee y escribe fila por fila (ahorra memoria)

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '7_User_Entitlement/FASTLOAD_38CAMPOS_20200125/')

source_filename = path + 'User_Entitlement_KM_20200125'
dest_filename = path + 'User_Entitlement_KM_20200125_ALL.csv'


path = ('C:/_Analisis Ad-hoc_TMP/Consumptions/')

source_filename = path + 'Consumptions_KM_20200304'
dest_filename = path + 'Consumptions_KM_20200304_ALL.csv'

n = 0

with open(dest_filename, 'w', encoding='utf-8') as fout:
    for i in range(24):
        sufijo = str(i)
        if i < 10:
            sufijo = '0' + sufijo
        fichero = source_filename + '_' + sufijo + '.csv'
        print('Processing:', fichero)
        with open(fichero, 'r', encoding='utf-8') as infile:
            for linea in infile:
                if n % 100000 == 0:
                    print('Lines processed so far:', n)
                n += 1
                fout.write(linea)

print('Total lines processed:', n)
print('File saved.')



######################
# Version que busca en la ruta (OJO: aún no está adaptada a Consump/Entitle)

import os

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '8_UserNavigation/Ficheros2h_{Rober}/2 horas/')
dest_filename = path + 'AllAppFiles.csv'

lines = []
n = 0
n_data = 0
n_headers = 0

for fichero in os.listdir(path):
    if fichero.endswith(".csv"):
        print('Processing:', fichero)
        with open(path + fichero, 'r', encoding='utf-8') as infile:
            for linea in infile:
                if linea[1:2] != '"' and linea[18:19] == ',':  # data
                    long = len(linea)
                    linea_nueva = linea[0:18] + linea[19:long]
                    linea_nueva = linea_nueva.replace('"', '')  # drop ""
                    lines.append(linea_nueva)
                    n_data += 1
                else:
                    n_headers += 1
                n += 1

print('Total lines processed:', n, ',', n_data, 'with data and',
      n_headers, 'with headers. Saving file...')

# Abrimos el fichero y escribimos las lineas
fout = open(dest_filename, 'w', encoding='utf-8')
fout.writelines(lines)
fout.close()
print('File saved.')
