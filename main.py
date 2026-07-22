import base64
from io import BytesIO
import os
from urllib.parse import urlparse
import uvicorn
import requests

from PIL import Image
from pathlib import Path
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

api_key = os.getenv("API_KEY")

@app.get("/APOD")
def apod():

    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")

    url = data.json()['url']

    resposta = requests.get(url)
    resposta.raise_for_status()

    nome_arquivo = Path(urlparse(url).path).name
    destino = Path("images") / nome_arquivo

    with open(destino, "wb") as f:
        f.write(resposta.content)
    print(url)

    date = data.json()['date']
    print(date)

    explanation = data.json()['explanation']
    print(explanation)

    hdurl = data.json()['hdurl']    
    print(hdurl)


    return data.json()


@app.get("/NEO")
def neo():

    data = requests.get(f"https://api.nasa.gov/neo/rest/v1/feed?api_key={api_key}")

    

    return data.json()

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000)
