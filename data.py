tables_description = {"carData": "This contains name and nufacture years for the cars that are sold all over the world", "labData" : "this contains information about employees"}
tables = ["carData", "labData"]
tables_structure = {"carData" : '''CREATE TABLE IF NOT EXISTS "carData" (
"id" INTEGER,
  "Car Model" TEXT,
  "Manufacture" INTEGER
);
''', "labData" : '''CREATE TABLE IF NOT EXISTS "labData" (
"id" INTEGER,
  "first_name" TEXT,
  "last_name" TEXT,
  "email" TEXT,
  "gender" TEXT,
  "ip_address" TEXT
);
'''} # table_name: table structire as a string 