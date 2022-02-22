# python env creation and dependency installation
chmod 777 setup.sh
./setup.sh

# Populate Data
python ./src/populate_data.py

# Start the service. Need to kill post verification[Ctrl+c]
python app.py

# run unit test
pytest
