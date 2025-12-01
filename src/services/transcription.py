from typing import Optional

import speech_recognition as sr
r = sr.Recognizer()


def get_transcription(path: str) -> Optional[str]:
    """
    Преобразует аудиофайл в формате .wav в транскрипцию .txt.

    Args:
        path (str): Путь к аудиофайлу в формате .wav

    Returns:
        Optional[str]: Текст транскрипции,
                       None в случае ошибки
    """
    try:
        with open(path, 'rb'):
            pass

    except FileNotFoundError:
        raise FileNotFoundError(f"Аудиофайл не найден по пути: {""}")
    except IOError:
        raise ValueError(f"Невозможно прочитать файл или неподдерживаемый формат: {""}")
