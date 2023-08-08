-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/N9jLFA
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

-- Modify this code to update the DB schema diagram.
-- To reset the sample schema, replace everything with
-- two dots ('..' - without quotes).

CREATE TABLE "gdp" (
    "country_name" varchar,
    "country_code" varchar,
    "year"         int    ,
    "gpd"          decimal(10,4)
);

CREATE TABLE "birth_rate" (
    "country_name" varchar,
    "country_code" varchar,
    "year"         int    ,
    "birth_rate"   decimal(10,4)
);

CREATE TABLE "population" (
    "country_name" varchar    ,
    "year"         int        ,
    "pop"          decimal(10),
    "pop_l01"      decimal(10),
    "pop_l05"      decimal(10),
    "pop_l25"      decimal(10),
    "pop_f15_t64"  decimal(10),
    "pop_g15"      decimal(10),
    "pop_g18"      decimal(10),
    "pop_e01"      decimal(10),
    "pop_f01_t04"  decimal(10),
    "pop_f05_t09"  decimal(10),
    "pop_f10_t14"  decimal(10),
    "pop_f15_t19"  decimal(10),
    "pop_f20_t29"  decimal(10),
    "pop_f30_t39"  decimal(10),
    "pop_f40_t49"  decimal(10),
    "pop_f50_t59"  decimal(10),
    "pop_f60_t69"  decimal(10),
    "pop_f70_t79"  decimal(10),
    "pop_f80_t89"  decimal(10),
    "pop_f90_t99"  decimal(10),
    "pop_g100"     decimal(10)
);

