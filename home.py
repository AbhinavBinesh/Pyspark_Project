from data_loading import Create_dataframe
import logs.log_fn as log

data_path="Data/Rider-Info.csv"
try:
    food_delivery=Create_dataframe(data_path,True)
    food_delivery.show()
    print("---Dataframe created successfully---")
    print("**************************************")
    food_delivery.printSchema()

    log.log_Info("---Dataframe created Successfully---")

except Exception as e:
    print(f'There is some error while creating table:{e}')
    print("**************************************")

    log.log_Error(e)

print("**************************Analytics1********************************")

from Analytics.file1 import Peak_Hours

try:
    result=Peak_Hours(food_delivery)
    result.show()
    result.write.csv('Result/Analytics1',header=True,mode="overwrite")
    log.log_Info("Analytics 1 executed and result generated")
except Exception as e:
    log.log_Error(e)

from Analytics.file2 import evening_riders

try:
    result=evening_riders(food_delivery)
    result.show()
    result.write.csv('Result/Analytics2',header=True,mode="overwrite")
    log.log_Info('Analytics2 executed and result generated')
except Exception as e:
    log.log_Error(e)