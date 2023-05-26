from pyspark.sql import SparkSession

# Inicializa uma sessão Spark
spark = SparkSession.builder \
    .appName("Vasco") \
    .getOrCreate()

# Carrega um arquivo CSV em um DataFrame
dataframe = spark.read.csv("clientes.csv", header=True, inferSchema=True)

# Registra o DataFrame como uma tabela temporária para consultas SQL
dataframe.createOrReplaceTempView("minha_tabela")

# Executa uma consulta SQL no DataFrame
resultado = spark.sql("SELECT * FROM minha_tabela WHERE coluna = 'valor'")

# Exibe o resultado
resultado.show()

# Encerra a sessão Spark
spark.stop()