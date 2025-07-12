@echo off
echo Parando containers do Docker (Redis)...
docker-compose down

echo Finalizando processos do Flask e Celery...
taskkill /FI "WINDOWTITLE eq FLASK" /T /F > nul
taskkill /FI "WINDOWTITLE eq CELERY" /T /F > nul

echo Todos os processos foram encerrados.
