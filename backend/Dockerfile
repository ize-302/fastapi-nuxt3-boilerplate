FROM python:3.9-alpine

# make the 'app' folder the current working directory
WORKDIR /app

# install/upgrade pip setuptool wheel
RUN python -m pip install --upgrade pip setuptools wheel

# copy requirements.txt
COPY requirements.txt .

# install dependencies from requirements.txt
RUN pip install -r requirements.txt

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# run app
CMD ["uvicorn", "src.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
