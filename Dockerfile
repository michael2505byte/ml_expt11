# Use official lightweight Python image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy all files to the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Render's dynamic port
EXPOSE 5000

# Use gunicorn for production instead of running Flask directly
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
