from fastapi import FastAPI, HTTPException
import json

app = FastAPI()

# Load JSON file
with open("data/ip_data.json", "r") as file:
    ip_data = json.load(file)

@app.get("/")
def home():
    return {"message": "FastAPI Running"}

@app.get("/ip/{ip_address}")
def get_ip_details(ip_address: str):

    for item in ip_data:
        if item["ip"] == ip_address:
            return item

    raise HTTPException(status_code=404, detail="IP not found")