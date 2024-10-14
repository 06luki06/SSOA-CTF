import { Router} from "express";
import passport from "passport";
import {db} from "../db/db";
import {users} from "../db/schema/schema";
import {eq} from "drizzle-orm";
import employeeRouter from "./employee";

const router  = Router();

router.use(employeeRouter);

router.get('/', (req, res) => {
    if (!req.isAuthenticated()) {
        res.redirect('/login');
    } else {
        res.redirect('/profile');
    }
});

// Route to render the login page
router.get('/login', (_req, res) => {
    res.render('login', { title: 'Nuclear Power Plant Login' });
});

router.post('/login',
    passport.authenticate('local', {
        successRedirect: '/employee',
        failureRedirect: '/login',
    })
);

router.post('/logout', (req, res, next) => {
    req.logout((err) => {
        if (err) { return next(err)}
        res.redirect('/login');
    })
})


router.post('/waste', async (req, _res) => {
    // TODO: change with db impl
    // Base 64 encode username and password of the user homer
    const [user] = await db.select().from(users).where(eq(users.username, "homer"));
    // @ts-ignore
    const token = Buffer.from(`${user.username}:${user.password}`).toString('base64');
    // get the url from the form data body
    const url = req.body.url;
    await fetch(url, {
        method: 'POST',
        headers: {
            'Authorization': `Basic ${token}`
        }
    });
});

export default router;