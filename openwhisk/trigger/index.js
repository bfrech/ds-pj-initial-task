function action(params) {
    const axios = require('axios');

    now = new Date()
   
    var config = {
         method: 'get',
         url: 'https://api.coindesk.com/v1/bpi/currentprice.json',
        headers: { }
    };

    return new Promise(function(resolve, reject){
        axios(config)
        .then(function (response) {
            result = response.data['bpi']['EUR']['rate']
            resolve ({ current_rate_EUR: result, timestamp: now});
        })
        .catch(function (error) {
            reject(error)
        });
    })

    
}

exports.main = action