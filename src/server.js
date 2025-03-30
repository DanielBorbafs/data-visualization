import express from 'express'
import sequelize from './config/database.js'
import userRoutes from './routes/userRoutes.js'

const app = express();
app.use(express.json());

const port = 3000;


// usando rota de funcionario
app.use('/api', userRoutes)
// rota para teste
sequelize.sync().then(() => {
    console.log('Banco de dados conectado com sucesso')
    app.listen(port, () => {
        console.log(`🚀 Servidor rodando na porta ${port}`);
    });
}).catch((err) => {
    console.error('Erro ao conectar no banco', err)
})


app.get('/', (req, res) => {
    res.send('Api conectada')
})