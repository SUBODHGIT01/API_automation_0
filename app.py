from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import subprocess
import os

app = FastAPI()

templates = Jinja2Templates(directory="ui/templates")

TEST_FOLDER = "tests"


def get_tests():
    tests = []
    for file in os.listdir(TEST_FOLDER):
        if file.startswith("test_") and file.endswith(".py"):
            tests.append(file)
    return tests


@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    tests = get_tests()

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "tests": tests
        }
    )


@app.get("/run_all")
def run_all():

    result = subprocess.run(
        ["pytest", "-v"],
        capture_output=True,
        text=True
    )

    return {"result": result.stdout}


@app.get("/run_marker/{marker}")
def run_marker(marker: str):

    result = subprocess.run(
        ["pytest", "-m", marker, "-v"],
        capture_output=True,
        text=True
    )

    return {"result": result.stdout}


@app.get("/run_test/{test_name}")
def run_single(test_name: str):

    result = subprocess.run(
        ["pytest", f"tests/{test_name}", "-v"],
        capture_output=True,
        text=True
    )

    return {"result": result.stdout}


@app.post("/add_api")
def add_api(api_name: str):

    path = f"tests/test_{api_name}.py"

    content = f"""
import pytest

@pytest.mark.regression
def test_{api_name}():
    assert True
"""

    with open(path, "w") as f:
        f.write(content)

    return {"message": "API added"}


@app.delete("/delete_api/{test_name}")
def delete_api(test_name: str):

    path = f"tests/{test_name}"

    if os.path.exists(path):
        os.remove(path)

    return {"message": "Deleted"}


app.mount("/static", StaticFiles(directory="ui/static"), name="static")