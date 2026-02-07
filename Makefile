dev-build:
	docker build --target builder -t practice:dev .
lint:
	docker run --rm practice:dev pylint main.py
test:
	docker run --rm practice:dev pytest tests/
prod-build:
  @echo "Building prod image with tag $(TAG)"
	docker build -t practice:$(TAG) .
	docker tag practice:$(TAG) practice:latest
prod-run:
	docker run --rm -e APP_MODE=prod practice:prod
dev-run:	
	docker run --rm -e APP_MODE=dev practice:prod
push:
	@echo "Pushing prod image with tag $(TAG)"
	docker push practice:$(TAG)
	docker push practice:latest
clean:
	docker system prune -af
