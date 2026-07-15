import os
import uvicorn
import requests

from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

api_key = os.getenv("API_KEY")

@app.get(f"/APOD")
def apod():

    data = requests.get(f"https://api.nasa.gov/planetary/apod?api_key={api_key}")

    url = data.json()['url']
    print(url)

    date = data.json()['date']
    print(date)

    explanation = data.json()['explanation']
    print(explanation)

    hdurl = data.json()['hdurl']    
    print(hdurl)


    return data.json()


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=5000, reload=True)
