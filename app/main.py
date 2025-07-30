from .settings import settings
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.responses import RedirectResponse, JSONResponse

from langchain_openai import ChatOpenAI

from .llm_integration import write_letter
from  .schemas import UserInput

def get_llm_client():
    llm = ChatOpenAI(
        model = settings.get_llm_name(),
        api_key = settings.get_llm_token(),
        base_url= settings.get_key_provider()
    )
    settings.llm = llm
    return llm

@asynccontextmanager
async def lifespan(app: FastAPI):
    get_llm_client()
    yield

letter_app = FastAPI(lifespan=lifespan)

@letter_app.get("/")
async def root():
    return RedirectResponse(url="/createLetter/", status_code=307)

@letter_app.post("/createLetter/")
async def send(user_input: UserInput) -> JSONResponse:
    result = await write_letter(user_input)
    return JSONResponse(content={
        "message": result,
        "user_name": user_input.name, 
        "user_reason": user_input.reason
    })
