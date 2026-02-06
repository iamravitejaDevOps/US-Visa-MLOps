import sys
from us_visa.exception import USvisaException
from us_visa.logger import logging
from us_visa.components.data_ingestion import DataIngestion
from us_visa.entity.config_entity import (DataingestionConfig)
from us_visa.entity.artifact_entity import (DataIngestionArtifact)




class TrainingPipeline:
  def __init__(self):
    self.data_ingestion_config = DataingestionConfig()

  
  def start_data_ingestion(self)-> DataIngestionArtifact:
    """
    
    This method of TrainingPipeline Class is responsible for starting Dataingestion component
    """
    try:
      logging.info("Enterd the start_data_ingestion method of TrainPipleine Class")
      logging.info("Getting the data from mongodb")
      data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
      data_ingestion_artifact = data_ingestion.intiate_data_ingestion()
      logging.info("Got the train_set and test_set from mongoDB")
      logging.info("Exited the start_data_ingestion method of TrainPipeline Class")

      return data_ingestion_artifact
    except Exception as e:
      raise USvisaException(e,sys)
    

  
  def run_pipeline(self,)->None:
    """
     This method of TrainPipeline class is responsible for running complete pipeline
    """

    try:
      data_ingestion_artifact = self.start_data_ingestion()


    except Exception as e:
      raise USvisaException(e,sys)    