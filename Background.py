import BotFunctions

class MyClient(BotFunctions.discord.Client):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		# create the background task and run it in the background
		self.bg_task = self.loop.create_task(self.Update())

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')


	async def Update(self):
		await self.wait_until_ready()
		channel = self.get_channel(480962084792958978) # channel ID goes here
		while not self.is_closed():
			clans = ["QL0V9GL"]
			for clan in clans:

				headers = {
					'auth':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ3MSwiaWRlbiI6IjQ3OTEwODM0ODgyMjgxNDcyMCIsIm1kIjp7InVzZXJuYW1lIjoiSGV5dGFsZVBhemd1YXRvIiwia2V5VmVyc2lvbiI6MywiZGlzY3JpbWluYXRvciI6IjEwMzkifSwidHMiOjE1MzQ4MjIzMzY2Njd9.XAEiUsbla6Cnd1f3DfgPS5B1mQhjXr8f-03VVQ-WbQw",
					}
				url = "https://api.royaleapi.com/clan/" + clan

				async with BotFunctions.aiohttp.ClientSession(headers=headers) as session:
					async with session.get(url) as clanInfoResponse:
						if clanInfoResponse.status == 200:
							print("Got clan info")
							infoClan = await clanInfoResponse.json()
						else:
							print("Error getting clan info: {}".format(clanInfoResponse.status))

				with open(clan + '_ClanInfo.txt', 'w') as outfileClan:
					BotFunctions.json.dump(infoClan, outfileClan)
		
				for member in infoClan["members"]:

					# Get member information
					while True:
						url = "https://api.royaleapi.com/player/" + member["tag"]
						async with BotFunctions.aiohttp.ClientSession(headers=headers) as session:
							async with session.get(url) as memberInfoResponse:
								if memberInfoResponse.status == 200:
									print("Got member info: {}".format(member["name"]))
									infoMember = await memberInfoResponse.json()
									break
								else:
									print("Error getting member {} info: {}".format(member["name"], memberInfoResponse.status))

					while True:
						url = "https://api.royaleapi.com/player/" + member["tag"]  + "/chests"
						async with BotFunctions.aiohttp.ClientSession(headers=headers) as session:
							async with session.get(url) as memberChestsResponse:
								if memberChestsResponse.status == 200:
									print("Got member chests info: {}".format(member["name"]))
									chestsMember = await memberChestsResponse.json()
									break
								else:
									print("Error getting member {} chests info: {}".format(member["name"], memberChestsResponse.status))

					while True:
						url = "https://api.royaleapi.com/player/" + member["tag"]  + "/battles"
						async with BotFunctions.aiohttp.ClientSession(headers=headers) as session:
							async with session.get(url) as memberBattlesResponse:
								if memberBattlesResponse.status == 200:
									print("Got member battles info: {}".format(member["name"]))
									battlesMember = await memberBattlesResponse.json()
									break
								else:
									print("Error getting member {} battles info: {}".format(member["name"], memberBattlesResponse.status))


					BotFunctions.PlayerInfo
					BotFunctions.PlayerInfo[member["tag"]] = {"PlayerInfo" : infoMember, "PlayerChests" : chestsMember, "PlayerBattles" : battlesMember}
	
					#print(PlayerInfo["VC0VQV09"]["PlayerInfo"]["name"])
					#print(PlayerInfo["VC0VQV09"]["PlayerChests"]["upcoming"])
					#sys.exit()

				with open('PlayersInfo.txt', 'w') as outfilePlayers:
					BotFunctions.json.dump(BotFunctions.PlayerInfo, outfilePlayers)

			BotFunctions.LoadData()

			print("Actualización completa")
			await BotFunctions.asyncio.sleep(900) # task runs every 900 seconds
			#threading.Timer(3600.0, Update).start()

	#async def my_background_task(self):
	#	await self.wait_until_ready()
	#	counter = 0
	#	channel = self.get_channel(480962084792958978) # channel ID goes here
	#	while not self.is_closed():
	#		counter += 1
	#		await channel.send(counter)
	#		my_background_task2()
	#		await asyncio.sleep(10) # task runs every 60 seconds

client = MyClient()
client.run('NDc5MTE5NzU2ODkzMzU2MDMz.DlUqKA.v_zyPKnWDG5R9YxF2GqIryLA-Jo')