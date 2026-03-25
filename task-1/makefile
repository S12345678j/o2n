run:
	python run.py

migrate:
	flask db migrate -m "migration"

upgrade:
	flask db upgrade

test:
	PYTHONPATH=. pytest

build:
	docker build -t student-api:1.0.0 .

run-docker:
	docker run -d -p 5000:5000 \
	-e DATABASE_URL=sqlite:///students.db \
	--name student-api student-api:1.0.0

stop-docker:
	docker stop student-api || true
	docker rm student-api || true


