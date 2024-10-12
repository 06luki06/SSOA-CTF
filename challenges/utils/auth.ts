import { Strategy as LocalStrategy } from "passport-local";
import { eq, and } from 'drizzle-orm';
import {db} from "../db/db";
import {users} from "../db/schema/schema";
import passport from "passport";

const fetchUser = async (username: string, password: string) => {
    const [result] = await db.select().from(users).where(
        and(
            eq(users.username, username),
        )
    );
    if (!result) {
        return null;
    }
    const isCorrect = password === result.password;
    return isCorrect ? result : null;
}

const fetchUserById = async (id: number) => {
    const [result] = await db
        .select()
        .from(users)
        .where(eq(users.id, id));
    return result;
}

passport.serializeUser((user, done) => {
    const { id } = user as { id: number };
    done(null, id);
});

passport.deserializeUser(async (id, done) => {
    if (id && typeof id === 'number') {
        const user = await fetchUserById(id);
        done(null, user);
    } else {
        done(null, null);
    }
});

const addAuthStrategies = async () => {
    passport.use(new LocalStrategy(async (username, password, done) => {
        const user = await fetchUser(username, password)
        if (!user) {
            return done(null, false, { message: "Incorrect username or password" });
        }
        return done(null, user);
    }));
}

export default new LocalStrategy(addAuthStrategies);