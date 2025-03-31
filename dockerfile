# Usando a imagem oficial do Node.js
FROM node:16

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copiar o arquivo package.json e package-lock.json (ou yarn.lock) para o container
COPY package*.json ./

# Instalar as dependências do projeto
RUN npm install

# Copiar todo o conteúdo do projeto para o diretório de trabalho dentro do container
COPY . .

# Expor a porta em que o servidor irá rodar (exemplo: 3000)
EXPOSE 3000

# Comando para rodar o servidor
CMD ["npm", "start"]
