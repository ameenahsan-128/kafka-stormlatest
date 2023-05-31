from hdfs import InsecureClient  # Importing the necessary module
import json
from queue import Queue
import logging
from streamparse import Bolt
import requests


class Emit(Bolt):  # Defining a class named Emit that extends the Bolt class

    def initialize(self, storm_conf, context):  # Initializing the bolt
        pass

    def process(self, tup):  # Method to process each tuple
        json_data = tup.values[0]  # Extracting the JSON data from the tuple
        try:
            user_data = json.loads(json_data)  # Parsing the JSON data
            personal_info = user_data.get('resume')  # Extracting the 'Personal_info' field from the JSON data
            folder_name = personal_info['Personal_info']['name']  # Extracting the 'Name' field from the 'Personal_info' field
            folder_name = folder_name.replace(" ", "") + str(tup.id)  # Modifying the folder name with tuple id
            id = str(tup.id)  # Converting the tuple id to a string
            if json_data is not None:  # Checking if JSON data exists
                try:
                    self.upload_to_hdfs(json_data, folder_name, id)  # Writing JSON data to HDFS
                    # self.log(f'{folder_name} added to HDFS')  # Logging a success message
                except Exception as e:
                    self.log(f'HDFS Error: {e}')  # Logging an error message
        except ValueError as v:
            self.log(f'ValueError: {v}')  # Logging an error message
            pass
        except TypeError as t:
            self.log(f'typeError: {t}')  # Logging an error message
            pass
        except KeyError as k:
            self.log(f'KeyError: {k}')  # Logging an error message
            pass
        except NameError as e:
            self.log(f'NameError: {e}')  # Logging an error message
            pass

    def upload_to_hdfs(self, json_data, folder_name, id):
        url = f'http://ec2-43-205-15-58.ap-south-1.compute.amazonaws.com:9864/webhdfs/v1/ameen/{str(folder_name+"_"+id[0:4])}/{str(folder_name.lower())}.json?op=CREATE&user.name=ubuntu&namenoderpcaddress=ec2-43-205-15-58.ap-south-1.compute.amazonaws.com:9000&createflag=&createparent=true&overwrite=false'
        headers = {'Content-Type': 'application/octet-stream'}
        response = requests.put(url, data=json_data, headers=headers)

        if response.status_code == 201:
            self.log(f'{folder_name} added to HDFS')
        else:
            self.log(f'HDFS Error: {response.text}')
