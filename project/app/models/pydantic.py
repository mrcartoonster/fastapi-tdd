# -*- coding: utf-8 -*-
from pydantic import BaseModel


class SummaryPayLoadSchema(BaseModel):
    url: str
