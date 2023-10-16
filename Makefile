install:
	pip install --upgrade pip && \
	pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
	black *.py

lint:
	# disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	# deploy goes here

all: install lint test format deploy

generate_and_push:
	# Create the markdown file
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add SQL log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi

extract:
	python main.py extract

transform_load:
	python main.py transform_load

query:
	python main.py general_query "SELECT a.state, AVG(a.median_household_income) AS average_median_household_income, AVG(a.share_unemployed_seasonal) AS average_share_unemployed_seasonal, a.share_population_in_metro_areas, b.gini_index FROM default.hate_crimes1DB AS a JOIN default.hate_crimes2DB AS b ON a.state = b.state GROUP BY a.state, a.share_population_in_metro_areas, b.gini_index ORDER BY b.gini_index LIMIT 5;"
