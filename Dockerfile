FROM python:3.11.7-bookworm
WORKDIR .
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]