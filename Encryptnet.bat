@ECHO OFF
TITLE Encryptnet
CLS

:MAIN
python encryptnet.py

REM // Restarting.
echo.
TIMEOUT /T 1 /NOBREAK >NUL
goto MAIN