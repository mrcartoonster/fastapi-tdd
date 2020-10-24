# -*- coding: utf-8 -*-
import logging

from app.api import ping, summaries
from app.db import init_db
from fastapi import FastAPI

log = logging.getLogger(__name__)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(ping.router, tags=["ping"])
    application.include_router(
        summaries.router,
        prefix="/summaries",
        tags=["summaries"],
    )

    return application


app = create_application()


@app.on_event("startup")
async def start_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
