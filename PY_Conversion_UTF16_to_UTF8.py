# Convert UTF-16 files into UTF-8
# Necesario en todos los ficheros Kaltura (CONSUMPTION y CONCILIATION)


path = ('G:/AO_TV/Planificacion/Kaltura_GLUIJKD/' +
        '1_CONCILIATION/FASTLOAD_TIPO_9CAMPOS_20200223/')

source_filename = path + '195_CONCILIATION_23022020103302.csv'
dest_filename = path + '195_CONCILIATION_23022020103302_UTF8.csv'

with open(source_filename, 'rb') as source_file:
    with open(dest_filename, 'wb') as dest_file:
        contents = source_file.read()
        dest_file.write(contents.decode('utf-16').encode('utf-8'))


# Recomendable procesar ficheros en local, si la red va lenta puede dar:
#   [Errno 22] invalid argument

path = 'C:/_Analisis Ad-hoc_TMP/FASTLOAD_9CAMPOS_CONCILIATION_20200419/'

source_filename = path + '195_CONCILIATION_19042020103006.csv'
dest_filename = path + '195_CONCILIATION_19042020103006_UTF8.csv'

with open(source_filename, 'rb') as source_file:
    with open(dest_filename, 'wb') as dest_file:
        contents = source_file.read()
        dest_file.write(contents.decode('utf-16').encode('utf-8'))
