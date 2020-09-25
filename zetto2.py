import discord
import openpyxl
import asyncio
import datetime
import requests 
from bs4 import BeautifulSoup
import traceback
import bs4
from urllib.request import urlopen, Request
import urllib
import smtplib
import sys
import pkg_resources 
import aiohttp
import os
import time
from pyowm import OWM
import sqlite3
from difflib import SequenceMatcher
import koreanbots
import dbl
import qrcode
from requests import get
import Dtime
import neispy
import tasks
import argparse
from captcha.image import ImageCaptcha
import random
from Dtime import Uptime
import ast
from discord.ext import commands
from discord.utils import get
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen 
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import json
import re
import requests as rq
from bs4 import BeautifulSoup as bs
from urllib.parse import quote
from urllib.request import urlopen, Request

heimteam = [534214957110394881, 524515155254444032, 556403526851624983]
# 공지,종료등등: #베인블 #제토  #아이픽누나
owner = [534214957110394881, 524515155254444032, 556403526851624983]
# 컴파일: #베인블 #제토  #아이픽누나
client = discord.Client()
queues = {}
Uptime.uptimeset()
start_time = time.time()
pingpongurl = 핑퐁토큰1
pingpongauth = 핑퐁토큰2
client_secret = "ZBHDeMCaMe"
opggsummonersearch = 'https://www.op.gg/summoner/userName='
tierScore = {
        'default': 0,
        'iron': 1,
        'bronze': 2,
        'silver': 3,
        'gold': 4,
        'platinum': 5,
        'diamond': 6,
        'master': 7,
        'grandmaster': 8,
        'challenger': 9
    }

r6URL = "https://r6stats.com"
playerSite = 'https://www.r6stats.com/search/'






@client.event
async def on_ready():
    print('=====================================')
    print("ready")
    print(client.user.id)
    print(client.user.name)
    print('=====================================')
    now=datetime.datetime.now()    



