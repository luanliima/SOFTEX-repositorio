adminRouter.get('/users/:name', (req, res) => {
    res.send('Faalaaa ' + req.params.name + '!')
  })
