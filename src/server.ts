import dotenv from "dotenv";
import express, { Express, Request, Response } from "express";

dotenv.config();
const app: Express = express();

const { SERVER_PORT = 8000 } = process.env;

app.get("/", (req: Request, res: Response) => {
  res.json("Hello World!");
});

app.listen(SERVER_PORT, () => {
  console.log(`Server is listening on port ${SERVER_PORT}.`);
});
