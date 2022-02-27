import json

def getColumnsFromSchema(SchemaRout) :
    f = open(SchemaRout)
    data = json.load(f)
    columnsInSchema = []
    for i in data["fields"]:
        columnsInSchema.append(i["name"])
    f.close()
    return columnsInSchema

def getVariables():
    user = input("Ingrese el código del usuario : ")
    f = open(f"/var/sds/homes/{user}/workspace/env.json")
    data = json.load(f)
    table = data["table"]
    partitionsString = data["partitions"]
    schema = data["schema"]
    columnsString = data["noDefaultColumns"]
    registersAmount = int(data["registersAmount"])
    f.close()
    partitions = partitionsString.split(";")
    tableRout = f"/var/sds/homes/{user}/workspace/{table}"
    schemaRout = f"/var/sds/homes/{user}/workspace/{schema}"
    columns = columnsString.split(";")
    return tableRout, schemaRout, columns, registersAmount, partitions, user

def getDefaultColumns(columns,columnsFromSchema):
    defaultColumns = list(set(columnsFromSchema)-set(columns))
    return defaultColumns

def getValuesForColumns(columns, user):
    f = open(f"/var/sds/homes/{user}/workspace/env.json")
    data = json.load(f)
    dataFrameDictionary = {
    }
    for i in columns:
        valuesString = data["values"][i]
        values = valuesString.split(";")
        dataFrameDictionary[i] = values
    f.close()
    return dataFrameDictionary

def getValuesForNullColumns(columns,registersAmount):
    dataFrameDictionary = {
    }
    for i in columns:
        values = [""] *  registersAmount
        dataFrameDictionary[i] = values
    return dataFrameDictionary

def mergeColumns(columnsWithNotNullValues,columnsWithNullValues):
    columnsWithNotNullValues.update(columnsWithNullValues)
    return columnsWithNotNullValues 
    