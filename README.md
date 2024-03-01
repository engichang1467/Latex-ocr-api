# Latex OCR API

This is a simple API that uses the LatexOCR from the [`pix2tex`](https://github.com/lukas-blecher/LaTeX-OCR) package to extract latex code from an image.

## Create the Environment

```bash
pip install virtualenv

# Create the virtual environment
virtualenv venv

# Activate the virtual environment
source venv/bin/activate
```

## Install the requirements

```bash
pip install -r requirements.txt

pip install -r requirements-dev.txt
```

## Run the API

```bash
uvicorn app.main:app --reload
```

## Test the API

```bash
pytest
```

## Build the Docker Image

```bash
docker build -t latex-ocr-api .
```

## Run the Docker Image

```bash
docker run -p 8000:8000 latex-ocr-api
```

