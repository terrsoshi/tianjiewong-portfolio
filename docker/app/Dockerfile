FROM node:22-alpine

WORKDIR /app

COPY ./app/ .

RUN npm install

ARG PORT
EXPOSE ${PORT}

CMD ["npm", "start"]