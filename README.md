
---

# Confirmacion Metrologica

This project aims to implement and manage a system for **metrological confirmation**, supported by **machine learning** and data processing. The project follows best development practices, using Docker for containerization and a development environment managed with `venv` and python.

## Table of Contents
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Scripts](#scripts)
  - [GitFlow Process](#gitflow-process)
  - [Start Coding](#start-coding)
- [Configuration](#configuration)
- [Best Practices](#best-practices)
- [License](#license)

## Estructura del Proyecto

La estructura del proyecto está organizada de la siguiente manera:

```
ConfirmacionMetrologica/
┣ data/                         # Carpeta para almacenar los datos relacionados con el proyecto.
┃ ┗ raw/                        # Datos sin procesar o datos brutos se almacenan aquí.
┃   ┗ DatosBajoCosto.csv        # Archivo CSV que contiene los datos iniciales sin procesar para el análisis.
┣ docker/                       # Archivos relacionados con la configuración de Docker.
┃ ┣ docker-compose.yml          # Archivo de configuración para definir y ejecutar servicios Docker en múltiples contenedores.
┃ ┗ Dockerfile                  # Definición de la imagen Docker para el entorno de desarrollo/producción.
┣ docs/                         # Carpeta destinada a la documentación del proyecto.
┣ model/                        # Contiene los archivos principales del modelo de machine learning y su configuración.
┃ ┣ configs/                    # Archivos de configuración utilizados para personalizar el modelo.
┃ ┃ ┣ config.example.yaml       # Ejemplo de archivo de configuración para guiar la creación de `config.yaml`.
┃ ┃ ┣ config.py                 # Script Python que maneja la carga y gestión de la configuración.
┃ ┃ ┗ config.yaml               # Archivo YAML que contiene configuraciones ajustables para el modelo.
┃ ┣ controller/                 # Controladores, incluyendo notebooks y scripts, para manejar el flujo de trabajo.
┃ ┃ ┣ notebooks/                # Notebooks de Jupyter utilizados para el procesamiento de datos y análisis.
┃ ┃ ┃ ┗ dataPreprocessing.ipynb # Notebook con el pipeline de preprocesamiento de datos.
┃ ┃ ┗ scripts/                  # Scripts para automatizar tareas de control y procesamiento.
┃ ┣ core/                       # Núcleo del proyecto que contiene las funciones y lógica del modelo.
┃ ┃ ┣ data/                     # Archivos relacionados con la manipulación y preprocesamiento de datos.
┃ ┃ ┃ ┗ DataPreprocess.py       # Script para preprocesar los datos antes del entrenamiento.
┃ ┃ ┗ model/                    # Aquí irían los archivos del modelo de machine learning, como su arquitectura.
┃ ┗ resources/                  # Recursos necesarios para el funcionamiento del proyecto.
┃   ┣ logs/                     # Carpeta para almacenar archivos de registro (logs).
┃   ┗ trainedModels/            # Carpeta destinada a almacenar los modelos entrenados.
┣ tests/                        # Pruebas unitarias y de integración para validar la funcionalidad del código.
┃ ┣ test_data_loader.py         # Prueba unitaria para la carga de datos.
┃ ┗ test_model.py               # Prueba unitaria para verificar la funcionalidad del modelo.
┣ utils/                        # Funciones auxiliares y utilidades comunes que se utilizan en todo el proyecto.
┃ ┗ DataLoader.py               # Script que gestiona la carga y preparación de datos para el modelo.
┣ .env                          # Archivo de entorno que contiene variables sensibles, como claves API y configuraciones.
┣ .env.example                  # Ejemplo del archivo `.env` para configuración.
┣ .gitignore                    # Lista de archivos y carpetas que Git debe ignorar.
┣ README.md                     # Documento que describe el proyecto, su uso, instalación y estructura.
┣ requirements.txt              # Lista de dependencias y bibliotecas necesarias para el proyecto.
┗ scripts.bat                   # Script por lotes para automatizar tareas, como instalación de dependencias y ejecución del proyecto.
```

## Requirements

Before starting, make sure you have the following installed:

- [Python 3.11+](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/)
- [Git](https://git-scm.com/)
- [VSCode](https://code.visualstudio.com/) (optional, but recommended)

## Installation

Follow these steps to set up the project on your local machine.

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/ConfirmacionMetrologica.git
   cd ConfirmacionMetrologica
   ```

2. **Set up the virtual environment and install dependencies**:
   ```bash
   .\scripts.bat startPoryect
   ```

3. **Set up the `.env` file**:
   automatically created by the scripts.bat file you can modify it if you need to.

## Usage

### Scripts

Use the `scripts.bat` file to automate tasks:

- **help to show the available commands**:
  ```bash
  .\scripts.bat help
  ```

### GitFlow Process

We follow **GitFlow** for version control and branch management. Here's a typical workflow for adding a new feature:

1. **Start a new feature**:
    ```bash
     
    git flow feature start mi-nueva-caracteristica # Crear y cambiar a la rama de característica
    git add .    # Después de realizar cambios
    git commit -m "Añadido mejora específica en funcionalidad X"
    
    git flow feature finish mi-nueva-caracteristica # Finalizar y fusionar en develop
    git push origin develop # Empuja los cambios a origin
    ```

2. **Start a new release**:
    ```bash
    git flow release start 0.1.0 # Crear y cambiar a la rama de lanzamiento
    git flow release finish 0.1.0 # Finalizar y fusionar en develop y master
    git push origin develop master --tags # Empuja los cambios a origin
    ```

3. **Start a hotfix**:
    ```bash
    git flow hotfix start hotfix-0.1.1 # Crear y cambiar a la rama de hotfix
    git flow hotfix finish hotfix-0.1.1 # Finalizar y fusionar en develop y master
    git push origin develop master --tags # Empuja los cambios a origin
    ```

4. **request a pull request**:
    ```bash
    # but have in mind that git flow automatically creates a pull request when you finish a feature, release or hotfix
    git request-pull master develop
    ```

## Start Coding

1.  **Use the controllers notebooks in the `model/controllers/notbooks/` folder**:
    follow the pipeline pattern and execute the functions in the order they are presented. 

2.  **Use the scripts  `model/controllers/scripts/` folder**:
    execute in the terminal the scripts available in the folder to automate the process.

    ```bash
    python script.py
    ```

## Configuration

there are two configuration file is located in the `configs/` and  `ConfirmacionMetrologica/` folder. You can modify the settings in `config.yaml` and `.env` as needed.

## Best Practices

- **Version Control**: Follow GitFlow to manage branches and releases effectively.
- **Documentation**: Keep your code well-documented, using meaningful comments and clear variable names.
- **Unit Testing**: Always run unit tests before making any significant commits.
- **Code Style**: Adhere to PEP 8 standards for Python code. you can see it here! [PEP 8](https://pep8.org/)
- **Dependency Management**: Update `requirements.txt` whenever you add or remove dependencies.
- **Docker**: Use Docker to ensure consistent environments across different machines and team members.

## License

---