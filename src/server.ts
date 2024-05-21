import cors from "cors";
import dotenv from "dotenv";
import { cleanEnv, str } from "envalid";
import { MongoClient, Db } from "mongodb";
import express, { Express, Request, Response } from "express";

// Load and use environment variables from the .env file
dotenv.config();

// Validate environment variables using Envalid before accessing them
const env = cleanEnv(process.env, {
  SERVER_PORT: str({ default: "8000" }),
  DB_URI: str(),
  DB_NAME: str(),
});
const { SERVER_PORT, DB_URI, DB_NAME } = env;

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
