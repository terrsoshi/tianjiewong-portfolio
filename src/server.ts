import cors from "cors";
import dotenv from "dotenv";
import express, { Express, Request, Response } from "express";

dotenv.config();
const { SERVER_PORT = 8000 } = process.env;

const app: Express = express();
app.use(cors());

app.get("/", (req: Request, res: Response) => {
  res.json("Hello World!");
});

app.listen(SERVER_PORT, () => {
  console.log(`Server is listening on port ${SERVER_PORT}.`);
});
