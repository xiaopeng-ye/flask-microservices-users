FROM python:3.6

# workdir
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# add dependencies
ADD ./requirements.txt /usr/src/app/requirements.txt

# install dependencies
RUN pip install -r requirements.txt

# add source code
ADD . /usr/src/app

# run server
CMD python manage.py runserver -h 0.0.0.0