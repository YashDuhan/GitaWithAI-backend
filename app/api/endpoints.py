import json
import os

# GITA PATH
GITA_JSON_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'geeta.json')

# Default route
async def root():
    return {"message": "Welcome to the Gita With AI Backend"}

# Health check route
async def health_check():
    return {"status": "ok"}

# Fetch chapters
async def fetch_chapters():
    with open(GITA_JSON_PATH, 'r', encoding='utf-8') as f:
        gita_data = json.load(f)
        chapters = [{
            "Chapter": chapter["Chapter"],
            "ChapterName": chapter["ChapterName"]
        } for chapter in gita_data]
    return {"chapters": chapters}

