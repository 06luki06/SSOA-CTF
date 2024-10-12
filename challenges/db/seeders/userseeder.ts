import {users} from "../schema/schema";
import {db} from "../db";
import {getEnvVar} from "../../utils/environment";

const password = getEnvVar("HOMER_PASSWORD");

export const seedUser = async () => {
    await db.insert(users).values({
        username: "homer",
        password: password,
    });
}
