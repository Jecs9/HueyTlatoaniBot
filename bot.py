import BotFunctions

def LoadVariables():
	BotFunctions.LoadData()
	BotFunctions.threading.Timer(900.0, LoadVariables).start()

bot = BotFunctions.commands.Bot(command_prefix='$', description='A bot that greets the user back.')

# Print in console if the bot's login is successful
@bot.event
async def on_ready():
	print('Logged in as')
	print(bot.user.name)
	print(bot.user.id)
	print('------')
	
@bot.command(aliases=['add'])
async def Add(ctx, arg):
	author = ctx.message.author
	arg = arg.upper()
	statusWhiteList = BotFunctions.AddToWhiteList(arg, author)
	if statusWhiteList == 1:
		embed = BotFunctions.discord.Embed(title = "Usuario registrado", description = "Jugador registrado exitosamente, bienvenido {}".format(author.mention), color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

		#await ctx.send("Jugador registrado exitosamente, bienvenido {}".format(author.mention))
		
	elif statusWhiteList == 2:
		embed = BotFunctions.discord.Embed(title = "Usuario registrado", description = "Jugador registrado con anterioridad, ALV {}".format(author.mention), color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

		#await ctx.send("El jugador ya está registrado")	
	else:
		embed = BotFunctions.discord.Embed(title = "Imposible registrar", description = "Lo siento  {}, no puedo registrarte ya que no perteneces al poderoso Clan Mex".format(author.mention), color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)
		#await ctx.send("Lo siento, no puedo registrarte ya que no perteneces al poderoso Clan Mex")

@bot.command(aliases=['cofres'])
async def Cofres(ctx):
	author = ctx.message.author

	if str(author) in BotFunctions.myWhiteList:

		chestdata = BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerChests"]

		mapEmoji = {
			'silver': '<:silverchest:481745484248121345>',
			'gold': '<:goldchest:481745679241445386>',
			'giant': '<:giantchest:481746663925612547>',
			'epic': '<:epicchest:481746475437785089>',
			'superMagical': '<:supermagicalchest:481750418834063361>',
			'magical': '<:magicalchest:481750288450191371>',
			'legendary': '<:legendarychest:481746828979732480>'
		}

		valuechestText, specialChestText = "", ""
		for chest, value in chestdata.items():
			if chest == "upcoming":
				for index in value:
					valuechestText += mapEmoji[index] + " "
			else:
				emojiChest = mapEmoji[chest]
				specialChestText += "{} +{} ".format(emojiChest, value + 1)

		embed = BotFunctions.discord.Embed(color = 16098851)
		embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/380832387195469826.png")
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.add_field(name="Cofres siguientes", value=valuechestText, inline=False)
		embed.add_field(name="Cofres especiales", value=specialChestText, inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

	else:
		embed = BotFunctions.discord.Embed(title = "Usuario no registrado", description = "Lo siento, no te tengo registrado", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.add_field(name="Para registrarte", value="Teclea $Add <ID de jugador de CR>", inline=False)
		embed.add_field(name="Ejemplo", value="$Add YRCRQ2YP", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

@bot.command(aliases=['clan'])
async def Clan(ctx):
	author = ctx.message.author
	if str(author) in BotFunctions.myWhiteList:
		embed = BotFunctions.discord.Embed(title = "Clan {} #{}".format(BotFunctions.ClanInfo["name"], BotFunctions.ClanInfo["tag"]), description = "{}".format(BotFunctions.ClanInfo["description"]), color = 16098851)
		embed.set_thumbnail(url=BotFunctions.ClanInfo["badge"]["image"])
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.add_field(name="Total de trofeos", value ="{}".format(BotFunctions.ClanInfo["score"]), inline=False)
		await ctx.send(embed=embed)
		
	else:
		embed = BotFunctions.discord.Embed(title = "Usuario no registrado", description = "Lo siento, no te tengo registrado", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.add_field(name="Para registrarte", value="Teclea $Add <ID de jugador de CR>", inline=False)
		embed.add_field(name="Ejemplo", value="$Add YRCRQ2YP", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

@bot.command(aliases=['donaciones'])
async def Donaciones(ctx):
	author = ctx.message.author
	if str(author) in BotFunctions.myWhiteList:
		donadores = sorted(BotFunctions.PlayerInfo, key=lambda x: BotFunctions.PlayerInfo[x]["PlayerInfo"]["clan"]["donationsDelta"], reverse=True)

		embed = BotFunctions.discord.Embed(title = "Top 5 de Donadores vs Mendigos", description = "Top 5 de jugadores que la relacion entre cartas donadas y cartas recibidas es mayor (Donadores) y menor (Mendigos) ", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.add_field(name="Generosos", value ="Jugadores que más donan", inline=False)
		embed.add_field(name="1° " + BotFunctions.PlayerInfo[donadores[0]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[0]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[0]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[0]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="2° " + BotFunctions.PlayerInfo[donadores[1]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[1]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[1]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[1]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="3° " + BotFunctions.PlayerInfo[donadores[2]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[2]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[2]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[2]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="4° " + BotFunctions.PlayerInfo[donadores[3]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[3]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[3]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[3]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="5° " + BotFunctions.PlayerInfo[donadores[4]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[4]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[4]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[4]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)

		embed.add_field(name="Mendigos", value="Jugadores que menos donan", inline=False)
		embed.add_field(name="1° " + BotFunctions.PlayerInfo[donadores[-1]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[-1]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[-1]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[-1]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="2° " + BotFunctions.PlayerInfo[donadores[-2]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[-2]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[-2]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[-2]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="3° " + BotFunctions.PlayerInfo[donadores[-3]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[-3]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[-3]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[-3]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="4° " + BotFunctions.PlayerInfo[donadores[-4]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[-4]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[-4]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[-4]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.add_field(name="5° " + BotFunctions.PlayerInfo[donadores[-5]]["PlayerInfo"]["name"], value= "```Cartas donadas: {}\nCartas recibidas: {}\nDonaciones netas: {}```".format(BotFunctions.PlayerInfo[donadores[-5]]["PlayerInfo"]["clan"]["donations"], BotFunctions.PlayerInfo[donadores[-5]]["PlayerInfo"]["clan"]["donationsReceived"], BotFunctions.PlayerInfo[donadores[-5]]["PlayerInfo"]["clan"]["donationsDelta"]), inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

	else:
		embed = BotFunctions.discord.Embed(title = "Usuario no registrado", description = "Lo siento, no te tengo registrado", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.add_field(name="Para registrarte", value="Teclea $Add <ID de jugador de CR>", inline=False)
		embed.add_field(name="Ejemplo", value="$Add YRCRQ2YP", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

@bot.command(aliases=['info'])
async def Info(ctx):
	embed = BotFunctions.discord.Embed(title = "@HeytalePazguato", description = "Hice el bot con el fin de ayudar al clan, quejas o sugerencias por DM", color = 16098851)
	embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
	embed.set_author(name="@HueyTlatoani Bot")
	embed.add_field(name="Version", value="1.0", inline=True)
	embed.add_field(name="Sigueme en Twitter", value="[@HeytalePazguato](https://twitter.com/HeytalePazguato)", inline=True)
	embed.set_footer(text=BotFunctions.CreateFooter())
	await ctx.send(embed=embed)

@bot.command(aliases=['melapelan'])
async def MeLaPelan(ctx):
	TuMas = BotFunctions.random.choice(ctx.guild.members)
	Frase = 'A {0.author.mention} se la pelan todos, pero {1.mention} se la come **ENTERA**'.format(ctx, TuMas)
	await ctx.send(Frase)

@bot.command(aliases=['perfil'])
async def Perfil(ctx):
	author = ctx.message.author

	if str(author) in BotFunctions.myWhiteList:

		with BotFunctions.urllib.request.urlopen(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["stats"]["favoriteCard"]["icon"]) as url:	
			s = url.read()

			await ctx.guild.create_custom_emoji(name="FavCard", image=s)
			FavCardEmote = BotFunctions.discord.utils.get(ctx.guild.emojis, name="FavCard")

		currentDeck = []
		cardLevel = []
		for card in BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["currentDeck"]:
			cardLevel.append(str(card["level"]))
			with BotFunctions.urllib.request.urlopen(card["icon"]) as url:
				currentDeck.append(url.read())


		await ctx.guild.create_custom_emoji(name="card0", image=currentDeck[0])
		await ctx.guild.create_custom_emoji(name="card1", image=currentDeck[1])
		await ctx.guild.create_custom_emoji(name="card2", image=currentDeck[2])
		await ctx.guild.create_custom_emoji(name="card3", image=currentDeck[3])
		await ctx.guild.create_custom_emoji(name="card4", image=currentDeck[4])
		await ctx.guild.create_custom_emoji(name="card5", image=currentDeck[5])
		await ctx.guild.create_custom_emoji(name="card6", image=currentDeck[6])
		await ctx.guild.create_custom_emoji(name="card7", image=currentDeck[7])

		currentDeck[0] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card0")
		currentDeck[1] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card1")
		currentDeck[2] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card2")
		currentDeck[3] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card3")
		currentDeck[4] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card4")
		currentDeck[5] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card5")
		currentDeck[6] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card6")
		currentDeck[7] = BotFunctions.discord.utils.get(ctx.guild.emojis, name="card7")

		#for card in BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["currentDeck"]:
		#	with urllib.request.urlopen(card["icon"]) as url:	
		#		s = url.read()
		#		await ctx.guild.create_custom_emoji(name="card{}".format(cardCount), image=s)
		#		currentDeck.append(BotFunctions.discord.utils.get(ctx.guild.emojis, name="card{}".format(cardCount)))
		#		cardCount += 1
				
		
		embed = BotFunctions.discord.Embed(title = "Clan {}".format(BotFunctions.ClanInfo["name"]), description = "#{}".format(BotFunctions.ClanInfo["tag"]), color = 16098851)
		embed.set_thumbnail(url="https://royaleapi.github.io/cr-api-assets/arenas/arena{}.png".format(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["arena"]["arenaID"]))
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.add_field(name="Trofeos", value ="Actual: {} / Máximo: {}".format(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["trophies"], BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["stats"]["maxTrophies"]), inline=False)
		embed.add_field(name="Victorias / Derrotas / Empates", value="{} / {} / {}".format(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["wins"], BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["losses"], BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["draws"]), inline=False)
		embed.add_field(name="Victorias% / Derrotas% / Empates%", value="{0:.2f}% / {1:.2f}% / {2:.2f}%".format(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["winsPercent"] * 100.0, BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["lossesPercent"] * 100.0, BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["games"]["drawsPercent"] * 100.0), inline=False)
		embed.add_field(name="Victorias de 3 coronas", value="{}".format(BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["stats"]["threeCrownWins"]), inline=False)
		embed.add_field(name="Carta favorita", value="{} Nivel: {}".format(str(FavCardEmote), BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["stats"]["favoriteCard"]["maxLevel"]), inline=False)
		embed.add_field(name="Mazo", value="{}{} {}{} {}{} {}{}\n{}{} {}{} {}{} {}{}\n[Copiar Mazo]({})".format(str(currentDeck[0]),cardLevel[0],str(currentDeck[1]),cardLevel[1],str(currentDeck[2]),cardLevel[2],str(currentDeck[3]),cardLevel[3],str(currentDeck[4]),cardLevel[4],str(currentDeck[5]),cardLevel[5],str(currentDeck[6]),cardLevel[6],str(currentDeck[7]),cardLevel[7],BotFunctions.PlayerInfo[BotFunctions.myWhiteList[str(author)]["tag"]]["PlayerInfo"]["deckLink"]))
		await ctx.send(embed=embed)
		await FavCardEmote.delete()
		await currentDeck[0].delete()
		await currentDeck[1].delete()
		await currentDeck[2].delete()
		await currentDeck[3].delete()
		await currentDeck[4].delete()
		await currentDeck[5].delete()
		await currentDeck[6].delete()
		await currentDeck[7].delete()
		
	else:
		embed = BotFunctions.discord.Embed(title = "Usuario no registrado", description = "Lo siento, no te tengo registrado", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.add_field(name="Para registrarte", value="Teclea $Add <ID de jugador de CR>", inline=False)
		embed.add_field(name="Ejemplo", value="$Add YRCRQ2YP", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

@bot.command(aliases=['?', 'ayuda'])
async def Ayuda(ctx):
	author = ctx.message.author

	if str(author) in BotFunctions.myWhiteList:
		embed = BotFunctions.discord.Embed(title = "Comandos disponibles", description = "Esta es la lista de comandos disponibles", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{} (#{})".format(BotFunctions.myWhiteList[str(author)]["name"], BotFunctions.myWhiteList[str(author)]["tag"]))
		embed.add_field(name="$Add", value="Te registra en la lista segura del bot para poder utilizar los demás comandos. Si dejas de ser miembro del Clan Mex automáticamente serás eliminado de la lista.", inline=False)
		embed.add_field(name="$Clan", value="Muestra información del clan", inline=False)
		embed.add_field(name="$Cofres", value="Muestra tu ciclo de cofres", inline=False)
		embed.add_field(name="$Donaciones", value="Muestra al top 5 de jugadores que más y menos donan cartas", inline=False)
		embed.add_field(name="$Info", value="Muestra información del bot", inline=False)
		embed.add_field(name="$Jugadores", value="Lista de miembros de acuerdo al Ranking", inline=False)
		embed.add_field(name="$Perfil", value="Muestra tu perfil", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

	else:
		embed = BotFunctions.discord.Embed(title = "Usuario no registrado", description = "Lo siento, no te tengo registrado", color = 16098851)
		#embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/924225458392260608/7fd_R_ov_400x400.jpg")
		embed.set_author(name="{}".format(author))
		embed.add_field(name="Para registrarte", value="Teclea $Add <ID de jugador de CR>", inline=False)
		embed.add_field(name="Ejemplo", value="$Add YRCRQ2YP", inline=False)
		embed.set_footer(text=BotFunctions.CreateFooter())
		await ctx.send(embed=embed)

@bot.command(name="eval")
@BotFunctions.commands.is_owner()
async def Prueba(ctx):
	# in an async function, such as an on_message handler or command
    	# note that it is often preferable to create a single session to use multiple times later - see below for this.

	await ctx.send("Dueño")

@bot.command()
async def Emote(ctx):
	TestEmote = []
	mapEmoji2 = {
			'1': 'https://vignette.wikia.nocookie.net/clashroyale/images/f/fa/Laughing_King.png/revision/latest?cb=20180717203754',
			'2': 'https://vignette.wikia.nocookie.net/clashroyale/images/1/1a/Thumbs-Up_King.png/revision/latest?cb=20180717203811',
			'3': 'https://vignette.wikia.nocookie.net/clashroyale/images/a/af/Crying_King.png/revision/latest?cb=20180717203736',
			'4': 'https://vignette.wikia.nocookie.net/clashroyale/images/4/42/Angry_King.png/revision/latest?cb=20180717203726',
			'5': 'https://vignette.wikia.nocookie.net/clashroyale/images/7/7e/Eye_Twitch_Goblin.png/revision/latest?cb=20180717203743',
			'6': 'https://vignette.wikia.nocookie.net/clashroyale/images/2/2c/Kiss_Goblin.png/revision/latest?cb=20180717204715',
			'7': 'https://vignette.wikia.nocookie.net/clashroyale/images/4/4f/Laughing_Goblin.png/revision/latest?cb=20180717203752'
		}

	#file = StringIO(urllib.request.urlopen("https://royaleapi.github.io/cr-api-assets/chests/chest-silver.png").read())
	#with urllib.request.urlopen("https://royaleapi.github.io/cr-api-assets/chests/chest-silver.png") as url:
	for number, urlEmoji in mapEmoji2.items():
		print(number)
		with BotFunctions.urllib.request.urlopen(urlEmoji) as url:	
			s = url.read()

			await ctx.guild.create_custom_emoji(name="Emote{}".format(int(number) - 1), image=s)
			emoji = BotFunctions.discord.utils.get(ctx.guild.emojis, name="Emote{}".format(int(number) - 1))
			print("Done {}".format(number))
			if emoji:
				TestEmote.append(emoji)
				await ctx.send("Listo" + str(emoji))
				await emoji.delete()

	#await ctx.send("Listo" + str(TestEmote[0]) + str(TestEmote[1]) + str(TestEmote[2])
	#						+ str(TestEmote[3]) + str(TestEmote[4]) + str(TestEmote[5])
	#						+ str(TestEmote[6]))

@bot.command()
async def Mazos(ctx, arg):
	if arg == "gran":
		url = "https://royaleapi.com/decks/winner/gc"
	elif arg == "clásico":
		url = "https://royaleapi.com/decks/winner/cc"
	else:
		url = "https://api.royaleapi.com/popular/decks"
	for clan in clans:
		headers = {
			'auth':"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MTQ3MSwiaWRlbiI6IjQ3OTEwODM0ODgyMjgxNDcyMCIsIm1kIjp7InVzZXJuYW1lIjoiSGV5dGFsZVBhemd1YXRvIiwia2V5VmVyc2lvbiI6MywiZGlzY3JpbWluYXRvciI6IjEwMzkifSwidHMiOjE1MzQ4MjIzMzY2Njd9.XAEiUsbla6Cnd1f3DfgPS5B1mQhjXr8f-03VVQ-WbQw",
			}

		url = "https://api.royaleapi.com/clan/" + clan
		clanInfoResponse = requests.request("GET", url, headers=headers)
		infoClan = clanInfoResponse.json()

		with open(clan + '_ClanInfo.txt', 'w') as outfileClan:
			json.dump(infoClan, outfileClan)



#Update the files
#loop = asyncio.get_event_loop()
#loop.run_until_complete(Update())

#Update()
#print("Preparando para actualizar")
#BotFunctions.threading.Timer(900.0, BotFunctions.LoadData.start()
LoadVariables()
#BotFunctions.LoadData()
#print("Actualizado")
#print(BotFunctions.myWhiteList)

#Run the bot
bot.run('NDc5MTE5NzU2ODkzMzU2MDMz.DlUqKA.v_zyPKnWDG5R9YxF2GqIryLA-Jo')