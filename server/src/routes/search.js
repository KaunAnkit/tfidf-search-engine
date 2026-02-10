const path = require("path");
require("dotenv").config({ path: path.resolve(__dirname, "../.env") });


const express = require("express");
const axios = require("axios");

const router = express.Router();

const PYTHON_SEARCH_URL = process.env.PYTHON_SEARCH_URL 


router.get("/", async (req, res) => {
  try {
    const query = req.query.q;

    if (!query) {
      return res.status(400).json({
        error: "Query parameter 'q' is required"
      });
    }

    const response = await axios.get(PYTHON_SEARCH_URL, {
      params: { q: query },
      timeout: 5000
    });

    res.status(200).json({
      query,
      results: response.data
    });

  } catch (err) {
    console.error("Search service error:", err.message);

    res.status(500).json({
      error: "Search service unavailable"
    });
  }
});

module.exports = router;
