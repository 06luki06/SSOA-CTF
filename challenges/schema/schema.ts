import { AnyPgColumn } from "drizzle-orm/pg-core";
import { pgEnum, pgTable as table } from "drizzle-orm/pg-core";
import * as t from "drizzle-orm/pg-core";


export const users = table(
    "users",
    {
        id: t.integer().primaryKey().generatedAlwaysAsIdentity(),
        username: t.varchar().notNull(),
        password: t.varchar().notNull(),
    },
);