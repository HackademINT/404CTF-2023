FROM bitnami/node:18.15.0

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

# If you are building your code for production
RUN npm ci --omit=dev

# Or if still in dev
# RUN npm install

# Bundle app source
COPY . .

EXPOSE 3000

USER 1001

CMD [ "node", "index.js" ]