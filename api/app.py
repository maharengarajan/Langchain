from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os


load_dotenv()

os.environ['OPENAI_API_KEY']=os.getenv("OPENAI_API_KEY")


app = FastAPI(
    title = "Langchain Server",
    version="1.0",
    description= "A simple API server"
)


model = ChatOpenAI()
llm = Ollama(model = "llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} for a 5 years child with 100 words")


add_routes(app,ChatOpenAI(), path="/openai")

add_routes(app, prompt1|model, path="/essayyyy")

add_routes(app, prompt2|llm, path="/poemmmmm")


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=5000)
