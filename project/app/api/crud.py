# -*- coding: utf-8 -*-
# project/app/api/crud.py
# These are the helper functions to the make calls to the postgres db table
# textsummary. This is where FastAPI function calls get the information from.

from typing import List, Union

from app.models.pydantic import SummaryPayloadSchema
from app.models.tortoise import TextSummary


async def post(payload: SummaryPayloadSchema) -> int:
    """
    The query that will add the url and summary to the textsummary
    database.json The FastAPI function call that handles this is
    create_summary.
    """
    summary = TextSummary(
        url=payload.url,
        summary="",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> Union[dict, None]:
    """
    The query that recieves a specific summary from the textsummary
    database.

    The FastAPI endpoint that handles this is the read_summary function.

    """
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary[0]
    return None


async def get_all() -> List:
    """
    This query gets all the values in the database.

    The read_all_summaries function uses this helper.

    """
    summaries = await TextSummary.all().values()
    return summaries


async def delete(id: int) -> int:
    """
    Deletes the select summary by id.
    """
    summary = await TextSummary.filter(id=id).first().delete()
    return summary


async def put(id: int, payload: SummaryPayloadSchema) -> Union[dict, None]:
    summary = await TextSummary.filter(id=id).update(
        url=payload.url,
        summary=payload.summary,
    )

    if summary:
        updated_summary = await TextSummary.filter(id=id).first().values()
        return updated_summary[0]

    return None
