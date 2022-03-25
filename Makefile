lint:
	pipenv run flake8 --count --max-complexity=10 --max-line-length=127 --show-source --statistics

format:
	pipenv run black .