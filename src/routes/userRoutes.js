import express from "express";
import { createFuncionario } from "../controllers/userController.js";

const router = express.Router();

// Rota para criar um novo funcionário
router.post("/funcionarios", createFuncionario);

export default router;
