FROM python:3.8-slim

RUN apt-get update && apt-get install -y libgl1-mesa-glx

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
