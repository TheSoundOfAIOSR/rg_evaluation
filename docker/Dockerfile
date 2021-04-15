FROM python:3.8.0-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "run_survey.py" ]
