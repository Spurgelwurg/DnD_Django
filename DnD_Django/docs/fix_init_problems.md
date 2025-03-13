// Delete this file after fixing the init problems


pip uninstall django -y
pip cache purge
pip install django==5.1.4


//Verify the installation
python -m django --version

# Exit the current virtual environment first
deactivate

# Delete and recreate the virtual environment
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate

# Install Django and any other required packages
pip install django==5.1.4


python3 manage.py makemigrations
python3 manage.py migrate


// Not sure if necessary
python3 manage.py createsuperuser