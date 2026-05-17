import os
import time
import requests
import logging
import asyncio
from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
import uvicorn

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("TTS-FAST")

OPENAI_API_KEY = ""
MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"
MAX_CHUNK_LEN = 900

# Custom pronunciation mappings - use phonetic spelling instead of IPA
PRONUNCIATION_MAP = {
    "Onified": "won-ee-fied",
}

app = FastAPI(title="Ultra Fast Text-to-Speech (Direct Key)")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def apply_pronunciation(text: str) -> str:
    """Replace words with their phonetic pronunciations."""
    import re
    result = text
    for word, pronunciation in PRONUNCIATION_MAP.items():
        # Case-insensitive replacement, preserving sentence boundaries
        result = re.sub(rf'\b{re.escape(word)}\b', pronunciation, result, flags=re.IGNORECASE)
    return result

def split_text(text, max_len=MAX_CHUNK_LEN):
    import re
    sentences = re.split(r'([।.!?])', text)
    chunks = []
    chunk = ""
    for i in range(0, len(sentences), 2):
        part = sentences[i]
        end = sentences[i+1] if i+1 < len(sentences) else ""
        if len(chunk) + len(part) + len(end) > max_len:
            if chunk:
                chunks.append(chunk.strip())
            chunk = part + end
        else:
            chunk += part + end
    if chunk:
        chunks.append(chunk.strip())
    return chunks

def stream_tts_chunk(text_chunk: str):
    url = "https://api.openai.com/v1/audio/speech"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
    }
    payload = {"model": MODEL, "voice": VOICE, "input": text_chunk}
    try:
        with requests.post(url, json=payload, headers=headers, stream=True, timeout=60) as r:
            if r.status_code != 200:
                logger.error(f"TTS chunk error: {r.status_code} - {r.text}")
                return
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    yield chunk
    except Exception as e:
        logger.error(f"TTS streaming failed: {e}")
        return

@app.post("/tts")
async def tts_endpoint(text: str = Form(...)):
    logger.info(f"TTS request: {text[:80]}...")
    
    # Apply pronunciation replacements
    processed_text = apply_pronunciation(text)
    logger.info(f"Applied pronunciations: {processed_text[:80]}...")
    
    async def combined_stream():
        chunks = split_text(processed_text)
        logger.info(f"Text split into {len(chunks)} parts")
        for i, chunk in enumerate(chunks):
            logger.info(f"Streaming part {i+1}/{len(chunks)}")
            for data in stream_tts_chunk(chunk):
                yield data
    headers = {
        "Content-Disposition": f'attachment; filename="tts_{int(time.time())}.mp3"'
    }
    return StreamingResponse(combined_stream(), media_type="audio/mpeg", headers=headers)

if __name__ == "__main__":
    uvicorn.run("tts_api:app", host="0.0.0.0", port=8181, reload=True)