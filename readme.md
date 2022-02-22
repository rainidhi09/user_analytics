# installation <change the path for venv inside setup.sh>
./setup.sh

# Populate Data
python ./src/populate_data.py

# Start the service
python app.py

# run unit test
pytest