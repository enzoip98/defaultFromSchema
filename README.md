# defaultFromSchema

El presenta programa permite la creación de archivos parquet para el proyecto CDD. Los archivos serán creados utilizando como base el esquema de forma que los parquets creados contengan todas las columnas que este contiene, esto con el objetivo de evitar inconsistencias en los dummys creados.

## Forma de uso

Para utilizar el archivo python defaultFromSchema.py se requiere de dos archivos:
 - Archivo de esquema de la tabla
 - Archivo json con información necesaria del dummy a crear
 
![alt text](https://github.com/enzoip98/defaultFromSchema/blob/main/images/archivos.jpg?raw=true)

Respecto al archivo de esquema deberá ser guardado en el directorio workspace del vbox

Respecto al json, este deberá contener las siguientes propiedades

| Atributo        | Valor                                                                                                        |
| :-------------: | :----------------------------------------------------------------------------------------------------------: |
| table           | Nombre de la tabla                                                                                           |
| partitions      | Nombre de las particiones separadas por un ;                                                                 |
| schema          | Nombre del esquema (incluyendo el .output.schema)                                                            |
| noDefaultColumns| Columnas que iran informadas separadas por un ;                                                              |
| registersAmount | Cantidad de registros que tendrá el parquet a crear                                                          |
| values          | Atributo que contendrá las columnas que iran informadas con sus valores anidados como atributos de las mismas|

 ![alt text](https://github.com/enzoip98/defaultFromSchema/blob/main/images/json.jpg?raw=true)
 
 Teniendo estos dos archivos se procederá a correr el archivo defaultFromSchema.py por medio del terminal usando la instrucción python defaultFromSchema.py
 ```
 python defaultFromSchema.py
 ```
 
 Se solicitará el usuario del dueño del vbox y con esto se obtendrá el archivo parquet en una carpeta informada con el nombre de la tabla
 
 ```
 Ingrese el código del usuario: XP63125
 ```
 
 ![alt text](https://github.com/enzoip98/defaultFromSchema/blob/main/images/carpeta.jpg?raw=true)
  
 ## NOTAS
 
- Asegurarse de que no existe ninguna carpeta con el nombre de la tabla en la ruta del workspace ya que de ser así el programa la borrará
- La cantidad de datos que se pongan en el atributo de values debe ser igual al de registersAmount
- No existe un control sobre el parámetro noDefaultColumns por lo que es muy importante verificar que el nombre de las columnas es el correcto al escribirlas
- Las columnas que sean particiones también deben ser informadas en el parámetro noDefaultColumns y deben tener valores en el parámetro values
- Al separar no usar espacios, solamente se requiere el caracter ";"
