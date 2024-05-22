FROM node:22-alpine

WORKDIR /app

COPY . .

RUN npm install

ARG SERVER_PORT
EXPOSE ${SERVER_PORT}

CMD ["npm", "run", "dev"]