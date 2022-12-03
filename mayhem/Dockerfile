# Build Stage
FROM fuzzers/atheris:2.0.7-python3.9

ADD ./mayhem/fuzz_loader.py /fuzz_loader.py
RUN pip install cle

CMD ["/fuzz_loader.py"]
