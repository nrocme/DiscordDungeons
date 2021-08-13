import pyodbc

print("Initializing SQL databse")

# Connect to Microsoft SQL Server Running Locally
cnxn = pyodbc.connect(
  "Driver={ODBC Driver 17 for SQL Server};"
  "Server=LAPTOP-4L23KID1\SQLEXPRESS01;"
  "Database=DiscordDungeons;"
  "Trusted_Connection=yes;"
  )

# Terminal cursor used to execute commands
c = cnxn.cursor()

# Switch to 'DiscordDungeons' database
c.execute("USE DiscordDungeons")

c.execute("DROP TABLE IF EXISTS users;")
c.execute("DROP TABLE IF EXISTS inventories;")
c.execute("DROP TABLE IF EXISTS items;")

# Initialize Tables
c.execute(
  "CREATE TABLE users(
    name VARCHAR(32), discord_id BIGINT, 
    wealth BIGINT, attack INT, 
    defense INT, strength INT, 
    fortitude INT, woodcutting INT, 
    mining INT, gathering INT, 
    PRIMARY KEY (discord_id)
    )"
  )

c.execute(
  "CREATE TABLE inventories(item_id INT, item_count BIGINT, discord_id BIGINT)"
  )

c.execute(
  "CREATE TABLE items(item_id INT, item_count BIGINT, PRIMARY KEY (item_id)"
  )

# Add items to items table

c.execute("INSERT INTO users VALUES('The Chosen One', 1)")

for r in c.execute("select * from users"):
  print(r)

# Print Standard Out
# print(c.messages)

# Commit Changes to Database
c.commit()

# Close cursor
c.close()
