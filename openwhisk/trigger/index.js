function action(params) {
    const axios = require('axios');

    time = Math.floor(Date.now() / 1000)

    var config = {
         method: 'get',
         url: 'https://showcase.api.linx.twenty57.net/UnixTime/fromunix?timestamp=' + time,
        headers: { }
    };

    return new Promise(function(resolve, reject){
        axios(config)
        .then(function (response) {
            resolve ({ msg: response.data});
        })
        .catch(function (error) {
            reject(error)
        });
    })

    
}

exports.main = action