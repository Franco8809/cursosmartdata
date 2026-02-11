# Databricks notebook source
# MAGIC %md
# MAGIC # Fundamentos de Apache Spark

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %md
# MAGIC ### Crear la sesión de Spark 

# COMMAND ----------

spark

# COMMAND ----------

# MAGIC %md
# MAGIC ### Crear el DataFrame

# COMMAND ----------

emp = [(1, "AAA", "dept1", 1000),
    (2, "BBB", "dept1", 1100),
    (3, "CCC", "dept1", 3000),
    (4, "DDD", "dept1", 1500),
    (5, "EEE", "dept2", 8000),
    (6, "FFF", "dept2", 7200),
    (7, "GGG", "dept3", 7100),
    (8, "HHH", "dept3", 3700),
    (9, "III", "dept3", 4500),
    (10, "JJJ", "dept5", 3400)]

dept = [("dept1", "Department - 1"),
        ("dept2", "Department - 2"),
        ("dept3", "Department - 3"),
        ("dept4", "Department - 4")
       ]

df = spark.createDataFrame(emp, ["id", "name", "dept", "salary"])
deptdf = spark.createDataFrame(dept, ["id", "name"])

# COMMAND ----------

df.show()

# COMMAND ----------

display(df)

# COMMAND ----------

df.display()

# COMMAND ----------

# MAGIC %md
# MAGIC # Operaciones básicas en DataFrames

# COMMAND ----------

# MAGIC %md
# MAGIC ### count
# MAGIC * Cuenta el número de filas

# COMMAND ----------

df.count()

# COMMAND ----------

# MAGIC %md
# MAGIC ### columns

# COMMAND ----------

df.columns

# COMMAND ----------

# MAGIC %md
# MAGIC ### dtypes
# MAGIC ** Accede al DataType de columnas dentro del DataFrame

# COMMAND ----------

df.dtypes

# COMMAND ----------

# MAGIC %md
# MAGIC ### schema
# MAGIC ** Comprueba cómo Spark almacena el esquema del DataFrame

# COMMAND ----------

df.schema

# COMMAND ----------

# MAGIC %md
# MAGIC ### printSchema

# COMMAND ----------

df.printSchema()

# COMMAND ----------

# MAGIC %md
# MAGIC ### select
# MAGIC * Seleccione columnas del DataFrame

# COMMAND ----------

df.select("id", "name").show()

# COMMAND ----------

df.select("id", "dept").display()

# COMMAND ----------

df.select("*").display()
#df.display()

# COMMAND ----------

#cols = df.columns[:-1]
cols = ["dept","id","salary"]
df.select(*cols).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### filter
# MAGIC
# MAGIC * Filtrar las filas según alguna condición.
# MAGIC * Intentemos encontrar las filas con id = 1.
# MAGIC * Hay diferentes formas de especificar la condición.

# COMMAND ----------

df.filter(df["id"] == 2).display()
df.filter(df.id == 1).display()

# COMMAND ----------

df.filter(col("id") == 3).display()
df.filter("id = 4").display()

# COMMAND ----------

lista = ["1","2","3"]
df.filter(col("id").isin(lista)).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### drop
# MAGIC * Elimina una columna en particular

# COMMAND ----------

df.drop("id").display()

# COMMAND ----------

df.display()

# COMMAND ----------

df = df.drop("id")
df.display()

# COMMAND ----------

newdf = df.drop("id")
newdf.display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Aggregations
# MAGIC * Podemos usar la función groupBy para agrupar los datos y luego usar la función "agg" para realizar la agregación de datos agrupados.

# COMMAND ----------

display(df)

# COMMAND ----------

#Ejecutar nuevamente la celda 6
(df.groupBy(col("dept")).
    agg(
        count("salary").alias("count"),
        sum("salary").alias("sum"),
        max("salary").alias("max"),
        min("salary").alias("min"),
        avg("salary").alias("avg")
    ).display()
)

# COMMAND ----------

df.groupBy("dept").\
        agg(
        count("salary").alias("count"),
        sum("salary").alias("sum"),
        max("salary").alias("max"),
        min("salary").alias("min"),
        avg("salary").alias("avg")
        ).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Sorting
# MAGIC
# MAGIC * Ordena los datos según el "salario". De forma predeterminada, la clasificación se realizará en orden ascendente.

# COMMAND ----------

