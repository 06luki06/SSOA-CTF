import {seedUser} from "./userseeder";


const runSeeders = async () => {
    await seedUser();
}

runSeeders();