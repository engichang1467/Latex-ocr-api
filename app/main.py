import io
import shutil
from PIL import Image
from pix2tex.cli import LatexOCR
from tempfile import NamedTemporaryFile

from fastapi.responses import JSONResponse
from fastapi import FastAPI, File, UploadFile

app = FastAPI()
latex_ocr_model = LatexOCR()

@app.get("/")
def read_root():
    return {"status": "ok"}

# Takes in an image and returns the latex code
@app.post("/latex/")
async def read_item(file: UploadFile = File(...)):
    # Create a temporary file to store the uploaded file's contents
    with NamedTemporaryFile(delete=False) as temp_file:
        # Copy the uploaded file's contents to the temporary file
        shutil.copyfileobj(file.file, temp_file)
        temp_file_path = temp_file.name

    # Ensure the file pointer is at the start
    file.file.seek(0)

    try:
        # Open the temporary file and pass its file object to the model
        with open(temp_file_path, 'rb') as temp_file_obj:
            img_data = temp_file_obj.read()

        img_bytes = io.BytesIO(img_data)
        img = Image.open(img_bytes)
        latex_code = latex_ocr_model(img)
        return {"latex": latex_code}
    except Exception as e:
        return JSONResponse(status_code=400, content={"message": str(e)})
    finally:
        # Clean up: close and remove the temporary file
        file.file.close()