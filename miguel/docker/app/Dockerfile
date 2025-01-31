FROM python:3.12-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

FROM base AS jupyter
RUN pip install jupyter==1.1.1
EXPOSE 8080
CMD jupyter notebook --ip='*' --port=8080 --no-browser --allow-root

FROM base
CMD [ "python", "main.py" ]
