# Use the official Python image from the Docker Hub
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set the environment variable for Flask
ENV FLASK_APP=core/server.py

# Expose the port your app runs on
EXPOSE 5000

# Command to run the app
CMD ["gunicorn", "-c", "gunicorn_config.py", "core.server:app"]


#In my computer I am using the python 3.12 but I am adding here 3.10
