FROM python:3.9

ENV PYTHONUNBUFFERED="1"
ENV PIP_DISABLE_PIP_VERSION_CHECK="1"

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    ffmpeg \
    libsm6 \
    libxext6 \
    ghostscript \
    && apt-get clean

WORKDIR /app

COPY . /app

EXPOSE 8081

RUN pip install -r requirements.txt

CMD gunicorn -b 0.0.0.0:8081 -w 1 -k gthread main:app --timeout 1000



