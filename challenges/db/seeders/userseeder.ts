import {users} from "../schema/schema";
import {db} from "../db";
import {getEnvVar} from "../../utils/environment";
import { faker } from '@faker-js/faker';

const hpw = getEnvVar("HOMER_PASSWORD");
const mpw = getEnvVar("BURNS_PASSWORD");

export const seedUser = async () => {
    await db.insert(users).values([
        {
            username: "hSimpson",
            name: "Homer Simpson",
            password: hpw,
            isAdmin: false,
        },
        {
            username: "wSmithers",
            name: "Waylon Smithers",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "cCarlson",
            name: "Carl Carlson",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "lLeonard",
            name: "Lenny Leonard",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "fGrimes",
            name: "Frank Grimes",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "cCharlie",
            name: "Charlie",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "mSimmons",
            name: "Mindy Simmons",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "sMackleberry",
            name: "Sherri Mackleberry",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "tMackleberry",
            name: "Terri Mackleberry",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "hScorpio",
            name: "Hank Scorpio",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "dDelgrosso",
            name: "Don Delgrosso",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "eFisk",
            name: "Eugene Fisk",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "hDuff",
            name: "Howard K. Duff VIII",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "jMarley",
            name: "Jack Marley",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "fKranepool",
            name: "Fred Kranepool",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "lSinclair",
            name: "Llewellyn Sinclair",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "cmBurns",
            name: "Charles Montgomery Burns",
            password: mpw,
            isAdmin: true,
        },
        {
            username: "cMontelongo",
            name: "Charlie Montelongo",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "mPowell",
            name: "Melvin Powell",
            password: faker.internet.password(),
            isAdmin: false,
        },
        {
            username: "dShutton",
            name: "Dave Shutton",
            password: faker.internet.password(),
            isAdmin: false,
        }
    ]);
}
