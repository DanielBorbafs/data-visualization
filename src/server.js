import express from 'express'
import sequelize from './config/database.js'

const app = express();
const port = 3000;
// rota para teste
sequelize.sync().then(() => {
    console.log('Banco de dados conectado com sucesso')
    app.listen(port, () => {
        console.log(`🚀 Servidor rodando na porta ${port}`);
    });
}).catch((err) => {
    console.error('Erro ao conectar no banco', err)
})
