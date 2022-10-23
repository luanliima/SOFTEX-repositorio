const sequelize = require('sequelize');
const database = require('/db');

const produto = database.define('produto',{
    id: {
         type:sequelize.INTEGER,
         autoincrement: true,
         allowNull: false,
         primarykey: true
    }
    nome: {
        type: sequelize.STRING,
        allowNull: false
    },
    preco: {
        type: sequelize.DOUBLE
    },
    descricao: sequelize.STRING
    })
