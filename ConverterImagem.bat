@echo off
REM ==================================================
REM Rodar Python invisível (pythonw.exe) via Power Automate
REM ==================================================

SET PYTHONW_EXE="C:\Users\francisco.horizonte\AppData\Local\Programs\Python\Python312\python.exe"
SET SCRIPT="C:\OneDrive\OneDrive - CIPP\SEQUENCIA POWER BI\ConverterPDF-IMG.py"

REM Pastas de entrada e saída
SET INPUT_DIR="C:\OneDrive\CIPP\GEOPP-GEOPP\03-CCO\SEQUENCIA-POWER-BI"
SET OUTPUT_DIR="C:\OneDrive\CIPP\GEOPP-GEOPP\03-CCO\SEQUENCIA-POWER-BI\imagem"

REM Executa o Python invisível
%PYTHONW_EXE% %SCRIPT% %INPUT_DIR% %OUTPUT_DIR%