df.sort("salary").display()
df.sort(desc("salary")).display()
df.sort(asc("salary")).limit(5).display()

# COMMAND ----------

display(df.sort(desc("dept"), asc("salary")).limit(6))

# COMMAND ----------

display(df.sort(desc("dept"), desc("salary")).limit(6))

# COMMAND ----------

df.sort(desc("dept"), desc("salary")).limit(6).display()

# COMMAND ----------

df.sort(desc("salary")).show(5)

# COMMAND ----------

df.sort(asc("salary")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Columnas derivadas
# MAGIC * Podemos usar la función "withColumn" para derivar la columna en función de las columnas existentes ...

# COMMAND ----------

df.withColumn("bonus", col("salary") * 0.1).display()

# COMMAND ----------

df.withColumn("salary",round(col("salary")*1.1)).display()

# COMMAND ----------

df.withColumn("flag",lit("1")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Joins
# MAGIC
# MAGIC * Podemos realizar varios tipos de combinaciones en múltiples DataFrames.

# COMMAND ----------

df.display()

# COMMAND ----------

display(deptdf)

# COMMAND ----------

#mala practica
deptdf = deptdf.withColumnRenamed("id","id_2")

# COMMAND ----------

deptdf = (deptdf.withColumnRenamed("id_2","id").
                withColumnRenamed("name","nombre")
        )

# COMMAND ----------

newdeptdf_2 = (deptdf.select(col("id").alias("id_nuevo"),
                            col("nombre").alias("name")))

# COMMAND ----------

#Forma de agregar una nueva columna usando select
deptdf.select("*",lit("1").alias("flag")).display()

# COMMAND ----------

display(newdeptdf_2)

# COMMAND ----------

display(df)

# COMMAND ----------

display(deptdf)

# COMMAND ----------

df.join(deptdf, df["dept"] == deptdf["id"]).display()
df.join(deptdf, df["dept"] == deptdf["id"],"inner").display()
df.join(deptdf, df["dept"] == deptdf["id"], how = "inner").display()

# COMMAND ----------

df_joined = df.join(deptdf, df["dept"] == deptdf["id"])

df_joined.select("id").display()

# COMMAND ----------

#Forma correcta para resolver columnas ambiguas despues de la union
df_joined = df.alias("a").join(deptdf.alias("b"), col("a.dept") == col("b.id"), how="inner")

df_joined.select("b.id","a.id").display()

# COMMAND ----------

array = ["a.id", "b.name"]

df_join = df.alias("a").join(deptdf.alias("b"), df["dept"] == deptdf["id"], "inner").select([col(column) for column in array])

df_join.display()

# COMMAND ----------

df_join.select(col("a.id"),col("b.name")).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Left Outer Join

# COMMAND ----------

df.display()
deptdf.display()

# COMMAND ----------

df.join(deptdf, df["dept"] == deptdf["id"], "left_outer").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Right Outer Join

# COMMAND ----------

df.join(deptdf, df["dept"] == deptdf["id"], "right_outer").display()

# COMMAND ----------

df.join(deptdf, df["dept"] == deptdf["id"], "right").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Full Outer Join

# COMMAND ----------

df.join(deptdf, df["dept"] == deptdf["id"], "outer").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Consultas SQL
# MAGIC * Ejecución de consultas tipo SQL.
# MAGIC * También podemos realizar análisis de datos escribiendo consultas similares a SQL. Para realizar consultas similares a SQL, necesitamos registrar el DataFrame como una Vista temporal.

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados

# COMMAND ----------

df_sql = spark.sql("select * from workspace.default.empleados")
df_sql.display()

# COMMAND ----------

bd = "workspace.default"

# COMMAND ----------

df = spark.sql(f"""with  b1 (
                    select *
                    from {bd}.empleados
                ) 
                select *
                from b1 
               """)

df = spark.sql(f"""select * from {bd}.empleados """)

df.createOrReplaceTempView("temp_table")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from temp_table

# COMMAND ----------

df.display()

# COMMAND ----------

# Register DataFrame as Temporary Table
df.createOrReplaceTempView("temp_table")

# Execute SQL-Like query.
spark.sql("select * from temp_table where id = 2").display()

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from temp_table where id = 3;

# COMMAND ----------

df_2 = spark.sql("""select * 
                    from temp_table limit 2
                    """)

df_2.display()

# COMMAND ----------

df_2.createOrReplaceTempView("temp_table_2")

# COMMAND ----------

# MAGIC %sql
# MAGIC select *
# MAGIC from temp_table_2

# COMMAND ----------

spark.sql("select distinct id from temp_table").display()

# COMMAND ----------

spark.sql("select * from temp_table where salario >= 1500").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Leyendo la tabla HIVE como DataFrame

# COMMAND ----------

# DB_NAME : Name of the the HIVE Database
# TBL_NAME : Name of the HIVE Table


df = spark.table("workspace.default.empleados")
df.display()

# COMMAND ----------

deptdf.display()

# COMMAND ----------

# MAGIC %sql
# MAGIC create table workspace.default.deptdf (
# MAGIC   id string,
# MAGIC   name string
# MAGIC )

# COMMAND ----------

deptdf.display()

# COMMAND ----------

deptdf_filtered = deptdf.filter(col("id")=="dept1")

deptdf_filtered.write.format("delta").mode("overwrite").saveAsTable("workspace.default.deptdf")

deptdf_filtered.write.format("delta").mode("overwrite").save("/Volumes/workspace/default/resultados/deptdf")

deptdf_filtered.write.format("delta").mode("overwrite").insertInto("workspace.default.deptdf")

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table workspace.default.deptdf

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.deptdf

# COMMAND ----------

deptdf_filtered = deptdf
deptdf_filtered.write.format("csv").save("/Volumes/workspace/default/resultados/deptdf_csv_completed")

# COMMAND ----------

deptdf_filtered.write.format("csv").save("/Volumes/workspace/default/resultados/deptdf_csv")

# COMMAND ----------

spark.read.csv("/Volumes/workspace/default/resultados/deptdf_csv_completed/").display()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Guardar DataFrame como tabla HIVE

# COMMAND ----------

df.write.saveAsTable("DB_NAME.TBL_NAME")

## También podemos seleccionar el argumento "modo" con overwrite", "append", "error" etc.
df.write.saveAsTable("DB_NAME.TBL_NAME", mode="overwrite")

# De forma predeterminada, la operación guardará el DataFrame como una tabla interna / administrada de HIVE

# COMMAND ----------

# MAGIC %md
# MAGIC ### Guardar el DataFrame como una tabla externa HIVE

# COMMAND ----------

df.write.saveAsTable("DB_NAME.TBL_NAME", path=<location_of_external_table>)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Crea un DataFrame a partir de un archivo CSV
# MAGIC * Podemos crear un DataFrame usando un archivo CSV y podemos especificar varias opciones como un separador, encabezado, esquema, inferSchema y varias otras opciones.

# COMMAND ----------

 df = spark.read.csv("path_to_csv_file", sep="|", header=True, inferSchema=True)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Guardar un DataFrame como un archivo CSV

# COMMAND ----------

df.write.csv("path_to_CSV_File", sep="|", header=True, mode="overwrite")

# COMMAND ----------

# MAGIC %md
# MAGIC ### Crea un DataFrame a partir de una tabla relacional
# MAGIC * Podemos leer los datos de bases de datos relacionales usando una URL JDBC.

# COMMAND ----------

# url : a JDBC URL of the form jdbc:subprotocol:subname
# TBL_NAME : Name of the relational table.
# USER_NAME : user name to connect to DataBase.
# PASSWORD: password to connect to DataBase.


relational_df = spark.read.format('jdbc')
                        .options(url=url, dbtable= <TBL_NAME>, user= <USER_NAME>, password = <PASSWORD>)
                        .load()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Guardar el DataFrame como una tabla relacional
# MAGIC * Podemos guardar el DataFrame como una tabla relacional usando una URL JDBC.

# COMMAND ----------

# url : a JDBC URL of the form jdbc:subprotocol:subname
# TBL_NAME : Name of the relational table.
# USER_NAME : user name to connect to DataBase.
# PASSWORD: password to connect to DataBase.


relational_df.write.format('jdbc')
                    .options(url=url, dbtable= <TBL_NAME>, user= <USER_NAME>, password = <PASSWORD>)
                    .mode('overwrite')
                    .save()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Conexión con Databricks Community

# COMMAND ----------

paciente_outputh_path = "/FileStore/dataset/smart_data/paciente.csv"

# COMMAND ----------

df_paciente = spark.read.csv(paciente_outputh_path, header=True)

# COMMAND ----------

df_paciente.display()
