from fastapi import FastAPI, Query
from duckduckgo_search import DDGS
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # В проде лучше ограничить доменами!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/image/search")
def image_search(q: str = Query(..., description="Search query")):
    with DDGS() as ddgs:
        results = list(ddgs.images(q, safesearch="moderate"))
        if not results:
            return {"error": "No images found"}
        return {"image": results[0]["image"]} 