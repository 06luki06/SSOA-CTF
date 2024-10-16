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