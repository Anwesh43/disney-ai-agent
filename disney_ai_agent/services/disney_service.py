from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 

load_dotenv()

class DisneyService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["DISNEY_BASE_URL"])

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "Error",
            "message": str(e)
        }
    def searchCharacters(self, name : str):
        try:
            response = self.client.getCall("character", qpParams={"name": name})
            characters = response["data"]
            result = []
            for character in characters:
                obj = {}
                obj["_id"] = character["_id"]
                obj["name"] = character["name"]
                result.append(obj)
            return result
        except Exception as e:
            return self._handleError(e)

    def getCharacterDetails(self, characterId : str):
        try:
            return self.client.getCall(f"character/{characterId}")
        except Exception as e:
            return self._handleError(e)
    