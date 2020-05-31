# Extraer N filas de un fichero

NFILAS = 200

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/8_Navigation/' +
        'FASTLOAD_XXCAMPOS_XXXXXXXX_Search/')

source_filename = path + 'NavigationSearch_KM_20200121.csv'
dest_filename = path + 'NavigationSearch_KM_20200121_' + str(NFILAS) + '.csv'

n = 0

with open(dest_filename, 'w', encoding='utf-8') as fout:
    print('Processing:', source_filename)
    with open(source_filename, 'r', encoding='utf-8') as infile:
        for linea in infile:
            fout.write(linea)
            n += 1
            if n == NFILAS:
                break

print('Total lines processed:', n)
print('File saved.')


###################
# CONSUNPTION, SUBSCRIPTIONS, CONCILIATION (UTF-16)

NFILAS = 2000

path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/1_CONCILIATION/' +
        'FASTLOAD_TIPO_9CAMPOS_20200105/')

source_filename = path + '195_CONCILIATION_05012020123320.csv'
dest_filename = path + '195_CONCILIATION_05012020123320_' + str(NFILAS) + '.csv'

n = 0

with open(dest_filename, 'w', encoding='utf-16') as fout:
    print('Processing:', source_filename)
    with open(source_filename, 'r', encoding='utf-16') as infile:
        for linea in infile:
            fout.write(linea)
            n += 1
            if n == NFILAS:
                break

print('Total lines processed:', n)
print('File saved.')
