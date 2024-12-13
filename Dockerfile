FROM python 

RUN pip install streamlit 

WORKDIR /VAR

COPY . .

EXPOSE 8501

CMD ["streamlit","run'"","etl.py"]