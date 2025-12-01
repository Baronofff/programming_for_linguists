import os


def validate_file_extension(filename: str) -> bool:
    """
    Проверяет, имеет ли файл допустимое расширение.

    Args:
        filename (str): Имя файла для проверки

    Returns:
        bool: True если расширение допустимо, False в противном случае
    """
    _, extension = os.path.splitext(filename)

    if extension != '.wav':
        return False
    return True


def validate_file_size(file_size: int, max_size_mb: int = 50) -> bool:
    """
    Проверяет, не превышает ли размер файла максимально допустимый.

    Args:
        file_size (int): Размер файла в мегабайтах
        max_size_mb (int): Максимальный допустимый размер в мегабайтах

    Returns:
        bool: True если размер допустим, False если превышает лимит
    """
    return file_size <= max_size_mb