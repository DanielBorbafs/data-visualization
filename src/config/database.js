import { Sequelize } from 'sequelize';
import dotenv from 'dotenv';

// Carregar as variáveis de ambiente
dotenv.config();


// Conexão com o banco de dados MySQL usando Sequelize
const sequelize = new Sequelize(process.env.DB_NAME, process.env.DB_USER, process.env.DB_PASS, {
    host: process.env.DB_HOST,
    dialect: 'mysql',
});

sequelize.authenticate()
    .then(() => {
        console.log('Conexão com o banco de dados realizada com sucesso');
    })
    .catch(err => {
        console.error('Erro ao conectar no banco de dados:', err);
    });


export default sequelize