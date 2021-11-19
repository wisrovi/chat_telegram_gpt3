FROM tensorflow/tensorflow
WORKDIR /app

RUN pip3 install openai
RUN pip3 install python-telegram-bot

COPY src .

CMD ["python3", "./service.py"]

