FROM node:20.10.0-slim AS builder

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY . /app

RUN npm ci \
    && npm run build

FROM nginx:1.25-bookworm

COPY --from=builder /app/dist /usr/share/nginx/html

COPY .nginx/nginx.conf /etc/nginx/conf.d/default.con
