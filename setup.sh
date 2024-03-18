#!/usr/bin/env bash

if command -v python3 &>/dev/null; then
  HOST_PYTHON=python3
elif command -v python &>/dev/null; then
  HOST_PYTHON=python
else
  echo "Python required in order to use this application. Please install Python 3!"
  exit 1
fi

PYTHON_VERSION=$($HOST_PYTHON -c "import sys; print(sys.version_info.major)")

if [ "$PYTHON_VERSION" -lt 3 ]; then
  echo "Your Python install is too old, please install Python 3!"
  exit 1
fi

if command -v pip3 &>/dev/null; then
  HOST_PIP=pip3
elif command -v pip &>/dev/null; then
  HOST_PIP=pip
else
  echo "Your python install is missing pip, make sure the required development packages are installed!"
  exit 1
fi

if [ ! -d venv ]; then
  if ! command -v virtualenv &>/dev/null; then
    $HOST_PIP install virtualenv
  fi
  virtualenv venv --python=python3.12
fi

source venv/bin/activate

if [ ! -f requirements.txt ]; then
    touch requirements.txt
fi

pip install --upgrade pip
pip install -r requirements.txt

echo "Setup complete, your application is now ready to use!"
