
import express, { Express, Request, Response, Application } from 'express';
import dotenv from 'dotenv';
import path from 'path';
import session from "express-session";
import passport from "passport";
import {Strategy as LocalStrategy} from "passport-local";
import AuthStrategy from "./utils/auth";

// For env File 
dotenv.config();

const app: Application = express();
const port = process.env.PORT || 8000;

// Set the view engine to EJS and set up the views directory
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware to serve static files (e.g. images, styles)
app.use(express.static(path.join(__dirname, 'public')));

// Express body parser
app.use(express.urlencoded({ extended: true }));

app.use(session({
    secret: 'secret',
    resave: false,
    saveUninitialized: true
}));

app.use(passport.initialize());
app.use(passport.session());


app.get('/', (req: Request, res: Response) => {
    if (!req.isAuthenticated()) {
        res.redirect('/login');
    } else {
        res.redirect('/profile');
    }
});

// Route to render the login page
app.get('/login', (req: Request, res: Response) => {
  res.render('login', { title: 'Nuclear Power Plant Login' });
});

passport.use(AuthStrategy);

app.post('/login',
    passport.authenticate('local', {
        successRedirect: '/profile',
        failureRedirect: '/login',
    })
);

function ensureAuthenticated(req: Request, res: Response, next: Function) {
    if (req.isAuthenticated()) {
        return next();
    }
    res.redirect('/login');
}

app.get('/profile', ensureAuthenticated, (req: Request, res: Response) => {

    const user = req.user;

    // @ts-ignore
    res.render('profile', { title: 'Nuclear Power Plant Profile', username: user.username});

});
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

