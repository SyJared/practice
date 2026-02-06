dev-build:
	docker build --target builder -t practice:dev .
lint:
	docker run --rm practice:dev pylint main.py
test:
	docker run --rm practice:dev pytest tests/
prod-build:
	docker build -t practice:prod .
prod-run:
	docker run --rm -e APP_MODE=prod practice:prod
dev-run:
	docker run --rm -e APP_MODE=dev practice:prod
clean:
	docker system prune -af
