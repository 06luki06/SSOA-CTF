import express from "express";
import {ensureAuthenticated} from "../middleware/auth";
import {db} from "../db/db";
import {users} from "../db/schema/schema";
import {eq, ilike} from "drizzle-orm";



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
    res.render('employee', {
        title: 'Nuclear Power Plant Profile',
        isAdmin: isAdmin,
        name: name
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

export default employeeRouter;