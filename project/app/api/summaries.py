# -*- coding: utf-8 -*-
# project/app/api/summaries.py
from typing import List

from app.api import crud
from app.models.pydantic import (
    SummaryPayloadSchema,
    SummaryResponseSchema,
    SummaryUpdatePayloadSchema,
)
from app.models.tortoise import SummarySchema
from fastapi import APIRouter, HTTPException, Path

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(
    payload: SummaryPayloadSchema,
) -> SummaryResponseSchema:
    """
    Yo Mama!
    """
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url,
    }
    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(
    id: int = Path(..., title="Retreiving summary", gt=0)
) -> SummarySchema:
    """
    Yo Daddy!
    """
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary


@router.get("/", response_model=List[SummarySchema])
async def read_all_summaries() -> List[SummarySchema]:
    return await crud.get_all()


@router.delete("/{id}/", response_model=SummaryResponseSchema)
async def delete_summary(
    id: int = Path(..., title="Remove summary by it's id", gt=0)
) -> SummaryResponseSchema:
    """
    Yo Papi!
    """
    summary = await crud.get(id)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    await crud.delete(id)
    return summary


@router.put("/{id}/", response_model=SummarySchema)
async def update_summary(
    *,
    id: int = Path(..., title="Update your summary", gt=0),
    payload: SummaryUpdatePayloadSchema,
) -> SummarySchema:
    """
    This endpoint is used to update the summary.
    """
    summary = await crud.put(id, payload)
    if not summary:
        raise HTTPException(status_code=404, detail="Summary not found")

    return summary
