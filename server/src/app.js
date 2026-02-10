const express = require("express");
const cors = require("cors");

const documentRoute = require("./routes/document");
const searchRoute = require("./routes/search");

const app = express();

app.use(cors());              
app.use(express.json());

app.use("/documents", documentRoute);
app.use("/search", searchRoute);

app.get("/health", (req, res) => {
  res.json({ health: "ok" });
});

module.exports = app;
