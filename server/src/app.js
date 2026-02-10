
const express = require("express")
const documentRoute = require("./routes/document")


const app = express()

app.use(express.json())
app.use("/documents", documentRoute)

app.get("/health", (req,res) => {
    res.json({
        "health" : "ok"
    })
})

module.exports = app