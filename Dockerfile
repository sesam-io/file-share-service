FROM python:3-alpine
MAINTAINER Geir Ove Grønmo "geir.gronmo@sesam.io"
COPY ./service /service
WORKDIR /service
RUN pip install -r requirements.txt
EXPOSE 5000/tcp
ENTRYPOINT ["python"]
CMD ["file-share-service.py"]
