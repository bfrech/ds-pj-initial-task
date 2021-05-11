
function md5hash(params) {
    const md5 = require('md5')
    var course = params.course || 'Distributed Systems Project';
    hash = md5(course + "Berit")
    return { string: course + " Berit" , md5hash:  hash};
}

exports.main = md5hash