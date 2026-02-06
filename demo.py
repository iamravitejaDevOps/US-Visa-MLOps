# from us_visa.logger import logging
# from us_visa.exception import USvisaException
# import sys



# # logging.info("Welcome to our custom log")


# try:
#   a=1/"10"
# except Exception as e:
#   raise USvisaException(e,sys) from e


# from us_visa.constants import DATABASE_NAME

# print(DATABASE_NAME)

# from us_visa.constants import * # all the variables 



from us_visa.pipline.training_pipeline import TrainingPipeline

pipeline = TrainingPipeline()
pipeline.run_pipeline()