var express = require('express');
var bodyParser = require('body-parser');
var app = express();
app.use(bodyParser.json());
var Query = require('./models/query');
var result = "";
//var spawn = require("child_process").spawn;
var https = require("https");

app.use(require('./controllers/static'));

function search(city) {
 city = encodeURIComponent(city);
    url = "https://api.foursquare.com/v2/venues/explore?client_id=MDREIXWEKU15QLSRJAH12CAWB4S4MTJEGDM3JYZPIALRJ5WJ&client_secret=PHQLBL3QSZMATWV30XN0H54V35N0U02TH53GB0T54AEFS1TA&v=20130815&near=" + city + "&section=topPicks&limit=10";

// get is a simple wrapper for request()
// which sets the http method to GET
    var request = https.get(url, function (response) {
        // data is streamed in chunks from the server
        // so we have to handle the "data" event
        var buffer = "",
            data;

        response.on("data", function (chunk) {
            buffer += chunk;
        });

        response.on("end", function (err) {
            data = JSON.parse(buffer);


            var displayString =  data.response.geocode.displayString;
            var locationGranularity =  data.response.headerLocationGranularity;
            var type =  data.response.groups[0].type;
            var name =  data.response.groups[0].items[0].venue.name;
            var location =  data.response.groups[0].items[0].venue.location.address;
            var category =  data.response.groups[0].items[0].venue.categories[0].name;
            var checkins =  data.response.groups[0].items[0].venue.stats.checkinsCount;
            var rating =  data.response.groups[0].items[0].venue.rating;
            var tips =  data.response.groups[0].items[0].tips[0].text;
            var tipsname =  data.response.groups[0].items[0].tips[0].user.firstName;
            console.log(displayString);
            console.log(locationGranularity);
            console.log(type);
            console.log(name);
            console.log(location);
            console.log(category);
            console.log(checkins);
            console.log(rating);
            console.log(tips);
            console.log(tipsname);

           // postres(displayString, locationGranularity, type ,name, location, category, checkins, rating, tips, tipsname);
        });
    });
}

/*
function callback(city){
    var process = spawn('python',["search.py", city]);
    process.stdout.on('data', function (data){
        data = data.toString('utf8');
        console.log(data);

    });
};

*/

app.get('/search', function (req,res, next) {
   Query.find(function (err,query) {
       if(err){ return next(err) }
       var city = query[query.length-1].query;
       search(city);
   });
});


app.post('/search', function(req, res, next) {
    var query = new Query({
        query: req.body.query
    })
    query.save(function (err,query) {
        if(err){ return next(err) }
        res.sendStatus(201).json(query)
    })
});
function postres(displayString, locationGranularity, type ,name, location, category, checkins, rating, tips, tipsname){
app.post('/results', function (req, res, next) {
    var result = new Result({
        displayString: displayString,

    })
})
};



var server = app.listen(3000, function () {
    console.log('Server', process.pid, 'listening on', 3000)
});


