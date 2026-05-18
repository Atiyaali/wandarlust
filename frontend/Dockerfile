FROM node:20-alpine as builder

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]

# RUN npm run build

# FROM nginx:alpine

# COPY --from=builder /app /usr/share/nginx/html

# EXPOSE 80

# EXPOSE 443  

# CMD ["nginx", "-g", "daemon off;"]

