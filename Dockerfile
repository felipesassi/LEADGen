FROM python:3.7

COPY ./dashboard /dashboard 
COPY ./scripts /scripts 
COPY ./data /data 
COPY ./dashboard.py /dashboard.py 

RUN pip install -r requirements.txt

EXPOSE 5000

CMD streamlit run dashboard.py