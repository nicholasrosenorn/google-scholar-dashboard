FROM python:3.10-slim-bullseye

RUN python -m pip install fastapi "uvicorn[standard]" jinja2 pandas plotly bs4 html5lib  

COPY . .

EXPOSE 8000

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]