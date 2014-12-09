FROM python:2

RUN apt-get update
RUN apt-get -y install gfortran libopenblas-dev liblapack-dev libsamplerate-dev

WORKDIR /app/

ADD requirements_first.txt /app/requirements_first.txt
RUN pip install -r requirements_first.txt
ADD requirements_second.txt /app/requirements_second.txt
RUN pip install -r requirements_second.txt

ADD analyze_db.py /app/analyze_db.py

CMD ["python", "analyze_db.py"]
