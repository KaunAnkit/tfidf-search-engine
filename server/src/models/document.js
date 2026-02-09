
const mongoose = require("mongoose")




const docSchema = new mongoose.Schema(
    {
        url : {
            type : String,
            required : true,
            unique : true

        },
        title : {
            type : String,
            required : true
        },
        text :{
            type : String,
            required : true
        }

    },{
        timestamps : true
    }
    
)

const document = mongoose.model('Document', docSchema)

module.exports = document