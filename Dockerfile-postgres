FROM postgres:16

# Install Python and Daff (https://github.com/paulfitz/daff)
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-venv

# Create a virtual environment and install daff in it
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install daff==1.3.46

# # Copy project files
COPY . /app
WORKDIR /app
ENV PATH=$PATH:/app/bin

RUN apt-get update && apt-get install -y locales && rm -rf /var/lib/apt/lists/* && \
    localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
