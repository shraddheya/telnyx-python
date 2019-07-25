init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run tox -p auto

ci:
	pipenv run pytest --cov=telnyx

coveralls:
	pipenv run coveralls

fmt:
	pipenv run tox -e fmt

fmtcheck:
	pipenv run tox -e fmt -- --check --verbose

lint:
	pipenv run tox -e lint

####

pipfile_to_requirements:
	jq -r '.default | to_entries[] | select(.key != "telnyx") | .key + .value.version + ([.value.hashes | " \\\n  --hash=" + .[]] | join("")) + "\n"' Pipfile.lock > requirements.txt
	jq -r '.develop | to_entries[] | select(.key != "black")  | .key + .value.version + ([.value.hashes | " \\\n  --hash=" + .[]] | join("")) + "\n"' Pipfile.lock > requirements-dev.txt
	echo "-r requirements.txt" >> requirements-dev.txt
