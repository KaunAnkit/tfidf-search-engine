
const express = require("express")


const app = express()

module.exports = app


app.get("/health", (req,res) => {
    
    res.json({
        "health" : "ok"
    })

    
})