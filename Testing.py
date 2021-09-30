# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

df = spark.sql("select * from consumer_insights_internal.abtests_master_table limit 100")

# COMMAND ----------

display(df)

# COMMAND ----------

df.show()

# COMMAND ----------


