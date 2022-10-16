FROM node:16-alpine as build-step

WORKDIR /usr/src/app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./
COPY ./src ./src
COPY ./public ./public

RUN npm install

RUN npm run build

COPY . .

# Build step #2: build an nginx container

FROM nginx:stable-alpine

COPY --from=build-step /usr/src/app/build /usr/share/nginx/html

#RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/
