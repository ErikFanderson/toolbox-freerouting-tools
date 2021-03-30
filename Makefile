# Author: Erik Anderson 
# Date Created: 03/30/2021

default: test

# Lints toolbox-freerouting-tools directory recursively
lint:
	pylint toolbox-freerouting-tools tests

# Formats toolbox-freerouting-tools directory recursively
format:
	yapf -i -r toolbox-freerouting-tools tests

# Type checks toolbox-freerouting-tools directory recursively
type:
	mypy toolbox-freerouting-tools tests

# Runs all tests in tests directory 
test:
	pytest -v tests

# Export anaconda environment
export:
	conda env export --from-history | grep -v "prefix" > environment.yml
