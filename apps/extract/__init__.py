from models.api import GetDocumentMetadataRequest
from models import GetDocumentMetadataRequest, REGISTRY
from pydantic import BaseModel
from google import genai
from google.genai import types
from fastapi import FastAPI, HTTPException, responses, status
from pathlib import Path
import os

app = FastAPI()


@app.get("/health")
async def health_check() -> responses.JSONResponse:
    return responses.JSONResponse(content={"status": "ok"}, status_code=status.HTTP_200_OK)


@app.get("/metadata")
async def get_metadata(request: GetDocumentMetadataRequest) -> responses.JSONResponse:
    client = genai.Client(api_key=os.environ["GENAI_API_KEY"])

    if isinstance(request.content, str):
        request.content = Path(request.content)
    if isinstance(request.content, Path):
        if request.content.is_dir():
            raise IsADirectoryError(f"Expected a file but got a directory: {request.content}")
        elif not request.content.exists():
            raise FileNotFoundError(f"File not found: {request.content}")

    descriptor = REGISTRY.get(request.type)
    if not descriptor:
        raise HTTPException(status_code=400, detail=f"Unsupported document type: {request.type}")

    uploaded_content = client.files.upload(
        file=request.content,
        config={
            "mime_type": request.content_mime_type,
            "display_name": descriptor.name.upper(),
        },
    )
    response = client.models.generate_content(
        model=request.model,
        contents=[uploaded_content],
        config=types.GenerateContentConfig(
            response_mime_type=descriptor.response_mime_type,
            response_schema=descriptor.response_schema,
            system_instruction=descriptor.system_instruction,
            temperature=request.temperature,
        ),
    )

    if isinstance(response.parsed, BaseModel):
        result = response.parsed.model_dump(mode="json")
    elif isinstance(response.parsed, dict):
        result = response.parsed
    else:
        raise TypeError("Unexpected response type")
    return responses.JSONResponse(content=result, status_code=status.HTTP_200_OK)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
