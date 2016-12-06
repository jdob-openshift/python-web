FROM python:latest

EXPOSE 8080

ENV HOME=/opt/app-root
ENV CONTENT=${HOME}/content

RUN mkdir -p ${CONTENT}

RUN useradd -u 1001 -r -g 0 -d ${HOME} -s /sbin/nologin \
    -c "Default python-web user" pythonweb

RUN chown -R 1001:0 ${HOME} && \
    find ${HOME} -type d -exec chmod g+ws {} \;

COPY web.py ${HOME}
COPY index.html ${CONTENT}

WORKDIR ${HOME}
USER 1001

CMD /bin/bash -c 'python3 -u ${HOME}/web.py'
