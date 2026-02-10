const express = require("express");
const mongoose = require("mongoose");

const router = express.Router();
const Document = require("../models/document");



router.post("/", async(req,res) => {

    try{
        const {url,title,text} = req.body


        if(!url||!title||!text){
            return res.status(400).json({
                error : "Url title ya text mai se kuch missing hai"
            })

        }

        const newDoc = new Document({url,title,text})
        const saveDoc = await newDoc.save();
         
        res.status(201).json({
            message : "Document saved",
            data : saveDoc
        })
    }
    catch(err){
        res.status(500).json({
            error : "Document save karte wakt kuch dikkat aagyi hai"
        })
    }


})

router.get("/", async(req,res) => {

    try{
        
        const loadDoc = await Document.find().select("url title")

        res.status(200).json({
            count : loadDoc.length,
            data : loadDoc
        })
    }
    catch(err){
        res.status(500).json({
            error : "Data fetch ni hora hai"
        })
    }


})


router.get("/:id", async(req,res) => {

    try{
        const id = req.params.id;

        const singleDoc = await Document.findById(id)

        if(!singleDoc){
            return res.status(404).json({
                error : "Specefic Doc nahi mila : ID might be wrong"
            })

        }

        res.status(200).json(singleDoc)
    }
    catch(err){
        res.status(400).json({
            error : "Invalid Id"
        })
    }


})

router.delete("/:id", async (req, res) => {
  try {
    const { id } = req.params;

    
    if (!mongoose.Types.ObjectId.isValid(id)) {
      return res.status(400).json({
        error: "Invalid document id",
      });
    }

    
    const deletedDoc = await Document.findByIdAndDelete(id);

    
    if (!deletedDoc) {
      return res.status(404).json({
        error: "Document not found",
      });
    }

    
    res.status(200).json({
      message: "Document deleted successfully",
      data: deletedDoc,
    });
    } 
    catch (err) {
        res.status(500).json({
        error: "Failed to delete document",
        });
    }
});


router.post("/bulk", async (req, res) => {
  try {
    const { documents } = req.body;

    if (!documents || !Array.isArray(documents)) {
      return res.status(400).json({
        error: "documents must be an array"
      });
    }

    const totalReceived = documents.length;

    const result = await Document.insertMany(documents, {
      ordered: false
    });

    res.status(201).json({
      received: totalReceived,
      inserted: result.length,
      skipped: totalReceived - result.length,
      message: "Bulk ingestion completed"
    });

  } catch (err) {
    
    if (err.insertedDocs) {
      const insertedCount = err.insertedDocs.length;
      const totalReceived = req.body.documents.length;

      return res.status(201).json({
        received: totalReceived,
        inserted: insertedCount,
        skipped: totalReceived - insertedCount,
        message: "Bulk ingestion completed with some skips (duplicates)"
      });
    }

    res.status(500).json({
      error: "Bulk insert failed completely"
    });
  }
});


module.exports = router
