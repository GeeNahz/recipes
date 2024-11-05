# FROM node:18-alpine AS builder
FROM node:20.18-alpine

WORKDIR /usr/src/app/frontend

COPY package*.json ./

RUN npm cache clean --force && npm install

COPY . .


EXPOSE 3000

CMD ["pnpm", "dev"]
