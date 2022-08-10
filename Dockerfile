FROM python:3.9.6-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /home
EXPOSE 8000
WORKDIR /home
COPY . .
RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8000", "mo_tech_pokemon.wsgi"]
