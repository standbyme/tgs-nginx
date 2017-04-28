FROM nginx
COPY pan.conf /etc/nginx/conf.d/pan.conf
COPY ghost.conf /etc/nginx/conf.d/ghost.conf
EXPOSE 80
