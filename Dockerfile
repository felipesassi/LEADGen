FROM python:3.7

COPY ./dashboard /dashboard 
COPY ./scripts /scripts 
COPY ./data /data 
COPY ./dashboard.py /dashboard.py 

RUN pip install numpy
RUN pip install -U scikit-learn
RUN pip install pandas
RUN pip install streamlit
RUN pip install -U matplotlib
RUN pip install yellowbrick
RUN pip install plotly==4.8.1

EXPOSE 5000

CMD streamlit run dashboard.py