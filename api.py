from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/hello-world")
def hello_world():
	return "Hello world"

if __name__ == "__main__":
	uvicorn.run(app, port=8000, host="127.0.0.1", reload=True)