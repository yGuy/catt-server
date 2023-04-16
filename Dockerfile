FROM python:3-slim-bullseye

RUN pip install catt

ENV CHROME_CAST_SERVER chromecast

EXPOSE 5000

RUN useradd --create-home --user-group --shell /bin/bash appuser

WORKDIR /app
COPY ./app /app
# Change the ownership of the /app directory to the appuser
RUN chown -R appuser:appuser /app

USER appuser

RUN pip install --no-cache-dir -r requirements.txt

CMD catt -d $CHROME_CAST_SERVER set_default && python server.py