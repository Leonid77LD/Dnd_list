from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def chek():
    return 'Hello world'
