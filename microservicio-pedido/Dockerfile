# Use an official Python runtime as the base image
FROM python:3.9-slim-buster

# Set the working directory to /app
# Copy the rest of the application code to the container
COPY ./configuracion /app
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install required packages
RUN pip install --no-cache-dir -r requirements.txt



# Expose port 8000 for the Django development server
EXPOSE 8001


# Run the command to start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
