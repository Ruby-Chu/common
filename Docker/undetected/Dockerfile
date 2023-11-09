FROM ultrafunk/undetected-chromedriver
RUN apt-get update -y
# time
RUN apt-get install -y --no-install-recommends tzdata
RUN TZ=Asia/Taipei \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone \
    && dpkg-reconfigure -f noninteractive tzdata
COPY ./ORACLE/oracle-instantclient-basic_21.10.0.0.0-2_amd64.deb /
RUN apt-get install libaio1 -y
RUN dpkg -i  oracle-instantclient-basic_21.10.0.0.0-2_amd64.deb
COPY ./requirements.txt /
RUN pip install -r requirements.txt
WORKDIR /app