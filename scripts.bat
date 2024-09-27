@echo off
SET TASK=%1

IF "%TASK%"=="Create-Venv" GOTO CreateVenv
IF "%TASK%"=="Install" GOTO InstallDependencies
IF "%TASK%"=="Clean" GOTO Clean
IF "%TASK%"=="Docker-Build" GOTO DockerBuild
IF "%TASK%"=="Docker-Up" GOTO DockerUp
IF "%TASK%"=="Docker-Down" GOTO DockerDown
GOTO Help

:CreateVenv
    echo Creating virtual environment...
    py -m venv .venv
    echo Virtual environment created.
    GOTO InstallDependencies

:InstallDependencies
    echo Activating virtual environment and installing dependencies...
    call .venv\Scripts\activate
    python.exe -m pip install --upgrade pip
    pip install -r requirements.txt
    echo Dependencies installed.
    GOTO End

:Clean
    echo Cleaning up old files and Python cache...
    REM Limpiar carpetas __pycache__ en todo el proyecto
    for /d /r %%d in (__pycache__) do (
        echo Removing %%d
        rmdir /S /Q "%%d"
    )
    REM Eliminar el archivo logs
    if exist resources\logs\*.log (
        del /S /Q resources\logs\*.log
        echo Logs cleaned.
    )

    REM Eliminar archivos de notebooks y temporales en ejecución
    if exist execution\notebooks\*.ipynb (
        del /S /Q execution\notebooks\*.ipynb
        echo Jupyter notebooks cleaned.
    )

    echo Clean-up process completed.
    GOTO End

:DockerBuild
    echo Building Docker image...
    docker-compose build
    echo Docker image built.
    GOTO End

:DockerUp
    echo Starting Docker containers...
    docker-compose up -d
    echo Docker containers started.
    GOTO End

:DockerDown
    echo Stopping and removing Docker containers...
    docker-compose down
    echo Docker containers stopped and removed.
    GOTO End

:Help
    echo Available commands:
    echo   Create-Venv    - Create virtual environment
    echo   Install        - Install dependencies
    echo   Clean          - Remove temporary files
    echo   Docker-Build   - Build Docker image
    echo   Docker-Up      - Start Docker containers
    echo   Docker-Down    - Stop Docker containers
    echo   help           - Show this help message
    GOTO End

:End
exit /b 0

# comand to run the script 
# .\scripts.bat Help

