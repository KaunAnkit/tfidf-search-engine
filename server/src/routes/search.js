const express = require("express");
const axios = require("axios");

const router = express.Router();


const PYTHON_SEARCH_URL = process.env.PYTHON_SEARCH_URL;

router.get("/", async (req, res) => {
  const query = req.query.q;

  if (!query) {
    return res.status(400).json({
      error: "Query parameter 'q' is required"
    });
  }

  if (!PYTHON_SEARCH_URL) {
    console.error("PYTHON_SEARCH_URL not set");
    return res.status(500).json({
      error: "Search service not configured"
    });
  }

  try {
    let response;

   
    try {
      response = await axios.get(PYTHON_SEARCH_URL, {
        params: { q: query },
        timeout: 20000 // 20s 
      });
    } catch (err) {
      console.warn("First attempt failed, retrying...", err.message);

      
      response = await axios.get(PYTHON_SEARCH_URL, {
        params: { q: query },
        timeout: 20000
      });
    }

    
    return res.status(200).json({
      query,
      results: response.data
    });

  } catch (err) {
    console.error("Search service error:", err.message);

    return res.status(502).json({
      error: "Search service unavailable"
    });
  }
});

module.exports = router;
