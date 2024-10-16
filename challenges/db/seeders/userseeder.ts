import {users} from "../schema/schema";
import {db} from "../db";
import {getEnvVar} from "../../utils/environment";
import { faker } from '@faker-js/faker';
import CryptoJS from 'crypto-js';

const hpw = getEnvVar("HOMER_PASSWORD");
const mpw = getEnvVar("BURNS_PASSWORD");

const names = [
    "Waylon Smithers",
    "Carl Carlson",
    "Lenny Leonard",
    "Frank Grimes",
    "Mindy Simmons",
    "Sherri Mackleberry",
    "Terri Mackleberry",
    "Hank Scorpio",
    "Don Delgrosso",
    "Eugene Fisk",
    "Howard K. Duff VIII",
    "Jack Marley",
    "Fred Kranepool",
    "Llewellyn Sinclair",
    "Charlie Montelongo",
    "Melvin Powell",
    "Dave Shutton"
];
const homer = {
        username: "hSimpson",
        name: "Homer Simpson",
        password: CryptoJS.MD5(hpw).toString(),
        isAdmin: false,
    };
const burns = {
    username: "cmBurns",
        name: "Charles Montgomery Burns",
        password: CryptoJS.MD5(mpw).toString(),
        isAdmin: true,
}

let userArray = names.map((name) => {
    const [firstname, ...lastnames] = name.split(" ");
    const lastname = lastnames.join(" ").replace(" ", "");
    return {
        password: CryptoJS.MD5(faker.internet.password()).toString(),
        isAdmin: false,
        name,
        username: firstname.charAt(0).toLowerCase()
            + lastname.charAt(0).toUpperCase()
            + lastname.substring(1).toLowerCase(),
    }
})

userArray.splice(4, 0, homer)
userArray.splice(16, 0, burns)

export const seedUser = async () => {
    await db.insert(users).values(userArray);
}
