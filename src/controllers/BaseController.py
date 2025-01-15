from helpers.config import get_settings, Settings
import os
import random
import string

class BaseController:
    def __init__(self):
        self.app_settings = get_settings()
        self.base_dir = os.path.dirname(os.path.dirname(__file__)) #to get the path of the `controllers` folder so we can access external folders
        self.file_dir = os.path.join(
                                    self.base_dir,
                                    "assets/files")
        
        self.database_dir = os.path.join(
            self.base_dir,
            "assets/database"       
            )
        
    def generate_random_string(self, lenght: int = 12):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=lenght))
    
    
    def get_database_name(self, db_name: str):
        database_path = os.path.join(
            self.database_dir, db_name
        )

        if not os.path.exists(database_path):
            os.makedirs(database_path)

        return database_path
        


 

   