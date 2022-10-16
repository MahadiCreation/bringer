FROM node:16-alpine as build-step

WORKDIR /usr/src/app

ENV PATH /app/node_modules/.bin:$PATH

COPY package*.json ./
COPY ./src ./src
COPY ./public ./public

RUN npm install

RUN npm run build

COPY . .

COPY --from=build-step /usr/src/app/build /usr/share/nginx/html



