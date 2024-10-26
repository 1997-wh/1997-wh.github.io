# Use the official Python image.
FROM python:3.9-slim

# Set the working directory.
WORKDIR /app

# Copy the requirements file.
COPY requirements.txt .

# Install the dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code.
COPY . .

# Expose the port the app runs on.
EXPOSE 5000

# Define the command to run your app.
CMD ["gunicorn", "-b", "0.0.0.0:5000", "chatbot:app"]
