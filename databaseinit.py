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

c.execute(
  "CREATE TABLE users(DISCORD_ID INT, PRIMARY KEY (DISCORD_ID))"
  )

c.execute("INSERT INTO users VALUES(1)")

for r in c.execute("select * from users"):
  print(r)

# Print Standard Out
# print(c.messages)

# Commit Changes to Database
c.commit()

# Close cursor
c.close()
