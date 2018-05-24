'use strict';
 
const express = require('express');
const bodyParser = require('body-parser');
const config = require('./config');
const app = new express();

app.get('/', (req, res) => {
    res.send('Hello World!');
});
 
// register JSON parser middlewear
app.use(bodyParser.json());
 
require('./personRoutes')(app);
require('./versionRoutes')(app, config);


app.listen(3000, () => {
    /* eslint-disable */
    console.log('Server is up!');
});