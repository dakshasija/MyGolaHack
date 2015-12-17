var express = require('express')
var router = express.Router();

//Serve Static assets like CSS and JS
router.use(express.static(__dirname + '/../assets'));


//Serve index.html at endpoint : '/'
router.get('/', function (req,res) {
    res.sendfile('layouts/index.html')
});
module.exports = router;
