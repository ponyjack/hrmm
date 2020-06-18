# start from an official Python image
FROM python:3.7

RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client

# arbitrary location choice: you can change the directory
# RUN mkdir -p /var/djangoapp
WORKDIR /djangoapp

# install our dependencies
COPY ./requirements.txt /djangoapp
RUN pip install -r requirements.txt

RUN pip install --pre djangorestframework-filters
# copy our project code

# run Django management commands at start

# expose the port 8000
EXPOSE 8000

# define the default command to run when starting the container
# CMD ["gunicorn",  "--bind", ":8000", "hrm.wsgi:application", "--reload"]