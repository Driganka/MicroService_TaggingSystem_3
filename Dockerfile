FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./api/v1 /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH /Users/driganka/.pyenv/shims/python

#CMD ["sh","run.sh"]
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
