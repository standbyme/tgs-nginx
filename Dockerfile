FROM nginx
COPY pan.conf /etc/nginx/conf.d/pan.conf
EXPOSE 80
