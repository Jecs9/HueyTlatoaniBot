import discord
from discord.ext import commands
import random
import requests
import asyncio
import json
import threading
import os
import time
import sys
from pytz import timezone
from datetime import datetime
import urllib
from io import StringIO
import aiohttp

global ClanInfo
global PlayerInfo
global ClanMembers
global myWhiteList

ClanInfo = {}
PlayerInfo = {}
ClanMembers = {}
myWhiteList = {}

def LoadData():
	clans = ["QL0V9GL"]
	for clan in clans:
		with open(clan + '_ClanInfo.txt') as infile:
			global ClanInfo
			global ClanMembers
			ClanInfo = json.load(infile)
			for member in ClanInfo["members"]:
				ClanMembers[member["tag"]] = {"name" : member["name"], "role" : member["role"]}

	with open('PlayersInfo.txt') as infile:
		global PlayerInfo
		PlayerInfo = json.load(infile)

	UpdateWhiteList()
		
def AddToWhiteList(arg, author):
	if arg in ClanMembers:
		with open('WhiteList.txt', 'r+') as infile:
			
			global myWhiteList
			myWhiteList = json.load(infile)

			if str(author) in list(myWhiteList):
				return 2

			else:
				myWhiteList[str(author)] = {"name": ClanMembers[arg]["name"], "rank": ClanMembers[arg]["role"], "tag": arg}
				infile.seek(0)
				json.dump(myWhiteList, infile)
				infile.truncate()
				UpdateWhiteList()
				return 1

	else:
		return 0

def UpdateWhiteList():
	with open('WhiteList.txt', 'r+') as infile:
		if os.stat('WhiteList.txt').st_size == 0:
			infile.write("{\"Prueba#9999\": {\"name\": \"Dummy\", \"rank\": \"XX\", \"tag\": \"TEST0000\"}}")
			return

		global myWhiteList
		myWhiteList = json.load(infile)

		for key, keyValue in list(myWhiteList.items()):
			if  keyValue["tag"] not in ClanMembers:
				del myWhiteList[key]

		infile.seek(0)
		json.dump(myWhiteList, infile)
		infile.truncate()
	#print(PlayerInfo["YRCRQ2YP"]["PlayerInfo"]["games"]["wins"])
	#print(myWhiteList)

def CreateFooter():
	timestamp = "Clan Mex: " + datetime.now(timezone('UTC')).astimezone(timezone('America/Mexico_City')).strftime('%H:%M:%S %d/%m/%Y')
	return timestamp

def CreateEmote(name, urlEmote):
	with urllib.request.urlopen(urlEmote) as url:	
		s = url.read()

		discord.Guild.create_custom_emoji(name=name, image=s)
		emote = discord.utils.get(discord.guild.emojis, name=name)
		return emote

