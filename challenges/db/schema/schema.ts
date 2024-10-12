import {AnyPgColumn, pgSchema} from "drizzle-orm/pg-core";
import * as t from "drizzle-orm/pg-core";


export const nuclearSchema= pgSchema("nuclear")

export const users = nuclearSchema.table(
    "users",
    {
        id: t.integer().primaryKey().generatedAlwaysAsIdentity(),
        username: t.varchar().notNull(),
        password: t.varchar().notNull(),
    },
);