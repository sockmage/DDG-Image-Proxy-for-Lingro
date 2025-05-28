from fastapi import FastAPI, Query
from duckduckgo_search import DDGS
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

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
            return JSONResponse(content={"error": "No images found"}, media_type="application/json")
        return JSONResponse(content={"image": results[0]["image"]}, media_type="application/json") 