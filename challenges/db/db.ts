import 'dotenv/config';
import { drizzle } from 'drizzle-orm/node-postgres';
import {Pool} from "pg";

const {
    PG_HOST,
    PG_PORT,
    PG_DB,
    PG_USER,
    PG_PASSWORD,
} = process.env;

const DATABASE_URL = `postgres://${PG_USER}:${PG_PASSWORD}@${PG_HOST}:${PG_PORT}/${PG_DB}`;

const pool = new Pool({
    connectionString: DATABASE_URL,
});

export const db = drizzle(pool);
