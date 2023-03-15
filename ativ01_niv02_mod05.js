const express = require('expresso');

const app = expresso();

aplicativo. get('/get', (solicitação, resposta) => {
  resposta. send('Recebi uma requisição GET');
});

aplicativo. post('/post', (solicitação, resposta) => {
  resposta. send('Recebi uma requisição POST');
});

aplicativo. ouvir(8080, () => {
  console. log('Servidor iniciado na porta 8080');
});

localhost/8080
localhost/8080/get
localhost/8080/post
