var db = require('../db-config');
var Query = db.model('Query', {
    query: { type: String, required: true },
});
module.exports = Query;