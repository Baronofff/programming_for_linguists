from fastapi import APIRouter


router = APIRouter(prefix="/api/v1", tags=["transcription"])


@router.post("/transcribe", summary="Транскрибация аудиофайла")
async def transcribe(file):
    """
    Принимает аудиофайл в формате .wav и возвращает его текстовую транскрипцию.

    Args:
        file: Аудиофайл для транскрибации. Поддерживается только .wav

    Returns:
        JSONResponse: JSON объект с транскрипцией и метаинформацией

    Raises:
        HTTPException: 400 - если файл имеет неверный формат или слишком большой
        HTTPException: 500 - если произошла внутренняя ошибка сервера
    """
    pass