import os
import re

def sanitize_folder_name(name):
    invalid_chars = r"[\\/<>*?\"|]"
    sanitized_name = re.sub(invalid_chars, "", name)  # Elimina caracteres inválidos excepto ':' y ';'
    sanitized_name = re.sub(r"([a-zA-Z])[:;]", r"\1 -", sanitized_name)  # Agrega espacio antes del guion si está junto a una letra
    sanitized_name = re.sub(r"[:;]([a-zA-Z])", r"- \1", sanitized_name)  # Agrega espacio después del guion si está junto a una letra
    sanitized_name = re.sub(r"[:;]", "-", sanitized_name)  # Reemplaza ':' y ';' por '-'
    return sanitized_name

def format_folder_name(name):
    exceptions = {"de", "y", "el", "la", "los", "las", "un", "una", "unos", "unas", "con", "en", "por", "para" ,"no", "ni", "to", "ga" "wo", "wa", "o", "e", "a", "i", "u", "na", "ne", "te", "se", "to", "ka", "sa", "ma", "ra", "ya", "ta", "wa", "ha", "na", "la", "za", "for", "of", "the", "and", "a", "an", "in", "on", "at", "with", "by", "to"}
    words = name.split()
    formatted_words = [word.capitalize() if word.lower() not in exceptions else word.lower() for word in words]
    return " ".join(formatted_words)

def create_folders_from_txt(file_path, base_path=".", subfolder_name="subcarpeta"):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                folder_name = line.strip()
                if folder_name:
                    sanitized_name = sanitize_folder_name(folder_name)
                    formatted_name = format_folder_name(sanitized_name)
                    folder_path = os.path.join(base_path, formatted_name)
                    os.makedirs(folder_path, exist_ok=True)
                    
                    subfolder_path = os.path.join(folder_path, subfolder_name)
                    os.makedirs(subfolder_path, exist_ok=True)
                    
                    print(f"Carpeta creada: {folder_path}")
                    print(f"Subcarpeta creada: {subfolder_path}")
    except Exception as e:
        print(f"Error: {e}")

# Ejemplo de uso
file_path = "input.txt"  # Nombre del archivo de texto con los nombres de las carpetas
base_path = "./Output"  # Directorio base donde se crearán las carpetas
subfolder_name = "Season 1"  # Nombre de la subcarpeta a crear en cada carpeta
create_folders_from_txt(file_path, base_path, subfolder_name)
