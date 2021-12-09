# uvicorn Server:app --reload --host 172.29.202.31 --port 2333
# uvicorn Server:app --reload --port 2333

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_routers import CMS, Mail, Printer, ReportFormDownload, User

app = FastAPI(debug=True)
app.include_router(router=Mail.router)
app.include_router(router=CMS.router)
app.include_router(router=User.router)
app.include_router(router=ReportFormDownload.router)
app.include_router(router=Printer.router)


# 跨域策略
origins = [
    "http://localhost:8080",
    "http://172.29.202.30:8080",
    "http://172.29.202.31:8080",
]
methods = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=methods,
    allow_credentials=True,
    allow_headers=["*"]
)


@app.get("/")
async def root() -> dict:
    """测试"""
    return {"Detail": "Server is running."}


if __name__ == '__main__':
    uvicorn.run(app, host='172.29.202.31', port=2333, debug=True)
