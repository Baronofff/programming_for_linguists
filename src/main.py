from fastapi import FastAPI

from src.api.routers import router

app = FastAPI(
    title='Audio Transcription Service',
    description='Сервис для транскрибации аудиофайлов .wav в текст',
    version='1.0.0',
    contact={
        'name': 'baronofff',
        'email': 'baronov.ev@gmail.com'
    }
)
app.include_router(router)


@app.get('/', summary='Корневая страница API')
async def root():
    """
    Корневойй эндпоинт.

    Returns:
        Dict[str, str]: Приветственное сообщение и ссылка на документацию
    """
    return {
        'message': 'Добро пожаловать в сервис транскрибации аудиофайлов',
        'documentation': {
            'swagger': '/docs',
            'redoc': '/redoc'
        },
        'endpoints': {
            'transcribe': 'POST /api/v1/transcribe',
            'health': 'GET /api/v1/health'
        }
    }


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True
    )
