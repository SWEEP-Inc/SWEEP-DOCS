# Python runtine as a parent image
FROM jdeskins/aws-python

WORKDIR /tmp

# when this Dockerfile is built to an image, task.py will be available inside the container at location /tmp
COPY hello_world.py /tmp

# This is run when the container launches
CMD python /tmp/hello_world.py
