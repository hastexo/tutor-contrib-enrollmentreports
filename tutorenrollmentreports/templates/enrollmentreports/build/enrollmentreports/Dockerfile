FROM ubuntu:20.04
RUN mkdir -p /etc/ansible/roles/enrollmentreports /etc/ansible/group_vars
RUN apt-get update && \
    apt install -y ansible git default-mysql-client rsync

RUN git -C /etc/ansible/roles clone https://github.com/hastexo/ansible-role-enrollmentreports.git enrollmentreports
COPY enrollment-report.yml .
