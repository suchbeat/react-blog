FROM node:latest
COPY package.json /ui/package.json
WORKDIR /ui
RUN npm install
RUN npm rebuild node-sass
COPY . /ui
CMD ["npm", "start"]