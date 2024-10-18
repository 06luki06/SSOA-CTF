import express from "express";
import {ensureAuthenticated} from "../middleware/auth";
import {db} from "../db/db";
import {comments, users} from "../db/schema/schema";
import {eq, ilike} from "drizzle-orm";
import { User } from "../utils/auth";

const employeeRouter = express.Router();

employeeRouter.get('/employee', ensureAuthenticated, (req, res) => {
    const user = req.user;
    // @ts-ignore
    res.render('profile', { title: 'Nuclear Power Plant Profile', username: user.username});
});

employeeRouter.get('/employee/:eid', ensureAuthenticated, async (req, res) => {
    const searchId = Number(req.params.eid);
    const user = req.user as User;
    const [{ eid, name, isAdmin}] = await db.select({
        eid: users.id,
        name: users.name,
        isAdmin: users.isAdmin,
    }).from(users).where(
        eq(users.id, searchId),
    );
    if (!eid || eid === user.id) {
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

    res.render('employee', {
        title: 'Nuclear Power Plant Profile',
        isAdmin: isAdmin,
        name: name,
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
    const { comment, recipientId } = req.body;

    const result = await db.insert(comments).values({
        authorId: user.id,
        comment,
        recipientId,
    })
    if (result.rowCount === 0) {
       res.status(400).send('Could not add comment');
       return;
    }
    res.send('Comment added');
});

employeeRouter.get('/comments/:eid', async (req, res) => {
    const searchId = req.params.eid;
    const selectString = `SELECT author_id, comment FROM nuclear.comments WHERE recipient_id = ` + searchId;
    const result = await db.execute(selectString);
    res.send(result.rows);
});

export default employeeRouter;