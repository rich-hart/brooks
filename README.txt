git clone https://github.com/rich-hart/brooks.git
cd brooks
virtualenv -p $(which python3.5) venv
source venv/bin/activate
pip install -U pip
pip install -r requirements.txt
./manage.py collectstatic
./manage.py runserver
