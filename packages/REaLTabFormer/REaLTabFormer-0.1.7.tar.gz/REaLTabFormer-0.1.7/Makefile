install:
	pip install .

clean:
	rm -rf build dist docs/build pip-wheel-metadata .mypy_cache .pytest_cache
	find . -regex ".*/__pycache__" -exec rm -rf {} +
	find . -regex ".*\.egg-info" -exec rm -rf {} +
	pre-commit clean || true

install-pip-setuptools:
	pip install -U "pip>=21.2" "setuptools>=38.0" wheel

lint:
	pre-commit run -a --hook-stage manual $(hook)

test:
	pytest tests --cov-config pyproject.toml --numprocesses 4 --dist loadfile

pip-compile:
	pip-compile -q -o -

secret-scan:
	trufflehog --max_depth 1 --exclude_paths trufflehog-ignore.txt .

package: clean install
	python setup.py sdist bdist_wheel

test-pypi-upload: package
	twine upload --repository testpypi dist/*

pypi-upload: package
	twine upload dist/*

install-test-requirements:
	pip install -r test_requirements.txt

install-pre-commit: install-test-requirements
	pre-commit install --install-hooks

uninstall-pre-commit:
	pre-commit uninstall

print-python-env:
	bash devtools/print_env.sh

sign-off:
	echo "git interpret-trailers --if-exists doNothing \c" >> .git/hooks/commit-msg
	echo '--trailer "Signed-off-by: $$(git config user.name) <$$(git config user.email)>" \c' >> .git/hooks/commit-msg
	echo '--in-place "$$1"' >> .git/hooks/commit-msg
	chmod +x .git/hooks/commit-msg
