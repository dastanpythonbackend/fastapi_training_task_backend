from fastapi import FastAPI
import uvicorn
from app.api.routes import router


app = FastAPI()
app.include_router(router)

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8080, reload=True)
