FROM lsiobase/kasmvnc:ubuntujammy-version-23bc0eb7

ENV FM_HOME=app
ENV START_DOCKER=true
ENV LC_ALL=pt_BR.UTF-8

# Atualize a lista de pacotes
RUN apt-get update

# Instale o Python e o Tkinter
RUN apt-get install -y python3 python3-tk python3-pip

# Verifique a instalação
RUN python3 --version
RUN python3 -c "import tkinter"
RUN curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py &&\
    python3 get-pip.py

# definindo o python padrao
RUN rm -f /usr/bin/python &&\
    rm -f /usr/bin/python3 &&\
    rm -f /usr/local/bin/python &&\
    rm -f /usr/local/bin/python3 &&\
    rm -f /usr/local/bin/pip &&\
    rm -f /usr/local/bin/pip3 &&\
    ln -sf /usr/bin/python3.10 /usr/bin/python &&\
    ln -sf /usr/bin/python3.10 /usr/bin/python3 &&\
    ln -sf /usr/bin/python3.10 /usr/local/bin/python &&\
    ln -sf /usr/bin/python3.10 /usr/local/bin/python3 &&\
    ln -sf /usr/bin/pip3 /usr/local/bin/pip3 &&\
    ln -sf /usr/bin/pip3 /usr/local/bin/pip

# Indo para a pasta padrao
WORKDIR /config/app
# Limpar o cache do apt-get e outros arquivos temporários
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 3000
EXPOSE 3001

WORKDIR /config/app
Copy . .
RUN  pip install -r /config/app/requirements.txt
RUN chmod +x /config/app/teste

CMD ["sh", "-c", "sleep infinity"]