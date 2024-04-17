echo "Installing python requirements"
pip install -r assets/requirements.txt

echo "\nInstalling fswebcam module"
sudo apt-get install fswebcam

echo "\nCreating executable"
chmod +x run.sh

echo "\nRunning setup.py script"
python setup/setup.py

exit 0