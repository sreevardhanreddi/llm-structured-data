ALLOWED_FILE_TYPES = [
    "image/jpeg",
    "image/png",
    "image/jpg",
    "application/pdf",
]

MAX_FILE_SIZE = 10 * 1024 * 1024


def validate_file(file_type: str, file_size: int):
    if file_type not in ALLOWED_FILE_TYPES:
        return False
    if file_size > MAX_FILE_SIZE:
        return False
    return True
