FROM nginx
{% for container in containers %}
COPY {{container.name}}.conf /etc/nginx/conf.d/{{container.name}}.conf
{% endfor %}
EXPOSE 80
