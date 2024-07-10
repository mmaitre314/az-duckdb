FROM mcr.microsoft.com/cbl-mariner/distroless/python:3.9-nonroot-cm2.0

ENV PATH=/home/nonroot/.local/bin:$PATH
WORKDIR /home/nonroot
COPY . .

RUN ["/usr/bin/python3", "install.py"]

EXPOSE 8888

CMD ["jupyter", "notebook", "--ip='0.0.0.0'", "--no-browser" ]
