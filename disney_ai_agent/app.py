from agents.disney_agent import analyseDisneyCharacters
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseDisneyCharacters(prompt=prompt))