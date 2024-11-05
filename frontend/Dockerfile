# FROM node:18-alpine AS builder
FROM node:20.18-alpine

WORKDIR /usr/src/app/frontend

RUN npm i -g pnpm

COPY package*.json ./

RUN pnpm install
# RUN npm cache clean --force && npm install --force

COPY . .


EXPOSE 3000

CMD ["pnpm", "dev"]
