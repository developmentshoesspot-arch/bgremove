from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove
import io

app = FastAPI()

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()

    # limit size (important)
    if len(input_image) > 2 * 1024 * 1024:
        return {"error": "Image too large (max 2MB)"}

    output = remove(input_image)

    return StreamingResponse(io.BytesIO(output), media_type="image/png")
