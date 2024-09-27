
---

# Confirmacion Metrologica

This project aims to implement and manage a system for **metrological confirmation**, supported by **machine learning** and data processing. The project follows best development practices, using Docker for containerization and a development environment managed with `venv` and python.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Scripts](#scripts)
  - [GitFlow Process](#gitflow-process)
- [Configuration](#configuration)
- [Best Practices](#best-practices)
- [License](#license)

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
   .\scripts.bat Create-Venv
   ```

3. **Set up the `.env` file**:
   Copy the `.env.example` file to `.env`  and `config.example.yaml` to `config.yaml` then modify the settings as needed:
   ```bash
   cp .env.example .env
   cp configs/config.example.yaml configs/config.yaml
   ```

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

## Configuration

The main configuration file is located in the `configs/` folder. You can modify the settings in `config.yaml` as needed. Copy `config.example.yaml` to `config.yaml` for the initial setup.

If necessary, you can override settings using the `.env` file.

## Best Practices

- **Version Control**: Follow GitFlow to manage branches and releases effectively.
- **Documentation**: Keep your code well-documented, using meaningful comments and clear variable names.
- **Unit Testing**: Always run unit tests before making any significant commits.
- **Code Style**: Adhere to PEP 8 standards for Python code. you can see it here! [PEP 8](https://pep8.org/)
- **Dependency Management**: Update `requirements.txt` whenever you add or remove dependencies.
- **Docker**: Use Docker to ensure consistent environments across different machines and team members.

## License

---