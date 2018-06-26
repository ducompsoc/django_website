FROM nginx
COPY conf/compsoc.conf /etc/nginx/conf.d/default.conf
COPY root/localhost-chain.cert.pem /etc/nginx/cert.pem
COPY root/localhost.key.pem /etc/nginx/key.pem
VOLUME /static
VOLUME /media
