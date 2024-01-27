FROM oven/bun:1

# make the 'app' folder the current working directory
WORKDIR /app

# copy both 'package.json' and 'bun.lockb' files
COPY package.json bun.lockb ./

# install project dependencies
RUN bun install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .

# build app for production with minification
RUN bun run build

# run app
CMD [ "bun", "dev" ]