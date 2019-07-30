FROM node:12.7-alpine

COPY . /trade
WORKDIR /trade

RUN yarn install

EXPOSE 3000

ENTRYPOINT ["yarn"]
CMD ["start"]
