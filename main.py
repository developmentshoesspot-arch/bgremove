from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from rembg import remove, new_session
import io

app = FastAPI()

session = new_session()

@app.post("/remove-bg/")
async def remove_bg(file: UploadFile = File(...)):
    input_image = await file.read()
    output = remove(input_image, session=session)
    return StreamingResponse(io.BytesIO(output), media_type="image/png")
