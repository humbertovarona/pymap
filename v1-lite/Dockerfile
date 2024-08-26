FROM python:3.12.5-slim-bookworm

RUN apt-get update && apt-get install -y \
    curl \
    unzip \
    libmariadb-dev \
    libpq-dev \
    libsqlite3-dev \
    gdal-bin \
    libgdal-dev \
    libhdf5-dev \
    libnetcdf-dev \
    libxml2-dev \
    libxslt1-dev \
    libopenjp2-7 \
    libzbar0 \
    libfreetype6-dev \
    libreoffice-calc \
    && rm -rf /var/lib/apt/lists/*

RUN useradd -m sciuser

WORKDIR /home/sciuser/WORKDIR

RUN python -m venv /home/sciuser/venv \
    && chown -R sciuser:sciuser /home/sciuser/venv

USER sciuser

COPY requirements.txt .

RUN /bin/bash -c "source /home/sciuser/venv/bin/activate && pip install --no-cache-dir -r requirements.txt"

RUN mkdir -p /home/sciuser/OUTPUT && chmod -R 777 /home/sciuser/OUTPUT

VOLUME /home/sciuser/OUTPUT

ENV DATA_PATH=/home/sciuser/data
ENV PATH="/home/sciuser/venv/bin:$DATA_PATH:$PATH"

CMD ["/bin/bash", "-c", "source /home/sciuser/.bashrc && exec \"$@\"", "--"]

