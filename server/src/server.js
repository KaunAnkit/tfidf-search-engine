
const path = require("path");
require("dotenv").config({ path: path.resolve(__dirname, "../.env") });

const app = require("./app");
const connectDB = require("./config/db");


const PORT = 5500


const startServer = async () => {
    try {
        
        await connectDB();
        
        app.listen(PORT, () => {
            console.log(`Database synced & server running on http://localhost:${PORT}`);
        });
    } catch (error) {
        console.error(" Failed server:", error);
        process.exit(1);
    }
};


startServer();

