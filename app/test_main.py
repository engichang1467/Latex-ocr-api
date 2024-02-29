from fastapi.testclient import TestClient

from .main import app  # Import your FastAPI app
from pathlib import Path
from PIL import Image
import io

client = TestClient(app)


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_valid_image_upload():
    # Create a sample image file in memory for testing
    image_file = Path.cwd().joinpath("app/image_samples/formula_test.png")

    with open(image_file, "rb") as file:
        img_data = file.read()

    image_bytes = io.BytesIO(img_data)

    response = client.post(
        "/latex/", files={"file": ("formula_test.png", image_bytes, "image/png")}
    )

    # Check if the response status code is 200 (OK)
    assert response.status_code == 200


def test_invalid_image_upload():
    # Create a sample text file in memory instead of an image for testing
    text_data = b"mock text data"
    text_file = io.BytesIO(text_data)

    response = client.post(
        "/latex/", files={"file": ("test_text.txt", text_file, "text/plain")}
    )

    # Check if the response status code is 400 (Bad Request) due to an exception being raised
    assert response.status_code == 400
