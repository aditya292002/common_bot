tables_description = {"cardata": "This contains name and nufacture years for the cars that are sold all over the world", "labdata" : "this contains information about employees"}
tables = ["cardata", "labdata"]
tables_structure = {"cardata" : '''CREATE TABLE IF NOT EXISTS "cardata" (
"id" INTEGER,
  "Car Model" TEXT,
  "Manufacture" INTEGER
);
''', "labdata" : '''CREATE TABLE IF NOT EXISTS "labdata" (
"id" INTEGER,
  "first_name" TEXT,
  "last_name" TEXT,
  "email" TEXT,
  "gender" TEXT,
  "ip_address" TEXT
);
'''}
# table_name: table structire as a string 