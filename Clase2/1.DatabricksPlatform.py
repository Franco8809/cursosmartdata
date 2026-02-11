# Databricks notebook source
# MAGIC %md 
# MAGIC # Databricks Platform
# MAGIC
# MAGIC Demonstrate basic functionality and identify terms related to working in the Databricks workspace.
# MAGIC
# MAGIC
# MAGIC ##### Objectives
# MAGIC 1. Execute code in multiple languages
# MAGIC 1. Create documentation cells
# MAGIC 1. Access DBFS (Databricks File System)
# MAGIC 1. Create database and table
# MAGIC 1. Query table and plot results
# MAGIC 1. Add notebook parameters with widgets
# MAGIC
# MAGIC
# MAGIC ##### Databricks Notebook Utilities
# MAGIC - <a href="https://docs.databricks.com/notebooks/notebooks-use.html#language-magic" target="_blank">Magic commands</a>: `%python`, `%scala`, `%sql`, `%r`, `%sh`, `%md`
# MAGIC - <a href="https://docs.databricks.com/dev-tools/databricks-utils.html" target="_blank">DBUtils</a>: `dbutils.fs` (`%fs`), `dbutils.notebooks` (`%run`), `dbutils.widgets`
# MAGIC - <a href="https://docs.databricks.com/notebooks/visualizations/index.html" target="_blank">Visualization</a>: `display`, `displayHTML`

# COMMAND ----------

# MAGIC %md ### Setup
# MAGIC Run classroom setup to mount Databricks training datasets and create your own database for BedBricks.
# MAGIC
# MAGIC Use the `%run` magic command to run another notebook within a notebook

# COMMAND ----------

# MAGIC %sh pwd

# COMMAND ----------

# MAGIC %md ### Execute code in multiple languages
# MAGIC Run default language of notebook

# COMMAND ----------

spark

# COMMAND ----------

print("Run default language")

# COMMAND ----------

# MAGIC %md Run language specified by language magic commands: `%python`, `%scala`, `%sql`, `%r`

# COMMAND ----------

print("Run python")

# COMMAND ----------

# MAGIC %scala
# MAGIC println("Run scala")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Run SQL"

# COMMAND ----------

# MAGIC %r
# MAGIC print("Run R", quote=FALSE)

# COMMAND ----------

# MAGIC %md Run shell commands on the driver using the magic command: `%sh`

# COMMAND ----------

# MAGIC %sh ps | grep 'java'

# COMMAND ----------

# MAGIC %md Render HTML using the function: `displayHTML` (available in Python, Scala, and R)

# COMMAND ----------

