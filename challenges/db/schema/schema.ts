import { relations } from "drizzle-orm";
import {pgSchema} from "drizzle-orm/pg-core";
import * as t from "drizzle-orm/pg-core";

export const nuclearSchema= pgSchema("nuclear")

export const users = nuclearSchema.table(
    "employees",
    {
        id: t.integer().primaryKey().generatedAlwaysAsIdentity(),
        username: t.varchar().notNull(),
        name: t.varchar().notNull(),
        isAdmin: t.boolean().notNull().default(false),
        password: t.varchar().notNull(),
    },
);

export const comments = nuclearSchema.table(
    "comments",
    {
        id: t.integer().primaryKey().generatedAlwaysAsIdentity(),
        authorId: t.integer("author_id").notNull(),
        comment: t.varchar().notNull(),
    },
);

export const usersRelations = relations(users, ({ many }) => ({
    comments: many(comments),
}));

export const commentsRelations = relations(comments, ({ one }) => ({
    author: one(users, {
    fields: [comments.authorId],
    references: [users.id],
})}));
