# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 build-essential && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install --default-timeout=200 --no-cache-dir -i https://pypi.org/simple -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Run Streamlit app (adjust the path if needed)
CMD ["streamlit", "run", "Home.py", "--server.port=8501", "--server.address=0.0.0.0"]