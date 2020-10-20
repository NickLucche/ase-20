FROM node
LABEL maintainer D4nt3 nicolo.lucchesi@gmail.com
RUN git clone -q https://github.com/docker-in-practice/todo.git
WORKDIR todo
RUN npm install
RUN chmod -R 777 /todo
# The EXPOSE instruction does not actually publish the port. 
# It functions as a type of documentation between the person 
# who builds the image and the person who runs the container, 
# about which ports are intended to be published.
#  To actually publish the port when running the container, use the -p flag on docker run
EXPOSE 8000
CMD ["npm", "start"]