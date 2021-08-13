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
  c.execute("INSERT INTO users (name, discord_id) VALUES('{}', {})".format(username, int(uid)))
  c.commit()

async def removeuser(uid):
  c = cnxn.cursor("DELETE FROM users WHERE discord_id={}".format(uid))
  c.commit()

async def fetchskills(uid):
  c = cnxn.cursor()
  userdata = c.execute("SELECT attack, defense, strength, fortitude, woodcutting, mining, gathering FROM users WHERE discord_id = {}".format(uid)).fetchone()
  msg = "Your Skills\nAttack             :  {:02d}  Defense        :   {:02d}\nStrength          :  {:02d}  Fortitude      :   {:02d}\nWoodcutting  :  {:02d}  Mining         :  {:02d}\nGathering        :  {:02d}".format(userdata.attack, userdata.defense, userdata.strength, userdata.fortitude, userdata.woodcutting, userdata.mining, userdata.gathering)
  
  # Return dictionary of skill
  return msg
  
