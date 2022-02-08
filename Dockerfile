FROM python:3.8-slim

LABEL maintainer="NachoCarher <e.nachoch64@go.ugr.es>" version="1.0" 

RUN groupadd -g 1000 -r myhams && \
    useradd -u 1000 -m -r -g myhams myhams

USER myhams

WORKDIR /app/test/

ENV PATH=$PATH:/home/myhams/.local/bin

COPY pyproject.toml poetry.lock tasks.py /app/

RUN pip install poetry && \
    poetry config virtualenvs.create false && \
    poetry install 

ENTRYPOINT ["inv", "test"]

