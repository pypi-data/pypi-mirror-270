import base64

class Base64ToFile:
    def __init__(self, base64_str, file_path, ext):
        decoded_data = base64.b64decode(base64_str)
    
        file_path = f"{file_path}.{ext}"
        
        with open(file_path, "wb") as file:
            file.write(decoded_data)
