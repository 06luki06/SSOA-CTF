import {seedUser} from "./userseeder";


const runSeeders = async () => {
    await seedUser();
}

runSeeders().catch((err) => { console.error(err) });