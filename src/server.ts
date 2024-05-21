import cors from "cors";
import dotenv from "dotenv";
import { MongoClient, Db } from "mongodb";
import express, { Express, Request, Response } from "express";

// Load and use environment variables from the .env file
dotenv.config();
const { SERVER_PORT = 8000, DB_URI = '', DB_NAME = "" } = process.env;

// Connect to MongoDB Database
const mongoClient: MongoClient = new MongoClient(DB_URI);
let db: Db;
const connectDB = async (): Promise<void> => {
  console.log(`Connecting to the ${DB_NAME} database...`);
  try {
    await mongoClient.connect();
    db = mongoClient.db(DB_NAME);
    console.log(`Successfully connected to the ${DB_NAME} database!`);
  } catch (err) {
    console.error(`Connection to the ${DB_NAME} database failed!`, err);
  }
};
connectDB();

const app: Express = express();
app.use(cors());

app.get("/", (req: Request, res: Response) => {
  res.json("Hello World!");
});

app.listen(SERVER_PORT, () => {
  console.log(`Server is listening on port ${SERVER_PORT}.`);
});
