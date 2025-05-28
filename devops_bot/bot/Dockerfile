FROM python:3.9-slim
WORKDIR /app
COPY . .
EXPOSE 5000
# Используйте зеркало pip (для Китая/России)
RUN  pip install python-telegram-bot==13.15 python-dotenv==1.0.1 paramiko

CMD ["python", "bot.py"]
