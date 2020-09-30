git clone https://github.com/di-unipi-socc/microFreshener
cd microFreshener/server
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt 
python manage.py migrate
python manage.py runserver >logs.txt 2>errors.txt &
cd ../client
npm install @angular/cli
npm install @angular-devkit/build-angular
npm run-script ng serve
