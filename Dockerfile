FROM python:3.7.5

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /backend/requirements.txt

WORKDIR /backend

# upgrade pip
RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools && pip install -r requirements.txt
COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
