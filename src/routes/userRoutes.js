import express from 'express';
import {
  createFuncionario,
  searchFuncionarios,
} from '../controllers/userController.js';

const router = express.Router();

// Rota para criar um novo funcionário
router.post('/funcionarios', createFuncionario);

//Rota para trazer todos os funcionários
router.get('/funcionarios', searchFuncionarios);

export default router;
