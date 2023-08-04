-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/WEpOTm
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.

CREATE TABLE "gpd" (
    "country_name" varchar(50)   NOT NULL,
    "country_code" varchar(03)   NOT NULL,
    "year" int NOT NULL,
    "gpd" decimal(10,4)  NOT NULL,
    CONSTRAINT "country_code" PRIMARY KEY (
        "country_code","year"
     )
);
