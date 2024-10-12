import { defineConfig } from 'drizzle-kit'
// via connection params
import dotenv from "dotenv";
import {getEnvVar} from "../../utils/environment";


const user = getEnvVar("PG_USER");
const password = getEnvVar("PG_PASSWORD");
const host = getEnvVar("PG_HOST");
const port:number = Number(getEnvVar("PG_PORT"));
const database = getEnvVar("PG_DB");

export default defineConfig({
    dialect: "postgresql",
    dbCredentials: {
        host: host,
        port: port,
        user: user,
        password: password,
        database: database,
        ssl: false,
    },
    schema: './db/schema/schema.ts',
    schemaFilter: ["nuclear"],
});