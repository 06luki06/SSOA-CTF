import passport from "passport";
import {Strategy as LocalStrategy} from "passport-local";


export const users = [
    {
        id: 1,
        username: 'homer',
        password: 'homer'
    }
]

passport.serializeUser((user, done) => {
    // @ts-ignore
    done(null, user.id);
});
passport.deserializeUser((id, done) => {
    const user = users.find(u => u.id === id);
    done(null, user);
});
const authenticateUser = (username: string, password: string, done: Function) => {
    const user = users.find(u => u.username === username);
    if (!user) {
        return done(null, false, { message: 'Incorrect username.' });
    }
    if (user.password !== password) {
        return done(null, false, { message: 'Incorrect password.' });
    }
    return done(null, user);
}

export default new LocalStrategy(authenticateUser);