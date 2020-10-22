@echo off
REM @auther mchsiaoj
REM set environment variable on windows: https://stackoverflow.com/questions/44597662/conda-command-is-not-recognized-on-windows-10?rq=1
REM https://dev.to/hygull/setting-anaconda-path-on-windows-2dmn
REM or key "PATH" in Anaconda Prompt

REM when PATH has has space: set PATH=... --> set "PATH=..."
REM when FUNC_NAME has space: python %FUNC_NAME%.py --> python "%FUNC_NAME%.py"
REM has cmd window: python.py xxx --> pythonw xxx.py (https://www.luoow.com/dc_tw/200782448)

REM C:\Users\b9903\Anaconda3;
REM C:\Users\b9903\Anaconda3\Library\mingw-w64\bin;
REM C:\Users\b9903\Anaconda3\Library\usr\bin;
REM C:\Users\b9903\Anaconda3\Library\bin;
REM C:\Users\b9903\Anaconda3\Scripts;
REM C:\Users\b9903\Anaconda3\bin;C:\Users\b9903\Anaconda3\condabin;

REM for user to modify:
set "PY_HOME=C:\Users\b9903\Anaconda3"
set "FUNC_NAME=imageAlignmentApp"

set "PATH=%PY_HOME%;%PY_HOME%\Library\mingw-w64\bin;%PY_HOME%\Library\usr\bin;%PY_HOME%\Library\bin;%PY_HOME%\Scripts;%PY_HOME%\bin;%PY_HOME%\condabin;%PATH%"

@echo on
pythonw "%FUNC_NAME%.py"

REM exit
REM pause()








