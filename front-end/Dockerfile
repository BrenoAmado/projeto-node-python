FROM node:lts
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN chmod a+x /app/node_modules/.bin/react-scripts
RUN npm run build
EXPOSE 8082
CMD [ "sh", "-c", "export BROWSER=none && npm start" ]