import sys
from cx_Freeze import setup, Executable

# Nome do arquivo Python que você quer converter
script = "main 01.py"

# Definir o base para GUI no Windows
base = None
if sys.platform == "win32":
    base = "Win32GUI"

# Crie o Executable
executables = [Executable(script, target_name="calculadora.exe", base=base)]

# Configurações adicionais
buildOptions = {
    "packages": ["tkinter", "customtkinter"],
    "include_files": []
}

setup(
    name="Calculadora Basica",
    version="1.0",
    description="Uma calculadora simples",
    options={"build_exe": buildOptions},
    executables=executables
)

