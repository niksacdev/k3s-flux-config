# syntax=docker/dockerfile:1
FROM --platform=$BUILDPLATFORM ubuntu AS build
ARG TARGETPLATFORM
ARG BUILDPLATFORM
RUN echo "I am running on $BUILDPLATFORM, building for $TARGETPLATFORM" > /log

FROM ubuntu
COPY --from=build /log /log

# Install python and pip
# Run commands that require root authority
RUN ln -s /usr/bin/dpkg-split /usr/sbin/dpkg-split
RUN ln -s /usr/bin/dpkg-deb /usr/sbin/dpkg-deb
RUN ln -s /bin/rm /usr/sbin/rm
RUN ln -s /bin/tar /usr/sbin/tar
RUN apt-get update && apt-get -y upgrade
RUN apt-get install -y python3 python3-pip
#RUN apt-get install -y cmake git wget nano xz-utils bzip2


# Get the right utilities
#########################################
# start from home directory
RUN cd ~

#########################################
# Run commands that require root authority
RUN apt-get update
#RUN apt-get install -y cmake git wget nano xz-utils bzip2
RUN pip install smbus smbus2
#RUN apt-get install -y python3-smbus

# install Robot Arm_Device package
RUN pip install Arm_Lib

COPY . /app
#RUN make /app
CMD ["/app/test.py"]
ENTRYPOINT ["python3"]