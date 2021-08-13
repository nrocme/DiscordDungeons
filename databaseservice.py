import pyodbc

print("Initializing SQL databse")

# Connect to Microsoft SQL Server Running Locally
cnxn = pyodbc.connect(
  "Driver={ODBC Driver 17 for SQL Server};"
  "Server=LAPTOP-4L23KID1\SQLEXPRESS01;"
  "Database=DiscordDungeons;"
  "Trusted_Connection=yes;"
  )

async def adduser(username, uid):
  c = cnxn.cursor()
  c.execute("INSERT INTO users VALUES('{}', {})".format(username, int(uid)))
  c.commit()

async def removeuser(uid):
  c = cnxn.cursor()
  
