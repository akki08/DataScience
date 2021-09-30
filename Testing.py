# Databricks notebook source
import pandas as pd

# COMMAND ----------

df = spark.sql("select * from consumer_insights_internal.abtests_master_table limit 10")

# COMMAND ----------

display(df)

# COMMAND ----------

df.show()

# COMMAND ----------


