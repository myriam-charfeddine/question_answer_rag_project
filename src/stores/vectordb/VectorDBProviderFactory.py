from .VectorDBEnums import VectorDBEnums
from .providers import QdrantDB
from controllers.BaseController import BaseController 

class VectorDBProviderFactory:
    def __init__(self, config):
        self.config = config
        self.base_controller = BaseController()

    def create(self, provider: str):
        if provider == VectorDBEnums.QDRANT.value:
            db_path = BaseController().get_database_name(db_name=self.config.VECTOR_DB_PATH)
            
            return QdrantDB(
                db_path=db_path,
                distance_method=self.config.VECTOR_DB_DISTANCE_METHOD
            )
        
        return None
