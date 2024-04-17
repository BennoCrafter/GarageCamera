echo "Installing python requirements"
pip install -r requirements.txt

echo "Installing fswebcam module"
sudo apt-get install fswebcam

echo "Creating executable"
chmod +x run.sh

echo "Running setup.py script"
python setup/setup.py

exit 0