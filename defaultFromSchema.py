import functions
import pandas as pd
import os
import shutil

# Se obtiene la ruta de la tabla y del esquema
tableRout,schemaRout,columns,registerAmount,partitions,user = functions.getVariables()
#Se intenta borrar el archivo
if os.path.exists(tableRout):
    shutil.rmtree(tableRout)
# Se obtienen las columnas del esquema
columnsFromSchema = functions.getColumnsFromSchema(schemaRout)
# Se obtienen las columnas que tendrán valor por default
defaultColumns = functions.getDefaultColumns(columns,columnsFromSchema)
# Se obtienen los diccionarios con las tuplas columna / valores
columnsWithNotNullValues = functions.getValuesForColumns(columns,user)
columnsWithNullValues = functions.getValuesForNullColumns(defaultColumns,registerAmount)
# Se combinan ambos diccinarios
columnsWithValues = functions.mergeColumns(columnsWithNotNullValues,columnsWithNullValues)
df = pd.DataFrame(columnsWithValues)
df.to_parquet(path = tableRout, partition_cols=partitions)
