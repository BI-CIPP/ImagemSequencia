@echo off
REM ==================================================
REM Rodar Python invisível (pythonw.exe) via Power Automate
REM ==================================================

SET PYTHONW_EXE="C:\Users\francisco.horizonte\AppData\Local\Programs\Python\Python312\python.exe"
SET SCRIPT="https://github.com/BI-CIPP/ImagemSequencia.git"

REM Executa o Python invisível
%PYTHONW_EXE% %SCRIPT% %INPUT_DIR% %OUTPUT_DIR%