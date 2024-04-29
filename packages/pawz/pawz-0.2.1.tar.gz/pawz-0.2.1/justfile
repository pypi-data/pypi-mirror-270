# Justfile

# load environment variables
set dotenv-load

# aliases
alias fmt:=format

# list justfile recipes
default:
    just --list

# setup
setup:
    @pip install uv
    @uv pip install -r dev-requirements.txt

# build
build:
    just clean
    @python -m build src/pawz-core
    @python -m build

# format
format:
    @cargo fmt --manifest-path src/pawz-core/Cargo.toml
    @ruff format .

# install
install:
    @maturin dev -m src/pawz-core/Cargo.toml
    @pip install --upgrade -e '.[all]'

# uninstall
uninstall:
    @pip uninstall pawz pawz-core -y

# release-test
release-test:
    just build
    @twine upload --repository testpypi src/pawz-core/dist/* -u __token__ -p ${PYPI_TEST_TOKEN}
    @twine upload --repository testpypi dist/* -u __token__ -p ${PYPI_TEST_TOKEN}

# release
release:
    just build
    @twine upload src/pawz-core/dist/* -u __token__ -p ${PYPI_TOKEN}
    @twine upload dist/* -u __token__ -p ${PYPI_TOKEN}

# clean
clean:
    @rm -r src/pawz-core/target || True
    @rm -rf src/pawz-core/dist || True
    @rm -rf dist || True
