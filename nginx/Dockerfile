# use the Nginx image
FROM nginx

# Removing defult nginx.conf
RUN rm /etc/nginx/conf.d/defult.conf

# Replace with our own nginx.conf
COPY nginx.conf /ect/nginx/conf.d/
