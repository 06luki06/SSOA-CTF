import express from "express";
import {ensureAuthenticated} from "../middleware/auth";
import {db} from "../db/db";
import {comments, users} from "../db/schema/schema";
import {eq, ilike, sql} from "drizzle-orm";
import { User } from "../utils/auth";

const employeeRouter = express.Router();

employeeRouter.get('/employee', ensureAuthenticated, (req, res) => {
    const user = req.user;
    // @ts-ignore
    res.render('profile', { title: 'Nuclear Power Plant Profile', username: user.username});
});

employeeRouter.get('/employee/:eid', ensureAuthenticated, async (req, res) => {
    const searchId = Number(req.params.eid);
    const [{ eid, name, isAdmin}] = await db.select({
        eid: users.id,
        name: users.name,
        isAdmin: users.isAdmin,
    }).from(users).where(
        eq(users.id, searchId),
    );
    if (!eid) {
        res.redirect('/employee');
    }
    res.render('employee', {
        title: 'Nuclear Power Plant Profile',
        isAdmin: isAdmin,
        name: name
    });
});

employeeRouter.get('/employee/admin/:eid', ensureAuthenticated, async (req, res) => {
    const searchId = Number(req.params.eid);
    const [{ eid, name, isAdmin}] = await db.select({
        eid: users.id,
        name: users.name,
        isAdmin: users.isAdmin,
    }).from(users).where(
        eq(users.id, searchId),
    );
    if (!eid || !isAdmin) {
        res.redirect('/employee');
    }

    const commentsData = await db.select().from(comments);
    console.log(commentsData);

    res.render('employee', {
        title: 'Nuclear Power Plant Profile',
        isAdmin: isAdmin,
        name: name,
        comments: commentsData
    });
});


employeeRouter.post('/employee/search', ensureAuthenticated, async (req, res) => {
    const search = req.body.employeeName;
    const [user] = await db.select({
        id: users.id,
        name: users.name,
        isAdmin: users.isAdmin,
    }).from(users).where(
        ilike(users.name, `%${search}%`)
    );
    if (!user) {
        res.redirect('/employee')
        return;
    }
    if (user.isAdmin) {
        res.redirect(`/employee/admin/${user.id}`);
        return;
    }
    res.redirect(`/employee/${user.id}`);
});

employeeRouter.post('/comments', ensureAuthenticated, async (req, res) => {
    const user = req.user as User;
    const comment = req.body.comment;

    const stringToInsert = `INSERT INTO nuclear.comments (author_id, comment) VALUES (${user.id}, '${comment}');`;
    console.log(stringToInsert);
    
    await db.execute(stringToInsert);
    res.send('Comment added');
});

export default employeeRouter;