# -*- coding: utf-8 -*-
<<<<<<< HEAD
from fastapi import Depends, FastAPI

from app.config import Settings, get_settings
||||||| 9955828
from fastapi import Depends, FastAPI

from config import Settings, get_settings
=======
from config import Settings, get_settings
from fastapi import Depends, FastAPI
>>>>>>> 996c3526f2152019d36e1bb1b1cf27e6ce66251c

app = FastAPI()


@app.get("/ping")
async def pong(settings: Settings = Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
    }
