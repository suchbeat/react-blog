FROM node:latest
COPY . /ui
WORKDIR /ui
RUN npm install
RUN npm rebuild node-sass
CMD ["npm", "start"]