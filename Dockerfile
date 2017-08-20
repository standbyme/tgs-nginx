FROM nginx
COPY container.conf /etc/nginx/conf.d/container.conf
EXPOSE 80
