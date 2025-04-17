from pyspark.sql.functions import hour,count,col,lpad,when,concat_ws,lit,date_format

def Peak_Hours(tablename):
    df = tablename.withColumn('Hour', hour(tablename['order_time']))
    # df.select('order_time', 'Hour').show()

    result = df.groupBy("Hour").agg(count('Hour').alias('No_of_orders'))
    result = result.orderBy(result.No_of_orders.desc())
    # result.show(n=24)

    result = result.withColumn("formatted_hour", concat_ws(":", col("Hour"), lit("00")))
    df_with_12hr = result.withColumn('Time_12hr', date_format(col("formatted_hour"), "hh:mm:a"))
    df_with_12hr=df_with_12hr.select('time_12hr','No_of_orders')
    return df_with_12hr