@echo off
chcp 65001 >nul
title Сборка ECG_decryptor.exe

echo Очистка старых сборок...
if exist "%~dp0release" rmdir /s /q "%~dp0release"

echo.
echo Сборка проекта...
python -m PyInstaller "%~dp0main.py" ^
  --onefile ^
  --name ECG_decryptor ^
  --add-data "%~dp0template.docx;." ^
  --distpath "%~dp0release" ^
  --workpath "%~dp0temporary" ^
  --specpath "%~dp0temporary"

echo.
echo ============================================
echo Сборка завершена!
echo Файл лежит здесь: %~dp0release\ECG_decryptor.exe
echo ============================================

echo.
echo Удаление временной папки...
if exist "%~dp0temporary" rmdir /s /q "%~dp0temporary"

pause
