from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post('/upload')
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()
    # TODO: process uploaded file content
    return {'filename': file.filename, 'status': 'received'}
