# Conversor DOCX para PDF Assíncrono com Flask, Celery e Redis

Este projeto é uma aplicação web simples para converter arquivos DOCX em PDF de forma assíncrona, utilizando Flask como framework web, Celery para gerenciamento de tarefas em background e Redis como broker e backend de resultados. Possui interface para upload, monitoramento de status e download do arquivo convertido.

---

## Tecnologias utilizadas

- Python 3.x  
- Flask  
- Celery  
- Redis (broker e backend)  
- Docker (para facilitar o uso do Redis)  
- Bootstrap 5 (frontend)  
- Werkzeug (para upload seguro)  

---

## Funcionalidades

- Upload de arquivos `.docx` pela interface web  
- Conversão assíncrona para PDF (não bloqueia o servidor)  
- Monitoramento do status da tarefa com atualização automática  
- Download do PDF gerado após conclusão  
- Feedback visual moderno com Bootstrap  

---

## Pré-requisitos

- Python 3.8+  
- Redis rodando localmente (pode ser via Docker)  
- pip (gerenciador de pacotes Python)  

---

## Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/dudamark/conversor-assincrono-python.git
cd conversor-assincrono-python
```

### 2. Crie e ative o ambiente virtual

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure e inicie o Redis (via Docker)

Se não tiver o Redis instalado, use Docker:

```bash
docker run -d -p 6379:6379 redis
```

Ou, se usar `docker-compose.yml`:

```bash
docker-compose up -d
```

### 5. Configure as variáveis de ambiente (opcional)

As configurações padrão apontam para Redis em `localhost:6379`. Se precisar mudar, edite o arquivo `config.py`.

### 6. Inicie o worker Celery

```bash
celery -A celery_worker.celery worker --pool=solo --loglevel=info
```

### 7. Rode o Flask

```bash
python run.py
```

### 8. Acesse no navegador

Abra http://127.0.0.1:5000 e envie arquivos `.docx`.

---

## Estrutura do projeto

```
.
├── app
│   ├── __init__.py
│   ├── tasks.py
│   ├── utils.py
│   ├── routes.py
│   ├── templates
│   │   ├── index.html
│   │   └── status.html
│   ├── uploads
│   └── converted
├── celery_worker.py
├── config.py
├── requirements.txt
├── run.py
└── docker-compose.yml (opcional para Redis)
```

---

## Arquivos importantes

- `app/tasks.py`: configuração do Celery e task de conversão  
- `app/routes.py`: rotas Flask para upload, status e download  
- `app/utils.py`: função utilitária para converter DOCX em PDF  
- `celery_worker.py`: entrypoint para rodar o worker Celery  
- `config.py`: configurações do projeto, incluindo paths e URLs do Redis  

---

## Possíveis melhorias futuras

- Autenticação de usuários  
- Suporte a mais formatos de arquivo  
- Monitoramento em tempo real via WebSocket (Flask-SocketIO)  
- Interface com histórico de conversões  
- Suporte para filas de prioridades  
- Deploy em nuvem (Heroku, AWS, etc)  

---

## Licença

MIT License - veja o arquivo LICENSE para detalhes.
