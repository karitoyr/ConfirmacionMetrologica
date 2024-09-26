# Variables
PYTHON=python
PIP=pip
DOCKER_COMPOSE=docker-compose
VENV=venv

# Help
.PHONY: help
help:  ## Display this help message
	@echo "Available commands:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# Virtual environment setup
.PHONY: venv
venv:  ## Create the virtual environment
	@$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created. Run 'source venv/bin/activate' to activate."

.PHONY: install
install:  ## Install project dependencies
	@$(PIP) install -r requirements.txt
	@echo "Dependencies installed."

# Clean up generated files
.PHONY: clean
clean:  ## Remove temporary files and old models
	@rm -rf Resources/models/*.pkl
	@rm -rf Resources/encoders/*.pkl
	@echo "Temporary files and old models removed."

# Docker
.PHONY: docker-build
docker-build:  ## Build the Docker image
	@$(DOCKER_COMPOSE) build
	@echo "Docker image built."

.PHONY: docker-up
docker-up:  ## Start Docker containers
	@$(DOCKER_COMPOSE) up -d
	@echo "Docker containers started."

.PHONY: docker-down
docker-down:  ## Stop and remove Docker containers
	@$(DOCKER_COMPOSE) down
	@echo "Docker containers stopped and removed."
