FROM python:3
ADD app.py /
COPY requirements.txt /tmp
WORKDIR /tmp
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r ./requirements.txt
CMD [ "python", "./app.py" ]
