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
    f = open("C:/Users/Enzo/Desktop/defaultFromSchema/env.json")
    data = json.load(f)
    user = data["user"]
    table = data["table"]
    partitionsString = data["partitions"]
    schema = data["schema"]
    columnsString = data["noDefaultColumns"]
    registersAmount = int(data["registersAmount"])
    f.close()
    partitions = partitionsString.split(";")
    tableRout = f"C:/Users/Enzo/Desktop/defaultFromSchema/{user}/{table}_dummy/"
    schemaRout = f"C:/Users/Enzo/Desktop/defaultFromSchema/{schema}"
    columns = columnsString.split(";")
    return tableRout,schemaRout,columns,registersAmount,partitions

def getDefaultColumns(columns,columnsFromSchema):
    defaultColumns = list(set(columnsFromSchema)-set(columns))
    return defaultColumns

def getValuesForColumns(columns):
    f = open("C:/Users/Enzo/Desktop/defaultFromSchema/env.json")
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
    