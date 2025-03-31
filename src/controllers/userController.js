import Funcionario from '../models/userModel.js';

// isso aqui cria o o template do funcionário.
export const createFuncionario = async (req, res) => {
  try {
    const { nome, departamento, salario, idade, data_contrato } = req.body;

    const novoFuncionario = await Funcionario.create({
      nome,
      departamento,
      salario,
      idade,
      data_contrato,
    });

    return res.status(201).json({
      message: 'Funcionário criado com sucesso',
      funcionario: novoFuncionario,
    });
  } catch (err) {
    console.error('Erro ao criar funcionário:', err);
    return res.status(500).json({ error: 'Erro interno do servidor' });
  }
};

export const searchFuncionarios = async (req, res) => {
  try {
    // Buscando todos os funcionários no banco de dados
    const funcionarios = await Funcionario.findAll();

    // Se não houver funcionários, retornamos uma resposta vazia
    if (funcionarios.length === 0) {
      return res
        .status(404)
        .json({ message: 'Nenhum funcionário encontrado.' });
    }

    // Retorna os funcionários encontrados como JSON
    return res.json(funcionarios);
  } catch (error) {
    // Em caso de erro, retorna status 500 e a mensagem de erro
    console.error(error); // Logando o erro no servidor para debugar
    res.status(500).json({ error: 'Erro ao buscar funcionários' });
  }
};
