from services.disney_service import DisneyService 

ds = DisneyService()

def searchCharacters(query : str):
    print(f"Calling searchCharacters tool {query}")
    return ds.searchCharacters(query)

def getCharacterDetails(characterId : str):
    print(f"Calling getCharacterDetails tool {characterId}")
    return ds.getCharacterDetails(characterId=characterId)
