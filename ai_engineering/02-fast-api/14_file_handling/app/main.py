from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil

app = FastAPI()

UPLOAD_DIR = "uploads"


@app.get("/", response_class=HTMLResponse)
async def get_upload_forms():
    return """
    <html>
        <body>
            <br>
            <h2>Upload File Using bytes</h2>
            <form method="post" action="/upload/bytes" enctype="multipart/form-data">
                <input type="file" name="file" required>
                <button type="submit">Upload</button>
            </form> <br>

            <hr><br>

            <h2>Upload File Using UploadFile</h2>
            <form method="post" action="/upload/file" enctype="multipart/form-data">
                <input type="file" name="file" required>
                <button type="submit">Upload</button>
            </form>
        </body>
    </html>
    """


# Route 1: Upload using bytes
@app.post("/upload/bytes")
async def upload_file_bytes(file: Annotated[bytes, File()]):
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    filename = f"{uuid.uuid4()}.bin"
    save_path = os.path.join(UPLOAD_DIR, filename)
    with open(save_path, "wb") as buffer:
        buffer.write(file)

    return {
        "message": "File uploaded using bytes",
        "filename": filename,
        "size_bytes": len(file),
        "path": save_path,
    }


# Route 2: Upload using UploadFile
@app.post("/upload/file")
async def upload_file_uploadfile(file: Annotated[UploadFile, File()]):
    os.makedirs(UPLOAD_DIR, exist_ok=True)

    extension = os.path.splitext(file.filename or "")[1]
    filename = f"{uuid.uuid4()}{extension}"
    save_path = os.path.join(UPLOAD_DIR, filename)

    try:
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        return {
            "message": "File uploaded using UploadFile",
            "filename": filename,
            "content_type": file.content_type,
            "size_bytes": os.path.getsize(save_path),
            "path": save_path,
        }
    finally:
        await file.close()
