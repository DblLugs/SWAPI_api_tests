Пример написания API автотестов с использованием python+pytest+requests+allure.  
API для тестов взято с ресурса https://swapi.dev/.  

python3 -m venv venv  
source venv/bin/activate  
pip install -r requirements.txt  
pytest -v --alluredir allure_report  
allure serve allure_report  


May the Force be with you. =)
