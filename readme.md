# change access for setup script
chmod 777 setup.sh

# python env creation and dependency installation
./setup.sh

# Activate venv
source ./userenv/bin/activate

# Populate Data
python ./src/populate_data.py

# Start the service. Need to kill post verification[Ctrl+c]
python app.py

# run unit test
pytest
