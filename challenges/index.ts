
import express, { Application } from 'express';
import dotenv from 'dotenv';
import path from 'path';
import session from "express-session";
import passport from "passport";
import AuthStrategy from "./utils/auth";
import Router from "./router";

// For env File 
dotenv.config();

const app: Application = express();
const port = process.env.PORT || 3000;

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
app.use(express.json());

passport.use(AuthStrategy);

app.use(Router)

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

