@echo off
echo Iniciando Redis com Docker...
docker-compose up -d

echo Ativando ambiente virtual...
call venv\Scripts\activate

echo Iniciando o servidor Flask...
start "FLASK" cmd /k "python run.py"

timeout /t 2

echo Iniciando Celery Worker (modo solo para evitar erro do Word)...
start "CELERY" cmd /k "celery -A celery_worker.celery worker --pool=solo --loglevel=info"

echo Todos os serviços foram iniciados.
