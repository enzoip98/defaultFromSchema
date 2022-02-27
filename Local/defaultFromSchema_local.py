import Local.functions_local as functions_local
import pandas as pd
import os
import shutil

# Se obtiene la ruta de la tabla y del esquema
tableRout,schemaRout,columns,registerAmount,partitions = functions_local.getVariables()
#Se intenta borrar el archivo
if os.path.exists(tableRout):
    shutil.rmtree(tableRout)
# Se obtienen las columnas del esquema
columnsFromSchema = functions_local.getColumnsFromSchema(schemaRout)
# Se obtienen las columnas que tendrán valor por default
defaultColumns = functions_local.getDefaultColumns(columns,columnsFromSchema)
# Se obtienen los diccionarios con las tuplas columna / valores
columnsWithNotNullValues = functions_local.getValuesForColumns(columns)
columnsWithNullValues = functions_local.getValuesForNullColumns(defaultColumns,registerAmount)
# Se combinan ambos diccinarios
columnsWithValues = functions_local.mergeColumns(columnsWithNotNullValues,columnsWithNullValues)
df = pd.DataFrame(columnsWithValues)
df.to_parquet(path = tableRout, partition_cols=partitions)