html = """<h1 style="color:red;text-align:center;font-family:Courier">Render HTML</h1>"""
displayHTML(html)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Create documentation cells
# MAGIC Render cell as <a href="https://www.markdownguide.org/cheat-sheet/" target="_blank">Markdown</a> using the magic command: `%md`  
# MAGIC
# MAGIC Below are some examples of how you can use Markdown to format documentation. Click this cell and press `Enter` to view the underlying Markdown syntax.
# MAGIC
# MAGIC
# MAGIC # Heading 1
# MAGIC ### Heading 3
# MAGIC > block quote
# MAGIC
# MAGIC 1. **bold**
# MAGIC 2. *italicized*
# MAGIC 3. ~~strikethrough~~
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC - [link](https://www.markdownguide.org/cheat-sheet/)
# MAGIC - `code`
# MAGIC
# MAGIC ```
# MAGIC {
# MAGIC   "message": "This is a code block",
# MAGIC   "method": "https://www.markdownguide.org/extended-syntax/#fenced-code-blocks",
# MAGIC   "alternative": "https://www.markdownguide.org/basic-syntax/#code-blocks"
# MAGIC }
# MAGIC ```
# MAGIC
# MAGIC ![Spark Logo](https://www.databricks.com/sites/default/files/2023-03/spark_logo_2x.png?v=1679022098)
# MAGIC
# MAGIC | Element         | Markdown Syntax |
# MAGIC |-----------------|-----------------|
# MAGIC | Heading         | `#H1` `##H2` `###H3` `#### H4` `##### H5` `###### H6` |
# MAGIC | Block quote     | `> blockquote` |
# MAGIC | Bold            | `**bold**` |
# MAGIC | Italic          | `*italicized*` |
# MAGIC | Strikethrough   | `~~strikethrough~~` |
# MAGIC | Horizontal Rule | `---` |
# MAGIC | Code            | ``` `code` ``` |
# MAGIC | Link            | `[text](https://www.example.com)` |
# MAGIC | Image           | `[alt text](image.jpg)`|
# MAGIC | Ordered List    | `1. First items` <br> `2. Second Item` <br> `3. Third Item` |
# MAGIC | Unordered List  | `- First items` <br> `- Second Item` <br> `- Third Item` |
# MAGIC | Code Block      | ```` ``` ```` <br> `code block` <br> ```` ``` ````|
# MAGIC | Table           |<code> &#124; col &#124; col &#124; col &#124; </code> <br> <code> &#124;---&#124;---&#124;---&#124; </code> <br> <code> &#124; val &#124; val &#124; val &#124; </code> <br> <code> &#124; val &#124; val &#124; val &#124; </code> <br>|

# COMMAND ----------

# MAGIC %md ## Access DBFS (Databricks File System)
# MAGIC The <a href="https://docs.databricks.com/data/databricks-file-system.html" target="_blank">Databricks File System</a> (DBFS) is a virtual file system that allows you to treat cloud object storage as though it were local files and directories on the cluster.
# MAGIC
# MAGIC Run file system commands on DBFS using the magic command: `%fs`

# COMMAND ----------

# MAGIC %fs help

# COMMAND ----------

# MAGIC %fs ls

# COMMAND ----------

# MAGIC %fs ls "dbfs:/Volumes/"

# COMMAND ----------

# MAGIC %fs ls "dbfs:/Workspace/"

# COMMAND ----------

# MAGIC %fs ls "dbfs:/databricks-datasets/"

# COMMAND ----------

# MAGIC %fs head /databricks-datasets/README.md

# COMMAND ----------

# MAGIC %md `%fs` is shorthand for the <a href="https://docs.databricks.com/dev-tools/databricks-utils.html" target="_blank">DBUtils</a> module: `dbutils.fs`

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.fs.ls("dbfs:/databricks-datasets/")

# COMMAND ----------

# MAGIC %fs
# MAGIC ls /databricks-datasets

# COMMAND ----------

files = dbutils.fs.ls("/databricks-datasets")
#display(files)

display(dbutils.fs.ls("/databricks-datasets"))

# COMMAND ----------

a = "clase"

# COMMAND ----------

# MAGIC %md
# MAGIC ###Widgets

# COMMAND ----------

dbutils.widgets.removeAll()

# COMMAND ----------

# MAGIC %sql
# MAGIC REMOVE WIDGET clase2

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET TEXT state DEFAULT "NA"

# COMMAND ----------

dbutils.widgets.text("clase2","25-11-2025")

# COMMAND ----------

valor = dbutils.widgets.get("state")
valor

# COMMAND ----------

# MAGIC %sql
# MAGIC select :state as state

# COMMAND ----------

# MAGIC %sql
# MAGIC select getArgument("state") as state

# COMMAND ----------

# MAGIC %sql
# MAGIC select ${state}

# COMMAND ----------

dbutils.widgets.text("name", "Brickster", "Name")

# COMMAND ----------

dbutils.widgets.multiselect("colors", "orange", ["red", "orange", "black", "blue"], "Favorite Color?")

# COMMAND ----------

# MAGIC %md
# MAGIC ###Uso de Widgets

# COMMAND ----------

## Catalog --> Schema / Database --> Table

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_catalog(),current_database()

# COMMAND ----------

# MAGIC %sql
# MAGIC create table empleados_test;

# COMMAND ----------

# MAGIC %sql
# MAGIC DROP TABLE IF EXISTS workspace.default.empleados;

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS workspace.default.empleados (
# MAGIC   id INT,
# MAGIC   nombre STRING,
# MAGIC   edad INT,
# MAGIC   salario DOUBLE
# MAGIC )
# MAGIC USING DELTA;

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC INSERT INTO workspace.default.empleados VALUES 
# MAGIC   (1, 'Ana', 30, 3500.0),
# MAGIC   (2, 'Luis', 45, 4200.0),
# MAGIC   (3, 'Carla', 28, 3000.0);

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE WIDGET TEXT nombre DEFAULT "";

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados

# COMMAND ----------

# MAGIC %md
# MAGIC ###Captura de parametros en SQL

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados where lower(nombre) = getArgument("nombre")

# COMMAND ----------

# MAGIC %sql
# MAGIC --select * from workspace.default.empleados where lower(nombre) = :nombre
# MAGIC select * from workspace.default.empleados where lower(nombre) = '$nombre'

# COMMAND ----------

# MAGIC %md
# MAGIC ###Captura de parametros en Python

# COMMAND ----------

dbutils.widgets.get("nombre")

# COMMAND ----------

from pyspark.sql.functions import *

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados

# COMMAND ----------

dbutils.widgets.multiselect("nombre1","nombre1",["Luis","Carla","Ana"])

dbutils.widgets.multiselect("colors", "orange", ["red", "orange", "black", "blue"], "Favorite Color?")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados where nombre in ($nombre)

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from workspace.default.empleados where nombre in ($nombre)

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_timestamp()

# COMMAND ----------

# MAGIC %sql
# MAGIC select date_format(current_timestamp(),"yyyy-MM-dd") as fecha

# COMMAND ----------

# MAGIC %sql
# MAGIC select date_format('$nombre',"yyyyMMdd") as fecha

# COMMAND ----------

valor = dbutils.widgets.get("nombre")
valor = valor.split(",")

spark.table("empleados").filter(col("nombre").isIn=valor).display()

# COMMAND ----------

# MAGIC %md
# MAGIC ###Catalog

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW CATALOGS

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT current_catalog()

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE CATALOG IF NOT EXISTS catalog_dev

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW DATABASES IN catalog_dev ;

# COMMAND ----------

# MAGIC %sql
# MAGIC SHOW SCHEMAS IN workspace ;

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_catalog();

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_dev.bronze;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_dev.silver;
# MAGIC CREATE SCHEMA IF NOT EXISTS catalog_dev.golden;

# COMMAND ----------

# MAGIC %md
# MAGIC ### Tipos de vistas en Spark SQL (Databricks)
# MAGIC
# MAGIC | Tipo de vista              | Persistencia        | Alcance                               | Disponible tras reinicio | Esquema requerido     |
# MAGIC |----------------------------|---------------------|----------------------------------------|---------------------------|------------------------|
# MAGIC | `CREATE VIEW`              | Persistente         | Global (visible en toda la base de datos) | ✅ Sí                    | Sí (`USE db_name`)     |
# MAGIC | `CREATE TEMP VIEW`         | Temporal (memoria)  | Solo dentro del notebook actual        | ❌ No                    | ❌ No                   |
# MAGIC | `CREATE GLOBAL TEMP VIEW`  | Temporal (memoria)  | Todos los notebooks de la sesión       | ❌ No                    | Sí: `global_temp`       |
# MAGIC
# MAGIC ✅ **Tips**:
# MAGIC - Usa `CREATE VIEW` para lógica reutilizable o reportes.
# MAGIC - Usa `TEMP VIEW` para cálculos intermedios dentro del notebook.
# MAGIC - Usa `GLOBAL TEMP VIEW` si necesitas compartir vistas entre notebooks de una misma sesión.
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC select current_catalog(),current_database()

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Vista disponible en cualquier notebook que acceda al schema creado
# MAGIC CREATE OR REPLACE VIEW empleados_fltrados AS
# MAGIC SELECT * FROM workspace.default.empleados

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from empleados_fltrados

# COMMAND ----------

# MAGIC %sql
# MAGIC --Resultado: Solo puedes usar esta vista en el mismo notebook. Se borra al cerrar el notebook.
# MAGIC CREATE OR REPLACE TEMP VIEW empleados_fltrados_tmp AS
# MAGIC SELECT * FROM workspace.default.empleados

# COMMAND ----------

# MAGIC %sql
# MAGIC -- Consulta view temporal
# MAGIC select * from empleados_fltrados_tmp

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE OR REPLACE GLOBAL TEMP VIEW empleados_fltrados_global AS
# MAGIC SELECT * FROM workspace.default.empleados

# COMMAND ----------

# MAGIC %md
# MAGIC ###Consultando archivos

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from csv.`dbfs:/databricks-datasets/COVID/coronavirusdataset/PatientRoute.csv`;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table workspace.default.clase2_smartdata as select * from csv.`dbfs:/databricks-datasets/COVID/coronavirusdataset/PatientRoute.csv`;

# COMMAND ----------

# MAGIC %sql
# MAGIC create table workspace.default.clase2_smartdata_csv (
# MAGIC   patient_id string, 
# MAGIC   date string,
# MAGIC   province string,
# MAGIC   city string,
# MAGIC   type string,
# MAGIC   latitude string,
# MAGIC   longitude string
# MAGIC )
# MAGIC options (
# MAGIC   header = "true",
# MAGIC   delimiter = ",",
# MAGIC   path = "dbfs:/databricks-datasets/COVID/coronavirusdataset/PatientRoute.csv"
# MAGIC )

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from json.`dbfs:/databricks-datasets/structured-streaming/events/file-0.json`;
