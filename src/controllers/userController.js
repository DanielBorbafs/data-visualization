import Funcionario from "../models/userModel.js";

// Exemplo de rota para criar um novo funcionário
export const createFuncionario = async (req, res) => {
    try {
        const { nome, departamento, salario, idade, data_contrato } = req.body;

        const novoFuncionario = await Funcionario.create({
            nome,
            departamento,
            salario,
            idade,
            data_contrato
        });

        return res.status(201).json(novoFuncionario);
    } catch (err) {
        console.error('Erro ao criar funcionário:', err);
        return res.status(500).json({ error: 'Erro interno do servidor' });
    }
};
