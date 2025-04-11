FROM {{ ENROLLMENTREPORTS_BASE_IMAGE }}
ENV TZ=Etc/UTC
ENV DEBIAN_FRONTEND=noninteractive
RUN mkdir -p /etc/ansible/roles/enrollmentreports /etc/ansible/group_vars
RUN apt-get update && \
    apt install -y ansible git default-mysql-client rsync

RUN git -C /etc/ansible/roles clone {{ ENROLLMENTREPORTS_REPOSITORY }} enrollmentreports
RUN git -C /etc/ansible/roles/enrollmentreports checkout {{ ENROLLMENTREPORTS_REVISION }}
COPY enrollment-report.yml .
