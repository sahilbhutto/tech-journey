# FastAPI Setup Guide

## 1. Create a Virtual Environment

```bash
python3 -m venv .venv
```

## 2. Activate the Virtual Environment

```bash
source .venv/bin/activate
```

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

## 4. Install FastAPI Standard

```bash
python -m pip install "fastapi[standard]"
```

## 5. Run the FastAPI Server

```bash
fastapi dev main.py
```

Open the API documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

## 6. Deactivate the Virtual Environment

```bash
deactivate
```

## 7. Activate Again Later

Whenever you reopen the project terminal:

```bash
source .venv/bin/activate
```

## 8. Check Installed Packages

```bash
python -m pip list
```

## 9. Save Dependencies

```bash
python -m pip freeze > requirements.txt
```

## 10. Install Dependencies Later

```bash
python -m pip install -r requirements.txt
```

**Note:** Activate the virtual environment before installing packages or running your application. Run these commands from your project directory.
