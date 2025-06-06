# Folder Generator

Generador de carpetas pensado para organizar Animes y Series en español, inglés y japonés.

## Descripción

Este script permite crear automáticamente carpetas y subcarpetas a partir de una lista de nombres, facilitando la organización de tus archivos multimedia. Los nombres de las carpetas se sanitizan y formatean para evitar caracteres inválidos y mantener una estructura ordenada.

## Requisitos

- Python 3.x

## Instalación

1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener Python instalado en tu sistema.

## Uso

1. Crea un archivo de texto (por ejemplo, `input.txt`) con un nombre de carpeta por línea.
2. Modifica las variables en `folder_generator.py` si deseas cambiar el nombre del archivo de entrada, la carpeta de salida o el nombre de la subcarpeta.
3. Ejecuta el script:

   ```bash
   python3 folder_generator.py
   ```

4. Se crearán las carpetas y subcarpetas en la ruta especificada.

## Ejemplo de entrada (`input.txt`):

```
Naruto: Shippuden
One Piece
Attack on Titan; Final Season
```

## Salida esperada

```
Output/
├── Naruto - Shippuden/
│   └── Season 1/
├── One Piece/
│   └── Season 1/
└── Attack on Titan - Final Season/
    └── Season 1/
```

## Licencia

MIT
