import dotenv from "dotenv";
import path from "path";

dotenv.config({ path: path.resolve(__dirname + '/../.env')});
console.log(path.resolve(__dirname + '/../.env'))

export const getEnvVar = (name: string): string => {
    const value = process.env[name];
    if (!value) {
        throw new Error(`Environment variable ${name} is not set`);
    }
    return value;
};