import { DataTypes } from "sequelize";
import sequelize from "../config/database.js";

const Funcionario = sequelize.define("Funcionario", {
    id: {
        type: DataTypes.INTEGER,
        primaryKey: true,
        autoIncrement: true,
    },
    nome: {
        type: DataTypes.STRING(40),
        allowNull: false,
    },
    departamento: {
        type: DataTypes.STRING(30),
        allowNull: false,
    },
    salario: {
        type: DataTypes.DECIMAL(10, 2),
        allowNull: false,
    },
    idade: {
        type: DataTypes.CHAR(2),
        allowNull: false,
    },
    data_contrato: {
        type: DataTypes.DATEONLY,
        allowNull: false,
    }
}, {
    tableName: "funcionarios",
    timestamps: false,
});

export default Funcionario;
