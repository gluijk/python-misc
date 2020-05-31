# Replace " fields delimiter by | (pipe)
# Necesario en ficheros: CONSUMPTION (si campo Provider sigue con Sinopsis)
# NavigationApps y NavigationChannels (campo BGAN)
# y User_Entitlement (campo BGAN)

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '2.1_CONSUMPTION/FASTLOAD_20CAMPOS_20191115/')

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '8_Navigation/FASTLOAD_29CAMPOS_20191118_Channels/')

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '7_User_Entitlement/FASTLOAD_38CAMPOS_20200125/')


source_filename = path + '195_CONSUMPTION_15112019162001_UTF8.csv'
dest_filename = path + '195_CONSUMPTION_15112019162001_UTF8_parsed.csv'

source_filename = path + 'NavigationChannels_KM_20191118.csv'
dest_filename = path + 'NavigationChannels_KM_20191118_parsed.csv'

source_filename = path + 'User_Entitlement_KM_20200125_ALL.csv'
dest_filename = path + 'User_Entitlement_KM_20200125_ALL_parsed.csv'


lines = []
n = 0

with open(source_filename, 'r', encoding='utf-8') as infile:
    for linea in infile:
        if n % 100000 == 0:
            print('Lines processed so far:', n)
        n += 1
        long = len(linea)
        substr = linea[1:(long - 2)]  # ignoramos primer y últimos 2 cars.
        substr = substr.replace('|', '│')  # por si hubiera pipes de partida
        linea_nueva = '|' + substr.replace('","', '|,|') + '|\n'
        lines.append(linea_nueva)

print('Total lines processed:', n)


# Abrimos el fichero y escribimos las líneas
fout = open(dest_filename, 'w', encoding='utf-8')
fout.writelines(lines)
fout.close()
print('File saved.')

"""
# Alternativa si los elementos de la lista no terminasen en \n
with open(dest_filename, 'w', encoding='utf-8') as outfile:
    for line in lines:
        outfile.write(line + "\n")
"""


######################
# Version que lee y escribe fila por fila (ahora memoria)

path = ('G:/AO_TV/Planificacion/Analisis Ad-hoc/201911/' +
        '2019_11_28_InformeUsoApps_VTV_Navegacion/' +
        'FASTLOAD_29CAMPOS_201911_Channels/')

source_filename = path + 'NavigationChannels_KM_201911_ALL.csv'
dest_filename = path + 'NavigationChannels_KM_201911_ALL_parsed.csv'


path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '7_User_Entitlement/FASTLOAD_38CAMPOS_20200312/')

source_filename = path + 'User_Entitlement_KM_20200312_02.csv'
dest_filename = path + 'User_Entitlement_KM_20200312_02_parsed.csv'


path = ('C:/_Analisis Ad-hoc_TMP/FASTLOAD_29CAMPOS_20200319_Channels/')

source_filename = path + 'NavigationChannels_KM_20200319.csv'
dest_filename = path + 'NavigationChannels_KM_20200319_parsed.csv'


n = 0

# fout = open(dest_filename, 'w', encoding='utf-8')
with open(dest_filename, 'w', encoding='utf-8') as fout:
    with open(source_filename, 'r', encoding='utf-8') as infile:
        for linea in infile:
            if n % 100000 == 0:
                print('Lines processed so far:', n)
            n += 1
            long = len(linea)
            substr = linea[1:(long - 2)]  # ignoramos primer y últimos 2 cars.
            substr = substr.replace('|', '│')  # por si hubiera pipes de partida
            linea_nueva = '|' + substr.replace('","', '|,|') + '|\n'
            fout.write(linea_nueva)

print('Total lines processed:', n)

# fout.close()
print('File saved.')

