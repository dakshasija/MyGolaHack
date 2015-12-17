var mongoose = require('mongoose')
mongoose.connect('mongodb://foodslack.cloudapp.net:27017/mygola', function () {
    console.log('Mongodb connected')
});
module.exports = mongoose;