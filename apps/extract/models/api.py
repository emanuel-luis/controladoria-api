from pydantic import BaseModel
from enum import StrEnum
from typing import Optional
from models.document import Type
from pathlib import Path


class GeminiModels(StrEnum):
    GEMINI_FLASH_2_5 = "gemini-2.5-flash"
    # Add other models as needed ...


class GetDocumentMetadataRequest(BaseModel):
    model: GeminiModels = GeminiModels.GEMINI_FLASH_2_5
    content: str | Path
    type: Type
    content_mime_type: Optional[str] = None
    temperature: Optional[float] = None
