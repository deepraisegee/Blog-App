FROM nginx:latest

# Copy the custom Nginx configuration file into the container
COPY default.conf /etc/nginx/conf.d/default.conf

# Remove the default Nginx configuration file if it exists
RUN rm -f /etc/nginx/conf.d/default.conf.default

# Expose the default HTTP port
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]