@client.event
async def on_member_join(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 입장',
            description=f'{member}님이{member.guild}에 입장 했습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=0x00ff00
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

@client.event
async def on_member_remove(member):
    syschannel = member.guild.system_channel.id 
    try:
        embed=discord.Embed(
            title=f'멤버 퇴장',
            description=f'{member}님이{member.guild}에 퇴장 했습니다.\n현재 서버 인원수: {str(len(member.guild.members))}명',
            colour=discord.Colour.red()
        )
        embed.set_thumbnail(url=member.avatar_url)
        await client.get_channel(syschannel).send(embed=embed)
    except:
        return None

@client.event
async def on_guild_join(guild):
    webhook = '웹훅'
    requests.post(webhook, {'content':f'{guild.name}({guild.id})에 봇 초대됨. owner = {guild.owner}({guild.owner.id})<a:yes:707786803414958100>\n서버수:{len(client.guilds)}개'})
    webhook = '웹훅'
    requests.post(webhook, {'content':f'{guild.name}({guild.id})에 봇 초대됨. owner = {guild.owner}({guild.owner.id})<a:yes:707786803414958100>\n서버수:{len(client.guilds)}개'})
    await guild.owner.send(f'`제토2`를 {guild.name}에 초대해주셔서 감사드립니다!\n앞으로 제토2는 더 발전하겠습니다\n채널 이름에 `봇-공지` 라는 이름이 들어간 채널이 있다면 \n제토2의 공지를 더 빨리 받아보실수 있습니다\n\
https://koreanbots.cf/bots/666879942667141128 여기서 하트추가를 눌러주세요!')

@client.event
async def on_guild_remove(guild):
    webhook = '웹훅'
    requests.post(webhook, {'content':f'{guild.name}({guild.id})에 봇 추방됨. owner = {guild.owner}({guild.owner.id})<a:no:707786855143309370>\n서버수:{len(client.guilds)}개'})
    webhook = '웹훅'
    requests.post(webhook, {'content':f'{guild.name}({guild.id})에 봇 추방됨. owner = {guild.owner}({guild.owner.id})<a:no:707786855143309370>\n서버수:{len(client.guilds)}개'})



@client.event
async def on_message(message):
    def htmltotext(html):
        soup = BeautifulSoup(html)
        text_parts = soup.findAll(text=True)
        return "".join(text_parts)
    async def makeembed(title):
        embed=discord.Embed(
            title=title,
            colour=0x00f000
        )
        await message.channel.send(embed=embed)
    async def insert_returns(body):
        # insert return stmt if the last expression is a expression statement
        if isinstance(body[-1], ast.Expr):
            body[-1] = ast.Return(body[-1].value)
            ast.fix_missing_locations(body[-1])

        # for if statements, we insert returns into the body and the orelse
        if isinstance(body[-1], ast.If):
            insert_returns(body[-1].body)
            insert_returns(body[-1].orelse)

        # for with blocks, again we insert returns into the body
        if isinstance(body[-1], ast.With):
            insert_returns(body[-1].body)
    async def req (url : str, header = None) :
        async with aiohttp.ClientSession () as session:
            async with session.get (url = url, headers=header) as r :
                data = await r.json()
        return data
    def earthquake(source):
        source = source.text.strip()
        if source:
            return source
        elif source == "" or source is None:
            return "정보가 없습니다."
    async def post_guild_count(token, guild_count):
        URL = 'https://api.koreanbots.cf/bots/servers'
        headers = {"token":token,"content-type":"application/json"}
        data = {'servers':guild_count}
        async with aiohttp.ClientSession() as cs:
            async with cs.post(URL, headers=headers, json=data) as r:
                response = await r.json()
                return response
    async def __init__(self, client):
        self.client = client
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY5NTU0NjU3NzI2MzEzMjY3NCIsImJvdCI6dHJ1ZSwiaWF0IjoxNTkwMDI0Njg1fQ.rW5IA2Dikv5Xbo6tskmWTqHZiQauEngrdKhzP54Pp0A'  # set this to your DBL token
        self.dblpy = dbl.DBLClient(self.client, self.token)
        self.CBSList = "http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json"
    def deleteTags(htmls):
        for a in range(len(htmls)):
            htmls[a] = re.sub('<.+?>', '', str(htmls[a]), 0).strip()
        return htmls


    def tierCompare(solorank, flexrank):
        if tierScore[solorank] > tierScore[flexrank]:
            return 0
        elif tierScore[solorank] < tierScore[flexrank]:
            return 1
        else:
            return 2

        warnings.filterwarnings(action='ignore')
    async def makeembed1(title, description):
        embed=discord.Embed(
            title=title,
            description=description,
            colour=0x00f000
        )
        embed.set_footer(icon_url=message.author.avatar_url, text=f'{message.author}에게 요청받음')
        await message.channel.send(embed=embed)
    async def makeembed2(title, description):
        embed=discord.Embed(
            title=title,
            description=description,
            colour=0x00e2ff
        )
        await message.channel.send(embed=embed)
    async def makeembed3(title):
        embed=discord.Embed(
            title=title,
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)

    async def makeembed4(title, description):
        embed=discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour.red()
        )
        await message.channel.send(embed=embed)
    channel = message.channel

    try:
        if message.content.startswith('제토2'):
            webhook = 'https://discordapp.com/api/webhooks/727684181160624178/uDibbeF5MrHJgkfVoNMVaP72oW7gAfkv3OJb1xvdkrK0dhzaw8sUl0onLiMnKl66H6fh'
            requests.post(webhook, {'content':f'**{message.author}** ('+ f'{message.author.id}) : `{message.content}`\n - {message.channel.guild} {message.channel.name}'})
            webhook = 'https://discordapp.com/api/webhooks/727688716436635769/jeqkpgcal39Wg3LqsEKEJFOAFQT3GPvoibypZtBQNhAtc4yF8tcYIgxpduk864QSqhkO'
            requests.post(webhook, {'content':f'**{message.author}** ('+ f'{message.author.id}) : `{message.content}`\n - {message.channel.guild} {message.channel.name}'})
            print(f'{message.author} ('+ f'{message.author.id}) : {message.content}')

            if message.author.bot:
                return None

            if message.author.id == 666879942667141128:
                return None

            elif message.content ==('제토2 환영설정'):
                await makeembed(f'시스템 메시지 설정 하시면 그곳에 환영인사함')
            elif message.content == '제토2 공지설정':
                await makeembed(f'봇-공지 라는 채널이 있다면 공지가 됨')
            elif message.content == '제토2 봇서버'  or  message.content == '제토2 서버':
                await makeembed1('제토2가 함께하는 서버, 유저 수', f'서버:{len(client.guilds)}개\n유저:{len(client.users)}명')
            elif message.content.startswith("제토2 타이머"):
                channel = message.channel
                if len(message.content[8:].split()) == 0:
                    await makeembed3('1~2개의 인수가 필요함')
                else:
                    time = message.content[8:].split()[0]
                    if len(message.content[8:].split()) >= 2:
                        reason = message.content[8:].split()[1]
                    else:
                        reason = "사유 없음"
                    try:
                        time = int(time)
                        await makeembed1('타이머',f':alarm_clock: {reason} | {str(time)}초(이)라는 타이머가 등록되었습니다.')
                        await asyncio.sleep(time)
                        try:
                            embed = discord.Embed(
                                title="타이머 (끝)",
                                description=f":alarm_clock: {reason}",
                                color=0x00f000,
                            )
                            await message.channel.send(f'<@{message.author.id}>',embed=embed)
                        except:
                            embed = discord.Embed(
                                title="타이머 (끝)",
                                description=f":alarm_clock: {reason}",
                                color=0x00f000,
                            )
                            await message.channel.send(f'<@{message.author.id}>',embed=embed)
                    except:
                        await makeembed3('타이머 명령어의 시간(초)는 숫자여야만 합니다!')
            elif message.content.startswith("제토2 매치"):
                channel = message.channel
                mlen = len(message.content[7:].split())
                if not mlen == 2:
                    await makeembed3('매치 명령어는 2개의 인수가 필요합니다!')
                else:
                    first = message.content[7:].split()[0]
                    second = message.content[7:].split()[1]
                    match = SequenceMatcher(None, first, second).ratio()*100
                    await makeembed1(f'{first} & {second} 의 비슷한 정도',f'{str(int(match))}%')
            elif message.content == "제토2 미세먼지":
                channel = message.channel
                url = "https://search.naver.com/search.naver?sm=top_hty&fbm=0&ie=utf8&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
                res = requests.get(url)
                html = res.text
                bs = bs4.BeautifulSoup(html, 'html.parser')
                mise = {}
                city = ['서울', '경기', '인천', '강원', '세종', '충북' ,'충남', '대전', '경북', '경남', '대구', '울산', '부산', '전북', '전남', '광주', '제주']
                num = 0
                for x in city:
                    mise[x] = bs.select(
                        "#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div > div.main_box > div.detail_box > div.tb_scroll > table > tbody > tr > td > span")[num].text
                    num += 3
                level = {}
                for x in city:
                    if int(mise[x]) <= 30:
                        level[x] = "좋음"
                    elif int(mise[x]) >= 31 and int(mise[x]) <= 80:
                        level[x] = "보통"
                    elif int(mise[x]) >= 81 and int(mise[x]) <= 150:
                        level[x] = "**나쁨**"
                    elif int(mise[x]) >= 151:
                        level[x] = "**매우나쁨**"
                    else:
                        level[x] = "오류"
                time = bs.select("#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div > div.info_box > div.guide_bx > div > span.update > em")[0].text
                embed = discord.Embed(title=f"PM10 미세먼지\n{time}기준",  color=0xff00, timestamp=message.created_at)
                for i in city:
                    embed.add_field(name="**"+i+"**", value=(mise[i]+"㎍/m³ | "+level[i]))
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content.startswith(f"제토2 캡챠"):
                author = message.author
                role = discord.utils.get(message.guild.roles, name="유저")
                lmage_captcha = ImageCaptcha()
                a = ""
                for i in range(6):
                    a += str(random.randint(0, 9))
                name = str(message.author.id) + ".png"
                lmage_captcha.write(a, name)

                await message.channel.send(file=discord.File(name))
                def check(msg):
                    return msg.author == message.author and msg.channel == message.channel

                try:
                    msg = await client.wait_for("message", timeout=10, check=check)
                except:
                    await makeembed4('시간초과!', '캡챠인증에 실패했습니다!')
                    return

                if msg.content == a:
                    await makeembed1('성공!', '캡챠인증에 성공했습니다!')
                    try:
                        role = discord.utils.get(message.guild.roles, name="유저")
                        await author.add_roles(role)
                    except:
                        return
                    await asyncio.sleep(3)
                    await message.channel.purge(limit=4)
                else:
                    await makeembed4('실패!', '캡챠인증에 실패했습니다!')
                    await asyncio.sleep(3)
                    await message.channel.purge(limit=4)
            elif message.content == "제토2 초미세먼지":
                channel = message.channel
                url = "https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%B4%88%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80"
                res = requests.get(url)
                html = res.text
                bs = bs4.BeautifulSoup(html, 'html.parser')
                mise = {}
                city = ['서울', '경기', '인천', '강원', '세종', '충북' ,'충남', '대전', '경북', '경남', '대구', '울산', '부산', '전북', '전남', '광주', '제주']
                num = 0
                for x in city:
                    mise[x] = bs.select(
                        "#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div > div.main_box > div.detail_box > div.tb_scroll > table > tbody > tr > td > span")[num].text
                    num += 3
                level = {}
                for x in city:
                    if int(mise[x]) <= 15:
                        level[x] = "좋음"
                    elif int(mise[x]) >= 16 and int(mise[x]) <= 35:
                        level[x] = "보통"
                    elif int(mise[x]) >= 36 and int(mise[x]) <= 75:
                        level[x] = "**나쁨**"
                    elif int(mise[x]) >= 76:
                        level[x] = "**매우나쁨**"
                    else:
                        level[x] = "오류"
                time = bs.select("#main_pack > div.content_search.section._atmospheric_environment > div > div.contents03_sub > div > div > div.info_box > div.guide_bx > div > span.update > em")[0].text
                embed = discord.Embed(title=f"PM2.5 미세먼지\n{time}기준",  color=0xff00, timestamp=message.created_at)
                for i in city:
                   embed.add_field(name="**"+i+"**", value=(mise[i]+"㎍/m³ | "+level[i]))
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content == "제토2 슬롯":
                channel = message.channel
                first = random.choice([":tada:", ":seven:", "<:Seeds:720462839784931338> ", ":star:", ":crown:", "<:teamsb:722654596828495903>"])
                second = random.choice([":tada:", ":seven:", "<:Seeds:720462839784931338> ", ":star:", ":crown:", "<:teamsb:722654596828495903>"])
                third = random.choice([":tada:", ":seven:", "<:Seeds:720462839784931338> ", ":star:", ":crown:", "<:teamsb:722654596828495903>"])
                await makeembed1('3개의 이모지가 모두 같을시 승리합니다.',f'[ {first}  | {second} | {third} ]')
                if first == second and first == third:
                    message = await makeembed(f'{message.author}님, 성공! 축하드립니다!')
                else:
                    message = await makeembed3(f'{message.author}님, 아쉽지만 실패했습니다.')
            elif message.content.startswith("제토2 랜덤숫자"):

                channel = message.channel
                random_len = len(message.content[9:].split())
                if not random_len == 2:
                    await makeembed3('2개의 인수가 필요합니다!')
                else:
                    try:
                        random_first = int(message.content[9:].split(" ")[0])
                        random_second = int(message.content[9:].split(" ")[1])
                        random_number = str(random.randrange(random_first, random_second))
                        await makeembed1(f'랜덤숫자\n{str(random_first)}~{str(random_second)}중 선택된 숫자',f'{random_number}')
                    except ValueError:
                        await makeembed3('인수는 꼭 숫자여야 합니다!')
            elif message.content.startswith("제토2 슛골인"):
                channel = message.channel
                if str(message.content[8:].split(" ")[0]) == "정보":
                    await makeembed1('난이도 선택',f'쉬움 - 1m~100m중 1m~50m이 나오면 승리\n**어려움** - 1m~100m중 1m~10m이 나오면 승리')
                elif str(message.content[8:].split(" ")[0]) == "쉬움":
                    dif = str(message.content[8:].split(" ")[0])
                    randnum = random.randint(1, 100)
                    if randnum >= 1 and randnum <= 50:
                        await makeembed(f'{message.author}님, 성공! 축하드립니다! (쉬움)\n({randnum}m)')
                    else:
                        await makeembed3(f'{message.author}님, 아쉽지만 실패했습니다.\n({randnum}m)')
                elif str(message.content[8:].split(" ")[0]) == "어려움":
                    dif = str(message.content[8:].split(" ")[0])
                    randnum = random.randint(1, 100)
                    if randnum >= 1 and randnum <= 10:
                        await makeembed(f'{message.author}님, 성공! 축하드립니다! (어려움)\n({randnum}m)')
                    else:
                        await makeembed3(f'{message.author}님, 아쉽지만 실패했습니다. \n({randnum}m)')
                else:
                    await makeembed3(f'인수는 정보 / 쉬움 / 어려움 이여야만 합니다!')
            elif message.content.startswith(f"제토2 추방"):
                if message.guild.get_member(client.user.id).guild_permissions.kick_members == True:
                    if message.author.guild_permissions.kick_members:
                        try:
                            try:
                                user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                            except:
                                user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                            if user.id == message.author.id:
                                await makeembed3("추방를 할수가 없는 유저입니다")
                            else:
                                try:
                                    reason = message.content.split('&')[1]
                                except:
                                    reason = "사유 없음"
                                await message.guild.kick(user, reason = f"{reason}")
                                try:
                                    embed = discord.Embed(title=f"{user} 추방", color=discord.Colour.red(), timestamp=message.created_at)
                                    embed.add_field(name=" 처리자", value=f"<@{message.author.id}> ({message.author})", inline = False)
                                    embed.add_field(name=" 유저", value=f'<@{user.id}> ({user})', inline = False)
                                    embed.add_field(name=" 정보", value=f'추방 사유:{reason}', inline = False)
                                    embed.set_footer(text=f"{message.author}처리자", icon_url=message.author.avatar_url)
                                    await message.channel.send(embed=embed)
                                    await user.send(f'{user}님 {message.guild.name}서버에 {reason} 사유로 __추방__ 되었습니다')
                                except:
                                    pass
                        except IndexError:
                            await makeembed4("형식이 틀린거같아요", "형식: 제토2 추방 <유저 맨션>&<사유>")
                        except:
                           await makeembed3("추방할 사람의 권한이 너무 높거나 그 유저가 서버에 없습니다.")
                    else:
                        await makeembed4("당신은 권한이 없어요","필요 권한 : 멤버 추방하기")
                else:
                    await makeembed4("제가 추방을 할 수 있는 권한을 가지고 있지 않아요","필요 권한 : 멤버 추방하기")

            elif message.content.startswith(f"제토2 차단"):
                if message.guild.get_member(client.user.id).guild_permissions.ban_members == True:
                    if message.author.guild_permissions.ban_members:
                        try:
                            try:
                                user = int(message.content.split('<@')[1].split('>')[0])
                            except:
                                user = int(message.content.split('<@!')[1].split('>')[0])
                            print(user)
                            if user == message.author.id:
                                await makeembed3("추방를 할수가 없는 유저입니다")
                            else:
                                try:
                                    reason = message.content.split('&')[1]
                                except:
                                    reason = "사유 없음"
                                    un = await client.fetch_user(user)
                                    await message.guild.ban(await client.fetch_user(user), reason=f"{reason}")
                                embed = discord.Embed(title=f"{un} 차단", color=discord.Colour.red(), timestamp=message.created_at)
                                embed.add_field(name=" 처리자", value=f"<@{message.author.id}> ({message.author})", inline = False)
                                embed.add_field(name=" 유저", value=f'<@{un.id}> ({un})', inline = False)
                                embed.add_field(name=" 정보", value=f'차단 사유:{reason}', inline = False)
                                embed.set_footer(text=f"{message.author}처리자", icon_url=message.author.avatar_url)
                                await message.channel.send(embed=embed)
                                await un.send(f'{un}님 {message.guild.name}서버에 {reason} 사유로 차단 되었습니다')
                        except IndexError:
                            await makeembed4("형식이 틀린거같아요","형식: 제토2 차단 <유저 맨션>&<사유>")
                        except Exception as ex:
                            await makeembed3(f"차단할 사람의 권한이 너무 높습니다.\n{ex}")
                    else:
                        await makeembed4("당신은 권한이 없어요!","필요 권한 : 멤버 차단하기")
                else:
                    await makeembed4("제가 차단을 할 수 있는 권한을 가지고 있지 않아요!","필요 권한 : 멤버 차단하기`")
            elif message.content.startswith("제토2 영한번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=ko&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "en", "target": "ko", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_us::flag_kr:번역된 문장',f':flag_us:영어```{text}```:flag_kr:한국어\n```{result}```')
    
    
            elif message.content.startswith("제토2 영일번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=ja&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "en", "target": "ja", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_us::flag_jp:번역된 문장',f':flag_us:영어```{text}```:flag_jp:일본어\n```{result}```')
    
    
            elif message.content.startswith("제토2 영중번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=en&target=zh-CN&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "en", "target": "zh-CN", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_us::flag_cn:번역된 문장',f':flag_us:영어```{text}```:flag_cn:중국어\n```{result}```')
    
    
            elif message.content.startswith("제토2 한영번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=en&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ko", "target": "en", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_kr::flag_us:번역된 문장',f':flag_kr:한국어```{text}```:flag_us:영어\n```{result}```')
    
    
            elif message.content.startswith("제토2 한일번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=ja&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ko", "target": "ja", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_kr::flag_jp:번역된 문장',f':flag_kr:한국어```{text}```:flag_jp:일본어\n```{result}```')

    
    
            elif message.content.startswith("제토2 한중번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=zh-CN&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ko", "target": "zh-CN", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_kr::flag_cn:번역된 문장',f':flag_kr:한국어```{text}```:flag_cn:중국어\n```{result}```')

            elif message.content.startswith("제토2 일한번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=ko&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ja", "target": "ko", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_jp::flag_kr:번역된 문장',f':flag_jp:일본어```{text}```:flag_kr:한국어\n```{result}```')
            
            elif message.content.startswith("제토2 일영번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=en&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ja", "target": "en", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_jp::flag_us:번역된 문장',f':flag_jp:일본어```{text}```:flag_us:영어\n```{result}```')
            
            elif message.content.startswith("제토2 일중번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ja&target=zh-CN&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ja", "target": "zh-CN", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_jp::flag_cn:번역된 문장',f':flag_jp:일본어```{text}```:flag_cn:중국어\n```{result}```')
            
            elif message.content.startswith("제토2 중일번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=ja&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "zh-CN", "target": "ja", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_cn::flag_jp:번역된 문장',f':flag_cn:중국어```{text}```:flag_jp:일본어\n```{result}```')

            elif message.content.startswith("제토2 중영번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=en-CN&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "zh-CN", "target": "en", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_cn::flag_us:번역된 문장',f':flag_cn:중국어```{text}```:flag_us:영어\n```{result}```')

            elif message.content.startswith("제토2 중한번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=zh-CN&target=ko-CN&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "zh-CN", "target": "ko", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_cn::flag_kr:번역된 문장',f':flag_cn:중국어```{text}```:flag_kr:한국어\n```{result}```')
            elif message.content.startswith("제토2 한태번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=ko&target=th&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "ko", "target": "th", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_kr::flag_th:번역된 문장',f':flag_kr:한국어```{text}```:flag_th:태국어\n```{result}```')
            elif message.content.startswith("제토2 태한번역"):
                channel = message.channel
                url="https://openapi.naver.com/v1/papago/n2mt?source=th&target=ko&text="
                text = message.content[9:]
                if text == "":
                    await makeembed3('번역할 내용를 입력해주세요')
                request_url = "https://openapi.naver.com/v1/papago/n2mt"
                headers= {"X-Naver-Client-Id": 토큰, "X-Naver-Client-Secret":토큰2}
                params = {"source": "th", "target": "ko", "text": text}
                response = requests.post(request_url, headers=headers, data=params)
                result = response.json()
                result = result['message']['result']['translatedText']
                await makeembed1(':flag_th::flag_kr:번역된 문장',f':flag_th:태국어```{text}```:flag_kr:한국어\n```{result}```')
            elif message.content.startswith("제토2 마크"):
                nickname = message.content[7:]
                channel = message.channel
                embed = discord.Embed(
                title = f'{nickname}님의 스킨',
                description = f'[[ 아바타 ]](https://minotar.net/helm/{nickname}/100.png) [[ 큐브 아바타 ]](https://minotar.net/cube/{nickname}/100.png) \n[[ 전신 ]](https://minotar.net/armor/body/{nickname}/100.png) [[ 반신 ]](https://minotar.net/armor/bust/{nickname}/100.png)\n[[ 스킨 다운로드 ]](https://minotar.net/download/{nickname})',
                color = 0xff00
               ).set_thumbnail(url = f"https://minotar.net/armor/bust/{nickname}/100.png")
                await message.channel.send(embed = embed)
            elif message.content.startswith("제토2 계산"):
                channel = message.channel
                math = message.content[7:30]
                if math == "":
                    await makeembed3('계산식를 입력해주세요')
                elif len(message.mentions) >= 1 or len(message.role_mentions) >= 1 or len(message.channel_mentions) >= 1:
                    await makeembed3('계산식이 올바르지 않습니다..')
                else:
                    mathtext = ""
                    allowed = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", "+", "-", "*", "/", "(", ")","^"]
                    for i in math:
                        if i in allowed:
                            mathtext += i
                        else:
                            mathtext += ""
                    try:
                        value = eval(mathtext)
                        await makeembed1(f'{mathtext}식의 결과',f'{str(value)}')
                    except:
                        await makeembed3('계산식이 올바르지 않습니다..')
            elif message.content.startswith("제토2 롤"):
                playerNickname = message.content[5:]
                """롤전적을 보여줍니다."""
                checkURLBool = urlopen(opggsummonersearch + quote(playerNickname))
                bs = BeautifulSoup(checkURLBool, 'html.parser')

                # 자유랭크 언랭은 뒤에 '?image=q_auto&v=1'표현이없다
                RankMedal = bs.findAll('img', {
                    'src': re.compile('\/\/[a-z]*\-[A-Za-z]*\.[A-Za-z]*\.[A-Za-z]*\/[A-Za-z]*\/[A-Za-z]*\/[a-z0-9_]*\.png')})
                # index 0 : Solo Rank
                # index 1 : Flexible 5v5 rank

                # for mostUsedChampion
                mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})

                # 솔랭, 자랭 둘다 배치가 안되어있는경우 -> 사용된 챔피언 자체가 없다. 즉 모스트 챔피언 메뉴를 넣을 필요가 없다.

                if len(playerNickname) == 1:
                    embed = discord.Embed(title="소환사 이름이 입력되지 않았습니다!", description="", color=0xff0000)
                    embed.add_field(name="Summoner name not entered",
                                    value="To use command !롤전적 : !롤전적 (Summoner Nickname)", inline=False)
                    await message.channel.send("Error : Incorrect command usage ", embed=embed)

                elif len(deleteTags(bs.findAll('h2', {'class': 'Title'}))) != 0:
                    embed = discord.Embed(title="존재하지 않는 소환사", description="", color=0xff0000)
                    embed.add_field(name="해당 닉네임의 소환사가 존재하지 않습니다.", value="소환사 이름을 확인해주세요", inline=False)
                    await message.channel.send("Error : Non existing Summoner ", embed=embed)
                else:
                    try:
                        # Scrape Summoner's Rank information
                        # [Solorank,Solorank Tier]
                        solorank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {'class': {'RankType', 'TierRank'}}))
                        # [Solorank LeaguePoint, Solorank W, Solorank L, Solorank Winratio]
                        solorank_Point_and_winratio = deleteTags(
                            bs.findAll('span', {'class': {'LeaguePoints', 'wins', 'losses', 'winratio'}}))
                        # [Flex 5:5 Rank,Flexrank Tier,Flextier leaguepoint + W/L,Flextier win ratio]
                        flexrank_Types_and_Tier_Info = deleteTags(bs.findAll('div', {
                            'class': {'sub-tier__rank-type', 'sub-tier__rank-tier', 'sub-tier__league-point',
                                    'sub-tier__gray-text'}}))
                        # ['Flextier W/L]
                        flexrank_Point_and_winratio = deleteTags(bs.findAll('span', {'class': {'sub-tier__gray-text'}}))

                        # embed.set_imag()는 하나만 들어갈수 있다.

                        # 솔랭, 자랭 둘다 배치 안되어있는 경우 -> 모스트 챔피언 출력 X
                        if len(solorank_Point_and_winratio) == 0 and len(flexrank_Point_and_winratio) == 0:
                            embed = discord.Embed(title="소환사 전적검색", description="", color=0xff00)
                            embed.add_field(name="Ranked Solo : Unranked", value="Unranked", inline=False)
                            embed.add_field(name="Flex 5:5 Rank : Unranked", value="Unranked", inline=False)
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                            await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)

                        # 솔로랭크 기록이 없는경우
                        elif len(solorank_Point_and_winratio) == 0:

                            # most Used Champion Information : Champion Name, KDA, Win Rate
                            mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                            mostUsedChampion = mostUsedChampion.a.text.strip()
                            mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                            mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                            mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                            mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                            FlexRankTier = flexrank_Types_and_Tier_Info[0] + ' : ' + flexrank_Types_and_Tier_Info[1]
                            FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " /" + flexrank_Types_and_Tier_Info[-1]
                            embed = discord.Embed(title="소환사 전적검색", description="", color=0xff00)
                            embed.add_field(name="Ranked Solo : Unranked", value="Unranked", inline=False)
                            embed.add_field(name=FlexRankTier, value=FlexRankPointAndWinRatio, inline=False)
                            embed.add_field(name="Most Used Champion : " + mostUsedChampion,
                                            value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                            inline=False)
                            embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                            await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)

                        # 자유랭크 기록이 없는경우
                        elif len(flexrank_Point_and_winratio) == 0:

                            # most Used Champion Information : Champion Name, KDA, Win Rate
                            mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                            mostUsedChampion = mostUsedChampion.a.text.strip()
                            mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                            mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                            mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                            mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                            SoloRankTier = solorank_Types_and_Tier_Info[0] + ' : ' + solorank_Types_and_Tier_Info[1]
                            SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + "/ " + solorank_Point_and_winratio[
                                1] + " " + solorank_Point_and_winratio[2] + " /" + solorank_Point_and_winratio[3]
                            embed = discord.Embed(title="소환사 전적검색", description="", color=0xff00)
                            embed.add_field(name=SoloRankTier, value=SoloRankPointAndWinRatio, inline=False)
                            embed.add_field(name="Flex 5:5 Rank : Unranked", value="Unranked", inline=False)
                            embed.add_field(name="Most Used Champion : " + mostUsedChampion,
                                            value="KDA : " + mostUsedChampionKDA + " / " + "WinRate : " + mostUsedChampionWinRate,
                                            inline=False)
                            embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                            await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)
                        # 두가지 유형의 랭크 모두 완료된사람
                        else:
                            # 더 높은 티어를 thumbnail에 안착
                            solorankmedal = RankMedal[0]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')
                            flexrankmedal = RankMedal[1]['src'].split('/')[-1].split('?')[0].split('.')[0].split('_')

                             # Make State
                            SoloRankTier = solorank_Types_and_Tier_Info[0] + ' : ' + solorank_Types_and_Tier_Info[1]
                            SoloRankPointAndWinRatio = solorank_Point_and_winratio[0] + "/ " + solorank_Point_and_winratio[
                                1] + " " + solorank_Point_and_winratio[2] + " /" + solorank_Point_and_winratio[3]
                            FlexRankTier = flexrank_Types_and_Tier_Info[0] + ' : ' + flexrank_Types_and_Tier_Info[1]
                            FlexRankPointAndWinRatio = flexrank_Types_and_Tier_Info[2] + " /" + flexrank_Types_and_Tier_Info[-1]

                            # most Used Champion Information : Champion Name, KDA, Win Rate
                            mostUsedChampion = bs.find('div', {'class': 'ChampionName'})
                            mostUsedChampion = mostUsedChampion.a.text.strip()
                            mostUsedChampionKDA = bs.find('span', {'class': 'KDA'})
                            mostUsedChampionKDA = mostUsedChampionKDA.text.split(':')[0]
                            mostUsedChampionWinRate = bs.find('div', {'class': "Played"})
                            mostUsedChampionWinRate = mostUsedChampionWinRate.div.text.strip()

                            cmpTier = tierCompare(solorankmedal[0], flexrankmedal[0])
                            embed = discord.Embed(title="소환사 전적검색", description="", color=0xff00)
                            embed.add_field(name=SoloRankTier, value=SoloRankPointAndWinRatio, inline=False)
                            embed.add_field(name=FlexRankTier, value=FlexRankPointAndWinRatio, inline=False)
                            embed.add_field(name="Most Used Champion : " + mostUsedChampion,
                                            value="KDA : " + mostUsedChampionKDA + " / " + " WinRate : " + mostUsedChampionWinRate,
                                            inline=False)
                            if cmpTier == 0:
                                embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                            elif cmpTier == 1:
                                embed.set_thumbnail(url='https:' + RankMedal[1]['src'])
                            else:
                                if solorankmedal[1] > flexrankmedal[1]:
                                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                                elif solorankmedal[1] < flexrankmedal[1]:
                                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                                else:
                                    embed.set_thumbnail(url='https:' + RankMedal[0]['src'])
                            await message.channel.send("소환사 " + playerNickname + "님의 전적", embed=embed)
                    except HTTPError as e:
                        embed = discord.Embed(title="소환사 전적검색 실패", description="", color=discord.Colour.red())
                        embed.add_field(name="", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
                        await message.channel.send("Wrong Summoner Nickname")

                    except UnicodeEncodeError as e:
                        embed = discord.Embed(title="소환사 전적검색 실패", description="", color=discord.Colour.red())
                        embed.add_field(name="???", value="올바르지 않은 소환사 이름입니다. 다시 확인해주세요!", inline=False)
                        await message.channel.send("Wrong Summoner Nickname", embed=embed)
            elif message.content.startswith("제토2 레식전적"):
                name = message.content[8:]
                """레식 전적을 보여줍니다"""
                playerNickname = name
                html = requests.get(playerSite + playerNickname + '/pc/').text
                bs = BeautifulSoup(html, 'html.parser')

                # 한번에 검색 안되는 경우에는 해당 반환 리스트의 길이 존재. -> bs.find('div',{'class' : 'results'}

                if bs.find('div', {'class': 'results'}) == None:
                    # Get latest season's Rank information
                    latestSeason = bs.find('div', {'class': re.compile('season\-rank operation\_[A-Za-z_]*')})

                    # if player nickname not entered
                    if len(name) == 1:
                        embed = discord.Embed(title="플레이어 이름이 입력되지 않았습니다", description="", color=0xff0000)
                        embed.add_field(name="Error : Player name not entered" + playerNickname,
                                        value="To use command : 제토2 레식전적 (nickname)")
                        await message.channel.send("Error : Player name not entered ", embed=embed)

                    # search if it's empty page
                    elif latestSeason == None:
                        embed = discord.Embed(title="해당 이름을 가진 플레이어가 존재하지않습니다.", description="", color=0xff0000)
                        embed.add_field(name="Error : Can't find player name " + playerNickname,
                                        value="Please check player's nickname")
                        await message.channel.send("Error : Can't find player name " + playerNickname, embed=embed)

                    # Command entered well
                    else:
                        # r6stats profile image
                        r6Profile = bs.find('div', {'class': 'main-logo'}).img['src']

                        # player level
                        playerLevel = bs.find('span', {'class': 'quick-info__value'}).text.strip()

                        RankStats = bs.find('div', {'class': 'card stat-card block__ranked horizontal'}).findAll('span', {
                                        'class': 'stat-count'})
                        # Get text from <span> values
                        for info in range(len(RankStats)):
                            RankStats[info] = RankStats[info].text.strip()
                        # value of variable RankStats : [Timeplayed, Match Played,kills per matchm, kills,death, KDA Rate,Wins,Losses,W/L Rate]

                        # latest season tier medal
                        lastestSeasonRankMedalLocation = latestSeason.div.img['src']
                        # latest Season tier
                        lastestSeasonRankTier = latestSeason.div.img['alt']
                        # latest season operation name
                        OperationName = latestSeason.find('div', {'class': 'meta-wrapper'}).find('div', {
                            'class': 'operation-title'}).text.strip()
                        # latest season Ranking
                        latestSeasonRanking = latestSeason.find('div', {'class': 'rankings-wrapper'}).find('span', {
                            'class': 'ranking'})

                        # if player not ranked, span has class not ranked if ranked span get class ranking
                        if latestSeasonRanking == None:
                            latestSeasonRanking = bs.find('span', {'class': 'not-ranked'}).text.upper()
                        else:
                            latestSeasonRanking = latestSeasonRanking.text

                        # Add player's MMR Rank MMR Information
                        playerInfoMenus = bs.find('a', {'class': 'player-tabs__season_stats'})['href']
                        mmrMenu = r6URL + playerInfoMenus
                        html = requests.get(mmrMenu).text
                        bs = BeautifulSoup(html, 'html.parser')

                        # recent season rank box
                        # Rank show in purpose : America - Europe - Asia. This code only support Asia server's MMR
                        getElements = bs.find('div', {
                            'class': 'card__content'})  # first elements with class 'card__contet is latest season content box

                        for ckAsia in getElements.findAll('div', {'class': 'season-stat--region'}):
                            checkRegion = ckAsia.find('div', {'class': 'season-stat--region-title'}).text
                            if checkRegion == "Asia":
                                getElements = ckAsia
                                break
                            else:
                                pass

                        # Player's Tier Information
                        latestSeasonTier = getElements.find('img')['alt']
                        # MMR Datas Info -> [Win,Losses,Abandon,Max,W/L,MMR]
                        mmrDatas = []
                        for dt in getElements.findAll('span', {'class': 'season-stat--region-stats__stat'}):
                            mmrDatas.append(dt.text)

                        embed = discord.Embed(title="r6stats에서 Rainbow Six Siege 플레이어 검색", description="",
                                                color=0x5CD1E5)
                        embed.add_field(name="r6stats에서 플레이어 검색", value=playerSite + playerNickname + '/pc/',
                                        inline=False)
                        embed.add_field(name="플레이어의 기본 정보",
                                        value="Ranking : #" + latestSeasonRanking + " | " + "Level : " + playerLevel,
                                        inline=False)
                        embed.add_field(name="최신 시즌 정보 | Operation : " + OperationName,
                                        value=
                                        "Tier(Asia) : " + latestSeasonTier + " | W/L : " + mmrDatas[0] + "/" + mmrDatas[
                                        1] + " | " + "MMR(Asia) : " + mmrDatas[-1],
                                        inline=False)

                        embed.add_field(name="총플레이시간", value=RankStats[0], inline=True)
                        embed.add_field(name="경기한수", value=RankStats[1], inline=True)
                        embed.add_field(name="경기당 처치", value=RankStats[2], inline=True)
                        embed.add_field(name="총킬", value=RankStats[3], inline=True)
                        embed.add_field(name="총사망", value=RankStats[4], inline=True)
                        embed.add_field(name="K/D 비율", value=RankStats[5], inline=True)
                        embed.add_field(name="우승", value=RankStats[6], inline=True)
                        embed.add_field(name="페베", value=RankStats[7], inline=True)
                        embed.add_field(name="W/L 비율", value=RankStats[8], inline=True)
                        embed.set_thumbnail(url=r6URL + r6Profile)
                        await message.channel.send("Player " + playerNickname + "'s stats search", embed=embed)
                else:
                    searchLink = bs.find('a', {'class': 'result'})
                    if searchLink == None:
                        embed = discord.Embed(title="해당 이름을 가진 플레이어가 존재하지않습니다.", description="", color=0xff0000)
                        embed.add_field(name="Error : Can't find player name " + playerNickname,
                                        value="Please check player's nickname")
                        await message.channel.send("Error : Can't find player name " + playerNickname, embed=embed)
                    else:
                        searchLink = r6URL + searchLink['href']
                        html = requests.get(searchLink).text
                        bs = BeautifulSoup(html, 'html.parser')
                        # Get latest season's Rank information
                        latestSeason = bs.findAll('div', {'class': re.compile('season\-rank operation\_[A-Za-z_]*')})[0]

                        # if player nickname not entered
                        if len(name) == 1:
                            embed = discord.Embed(title="플레이어 이름이 입력되지 않았습니다", description="", color=0xff0000)
                            embed.add_field(name="Error : Player name not entered" + playerNickname,
                                            value="To use command : !레식전적 (nickname)")
                            await message.channel.send("Error : Player name not entered ", embed=embed)

                        # search if it's empty page
                        elif latestSeason == None:
                            embed = discord.Embed(title="해당 이름을 가진 플레이어가 존재하지않습니다.", description="", color=0xff0000)
                            embed.add_field(name="Error : Can't find player name " + playerNickname,
                                            value="Please check player's nickname")
                            await message.channel.send("Error : Can't find player name " + playerNickname, embed=embed)

                        # Command entered well
                        else:

                            # r6stats profile image
                            r6Profile = bs.find('div', {'class': 'main-logo'}).img['src']

                            # player level
                            playerLevel = bs.find('span', {'class': 'quick-info__value'}).text.strip()

                            RankStats = bs.find('div', {'class': 'card stat-card block__ranked horizontal'}).findAll('span', {
                                'class': 'stat-count'})
                           # Get text from <span> values
                            for info in range(len(RankStats)):
                                RankStats[info] = RankStats[info].text.strip()
                            # value of variable RankStats : [Timeplayed, Match Played,kills per matchm, kills,death, KDA Rate,Wins,Losses,W/L Rate]

                            # latest season tier medal
                            lastestSeasonRankMedalLocation = latestSeason.div.img['src']
                            # latest Season tier
                            lastestSeasonRankTier = latestSeason.div.img['alt']
                            # latest season operation name
                            OperationName = latestSeason.find('div', {'class': 'meta-wrapper'}).find('div', {
                                'class': 'operation-title'}).text.strip()
                            # latest season Ranking
                            latestSeasonRanking = latestSeason.find('div', {'class': 'rankings-wrapper'}).find('span', {
                                'class': 'ranking'})

                            # if player not ranked, span has class not ranked if ranked span get class ranking
                            if latestSeasonRanking == None:
                                latestSeasonRanking = bs.find('span', {'class': 'not-ranked'}).text.upper()
                            else:
                                latestSeasonRanking = latestSeasonRanking.text

                            # Add player's MMR Rank MMR Information
                            playerInfoMenus = bs.find('a', {'class': 'player-tabs__season_stats'})['href']
                            mmrMenu = r6URL + playerInfoMenus
                            html = requests.get(mmrMenu).text
                            bs = BeautifulSoup(html, 'html.parser')

                            # recent season rank box
                            # Rank show in purpose : America - Europe - Asia. This code only support Asia server's MMR
                            getElements = bs.find('div', {
                                'class': 'card__content'})  # first elements with class 'card__contet is latest season content box

                            for ckAsia in getElements.findAll('div', {'class': 'season-stat--region'}):
                                checkRegion = ckAsia.find('div', {'class': 'season-stat--region-title'}).text
                                if checkRegion == "Asia":
                                    getElements = ckAsia
                                    break
                                else:
                                    pass
                            # Player's Tier Information
                            latestSeasonTier = getElements.find('img')['alt']
                            # MMR Datas Info -> [Win,Losses,Abandon,Max,W/L,MMR]
                            mmrDatas = []
                            for dt in getElements.findAll('span', {'class': 'season-stat--region-stats__stat'}):
                                mmrDatas.append(dt.text)

                            embed = discord.Embed(title="r6stats에서 Rainbow Six Siege 플레이어 검색", description="",
                                                color=0x5CD1E5)
                            embed.add_field(name="r6stats에서 플레이어 검색", value=searchLink,
                                            inline=False)
                            embed.add_field(name="플레이어의 기본 정보",
                                            value="Ranking : #" + latestSeasonRanking + " | " + "Level : " + playerLevel,
                                            inline=False)
                            embed.add_field(name="최신 시즌 정보 | Operation : " + OperationName,
                                            value=
                                            "Tier(Asia) : " + latestSeasonTier + " | W/L : " + mmrDatas[0] + "/" + mmrDatas[
                                                1] + " | " + "MMR(Asia) : " + mmrDatas[-1],
                                            inline=False)

                            embed.add_field(name="총플레이시간", value=RankStats[0], inline=True)
                            embed.add_field(name="경기한수", value=RankStats[1], inline=True)
                            embed.add_field(name="경기당 처치", value=RankStats[2], inline=True)
                            embed.add_field(name="총킬", value=RankStats[3], inline=True)
                            embed.add_field(name="총사망", value=RankStats[4], inline=True)
                            embed.add_field(name="K/D 비율", value=RankStats[5], inline=True)
                            embed.add_field(name="우승", value=RankStats[6], inline=True)
                            embed.add_field(name="패배", value=RankStats[7], inline=True)
                            embed.add_field(name="W/L 비율", value=RankStats[8], inline=True)
                            embed.set_thumbnail(url=r6URL + r6Profile)
                            await message.channel.send("Player " + playerNickname + "'s stats search", embed=embed)
            elif message.content.startswith("제토2 블로그"):
                query = message.content[7:]
                channel = message.channel
                req = requests.get(("https://search.naver.com/search.naver?where=post&sm=tab_jum&query="+query))
                source = req.text
                soup = BeautifulSoup(source, "html.parser")
                last = ""
                try:
                    for i in range(1, 10):
                        titles = soup.select("#sp_blog_"+str(i)+" > dl > dt > a")[0].text
                        links = soup.select("#sp_blog_"+str(i)+" > dl > dd.txt_block > span > a.url")[0].text
                        final = ("["+titles+"](https://"+links+")\n")
                        last += final
                    await makeembed1(f'{query}에 대한 네이버 블로그 검색결과', f'{last}')
                except:
                    await makeembed3(f'{query}에 대한 네이버 블로그 검색결과가 없습니다.')
            elif message.content.startswith("제토2 매직8볼"):
                text = message.content[9:]
                channel = message.channel
                answer = random.choice(["절대 안돼.", "마음대로 해.", "안돼. 절대 하지마.", "그래.", "하든지 말든지.", "절대 안돼.", "안돼. 절대 하지마.", "절대 안돼.", "안돼. 절대 하지마."])
                await makeembed1(f'{text}',f'{answer}')
            elif message.content  ==  '제토2 주인' or message.content  ==  '제토2 개발자':
                embed = discord.Embed(title=f"{client.user.name} 개발자", description="제토2 주인 정보입니다.", color=0xff00, timestamp=message.created_at)
                embed.add_field(name="개발자", value="<@534214957110394881>님", inline=True)
                embed.set_thumbnail(url ="https://cdn.discordapp.com/attachments/704709508001169438/710051187206127636/SPOILER_KakaoTalk_20200402_000010957.png")
                embed.add_field(name="도움", value="<@524515155254444032>님", inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                await makeembed2('관리자님 에게 힘주기', '[하트❤ 주로가기](https://koreanbots.dev/bots/666879942667141128)\n[vote(투표📩) 하러 가기](https://top.gg/bot/666879942667141128)')
            elif  message.content.startswith('제토2 놀아줘') or  message.content.startswith('제토2 문제'):
                a = ['헤어 나올 수 없는 곳은?','본인이 직접 만든 총은?','선풍기에는 회전하는 날개에 손이 다치지 않도록 겉에 철망을 씌우는데,이 철망을 벗겨낸 선풍기는?'
                ,'오리를 생으로 먹으면?','소가 감전해서 죽으면?','소랑 개랑 부딧히면?','벌을 잡았다 어디서 잡았을까?','아이를 셋 날은 계획을 세우면?'
                ,'만나면 서로 인사하지 않은걸 뭐라고 할까요?','세상에서 가장 더러운 얼음은?','돈을 잘버는 개를 뭐라고 할까요?','소고기를 안넣고 끓인 국은?',
                '파스에 불이붙으면?','트랜스포머가 여자친구가 없는 이유는?','유럽인의 식사를 뭐라고 할까요?','한의사가 갖춰야할 직업관은?','모래 사장에 사는 마녀를 뭐라 부를까요?','소가 구걸하면?','호랑이들이 배가고프면?'
                ,'불이났는데 소가 가만히 보고만 있는것은?','모자를 때릴수있는 도구','경상도 쥐가 개그를 쳤는데 아무 반응 없을 때 하는말은?','베를린 사람이 주는 음식은 함부러 먹으면 안된다 왜그럴까?'
                ,'친구들과 술집에 가서, 계산 할때 추는 춤은?','곤충끼리 부딪히면?','딸기가 도망가면?','자동차가 우는나라','엄마와 아들이건다가 넘어지면 뭐라할까요','코가 긴사람들이 하는 스포츠는?','차를 갑자기 발로 차면',
                '눈과 구름을 자르는 칼은?','물을 자르면?','D가 나무를 캐면?','배렛나루가 없는사람이 카톡을 못하는 이유는 뭘까요?','사람들이그늘에 있는 이유는?','흑인이 자기소개 하면?','머리를 감을떄 어디부터 감을까?']
                c = random.choice(a)
                await message.channel.send(""+c+"")
                msg=await message.channel.send('두근두근두근 <a:discord:707800624737157120>')
                await asyncio.sleep(5)
                await msg.delete()

                if c == '머리를 감을떄 어디부터 감을까?':
                 if c == '머리를 감을떄 어디부터 감을까?':
                    await message.channel.send("`눈`\nㅋㅎㅋㅎ")
                if c == '흑인이 자기소개 하면?':
                    await message.channel.send("`암흑`\nㅋㅎㅋㅎ")
                if c == '사람들이그늘에 있는 이유는?':
                    await message.channel.send("`해피하려고`\nㅋㅎㅋㅎ")
                if c == '배렛나루가 없는사람이 카톡을 못하는 이유는 뭘까요?':
                    await message.channel.send("`배털이 없어서`\nㅋㅎㅋㅎ")
                if c == 'D가 나무를 캐면?':
                    await message.channel.send("`목캔드`\nㅋㅎㅋㅎ")
                if c == '물을 자르면?':
                    await message.channel.send("`수컷`\nㅋㅎㅋㅎ")
                if c == '눈과 구름을 자르는 칼은?':
                    await message.channel.send("`설운도`\nㅋㅎㅋㅎ")
                if c == '가장 믿음직스러운 오리는?':
                    await message.channel.send("`카놀라유`\nㅋㅎㅋㅎ")
                if c == '차를 갑자기 발로 차면':
                    await message.channel.send("`카놀라유`\nㅋㅎㅋㅎ")
                if c == '코가 긴사람들이 하는 스포츠는?':
                    await message.channel.send("`미어캣`\nㅋㅎㅋㅎ")
                if c == '엄마와 아들이건다가 넘어지면 뭐라할까요':
                    await message.channel.send("`모자이크`\nㅋㅎㅋㅎ")
                if c == '자동차가 우는나라':
                    await message.channel.send("`앙카`\nㅋㅎㅋㅎ")
                if c == '딸기가 도망가면?':
                    await message.channel.send("`딸기 쨈`\nㅋㅎㅋㅎ")
                if c == '곤충끼리 부딪히면?':
                    await message.channel.send("`충돌`\nㅋㅎㅋㅎ")
                if c == '친구들과 술집에 가서, 계산 할때 추는 춤은?':
                    await message.channel.send("`주춤주춤`\nㅋㅎㅋㅎ")
                if c == '베를린 사람이 주는 음식은 함부러 먹으면 안된다 왜그럴까?':
                    await message.channel.send("`독일 수도....`\nㅋㅎㅋㅎ")
                if c == '경상도 쥐가 개그를 쳤는데 아무 반응 없을 때 하는말은?':
                    await message.channel.send("`마! 우스라고(마우스 라고)`\nㅋㅎㅋㅎ")
                if c == '모자를 때릴수있는 도구':
                    await message.channel.send("`캡쳐도구`\nㅋㅎㅋㅎ")
                if c == '불이났는데 소가 가만히 보고만 있는것은?':
                    await message.channel.send("`소방관`\nㅋㅎㅋㅎ")
                if c == '호랑이들이 배가고프면?':
                    await message.channel.send("`기아타이거즈`\nㅋㅎㅋㅎ")
                if c == '소가 구걸하면?':
                    await message.channel.send("`우거지`\nㅋㅎㅋㅎ")
                if c == '모래 사장에 사는 마녀를 뭐라 부를까요?':
                    await message.channel.send("`샌드위치`\nㅋㅎㅋㅎ")
                if c == '한의사가 갖춰야할 직업관은?':
                    await message.channel.send("`인생은 한방이다`\nㅋㅎㅋㅎ")
                if c == '유럽인의 식사를 뭐라고 할까요?':
                    await message.channel.send("`이유식(EU식)`\nㅋㅎㅋㅎ")
                if c == '트랜스포머가 여자친구가 없는 이유는?':
                    await message.channel.send("`차여서`\nㅋㅎㅋㅎ")
                if c == '파스에 불이붙으면?':
                    await message.channel.send("`파스타`\nㅋㅎㅋㅎ")
                if c == '헤어 나올 수 없는 곳은?':
                    await message.channel.send("`대머리`\nㅋㅎㅋㅎ")
                if c == '본인이 직접 만든 총은?':
                    await message.channel.send("`손수건`\nㅋㅎㅋㅎ")
                if c == '선풍기에는 회전하는 날개에 손이 다치지 않도록 겉에 철망을 씌우는데,이 철망을 벗겨낸 선풍기는?':
                    await message.channel.send("`깐풍기`\nㅋㅎㅋㅎ") 
                if c == '오리를 생으로 먹으면?':
                    await message.channel.send("`우사인볼트`\nㅋㅎㅋㅎ")
                if c == '소가 감전해서 죽으면?':
                    await message.channel.send("`회오리`\nㅋㅎㅋㅎ")
                if c == '소랑 개랑 부딧히면?':
                    await message.channel.send("`소개팅`\nㅋㅎㅋㅎ")
                if c == '벌을 잡았다 어디서 잡았을까?':
                    await message.channel.send("`갯벌(get 벌)`\nㅋㅎㅋㅎ")
                if c == '아이를 셋 날은 계획을 세우면?':
                    await message.channel.send("`미래에셋`\nㅋㅎㅋㅎ")
                if c == '만나면 서로 인사하지 않은걸 뭐라고 할까요?':
                    await message.channel.send("`하의실종(HI 실종)`\nㅋㅎㅋㅎ")
                if c == '세상에서 가장 더러운 얼음은?':
                    await message.channel.send("`오무라이스(오물 아이스)`\nㅋㅎㅋㅎ")
                if c == '돈을 잘버는 개를 뭐라고 할까요?':
                    await message.channel.send("`번개`\nㅋㅎㅋㅎ")
                if c == '소고기를 안넣고 끓인 국은?':
                    await message.channel.send("`소고기 무국`\nㅋㅎㅋㅎ")
            elif message.content.startswith('제토2 건의') or  message.content.startswith('제토2 문의'):
                learn = message.content[7:]
                if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                    await makeembed("건의 메시지를 입력해주세요")
                    return
                if "@everyone" in learn or "@here" in learn:
                    embed = discord.Embed(
                        title="경고",
                        description="`@everyone`이나 `@here`은 다른 관리자에게 피해를 줄 수 있어요.\n사용을 제한할께요!",
                    )
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                    return
                else:
                    try:
                        embed = discord.Embed(title="건의 기능",color=0xff00, timestamp=message.created_at)
                        embed.set_thumbnail(url=message.author.avatar_url)
                        embed.add_field(name=f'{message.author}({message.author.id})의 건의', value=f'{learn}')
                    except IndexError:
                        await message.channel.send(f"건의 메시지를 입력해주세요")
                        return
                    m = await message.channel.send(f"건의내용: **{learn}**\n 라고 발신 하겠습니까?")
                    await m.add_reaction('<a:yes:707786803414958100>')
                    await m.add_reaction('<a:no:707786855143309370>')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['<a:yes:707786803414958100>', '<a:no:707786855143309370>'])
                except asyncio.TimeoutError:
                    await makeembed3('시간이 초과되었습니다.')
                else:
                    if str(reaction.emoji) == "<a:no:707786855143309370>":
                        await makeembed3("전송 안할게요^^")
                        await asyncio.sleep(2.5)
                        await m.delete()
                    elif str(reaction.emoji) == "<a:yes:707786803414958100>":
                        author=message.guild.get_member(534214957110394881)
                        await client.get_channel(int(683950964050624513)).send(embed=embed)
                        await client.get_channel(int(723715396292837506)).send(embed=embed)
                        webhook = 'https://discordapp.com/api/webhooks/728136224673366066/miYwTDArZLTqcZ0cb0l_8Ei8POmUyHO8DzpFrY5_eLaiCc6GAdedaETabXobb1ayLROZ'
                        requests.post(webhook, {'content':f'{message.author}({message.author.id})님이 건의를 입니다!\n > 건의내용: {str(learn)}'})
                        await author.send(embed=embed)
                        await message.delete()
                        embed = discord.Embed(title="건의 전송", color=0xff00, timestamp=message.created_at)
                        embed.add_field(name="건의", value="건의 성공적 관리자 한테 전달됨 <a:yes:707786803414958100>", inline=True)
                        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                        embed.set_footer(text=f"{message.author}님의 건의", icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                        await asyncio.sleep(2.5)
                        await m.delete()
            elif message.content.startswith(f"제토2 공지"):
                if message.author.id in heimteam:
                    if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                        await makeembed("공지 메시지를 입력해주세요")
                        return
                    try:
                        msg = message.content[7:]
                        oksv = 0
                        embed = discord.Embed(
                            title = msg.split('&')[0],
                            description = msg.split('&')[1] + f"\n\n이 채널에 공지가 오기 싫다면 `봇-공지` 채널을 만들어주세요!\n[제토2 초대하기](https://discord.com/oauth2/authorize?client_id=666879942667141128&scope=bot&permissions=268706022)\n[제토봇 포럼](https://discord.gg/SC8hE25)\n[팀SB 공식 포럼](https://discord.gg/c9daxpF)\n[제토2 하트 누르기](https://koreanbots.dev/bots/666879942667141128)",
                            colour = 0x00f000,
                            timestamp = message.created_at
                        ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - 인증됨') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                        embed.set_thumbnail(url = client.user.avatar_url)
                    except IndexError:
                        await message.channel.send(f"형식이 틀렸습니다. ``제토2 공지 <제목>&<내용>``으로 다시 시도해보세요!")
                        return
                    m = await message.channel.send("아래와 같이 공지가 발신됩니다!", embed=embed)
                    await m.add_reaction('<a:yes:707786803414958100>')
                    await m.add_reaction('<a:no:707786855143309370>')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['<a:yes:707786803414958100>', '<a:no:707786855143309370>'])
                    except asyncio.TimeoutError:
                        await makeembed3('시간이 초과되었습니다.')
                    else:
                        if str(reaction.emoji) == "<a:no:707786855143309370>":
                            await makeembed3('발신 안할게요..')
                            await asyncio.sleep(2.5)
                            await m.delete()
                        elif str(reaction.emoji) == "<a:yes:707786803414958100>":
                            n=await message.channel.send("공지 발신중입니다....\n잠시만 기다려주세요")
                            for i in client.guilds:
                                arr = [0]
                                alla = False
                                flag = True
                                z = 0
                                for j in i.channels:
                                    arr.append(j.id)
                                    z+=1
                                    if "제토2-봇-공지" in j.name or"봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "봇ㆍ공지" in j.name:
                                        if str(j.type)=='text':
                                            try:
                                                oksv += 1
                                                await j.send(embed=embed)
                                                alla = True
                                            except:
                                                pass
                                            break
                                if alla==False:
                                    try:
                                        chan=i.channels[1]
                                    except:
                                        pass
                                    if str(chan.type)=='text':
                                        try:
                                            oksv += 1
                                            await chan.send(embed=embed)
                                        except:
                                            pass
                            await message.channel.send(f'<a:yes:707786803414958100> 공지 발신 완료 <a:yes:707786803414958100>\n\n{len(client.guilds)}개의 서버 중 {oksv}개의 서버에 발신 완료<a:yes:707786803414958100>, {len(client.guilds) - oksv}개의 서버에 발신 실패<a:no:707786855143309370>')
                            await asyncio.sleep(2.5)
                            await m.delete()
                            await n.delete()
                else:
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 컴파일'):
                if message.author.id in owner:
                    a=message.content[7:]
                    if a == "":
                        await makeembed('컴파일 내용을 입력해주세요')
                    try:
                        msg=await message.channel.send(embed=discord.Embed(color=0x2F3136, title="evaling...",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
evaling...
```"""))
                        aa=await eval(a)
                    except Exception as e:
                        await msg.edit(embed=discord.Embed(color=0x2F3136, title="eval",description=f"""📥INPUT📥
                
```py
{a}          
```
📤OUTPUT📤
```py
{e}
```"""))

                        try:
                            aa = eval(a)
                        except Exception as e:
                            await msg.edit(embed=discord.Embed(color=0x2F3136, title="eval",description=f"""📥INPUT📥
                
```py
{a}
```
📤OUTPUT📤
```py
{e}
```"""))

                        else:
                            await msg.edit(embed=discord.Embed(color=0x2F3136, title=f"eval",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
{aa}
```""")) 

                    else:
                        await msg.edit(embed=discord.Embed(color=0x2F3136, title="eval",description=f"""📥INPUT📥
```py
{a}
```
📤OUTPUT📤
```py
{aa}
```"""))
                else:
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)

            elif message.content.startswith(f"제토2 eval"):
                if message.author.id in owner:
                    if str(message.content[9:]) == '' or str(message.content[9:]) == ' ':
                        await makeembed("공지 메시지를 입력해주세요")
                        return
                    try:
                        cmd=message.content[9:]
                        fn_name = "_eval_expr"

                        cmd = cmd.strip("` ")

                        # add a layer of indentation
                        cmd = "\n".join(f"    {i}" for i in cmd.splitlines())

                        # wrap in async def body
                        body = f"async def {fn_name}():\n{cmd}"

                        parsed = ast.parse(body)
                        body = parsed.body[0].body

                        insert_returns(body)

                        env = {
                            'client': client,
                            'discord': discord,
                            'message': message,
                            '__import__': __import__
                        }
                        exec(compile(parsed, filename="<ast>", mode="exec"), env)

                        result = (await eval(f"{fn_name}()", env))
                        embed=discord.Embed(title="EVAL")
                        embed.add_field(name="Input (들어가는 내용)", value=f"{cmd}",inline=False)
                        embed.add_field(name="Output (나오는 내용)", value=f"{result}",inline=False)
                        embed.add_field(name="Type (타입)",value=f"{type(result)}",inline=False)
                        embed.add_field(name="Latency (지연시간)",value=str((datetime.datetime.now()-message.created_at)*1000).split(":")[2],inline=False)
                        await message.channel.send(embed=embed)
                            

                    except Exception as e:
                        await message.channel.send(e)

            elif message.content == '제토2 초대':
                embed=discord.Embed(title=f"{client.user.name} 추가 링크입니다.", url="https://discord.com/oauth2/authorize?client_id=666879942667141128&scope=bot&permissions=268706022",colour=0xff00)
                embed.set_author(name=f"{client.user.name}", url="https://discord.com/oauth2/authorize?client_id=666879942667141128&scope=bot&permissions=268706022", icon_url="https://cdn.discordapp.com/avatars/666879942667141128/4f04de54a2a2d6102d43ce4ef30592f7.webp?size=1024")
                await message.channel.send(embed=embed)
            elif message.content == '제토2 이용약관':
                await makeembed1('이용약관', '[제토2 이용약관](https://zetto2bot.netlify.app/privacy-policy.html)')
            elif message.content == '제토2 공식서버':
                embed=discord.Embed(title=f"{client.user.name} 공식서버 링크입니다", url="https://discordapp.com/invite/SC8hE25",colour=0xff00)
                embed.set_author(name="제토봇 포럼( Zettobot Forum)", url="https://discordapp.com/invite/SC8hE25", icon_url="https://cdn.discordapp.com/icons/683946140764209177/237d470e10ed512c22ab929ba2bcde24.png")
                await message.channel.send(embed=embed)
            elif message.content == '제토2 사이트':
                embed=discord.Embed(title=f"{client.user.name} 사이트 링크입니다.", url="https://zetto2bot.netlify.app/index.html",colour=0xff00)
                embed.set_author(name=f"{client.user.name}", url="https://zetto2bot.netlify.app/index.html", icon_url="https://cdn.discordapp.com/avatars/666879942667141128/4f04de54a2a2d6102d43ce4ef30592f7.webp?size=1024")
                await message.channel.send(embed=embed)
            elif message.content  == '제토2 핑':
                ping= round(client.latency * 1000)
                if ping >= 0 and ping <= 100:
                    pings = "🔵아주 좋음"
                    embed = discord.Embed(title=f" 퐁🏓",color=0x00e2ff, timestamp=message.created_at)
                    embed.add_field(name="현재핑", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
                    await message.channel.send(embed=embed)
                elif ping >= 101 and ping <= 200:
                    pings = "🟢 좋음" 
                    embed = discord.Embed(title=f" 퐁🏓",color=0x00ff24, timestamp=message.created_at)
                    embed.add_field(name="현재핑", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
                    await message.channel.send(embed=embed)
                elif ping >= 201 and ping <= 500:
                    pings = "🟡 보통"
                    embed = discord.Embed(title=f" 퐁🏓",color=0xfeff0e, timestamp=message.created_at)
                    embed.add_field(name="현재핑", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
                    await message.channel.send(embed=embed)
                elif ping >= 501 and ping <= 1000:
                    pings = "🟠 위험"
                    embed = discord.Embed(title=f" 퐁🏓",color=0xff9f0e, timestamp=message.created_at)
                    embed.add_field(name="현재핑", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
                    await message.channel.send(embed=embed)
                elif ping >= 1000:
                    pings = "🔴 아주위험"
                    embed = discord.Embed(title=f" 퐁🏓",color=0xff0000, timestamp=message.created_at)
                    embed.add_field(name="현재핑", value=f'{round(client.latency * 1000)}ms\n{pings}', inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/1Gk4tOj.png")
                    await message.channel.send(embed=embed)
            elif message.content.startswith(f"제토2 가위바위보"):
                m = await message.channel.send(f"<@{message.author.id}>\n안 내면진다 가위 바위 보")
                await m.add_reaction('✌')
                await m.add_reaction('✊')
                await m.add_reaction('🖐')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✌', '✊', '🖐'])
                except asyncio.TimeoutError:
                    await message.channel.send(f'<@{message.author.id}>\n안 냈으니까 제토2의 승!')
                else:
                    if str(reaction.emoji) == "✌":
                        a = ['가위','보','바위']
                        c = random.choice(a)
                        if c == '가위':
                            embed = discord.Embed(title=f"비겼습니다",color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"가위✌", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '보':
                            embed = discord.Embed(title=f"{message.author} 이겼습니다",color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"보🤚", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '바위':
                            embed = discord.Embed(title=f"{message.author} 졌습니다",color=discord.Colour.red(), timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"바위✊", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"가위✌", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    elif str(reaction.emoji) == "✊":
                        a = ['가위','보','바위']
                        c = random.choice(a)
                        if c == '가위':
                            embed = discord.Embed(title=f"{message.author} 이겼습니다",color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"가위✌", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '보':
                            embed = discord.Embed(title=f"{message.author} 졌습니다",color=discord.Colour.red(), timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"보🤚", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '바위':
                            embed = discord.Embed(title=f"비겼습니다",color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"바위✊", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"바위✊", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    elif str(reaction.emoji) == "🖐":
                        a = ['가위','보','바위']
                        c = random.choice(a)
                        if c == '가위':
                            embed = discord.Embed(title=f"{message.author} 졌습니다",color=discord.Colour.red(), timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"가위✌", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '보':
                            embed = discord.Embed(title=f"비겼습니다",color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"보🤚", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '바위':
                            embed = discord.Embed(title=f"{message.author} 이겼습니다",color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=f"제토2#5434", value=f"바위✊", inline=True)
                            embed.add_field(name=f"{message.author}", value=f"보🤚", inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 청소') or message.content.startswith('제토2 삭제'):
                if message.author.guild_permissions.administrator or message.author.guild_permissions.manage_messages or message.author.id == 534214957110394881:
                    varrr=message.content.split(' ')
                    await message.channel.purge(limit=int(varrr[2])+1)
                    now=datetime.datetime.now()
                    msg=await message.channel.send(embed=discord.Embed(title=f'메시지 {str(int(varrr[2]))}개 삭제 완료!', descirption='제토2가 삭제했어요!!', colour=0xff00).set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일'))
                    await asyncio.sleep(2.5)
                    await msg.delete()
                else:    
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(서버 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif message.content == '제토2 야구순위' or message.content == '제토2 KOB순위':
                url = "https://sports.news.naver.com/kbaseball/record/index.nhn"
                soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
                result = soup.find("tbody", id="regularTeamRecordList_table")
                result2 = result.find_all("span") + result.find_all("strong")
                s = ""
                a = 0
                M = [[str(i) + "."] * 12 for i in range(11)]
                M[0] = ["\n**", " ", " |** ", "경기 ", "승 ", "패 ", "무 **|** 승률: ", " 게임차: ", " 연속: ", " 출루율: ", " 장타율: ",
                        " 최근 10경기: "]
                for n in result2:
                    a += 1
                    if 1 <= a <= 100:
                        M[(a - 1) // 10 + 1][(a - 1) % 10 + ((a - 1) % 10 > 4) + 1] = n.contents[0]
                    elif a % 2 == 0:
                        M[(a - 100) // 2][6] = n.contents[0]
                for i in range(10):
                    for j in range(8):
                        s += M[0][j]
                        s += M[i + 1][j]
                embed=discord.Embed(title=f"2020 KBO 순위", description=s, color=0xff00)
                embed.set_thumbnail(url = 'https://upload.wikimedia.org/wikipedia/en/3/37/2020_KBO_League.png')
                await message.channel.send(embed=embed)
            elif message.content == '제토2 멜론차트' or message.content == '제토2 멜차':
                if __name__=="__main__":
                    RANK=10
                    header={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko'}
                    req = requests.get('https://www.melon.com/chart/index.htm', headers = header)
                    html = req.text
                    parse = BeautifulSoup(html, 'html.parser')
                    titles = parse.find_all("div", {"class": "ellipsis rank01"})
                    songs = parse.find_all("div", {"class": "ellipsis rank02"})
                    title = []
                    song = []
                    embed=discord.Embed(
                        title="멜론차트 순위 입니다",
                        colour=0xff00
                    )
                    for t in titles:
                        title.append(t.find('a').text)
                    for s in songs:
                        song.append(s.find('span', {"class": "checkEllipsis"}).text)
                    for i in range(RANK):
                        embed.add_field(name='%3d위'%(i+1), value='%s - %s'%(title[i], song[i]), inline=False)
                    now=datetime.datetime.now()
                    embed.set_footer(icon_url=message.author.avatar_url, text=f'  {str(message.author.display_name)}에게 요청 받음 | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                    embed.set_thumbnail(url ="https://yt3.ggpht.com/a/AATXAJw2h2wZcZDBmQspbRxwZpYsWEz67fDx4Gir=s900-c-k-c0xffffffff-no-rj-mo")
                    await message.channel.send(embed=embed)
            elif message.content == '제토2 한국 디스코드봇 순위':
                data = await req(f'https://api.koreanbots.cf/bots/get')
                a = str()
                n = 1
                for i in data['data']:
                    a += f"{n}위 -{i['name']} : {i['servers']}서버 ❤️{i['votes']}\n"
                    n += 1
                await makeembed2('한국 디스코드봇 순위',f'{a}')
            elif message.content.startswith("제토2 날씨"):
                learn = message.content.split(" ")
                location = learn[2]
                enc_location = urllib.parse.quote(location+'날씨')
                hdr = {'User-Agent': 'Mozilla/5.0'}
                url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
                req = Request(url, headers=hdr)
                html = urllib.request.urlopen(req)
                bsObj = bs4.BeautifulSoup(html, "html.parser")
                todayBase = bsObj.find('div', {'class': 'main_info'})
                todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
                todayTemp = todayTemp1.text.strip()  # 온도
                todayValueBase = todayBase.find('ul', {'class': 'info_list'})
                todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
                todayValue = todayValue2.text.strip()
                todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
                todayFeelingTemp = todayFeelingTemp1.text.strip()
                todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
                todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
                todayMiseaMongi3 = todayMiseaMongi2.find('dd')
                todayMiseaMongi = todayMiseaMongi3.text
                tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
                tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
                tomorrowTemp2 = tomorrowTemp1.find('dl')
                tomorrowTemp3 = tomorrowTemp2.find('dd')
                tomorrowTemp = tomorrowTemp3.text.strip()
                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
                tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
                tomorrowMoring = tomorrowMoring2.text.strip()
                tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
                tomorrowValue = tomorrowValue1.text.strip()
                tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
                tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
                tomorrowAfter1 = tomorrowAllFind[1]
                tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
                tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
                tomorrowAfterTemp = tomorrowAfter3.text.strip()
                tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
                tomorrowAfterValue = tomorrowAfterValue1.text.strip()
                embed = discord.Embed(
                    title=location+ '날씨 정보',
                    description=location+ '날씨 정보입니다.',
                    colour=0xff00
                )
                now=datetime.datetime.now()
                embed.set_footer(icon_url=message.author.avatar_url, text=f' | {str(message.author.display_name)} | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
                embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
                embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
                embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
                embed.add_field(name='오늘 오전과 오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
                embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
                embed.add_field(name='내일 오전의 온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
                embed.add_field(name='내일 오전의 날씨, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태    
                embed.add_field(name='내일 오후의 온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
                embed.add_field(name='내일 오후의 날씨, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
                embed.set_thumbnail(url ="https://www.weather.go.kr/home/images/icon/DY/DB03.png")
                await message.channel.send(embed=embed)
            elif message.content == '제토2 영화순위' or message.content == '제토2 영순':
                url = urlopen("https://movie.naver.com/movie/running/current.nhn")
                bs = BeautifulSoup(url, 'html.parser')
                body = bs.body
                now=datetime.datetime.now()
                target = body.find(class_="lst_detail_t1")
                embed=discord.Embed(title="영화 순위", description="영화 순위 입니다", colour=0x00f000).set_footer(icon_url=message.author.avatar_url, text=f' {str(message.author.display_name)}에게 요청받음  | {str(now.year)}년 {str(now.month)}월 {str(now.day)}일')
                list = target.find_all('li')
                no = 1
                for n in range(0, 9) :
                    no += 1
                    title = list[n].find(class_="tit").find("a").text
                    try:
                        director = list[n].find(class_="info_txt1").find_all("dd")[1].find("span").find_all("a")
                        directorList = [director.text.strip() for director in director]
                    except IndexError:
                        directorList="정보 없음"
                    try:
                        cast = list[n].find(class_="lst_dsc").find("dl", class_="info_txt1").find_all("dd")[2].find(class_="link_txt").find_all("a")
                        castList = [cast.text.strip() for cast in cast]
                    except IndexError:
                        castList="정보 없음"
                    embed.add_field(name=f'{no}등', value=f"영화 제목:  {title}\n제작 감독:  {directorList}\n출연 배우:  {castList}", inline=False)
                    embed.set_thumbnail(url ="https://img.vogue.co.kr/vogue/2016/03/style_56d7c79069e99.png")
                await message.channel.send(embed=embed)
            elif message.content.startswith("제토2 위키백과"):
                channel = message.channel
                a = message.content[9:]
                title = "https://ko.wikipedia.org/wiki/" + a.replace(" ", "%20")
                async with aiohttp.ClientSession() as session:
                    async with session.get(title) as r:
                        if r.status == 404:
                            await makeembed3(f"{a}에 대한 위키백과 검색결과가 없습니다.")
                        else:
                            data = await r.text()
                            soup = BeautifulSoup(data, "html.parser")
                            d = soup.find("div", {"class": "mw-content-ltr", "id":"mw-content-text", "lang":"ko", "dir":"ltr"}).text
                            content = d[:200]
                            await makeembed1(f'{a}에 대한 위키백과 검색결과', f'{content}...\n\n[[ 자세히 보기 ]]({title})')
            elif message.content == '제토2 실검' or message.content == '제토2 실시간 검색':
                embed=discord.Embed(title=f"네이버 실시간 검색어",  description='현재 시각 기준 네이버의 실시간 검색어입니다.', colour=0x00f000, timestamp=datetime.datetime.utcnow())
                embed.set_thumbnail(url ="https://lh3.googleusercontent.com/Kbu0747Cx3rpzHcSbtM1zDriGFG74zVbtkPmVnOKpmLCS59l7IuKD5M3MKbaq_nEaZM")
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                for r in requests.get('https://www.naver.com/srchrank?frm=main').json().get("data")[:10]:
                    embed.add_field(name=f"**{r.get('rank')}위**", value=f"[{r.get('keyword')}](https://search.naver.com/search.naver?where=nexearch&query={r.get('keyword').replace(' ', '+')})", inline=False)
                await message.channel.send(embed=embed)
            elif message.content == '제토2 시간' or message.content == '제토2 날짜' or  message.content == '제토2 시계':
                now = datetime.datetime.now()
                channel = message.channel
                if now.hour >= 13:
                    pmhour = str(now.hour-12)
                    time = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일\n오후 " + pmhour + "시 " + str(now.minute) + "분 " + str(now.second) + "초"
                else:
                    amhour = str(now.hour)
                    time = str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일\n오전 " + amhour + "시 " + str(now.minute) + "분 " + str(now.second) + "초"
                embed = discord.Embed(title="시간", color=0xff00, timestamp=message.created_at)
                embed.add_field(name="현재 시간", value=f'{time}',  inline = False)
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                embed.set_thumbnail(url ="https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcT3z0ZnPtbUG_rWLsdmKq8S3A5pCD-96XYB4v81D4E3wGUqSbPk&usqp=CAU")
                await message.channel.send(embed=embed)
            elif message.content == '제토2 서버정보' or message.content == '제토2 섭정보':
                server = message.guild
                ver = server.verification_level
                roles = [role for role in message.guild.roles]
                embed = discord.Embed(colour=0xfeff0e, title=f"서버정보 - {message.guild.name}", timestamp=message.created_at)
                embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
                embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
                embed.add_field(name="서버 주인", value=f"{message.guild.owner}", inline=False)
                embed.add_field(name="서버 주인 ID", value=message.guild.owner.id, inline=False)
                embed.add_field(name="서버 국가", value=message.guild.region, inline=False)
                embed.add_field(name="서버 제작일", value = message.guild.created_at.strftime("20%y년 %m월 %d일"), inline=False)
                embed.add_field(name="서버 멤버 수", value = f'전체 유저 : {len(message.guild.members)}명', inline=False)
                embed.add_field(name="서버 채널 수", value = f'전체 채널 : {len(message.guild.channels)}개\n └ 채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개', inline=False)
                embed.add_field(name="서버 이모지 수", value = f'{len(message.guild.emojis)}개', inline=False)
                embed.add_field(name="보안 수준", value=ver, inline=False)
                embed.add_field(name='역할 수', value= f'({len(roles)-1}개)', inline=False)

                if message.guild.afk_channel != None:
                    embed.add_field(name=f'서버 잠수 채널', value=f'\n{message.guild.afk_channel.name}\n └ (타이머: {message.guild.afk_timeout})', inline=False)
                else:
                    embed.add_field(name=f'서버 잠수 채널', value=f'❌잠수 채널이 존재하지 않습니다.', inline=False)
                if message.guild.system_channel != None:
                    embed.add_field(name=f'서버 시스템 채널', value=f'\n({message.guild.system_channel.name} (<#{message.guild.system_channel.id}>))', inline=False)
                else:
                    embed.add_field(name=f'서버 시스템 채널', value=f'❌ | 시스템 채널이 존재하지 않습니다.', inline=False)
                embed.add_field(name=f'서버 부스트 레벨', value=f'Level: {message.guild.premium_tier}', inline=False)
                embed.add_field(name=f'서버 부스트 개수', value=f'Boost: {message.guild.premium_subscription_count}', inline=False)
                embed.set_thumbnail(url=message.guild.icon_url)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content.startswith("제토2 따라해"):
                args = message.content[7:]
                if args == "":
                    embed = discord.Embed(
                        title="주의", description="봇 따라해 `할말`로 입력해주세요!\n아무 값도 받지 못했어요.",
                    )
                    await message.channel.send(embed=embed)
                    return

                if "@everyone" in args or "@here" in args:
                    embed = discord.Embed(
                        title="경고",
                        description="`@everyone`이나 `@here`은 다른 사용자에게 피해를 줄 수 있어요.\n사용을 제한할께요!",
                    )
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        await message.channel.send(f'{args}\n```라고 {message.author.name}님이 따라하라고 하셨어요!```')
                    except:
                        pass
            elif message.content.startswith("제토2 거꾸로"):
                args = message.content[7:]
                args2 = message.content[7:]
                if args == "":
                    embed = discord.Embed(
                        title="주의", description="봇 거꾸로 `할말`로 입력해주세요!\n아무 값도 받지 못했어요.",
                    )
                    await message.channel.send(embed=embed)
                    return

                args = "".join(reversed(args))
                if "@everyone" in args or "@here" in args:
                    embed = discord.Embed(
                        title="경고",
                        description="`@everyone`이나 `@here`은 다른 사용자에게 피해를 줄 수 있어요.\n사용을 제한할께요!",
                    )
                    embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        embed = discord.Embed(
                            title=f"**{args2}** 거꾸로",
                            description=f"{args}",
                        )
                        embed.set_footer(text=message.author, icon_url=message.author.avatar_url)
                        await message.channel.send(embed=embed)
                    except:
                        pass
            elif message.content.startswith("제토2 역할정보"):
                channel = message.channel
                rname = message.content[9:]
                if not len(message.mentions) == 0 or not len(message.role_mentions) == 0 or message.mention_everyone:
                    await makeembed3(f"존재하지 않는 역할 이름입니다!")
                    return
                try:
                    if rname == "everyone":
                        role = discord.utils.get(message.server.roles, name="@everyone")
                    else:
                        role = discord.utils.get(message.server.roles, name=rname)
                        rid = role.id
                except:
                    await makeembed3(f"존재하지 않는 역할 이름입니다!")
                    return
                rid = role.id
                name = role.name
                admin = str(role.permissions.administrator)
                color = str(role.colour)
                pos = str(role.position+1) + "번"
                men = str(role.mentionable)
                hoist = str(role.hoist)
                created = str(role.created_at)
                managed = str(role.managed)
                ev = str(role.is_everyone)
                embed = discord.Embed(colour=0x31e4f7, title=f"역할정보 - {message.guild.name}", timestamp=message.created_at)
                embed.add_field(name="**이름**", value=name, inline=False)
                embed.add_field(name="**역할 ID**", value=rid, inline=False)
                embed.add_field(name="**역할 생성일**", value=created, inline=False)
                embed.add_field(name="**색**", value=color, inline=False)
                embed.add_field(name="**역할 순서**", value=pos, inline=False)
                embed.add_field(name="**언급 가능**", value=men, inline=False)
                embed.add_field(name="**분리 표시**", value=hoist, inline=False)
                embed.add_field(name="**플랫폼 매니지드**", value=managed, inline=False)
                embed.add_field(name="**에브리원 여부**", value=ev, inline=False)
                embed.add_field(name="**관리자 권한**", value=admin, inline=False)
                await message.channel.send(embed=embed)
            elif message.content == '제토2 종료':
                if message.author.id in heimteam:
                    m = await message.channel.send("진짜로 종료 하겠습니까?")
                    await m.add_reaction('<a:yes:707786803414958100>')
                    await m.add_reaction('<a:no:707786855143309370>')
                    try:
                        reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['<a:yes:707786803414958100>', '<a:no:707786855143309370>'])
                    except asyncio.TimeoutError:
                        await makeembed3('시간이 초과되었습니다.')
                    else:
                        if str(reaction.emoji) == "<a:no:707786855143309370>": 
                            await message.channel.send("종료 안할게요!!")
                            await asyncio.sleep(2.5)
                            await m.delete()
                        elif str(reaction.emoji) == "<a:yes:707786803414958100>":
                            await client.get_channel(int(744032691107659896)).edit(name=f'봇 꺼짐')
                            await client.get_channel(int(744032691107659896)).edit(name=f'봇 꺼짐')
                            await client.get_channel(int(744032973199900702)).edit(name=f'봇 꺼짐')
                            await client.get_channel(int(744032273334140948)).edit(name=f'🚥봇 상태 : off')
                            now=datetime.datetime.now()
                            webhook = 'https://discordapp.com/api/webhooks/728133432638439427/XNkaLWwo2MqmN4aiz7nMYbH0CyPf7ZD4neK-88zJKZs2dZmt4jsNCn3RVljkjjQUt8Cn'
                            requests.post(webhook, {'content':f'`제토2`가 종료되었습니다 <:status_offline:707783990953771069>=>{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초\n\
> 봇 종료 최초 핑: {round(client.latency * 1000)}ms'})
                            embed = discord.Embed(title=f"{client.user.name} 종료 명령어",colour=discord.Colour.red(), timestamp=message.created_at)
                            embed.add_field(name=f"{client.user.name} 종료 중...", value="정상적으로 종료됨 <a:yes:707786803414958100>", inline = False)
                            embed.set_footer(text=f'{client.user.name} | {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초', icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                            print(f'{client.user.name}을 종료합니다.')  
                            await asyncio.sleep(2.5)
                            await client.logout()
                            await m.delete()
                else:
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 카트'):
                learn=message.content[6:]
                response = requests.get(f'http://kart.nexon.com/Garage/Main?strRiderID={learn}')
                response2 = requests.get(f'http://kart.nexon.com/Garage/Record?strRiderID={learn}')
        
                readerhtml = response.text
                readerhtml2 = response2.text
        
                soup = BeautifulSoup(readerhtml, 'lxml')
                soup2 = BeautifulSoup(readerhtml2, 'lxml')

                #차고1#
                nick = soup.find('span', {'id' : 'RiderName'}).text #닉네임
                club = soup.find('span', {'id' : 'GuildName'}).text #클럽
                rprank = soup.find('span',{'class' : 'RecordData1'}).text #RP 순위
                rp = soup.find('span',{'class' : 'RecordData2'}).text #RP
                avatar = soup.find('div', {'id' : 'CharInfo'}) #avatar.png
                avatar2 = avatar.find('img').get('src') #avatar.png표시
        
                #차고2#
                cnt = soup2.find('div', {'id' : 'CntRecord2'}) #차고 메인 전체 크롤링
                dlfind = cnt.findAll('dl') #dl태그 찾기
                starty = dlfind[0].find('dd').text[0:4] #게임시작 년
                startm = dlfind[0].find('dd').text[5:7] #게임시작 월
                startd = dlfind[0].find('dd').text[8:10] #게임시작 일
                startday = dlfind[0].find('dd').text[11:] #게임 시작후 지금까지 일
                racing = dlfind[1].find('dd').text #게임시간
                gameon = dlfind[2].find('dd').text #게임 실행
                recenty = dlfind[3].find('dd').text[0:4] #최근 실행 년
                recentm = dlfind[3].find('dd').text[5:7] #최근 실행 월
                recentd = dlfind[3].find('dd').text[8:10] #최근실행 일

                #전체 승률#
                recorddata2 = soup2.find('div', {'id' : 'CntRecord'}) #승률창 크롤링
                allwinrate = recorddata2.find('td',{'class' : 'RecordL2'}).text[0:3] #전체승률 %
                allwin = recorddata2.find('td',{'class' : 'RecordL2'}).text[4:] #전체 전적
                allwinrp = recorddata2.find('td',{'class' : 'RecordL3'}).text #전체 RP 랭킹
        
                #스피드#
                winrate = recorddata2.find('table', {'class' : 'RecordL'}) #스피드 크롤링
                sprate = winrate.findAll('td') #스피드전적창에서 td찾기
                spallrt = sprate[4].text[0:3] #스피드 전체 %
                spallrt2 = sprate[4].text[4:] #스피드 전체 전적
                sprprank = sprate[5].text #스피드 RP 랭킹
        
                #아이템#
                iprallrt = sprate[7].text[0:3] #스피드 크롤링과 같은 클래스 아이템 전체 %
                iprallrt2 = sprate[7].text[4:] #아이템 전체 전적
                iprprank = sprate[8].text #아이템 RP 랭킹
        
                #출력#
                embed = discord.Embed(color=0xfeff0e, title = f'{learn}') #버건디 컬러 embed + 닉네임
                embed.add_field(name = "NickName", value = nick, inline = True) #닉네임 출력
                embed.add_field(name = "Club", value = club, inline = True) #클럽 출력
                embed.add_field(name = "RP", value = rprank + "\n" + rp, inline = True) #RP순위와 RP출력
                embed.add_field(name = "All Win Rate", value = allwinrate + "\n" + "(" + allwin + ")", inline = True) #전체승률 출력
                embed.add_field(name = "Speed Win Rate", value = spallrt + "\n" + "(" + spallrt2 + ")", inline = True) #스피드 승률 출력
                embed.add_field(name = "Item Win Rate", value = iprallrt + "\n" + "(" + iprallrt2 + ")", inline = True) #아이템 승률 출력
                embed.add_field(name = "All RP", value = allwinrp, inline = True) #전체 RP 출력
                embed.add_field(name = "Speed RP", value = sprprank, inline = True) #스피드 RP 출력
                embed.add_field(name = "Item RP", value = iprprank, inline = True) #아이템 RP 출력
                embed.add_field(name = "Rider Creation", value = f'{starty}년 '+f'{startm}월 '+f'{startd}일' "\n" + startday, inline = True)
                #게임시작일 출력
                embed.add_field(name = "Driving Time", value = racing, inline = True) #주행시간 출력
                embed.add_field(name = "Game Runs", value = gameon, inline = True) #게임 실행 횟수 출력
                embed.add_field(name = "Recent Access", value = f'{recenty}년 '+f'{recentm}월 '+f'{recentd}일') #게임 최근 접속일 출력
                embed.add_field(name="TMI",value=f'[KartRiderTMI](https://tmi.nexon.com/kart/user?nick={nick})') #카트라이더 TMI 연결
                embed.set_footer(text="Source - NextHeroes\nLv2 S2 KartRiderClub NextLv's Bot") #만든 사람
                embed.set_thumbnail(url = avatar2) #avatar.png 출력
                await message.channel.send(embed=embed) #embed
            elif message.content.startswith('제토2 투표'):
                    msg=message.content[6:]
                    if msg [0] == '':
                        await message.channel.send('투표 주제를 입력해주세요')
                        return
                    if not '&' in msg:
                        embed = discord.Embed(
                            title = msg, 
                            color = 0xff00,
                        )
                        embed.set_footer(icon_url=message.author.avatar_url, text=f'{message.author}님의 찬반투표')
                        mesg = await message.channel.send(embed = embed)
                        await mesg.add_reaction('<a:yes:707786803414958100>')
                        await mesg.add_reaction('<a:no:707786855143309370>')
                        return
                    msg = msg.split('&')
                    try:
                        if msg[1] == '':
                            await message.channel.send('투표 항목은 2개 이상이여야 합니다')
                            return
                        if msg[2] == '':
                            await message.channel.send('투표 항목은 2개 이상이여야 합니다')
                            return
                    except IndexError:
                        await message.channel.send('투표 항목은 2개 이상이여야 합니다')
                        return
                    string = ''
                    for i in range(len(msg) ):
                        if i == 0:
                            continue
                        if i >= 10:
                            await message.channel.send('투표 항목은 10개 이하여야 합니다')
                            return
                        string += f'{i}. {msg[i]}\n'
                    embed = discord.Embed(
                        title = msg[0],
                        description = string,
                        color = 0xff00
                    )
                    embed.set_footer(icon_url=message.author.avatar_url, text=f'{message.author}님의 항목투표')
                    mesg = await message.channel.send(embed = embed)
                    for i in range(len(msg)):
                        if i == 0:
                            continue
                        await mesg.add_reaction({1:'1️⃣', 2:'2️⃣', 3:'3️⃣', 4:'4️⃣', 5:'5️⃣', 6:'6️⃣', 7:'7️⃣', 8:'8️⃣', 9:'9️⃣', 10:'🔟', }.get(i, 'default'))
            elif message.content.startswith(f'제토2 스탯'): #counter update
                if message.author.id in heimteam:
                    await client.get_channel(int(744032691107659896)).edit(name=f'🏠서버 수 : {len(client.guilds)}')
                    await client.get_channel(int(744032954480722072)).edit(name=f'👥유저 수 : {len(client.users)}')
                    await client.get_channel(int(744032273334140948)).edit(name=f'🚥봇 상태 : ON')
                    ping= round(client.latency * 1000)
                    if ping >= 0 and ping <= 100:
                        pings = "🔵"
                        await client.get_channel(int(744032973199900702)).edit(name=f'{pings} : {ping}ms')
                    elif ping >= 101 and ping <= 200:
                        pings = "🟢" 
                        await client.get_channel(int(744032973199900702)).edit(name=f'{pings} : {ping}ms')
                    elif ping >= 201 and ping <= 500:
                        pings = "🟡"
                        await client.get_channel(int(744032973199900702)).edit(name=f'{pings} : {ping}ms')
                    elif ping >= 501 and ping <= 1000:
                        pings = "🟠"
                        await client.get_channel(int(744032973199900702)).edit(name=f'{pings} : {ping}ms')
                    elif ping >= 1000:
                        pings = "🔴"
                        await client.get_channel(int(744032973199900702)).edit(name=f'{pings} : {ping}ms')

                    msg = await message.channel.send(f'스탯 업데이트 완료!')
                    await asyncio.sleep(5)
                    await msg.delete()
                    await message.delete()
                else:
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 단축'):
                print(f'{message.author} ('+ f'{message.author.id}) : {message.content}')
                target=message.content.split(' ')[2]
                client_id=토큰
                client_secret=토큰2
                header = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
                naver = 'https://openapi.naver.com/v1/util/shorturl'
                data = {'url': target}
                maker=requests.post(url=naver,data=data,headers=header)
                maker.close()
                output=maker.json()['result']['url']
                embed = discord.Embed(title="URL 단축기능",color=0xff00, timestamp=message.created_at)
                embed.add_field(name="단축 링크", value=f'{output}', inline = False)
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content.startswith(f"제토2 건답"):
                if message.author.id in heimteam:
                    msg = message.content[7:]
                    user = msg.split('/')[0]
                    description = msg.split('/')[1]
                    try:
                        await client.get_user(int(user)).send(f"{description}\n\n발신인 : {message.author}")
                        await message.channel.send(f"{client.get_user(int(user))}님께 답변을 완료했어요!")
                    except Exception as ex:
                        await message.channel.send(f"오류가 발생했어요! 아마도 DM을 못보내서 오류난거같은데 확인해보세요!\n오류 : {ex}")
                else:    
                    embed = discord.Embed(color=discord.Colour.red(),title='<a:no:707786855143309370> 사용불가 <a:no:707786855143309370> ',description='사용불가 명령어 입니다\n(봇 관리자 명령어)', timestamp=message.created_at)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 qr') or message.content.startswith('제토2 QR') or message.content.startswith('제토2 큐알'):
                target=message.content[7:]
                if target == "":
                    await makeembed('링크 입력해주세요')
                client_id=토큰
                client_secret=토큰2
                header = {'X-Naver-Client-Id': client_id, 'X-Naver-Client-Secret': client_secret}
                naver = 'https://openapi.naver.com/v1/util/shorturl'
                data = {'url': target}
                maker=requests.post(url=naver,data=data,headers=header)
                maker.close()
                output=maker.json()['result']['url']
                qr=qrcode.QRCode(
                version=1,
                box_size=13,
                border=2

                )
                data=output
                qr.add_data(data)
                qr.make(fit=True)
                img=qr.make_image(fill="black", back_color="white")
                img.save(f'{message.author.id}' + '.png')
                name = str(f'{message.author.id}' + '.png')
                embed=discord.Embed(title=f'{message.author}님이 요청하신 QR코드입니다.\n요청하신 URL : {output}\nURL이 길수도 있어서 단축URL로 QR코드를 생성합니다', description='QR코드를 우클릭해서 이미지저장하세요!!', colour=0xff00, timestamp=message.created_at)
                embed.set_footer(text=f'{message.author}', icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                await message.channel.send(file=discord.File(name))
            elif message.content.startswith('제토2 프사'):
                if str(message.content[7:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
                    else:
                        embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                    embed.add_field(name="유저정보", value= f'{user}님 프사', inline=True)
                    embed.set_image(url=user.avatar_url)
                    embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                            embed.add_field(name="유저정보", value= f'{user}님 프사', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            else:
                                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                            embed.add_field(name="봇정보", value= f'{user}님 프사', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    except:
                        user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                            embed.add_field(name="유저정보", value= f'{user}님 프사', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            else:
                                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                            embed.add_field(name="봇정보", value= f'{user}님 프사', inline=True)
                            embed.set_image(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
            elif message.content  ==  '제토2 주사위':
                a = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
                c = random.choice(a)
                await message.channel.send(f"<@{message.author.id}>님\n "+c+" 나왔습니다")
            elif message.content  ==  '제토2 낚시':
                fish = ['고등어!','��구!','연어!','참치!','복어!','연어!','참치!','복어!','아무것도 �������!','아무것도 못!','아무것��� 못!','귀상어과!','악상어목!','브램블 샤크!',
                        '아무것도 못!','상어!','고등어!','고등어!','대구!','대구!','대구!','고등어!','대구!`','고등어!','대구!','가시고기!','가시고기!','가시고기!','가시고기!','가시고기!','가시고기!','가시고기!','가시고기!','가시고기!',
                        '고등어!', '대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!','빙어!',
                        '고등어!', '대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','고등어!','대구!','홍어!','홍어!','쉬리!','쉬리!','송사리!','송사리!','산천어!','산천어!','산천어!','산천어!','산천어!','산천어!','산천어!','산천어!','산천어!',
                        '고등어!', '대구!','고등어!','대구!','고래!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!',
                        '아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','아무것도 못!','인어공주','제토']
                a = ['20cm','21cm','22cm','23cm','24cm','25cm','30cm','31cm','32cm','33cm','34cm','35cm','36cm','37cm','38cm','39cm','40cm']
                y = random.choice(a)
                u = ['33.58m','24.59m','30.10m','40.10m']
                O = random.choice(u)
                embed=discord.Embed(colour=0x00f000, timestamp=message.created_at)
                embed = discord.Embed(title='낚시대로 내리까?\n 내리자!<a:yes:707786803414958100> 낚시 하지말자<a:no:707786855143309370>')
                m=await message.channel.send(f'<@{message.author.id}>',embed=embed)
                await m.add_reaction('<a:yes:707786803414958100>')
                await m.add_reaction('<a:no:707786855143309370>')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 50, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['<a:yes:707786803414958100>', '<a:no:707786855143309370>'])
                except asyncio.TimeoutError:
                    await message.channel.send("낚시를 안하시네요....")
                else:
                    if str(reaction.emoji) == "<a:yes:707786803414958100>":
                        c = random.choice(fish)
                        if c == '제토':
                            msg=await message.channel.send("이게 뭐야?<a:typing:707785134404927539>")
                            await asyncio.sleep(5)
                            await msg.delete()
                            embed = discord.Embed(title='제토 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'몰음',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'왕 전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("뭐야!! 주인님이자냐!!")
                            await msm.add_reaction('🎉')
                        if c == '인어공주':
                            msg=await message.channel.send("이게 뭐야?<a:typing:707785134404927539>")
                            await asyncio.sleep(5)
                            await msg.delete()
                            embed = discord.Embed(title='인어공주 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'몰음',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'왕 전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 왕 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '상어!':
                            embed = discord.Embed(title='상어🦈 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{O}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '브램블 샤크!':
                            embed = discord.Embed(title='브램블 샤크🦈 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{O}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '고래!':
                            embed = discord.Embed(title='고래🐳를 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{O}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '악상어목!':
                            embed = discord.Embed(title='악상어목🦈 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{O}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '귀상어과!':
                            embed = discord.Embed(title='귀상어과🦈를 잡았습니다',color=0x00e2ff, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{O}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'전설',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            msm=await message.channel.send(embed=embed)
                            await message.channel.send("🎉축하합니다 전설이네요!!🎉")
                            await msm.add_reaction('🎉')
                        if c == '가시고기!':
                            embed = discord.Embed(title='가시고기🐟를 잡았습니다',color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'일반',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '빙어!':
                            embed = discord.Embed(title='빙어🐟를 잡았습니다',color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'일반',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '산천어!':
                            embed = discord.Embed(title='산천어🐟를 잡았습니다',color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'일반',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '대구!':
                            embed = discord.Embed(title='대구🐟를 잡았습니다',color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'일반',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '홍어!':
                            embed = discord.Embed(title='홍어🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '쉬리!':
                            embed = discord.Embed(title='쉬리🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '송사리!':
                            embed = discord.Embed(title='송사리🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '고등어!':
                            embed = discord.Embed(title='고등어🐟를 잡았습니다',color=0xff00, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'일반',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '연어!':
                            embed = discord.Embed(title='연어🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '참치!':
                            embed = discord.Embed(title='참치🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '복어!':
                            embed = discord.Embed(title='복어🐠를 잡았습니다',color=0xe4f05a, timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'{y}',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'희귀',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                        if c == '아무것도 못!':
                            embed = discord.Embed(title='아무것도 못잡았습니다',color=discord.Colour.red(), timestamp=message.created_at)
                            embed.add_field(name=":straight_ruler: 크기", value=f'없음',  inline=True)
                            embed.add_field(name="🏆 희귀도", value=f'없음',  inline=True)
                            embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                            await message.channel.send(embed=embed)
                    elif str(reaction.emoji) == "<a:no:707786855143309370>":
                        await message.channel.send(f"<@{message.author.id}>,낚시를 안하시네요....")
            elif message.content  ==  '제토2 뉴스':
                await message.channel.send("오늘의 주요 네이버뉴스입니다.(총 5개 나옴)")
                url = 'https://news.naver.com/'
                html = urllib.request.urlopen(url)
                # print(html)
                bsObj = bs4.BeautifulSoup(html, "html.parser")
                news = bsObj.select('#today_main_news > div.hdline_news > ul > li > div.hdline_article_tit > a')
                splitted_str = ["`"+a.text.strip()+"`" for a in news]
                await message.channel.send("\n".join(splitted_str))
            elif message.content == '제토2 도움말' or message.content == '제토2 도움' or message.content == '제토2 명령어' or message.content == '제토2 help':
                a = '__제토2 채팅 기능__\n ```제토2 (아무말) \n제토2 (가위,바위,보)\n제토2 낚시\n제토2 봇정보\n제토2 핑\n제토2 업타임\n제토2 슬롯\n제토2 슛골인 정보\n제토2 환영설정\n제토2 투표 (투표제목)또는 (투표제목)&(항목1)&(항목2) [최대 항목 10개 가능]\n제토2 날짜\n제토2 시간\n제토2 계산 (계산식)\n제토2 타이머 (초) (이름)\n제토2 사계절\n제토2 매직8볼\n제토2 매치(수) (수)\n제토2 랜덤숫자 (수) (수)\n제토2 따라해 (내용)\n제토2 거꾸로 (내용)```'
                b = '__제토2 전송기능/유저정보(응용 기능)__\n```제토2 정보 (@멘션)\n제토2 프사 (@멘션)\n제토2 건의 (건의 내용)\n제토2 채널정보 (#채널이름)```'
                n = '__제토2 외부기능__ \n```제토2 코로나19\n제토2 실검\n제토2 멜론차트\n제토2 날씨 (지역) [*없는 지역하면 오류나옴*]\n제토2 영화순위\n제토2 단축 (링크) [*단축 링크를 단축하면 오류나옴*]\n제토2 띠 (년도)\n제토2 뉴스\n제토2 qr (링크)\n\
제토2 미세먼지\n제토2 초미세먼지\n제토2 블로그 (검색)\n제토2 위키백과 (검색)\n제토2 한국 디스코드봇 순위\n제토2 하트 (@이름)\n제토2 네이버링 (검색이름)\n제토2 캡챠\n제토2 (한,일,중,영,태)(한,일,중,영,태)번역 (번역할 내용)\n제토2 롤 (롤 이름)\n제토2 이미지 (검색)\n제토2 레식전적 (이름)\n제토2 재난문자\n\
제토2 카트 (이름)\n제토2 지진\n제토2 제토2 가사 (노래이름)\n제토2 나무위키 (검색)```'
                y = '__제토2 서버관리자 기능__ \n```제토2 청소 (수)\n제토2 추방 (@이름)\n제토2 차단 (@이름)\n제토2 팔로워공지 (채널아이디)&(메시지아이디)```'
                t = '__봇 관리자용 기능__\n```제토2 종료\n제토2 공지 (공지제목)&(공지내용)\n제토2 건답 (@이름)/(내용)\n제토2 컴파일 (컴파일 내용)\n제토2 eval (eval 내용)\n제토2 스탯```'
                v = '__도움&질문 등 부가서비스__ \n도움이나 질문는 제토#8759 또는 https://discord.gg/SC8hE25 으로 문의해 주시기 바랍니다.'
                await message.author.send(f'{a}\n\n{b}\n\n{n}\n\n{y}\n\n{t}\n\n{v}\n')
                embed = discord.Embed(color=0x00f000,title='제토2 도움말',description='DM으로 전송됨', timestamp=message.created_at)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 띠 '):
                learn=message.content[5:]
                if learn == '':
                    await  message.channel.send('년도를 입력해주세요')
                birth_year = int(f'{learn}') % 12
                if birth_year == 0:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년띠", value=f"원숭이 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 1:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"닭 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 2:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"개 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 3:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"돼지 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 4:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"쥐 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 5:
                    embed = discord.Embed(title=f" {client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"소 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 6:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"호랑이 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 7:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"토끼 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 8:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"용 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 9:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"뱀 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 10:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"말 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if birth_year == 11:
                    embed = discord.Embed(title=f"{client.user.name} 띠 기능",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name=f"{learn}년 띠 는", value=f"양 띠", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
            elif message.content == '제토2 사계절':
                now=datetime.datetime.now()
                if 3 <= now.month <= 5:
                    embed = discord.Embed(title="계절 ",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name="현재 계절", value=f"이번 달은 {str(now.month)}월로 `봄`입니다!", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if 6 <= now.month <= 8:
                    embed = discord.Embed(title="계절 ",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name="현재 계절", value=f"이번 달은 {str(now.month)}월로 `여름`입니다!", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed=embed)
                if 9 <= now.month <= 11:
                    embed = discord.Embed(title="계절 ",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name="현재 계절", value=f"이번 달은 {str(now.month)}월로 `가을`입니다!", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
                if now.month == 12 or 1 <= now.month <= 2:
                    embed = discord.Embed(title="계절 ",color=0xff00, timestamp=message.created_at)
                    embed.add_field(name="현재 계절", value=f"이번 달은 {str(now.month)}월로 `겨울`입니다!", inline = False)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    await message.channel.send(embed = embed)
            elif message.content == '제토2 로그':
                if message.author.guild_permissions.administrator or message.author.guild_permissions.kick_members:
                    guild = message.guild
                    await guild.create_text_channel(name=f'zetto2-log')
                    await makeembed1('제토2 로그기능', '제토2 로그를 켰습니다')
            elif message.content == '제토2 봇정보':
                embed = discord.Embed(
                title = '제토2 정보',
                description = f'> 봇 이름: 제토2\n\
> 봇 id: {client.user.id}\n\
> 봇 탄생: 2020년 1월 30일\n\n\
> 개발자: 제토#8759\n\
> 도움:Bainble0211#5632\n\n\
> 서버 수: {len(client.guilds)}\n\
> 유저 수: {len(client.users)}\n\n\
> 봇 초대: [봇초대](https://c11.kr/frpg)\n\
> 공식서버: [공식서버](https://discordapp.com/invite/SC8hE25)\n\n\
> 파이썬 버전: {sys.version.split(" ")[0]}\n\
> discord.py 버전: {pkg_resources.get_distribution("discord.py").version}',
                color = 0xff00
               ).set_thumbnail(url = client.user.avatar_url)
                await message.channel.send(embed = embed)
            elif message.content == '제토2 업타임' or message.content == '제토2 가동시간':
                uptime = str(Uptime.uptime()).split(":")
                hours = uptime[0]
                minitues = uptime[1]
                seconds = uptime[2].split(".")[0]
                await message.channel.send(embed = discord.Embed(title='제토2 업타임', description=f"{hours}시간 {minitues}분 {seconds}초"))
            elif message.content.startswith("제토2 채널정보"):
                if len(message.channel_mentions) == 0:
                    channel = message.channel
                else:
                    channel = message.channel_mentions[0]
                name = channel.name
                cid = channel.id
                topic = channel.topic 
                if topic == "" or topic == None:
                    topic = "없음"
                pos = str(channel.position+1) + "번"
                ctype = str(channel.type)
                created = str(channel.created_at)
                embed = discord.Embed(title=f"{name} 채널정보", color=0xff00, timestamp=message.created_at)
                embed.add_field(name="이름", value=name, inline = False)
                embed.add_field(name="채널 ID", value=cid, inline = False)
                embed.add_field(name="주제", value=topic, inline = False)
                embed.add_field(name="채널 순서", value=pos, inline = False)
                embed.add_field(name="채널 종류", value=ctype, inline = False)
                embed.add_field(name="채널 생성일", value=created, inline = False)
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                await message.channel.send(embed = embed)
            elif message.content == '제토2 코로나' or message.content == '제토2 코로나19' or  message.content == '제토2 COVID-19'or   message.content == '제토2 covid-19' or message.content == '제토2 사스2':
                hdr = {'User-Agent': 'Mozilla/5.0'}   
                url =  'http://ncov.mohw.go.kr/'
                req = Request(url, headers=hdr)
                html = urllib.request.urlopen(req)
                bsObj = bs4.BeautifulSoup(html, "html.parser")
                corona = bsObj.find('div', {'class': 'mainlive_container'})
                corona2 = corona.find('div', {'class': 'container'})
                corona3 = corona2.find('div', {'class': 'liveboard_layout'})
                corona4 = corona3.find('div', {'class': 'live_left'})
                corona4 = corona3.find('div', {'class': 'liveNum'})
                corona5 = corona4.find('ul', {'class': 'liveNum'})
                corona6 = corona5.find_all('li')
                coronacount = corona6[0]
                coronacount2 = coronacount.find('span', {'class': 'num'})
                coronacount3 = coronacount2.text.strip()
                coronacountp = corona6[0]
                coronacount2p = coronacountp.find('span', {'class': 'before'})
                coronacount3p = coronacount2p.text.strip()
                coronafin = corona6[1]
                coronafin2 = coronafin.find('span', {'class': 'num'})
                coronafin3 = coronafin2.text.strip()
                coronafinp = corona6[1]
                coronafin2p = coronafinp.find('span', {'class': 'before'})
                coronafin3p = coronafin2p.text.strip()
                coronadoc = corona6[2]
                coronadoc2 = coronadoc.find('span', {'class': 'num'})
                coronadoc3 = coronadoc2.text.strip()
                coronadocp = corona6[2]
                coronadoc2p = coronadocp.find('span', {'class': 'before'})
                coronadoc3p = coronadoc2p.text.strip()
                coronarip = corona6[3]
                coronarip1 = coronarip.find('span', {'class': 'num'})
                coronarip2 = coronarip1.text.strip()
                coronaripp = corona6[3]
                coronarip1p = coronaripp.find('span', {'class': 'before'})
                coronarip2p = coronarip1p.text.strip()
                embed = discord.Embed(title='코로나 바이러스 감염증-19',colour=discord.Colour.red())
                embed.set_thumbnail(url ="https://www.sciencetimes.co.kr/wp-content/uploads/2020/03/800px-2019-nCoV-CDC-23312_without_background-478x480.png")
                embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                embed.add_field(name='확진환자', value=coronacount3+'명', inline=False)
                embed.add_field(name='완치', value=coronafin3 + '명', inline=False)
                embed.add_field(name='치료중', value=coronadoc3 + '명', inline=False)
                embed.add_field(name='사망자', value=coronarip2 + '명', inline=False)
                embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
                embed.add_field(name='확진환자(전일대비)', value=coronacount3p + '명', inline=False)
                embed.add_field(name='완치(전일대비)', value=coronafin3p + '명', inline=False)
                embed.add_field(name='치료중(전일대비)', value=coronadoc3p + '명', inline=False)
                embed.add_field(name='사망자(전일대비)', value=coronarip2p + '명', inline=False)
                await message.channel.send(embed=embed)
            elif message.content.startswith(f"제토2 정보"):
                if str(message.content[7:]) == '':
                    user = message.author
                    date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                    status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                        discord.Status.offline: '<:status_offline:728527943831126036>  오프라인',
                        discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                        discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                    user_status = status_dict[user.status]
                    if not len(message.author.roles) == 1:
                        roles = [role for role in user.roles]
                        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
                    else:
                        embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"유저정보 - {user}")
                    embed.set_author(name=f"유저정보 - {user}")
                    embed.set_thumbnail(url=user.avatar_url)
                    embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                    embed.add_field(name="아이디", value=user.id, inline = False)
                    embed.add_field(name="닉네임", value=user.display_name,  inline = False)
                    embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                    embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                    embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
                    embed.add_field(name="가장 높은 역할", value=user.top_role.mention,  inline = False)
                    embed.add_field(name ="상태", value =f'{user_status}', inline = False)
                    embed.add_field(name="봇", value=user.bot, inline = False)
                    if 'Custom Status' in str(user.activity):
                        embed.add_field(name = '하는 게임& 상태메시지', value = user.activity.state, inline = False)
                    else:
                        embed.add_field(name = '하는 게임& 상태메시지', value = user.activity, inline = False)
                    await message.channel.send(embed=embed)
                else:
                    try:
                        user = message.guild.get_member(int(message.content.split('<@!')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036>  오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                            embed.set_author(name=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=user.id, inline = False)
                            embed.add_field(name="닉네임", value=user.display_name,  inline = False)
                            embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
                            embed.add_field(name="가장 높은 역할", value=user.top_role.mention,  inline = False)
                            embed.add_field(name ="상태", value =f'{user_status}', inline = False)
                            embed.add_field(name="봇", value=user.bot, inline = False)
                            if 'Custom Status' in str(user.activity):
                                embed.add_field(name = '하는 게임& 상태메시지', value = user.activity.state, inline = False)
                            else:
                                embed.add_field(name = '하는 게임& 상태메시지', value = user.activity, inline = False)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036>  오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            else:
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            embed.set_author(name=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=user.id, inline = False)
                            embed.add_field(name="닉네임", value=user.display_name,  inline = False)
                            embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
                            embed.add_field(name="가장 높은 역할", value=user.top_role.mention,  inline = False)
                            embed.add_field(name ="상태", value =f'{user_status}', inline = False)
                            embed.add_field(name="봇", value=user.bot, inline = False)
                            if 'Custom Status' in str(message.author.activity):
                                embed.add_field(name = '하는 게임& 상태메시지', value = user.activity.state, inline = False)
                            else:
                                embed.add_field(name = '하는 게임& 상태메시지', value =user.activity, inline = False)
                            embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                            await message.channel.send(embed=embed)
                    except:
                        user = message.guild.get_member(int(message.content.split('<@')[1].split('>')[0]))
                        if user.bot == False:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036>  오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"유저정보 - {user}")
                            else:
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"유저정보 - {user}")
                            embed.set_author(name=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=user.id, inline = False)
                            embed.add_field(name="닉네임", value=user.display_name,  inline = False)
                            embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
                            embed.add_field(name="가장 높은 역할", value=user.top_role.mention,  inline = False)
                            embed.add_field(name ="상태", value =f'{user_status}', inline = False)
                            embed.add_field(name="봇", value=user.bot, inline = False)
                            if 'Custom Status' in str(user.activity):
                                embed.add_field(name = '하는 게임& 상태메시지', value =user.activity.state, inline = False)
                            else:
                                embed.add_field(name = '하는 게임& 상태메시지', value = user.activity, inline = False)
                            await message.channel.send(embed=embed)
                        else:
                            date = datetime.datetime.utcfromtimestamp(((int(user.id) >> 22) + 1420070400000) / 1000)
                            status_dict: dict = {discord.Status.online: '<:status_online:728527943827062804> 온라인',
                                discord.Status.offline: '<:status_offline:728527943831126036>  오프라인',
                                discord.Status.idle: "<:status_idle:728527943806091364> 자리비움",
                                discord.Status.do_not_disturb: "<:status_dnd:728527943684456459> 방해금지"}
                            user_status = status_dict[user.status]
                            if not len(user.roles) == 1:
                                roles = [role for role in user.roles]
                                embed=discord.Embed(colour=user.color, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            else:
                                embed=discord.Embed(colour=0x31e4f7, timestamp=message.created_at, title=f"봇정보<:bot:653893296837623818> - {user}")
                            embed.set_author(name=f"유저정보 - {user}")
                            embed.set_thumbnail(url=user.avatar_url)
                            embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
                            embed.add_field(name="아이디", value=user.id, inline = False)
                            embed.add_field(name="닉네임", value=user.display_name,  inline = False)
                            embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
                            embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
                            embed.add_field(name="가장 높은 역할", value=user.top_role.mention,  inline = False)
                            embed.add_field(name ="상태", value =f'{user_status}', inline = False)
                            embed.add_field(name="봇", value=user.bot, inline = False)
                            if 'Custom Status' in str(user.activity):
                                embed.add_field(name = '하는 게임& 상태메시지', value =user.activity.state, inline = False)
                            else:
                                embed.add_field(name = '하는 게임& 상태메시지', value = user.activity, inline = False)
                            embed.add_field(name="봇 초대링크 (관리자 권한)", value=f"[초대하기](https://discordapp.com/oauth2/authorize?client_id={user.id}&scope=bot&permissions=8)", inline=False)
                            await message.channel.send(embed=embed)
            elif message.content == '제토2 재난문자':
                """최근에 발생한 재난문자를 보여줍니다"""
                async with aiohttp.ClientSession() as session:
                    async with session.get('http://m.safekorea.go.kr/idsiSFK/neo/ext/json/disasterDataList/disasterDataList.json') as r:
                        data = await r.json()

                embed = discord.Embed(
                    title="📢 재난문자",
                    description="최근 발송된 5개의 재난문자를 보여줘요.",
                    color=0xE71212
                )

                for i in data[:5]:
                    embed.add_field(name=i["SJ"], value=i["CONT"], inline=False)
                await message.channel.send(embed=embed)
            elif message.content == '제토2 지진':
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        "https://m.kma.go.kr/m/eqk/eqk.jsp?type=korea"
                    ) as r:

                        c = await r.text()
                        soup = BeautifulSoup(c, "html.parser")
                        table = soup.find("table", {"class": "table02 style01"})
                        td = table.find_all("td")

                        date = earthquake(td[1])
                        gyumo = earthquake(td[3])
                        jindo = earthquake(td[5])
                        location = earthquake(td[7])
                        depth = earthquake(td[9])
                        detail = earthquake(td[10])

                        embed = discord.Embed(
                            title="지진 정보", description=date, color=0xff00
                        )
                        try:
                            img = soup.find("div", {"class": "img-center"}).find("img")[
                                "src"
                            ]
                            img = "http://m.kma.go.kr" + img
                            if img is None:
                                pass
                            else:
                                embed.set_image(url=img)

                        except:
                            pass

                        embed.add_field(name="규모", value=gyumo, inline=True)
                        embed.add_field(name="발생위치", value=location, inline=True)
                        embed.add_field(name="발생깊이", value=depth, inline=True)
                        embed.add_field(name="진도", value=jindo, inline=True)
                        embed.add_field(name="참고사항", value=detail, inline=True)
                        embed.set_footer(text="기상청")

                        await message.channel.send(embed=embed)
            elif message.content.startswith('제토2 가사'):
                args = message.content[6:]
                async with aiohttp.ClientSession() as session:
                    async with session.get(
                        "http://music.naver.com/search/search.nhn?query="
                        + args
                        + "&target=track"
                    ) as r:

                        c = await r.text()
                        soup = BeautifulSoup(c, "html.parser")
                        f = soup.find_all("a", {"title": "가사"})[0]["class"][1]
                        f = f.split(",")
                        # print(f)
                        f = f[2]
                        f = f[2:]
                        load = "http://music.naver.com/lyric/index.nhn?trackId=" + f

                    async with session.get(load) as r:
                        c = await r.text()
                        soup = BeautifulSoup(c, "html.parser")
                        f = soup.find("div", {"id": "lyricText"})
                        f = f.get_text(separator="\n")
                        title = soup.find("span", {"class": "ico_play"}).get_text()
                        f = f[:2048]
                    embed = discord.Embed(
                        title=f"🎵{title}의 가사",
                        description=f"\n{f}\n\n[바로가기]({load})",
                        color=0xff00,
                    )
                    await message.channel.send(embed=embed)
            elif message.content == '제토2':
                await message.channel.send("`제토2 도움말`로 명령어를 알수 있어요")
            elif message.content.startswith("제토2"):
                msg = message.content[3:]
                header = {
                     'Authorization': pingpongauth,
                    'Content-Type': 'application/json'
                }
                param = {
                    'request': {
                        'query': msg
                    }
                }
                async with aiohttp.ClientSession(headers=header) as session:
                    async with session.post(pingpongurl+f'/{message.author.id}', json=param) as res:
                        data = await res.json()
                        assert 'response' in data
                        assert 'replies' in data['response']
                        for reply in data['response']['replies']:
                            if 'text' in reply:
                                await message.channel.send(reply['text'])
            else:
                embed=discord.Embed(colour=discord.Colour.red(), timestamp=message.created_at)
                embed.add_field(name=" <a:no:707786855143309370>  명령어 안내  <a:no:707786855143309370> ", value=f"{client.user.name}에 없는 명령어입니다 \n `제토2 도움말` 이용해서 명령어를 알아봅시다", inline=True)
                embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
           
    except Exception as ex:
        embed=discord.Embed(colour=discord.Colour.red(), timestamp=message.created_at)
        embed.add_field(name=" <a:no:707786855143309370>  오류발생  <a:no:707786855143309370> ", value=f'{client.user.name} 에러 발생\n에러에 대한 내용이<@534214957110394881>님한테 전송됨\n에러 내용 : {str(ex)}', inline=True)
        embed.set_footer(text=f"{message.author}", icon_url=message.author.avatar_url)
        print(f'오류 발생, 에러 내용 : {str(ex)}')
        await message.channel.send(embed=embed)


             
async def my_background_task():
    await client.wait_until_ready()
    while not client.is_closed():
        game = discord.Game(f"{client.user.name} 도움말 를 이용해서 명령어를 알아보자")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game(f'서버:{len(client.guilds)}개/유저:{len(client.users)}명')
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
        game = discord.Game("이 메세지는 10초마다 바뀝니다")
        await client.change_presence(status=discord.Status.online, activity=game)
        await asyncio.sleep(10)
client.loop.create_task(my_background_task())
    
client.run(토큰)
