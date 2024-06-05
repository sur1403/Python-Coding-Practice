# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    qt5-qmake \
    qtbase5-dev \
    qtbase5-dev-tools \
    libqt5gui5 \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY requirements.txt .
# Install any needed packages specified in requirements.txt
#RUN pip install --no-cache-dir -r requirements.txt

# RUN pip3 install PyQt5
# RUN pip3 install pillow
# RUN pip3 install matplotlib


RUN apt-get update && \
    apt-get install -y libgl1 && \
    rm -rf /var/lib/apt/lists/*

# RUN apt-get update && apt-get install -y \
#     python3-pyqt5 \
#     python3-pyqt5.qtwebengine

RUN pip3 install PyQt5
RUN pip3 install pillow
RUN pip3 install matplotlib

RUN apt-get update && apt-get install -y \
    python3-pyqt5 \
    python3-pyqt5.qtwebengine


# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["python3", "StarterApp_window.py"]

