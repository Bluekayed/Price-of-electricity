from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import aiosqlite
import httpx

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_PATH = "prices.db"
BASE_URL = "https://www.sahkohinta-api.fi/api/v1/halpa?"
HOURS = "24"
RESULT = "haja"

async def init_db():
    async with aiosqlite.connect(DB_PATH) as db:
        await db.execute("""
            CREATE TABLE IF NOT EXISTS prices (            
                time INTEGER
                price REAL               
                         )""")

        await db.commit()

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
async def get_data():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}tunnit={HOURS}&tulos={RESULT}")
        return response.json()