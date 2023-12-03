# Build: Builds the Docker images without using cache
build:
	docker compose -f docker-compose-dev.yml build --no-cache

# Migrate: Executes the migration script
migrate:
	./scripts/migrate.sh docker-compose-dev.yml

# Start: Starts the Docker containers
start:
	docker compose -f docker-compose-dev.yml up

# Startd: Starts the Docker containers in the background. Execute the exec commands after running this command
startd:
	docker compose -f docker-compose-dev.yml up -d

# Stop: Stops the Docker containers
stop:
	docker compose -f docker-compose-dev.yml down

# Test: Runs tests using pytest. Execute this command after running the startd command
test:
	docker compose -f docker-compose-dev.yml exec app poetry run pytest

# Lint: Lints the code using flake8. Execute this command after running the startd command
lint:
	docker compose -f docker-compose-dev.yml exec app poetry run flake8

# Format: Formats the code using black. Execute this command after running the startd command
format:
	docker compose -f docker-compose-dev.yml exec app poetry run black .

# Typecheck: Checks the types using mypy. Execute this command after running the startd command
typecheck:
	docker compose -f docker-compose-dev.yml exec app poetry run mypy .
