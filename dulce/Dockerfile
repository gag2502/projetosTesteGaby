FROM node:8.6-alpine
 
RUN mkdir -p /home/gabriela/EPS/dulce
WORKDIR /home/gabriela/EPS/dulce
 
COPY package.json ./
RUN npm install
 
COPY . .
 
EXPOSE 3000
CMD ["npm", "start"]
