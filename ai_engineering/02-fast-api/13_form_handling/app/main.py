from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel, Field

app = FastAPI()

class FormData(BaseModel):
    username: str = Field(min_length=3)
    password: str = Field(min_length=8)


# Simple HTML form for testing
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <html>
      <body>
        <h2>Login Form</h2>

        <form action="/login" method="post">
          <label for="username">Username:</label><br/>
          <input type="text" id="username" name="username" required/><br/>

          <label for="password">Password:</label><br/>
          <input type="password" id="password" name="password" required/><br/><br/>

          <input type="submit" value="Submit"/>
        </form>
      </body>
    </html>
    """

# Login Route
@app.post("/login")
async def login(
    username: Annotated[str, Form()],
    password: Annotated[str, Form()]
):
    print(f"Username: {username}")
    print(f"Password: {password}")

    return {
        "message": "Login form submitted successfully",
        "username": username
    }


# With Pydantic Model
@app.post("/login")
async def login(data: Annotated[FormData, Form()]):
    return data


