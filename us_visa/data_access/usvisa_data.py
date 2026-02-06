from us_visa.configuration.mongo_db_connection import MongoDBClient
from us_visa.constants import DATABASE_NAME
from us_visa.exception import USvisaException
from us_visa.logger import logging
import pandas as pd
import sys
from typing import Optional
import numpy as np


class USvisaData:
  """
    This class help to export entire mongodb record as pandas dataframe
  """

  def __init__(self):
    
    
    try:
      self.mongo_client = MongoDBClient(database_name=DATABASE_NAME)
    except Exception as e:
      raise USvisaException(e,sys)
    


  def export_collection_as_dataframe(self,collection_name:str,data_base_name:Optional[str]=None)->pd.DataFrame:
    try:
      """
      export entire collection as dataframe:
      return pd.DataFrame of collection
      """

      if  data_base_name is None:
        collection  = self.mongo_client.database[collection_name]
      else:
        collection_name = self.mongo_client[data_base_name][collection_name]
      
      df = pd.DataFrame(list(collection.find()))

      if "_id " in df.columns.tolist():
        df = df.drop(columns=['_id'],axis=1)
      df.replace({"na":np.nan},inplace=True)
      return df
    except Exception as e:
      raise USvisaException(e,sys)