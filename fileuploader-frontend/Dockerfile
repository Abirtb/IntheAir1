# Use an official Node runtime as a parent image
FROM node:22

# Set the working directory in the container
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json ./
COPY package-lock.json ./
RUN npm install

# Bundle app source inside Docker image
COPY . .

# Build production app
RUN npm run build

# Install a simple HTTP server to serve static content
CMD ["npm", "start"]

# Make port 3000 available to the world outside this container
EXPOSE 3000
