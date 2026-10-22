from services.disney_service import DisneyService 

ds = DisneyService()

def searchCharacters(query : str):
    print(f"Calling searchCharacters tool {query}")
    return ds.searchCharacters(query)

def getCharacterDetails(characterId : str):
    print(f"Calling getCharacterDetails tool {characterId}")
    return ds.getCharacterDetails(characterId=characterId)

def writeHTML(htmlStr: str, fileName : str):
    print(f"Calling writeHTML tool saving in {fileName}")
    with open(fileName, "w") as f:
        f.write(htmlStr)
    return {
        "status": "success",
        "message": f"Written html in {fileName}, please don't display html code in user input only fileName"
    }

def getAvailableTools():
    return [
        searchCharacters,
        getCharacterDetails,
        writeHTML
    ]