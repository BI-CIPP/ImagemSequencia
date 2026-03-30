@echo off REM

chcp 65001
 ================================================== 
REM Rodar Python invisível (pythonw.exe) via Power Automate REM 
================================================== 
SET PYTHONW_EXE="C:\Users\francisco.horizonte\AppData\Local\Programs\Python\Python312\python.exe" 

SET SCRIPT="C:\OneDrive\CIPP\GEOPP - GEOPP\01-ENGENHARIA OPERACIONAL\13- ACOMP MENSAL OPERAÇÃO\Relatório Power Bi\Repositório\ImagemSequencia\ImagemSequencia.py" 

REM Executa o Python invisível 
%PYTHONW_EXE% %SCRIPT% %INPUT_DIR% %OUTPUT_DIR% 
