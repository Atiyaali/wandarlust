FROM node:20-alpine

WORKDIR /app

# COPY ./backend/package*.json ./
COPY package*.json ./
RUN npm install -g pm2 && npm install

# COPY ./backend/ .
COPY . .
EXPOSE 8000

CMD ["pm2-runtime", "server.js", "--name", "wanderlust-backend"]