import discord
import random
import time
from datetime import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
games = ['Кость']


def randomizer():
    instance = random.randrange(1, 6)
    return instance




@client.event
async def on_message(message):
    await client.process_commands(message)
    try:
        if message.author == client.user:
            return

        if message.content.lower().startswith('расписание'):
            currentDate = datetime.today()
            currentDay = datetime.weekday(currentDate)

            if currentDay == 0: # Понедельник:
                dayName = "Понедельник"
                lessons = ['Выходной, но ты можешь раскидать уроки на неделю']
                links = ['И да похавать не забудь']

            elif currentDay == 1: # Вторник
                dayName = "Вторник"
                lessons = ['Нелинейные системы автоматического регулирования(лекция). Касимов А. О.', 'Программное обеспечение SCADA(лекция). Абдрешова С. Б.', "Программное обеспечение SCADA(лекция).Абдрешова С. Б.", "Инструменты и методы бытовой автоматизации(лабораторное занятие). Шортанбаева А. Т.", "Инструменты и методы бытовой автоматизации(лабораторное занятие). Шортанбаева А. Т.", "Основы машинного обучения(лекция). Нұрмұрат А. Ш.", "Основы машинного обучения(лекция). Нұрмұрат А. Ш."]
                links = ['https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fteam%2F19%3A9407bbe1cf6747499da8c3674d8e0951%40thread.tacv2%2Fconversations%3FgroupId%3Daf2e6638-66d5-41a3-8f9c-cd8f140c32ad%26tenantId%3Db0ab71a5-75b1-4d65-81f7-f479b4978d7b&type=team&deeplinkId=d31a048e-1478-45bb-8b3f-715c6bd14c0d&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true','https://us04web.zoom.us/j/79801399599?pwd=ZlVRUVlwR3dJdGNCR1hQUVE2NFBjdz09','https://us04web.zoom.us/j/79801399599?pwd=ZlVRUVlwR3dJdGNCR1hQUVE2NFBjdz09','https://zoom.us/j/9489058964?pwd=S2hOMmlKYktxWjB3T1E3VUJBVm4rdz09','https://zoom.us/j/9489058964?pwd=S2hOMmlKYktxWjB3T1E3VUJBVm4rdz09','https://us04web.zoom.us/j/73179029713?pwd=KzhyRjJMV1Z6c2tDZndXOUJlWnplUT09','https://us04web.zoom.us/j/73179029713?pwd=KzhyRjJMV1Z6c2tDZndXOUJlWnplUT09']

            elif currentDay == 2: # Среда
                dayName = "Среда"
                lessons = ['Функциональное программирование(лекция). Мошқалов А. Қ.', 'Функциональное программирование(лекция). Мошқалов А. Қ.', "Программирование для Data Mining(лекция). Кожамбердиева М. И.", "Программирование для Data Mining(лекция). Кожамбердиева М. И.", "Инструменты и методы бытовой автоматизации(лекция). Ашимов Е. К.", "Инструменты и методы бытовой автоматизации(лекция). Ашимов Е. К."]
                links = ['Ссылка отсутствует', 'Ссылка отсутствует', 'https://us05web.zoom.us/j/3098104386?pwd=N0svYlpUYnkwZEhIR2wrQnhtTE5SQT09', 'https://us05web.zoom.us/j/3098104386?pwd=N0svYlpUYnkwZEhIR2wrQnhtTE5SQT09', 'https://us04web.zoom.us/j/77939611326?pwd=VnpMWGI4WE1Tb1FFeWdTTWNJRTBrQT09','https://us04web.zoom.us/j/77939611326?pwd=VnpMWGI4WE1Tb1FFeWdTTWNJRTBrQT09']

            elif currentDay == 3:
                dayName = "Четверг"
                lessons = ['Нелинейные системы автоматического регулирования(лабораторное занятие). Жунусова Ж. Х.', 'Нелинейные системы автоматического регулирования(лабораторное занятие). Жунусова Ж. Х.', "Программирование для Data Mining(лабораторное занятие). Жұмашева А. А.", "Программирование для Data Mining(лабораторное занятие). Жұмашева А. А."]
                links = ['https://us04web.zoom.us/j/76728506331?pwd=R3VRM08rTXpkVjlTME5JZEtNVGVNdz09', 'https://us04web.zoom.us/j/76728506331?pwd=R3VRM08rTXpkVjlTME5JZEtNVGVNdz09', 'https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fteam%2F19%3A515f18c686d54a198b02a0237c2fe592%40thread.tacv2%2Fconversations%3FgroupId%3D7d649d2c-b6b9-4006-8915-02d0c31f444c%26tenantId%3Db0ab71a5-75b1-4d65-81f7-f479b4978d7b&type=team&deeplinkId=9ad8e4ae-464a-4152-ae15-6a3ec3b987bd&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true', 'https://teams.microsoft.com/dl/launcher/launcher.html?url=%2F_%23%2Fl%2Fteam%2F19%3A515f18c686d54a198b02a0237c2fe592%40thread.tacv2%2Fconversations%3FgroupId%3D7d649d2c-b6b9-4006-8915-02d0c31f444c%26tenantId%3Db0ab71a5-75b1-4d65-81f7-f479b4978d7b&type=team&deeplinkId=9ad8e4ae-464a-4152-ae15-6a3ec3b987bd&directDl=true&msLaunch=true&enableMobilePage=true&suppressPrompt=true']

            elif currentDay == 4:
                dayName = "Пятница"
                lessons = ['Основы машинного обучения(лабораторное занятие). Нұрмұрат А. Ш.', 'Основы машинного обучения(лабораторное занятие). Нұрмұрат А. Ш.', "Функциональное программирование(лабораторное занятие). Дуйсембаева Л. С.", "Функциональное программирование(лабораторное занятие). Дуйсембаева Л. С.", 'Основы машинного обучения(семинар). Нұрмұрат А. Ш.']
                links = ['https://us04web.zoom.us/j/73179029713?pwd=KzhyRjJMV1Z6c2tDZndXOUJlWnplUT09','https://us04web.zoom.us/j/73179029713?pwd=KzhyRjJMV1Z6c2tDZndXOUJlWnplUT09','https://us04web.zoom.us/j/78177705224?pwd=Tzl1SmpLbUZ4U1NpNlB2NTNURDZJdz09','https://us04web.zoom.us/j/78177705224?pwd=Tzl1SmpLbUZ4U1NpNlB2NTNURDZJdz09','https://us04web.zoom.us/j/73179029713?pwd=KzhyRjJMV1Z6c2tDZndXOUJlWnplUT09']

            elif currentDay == 5:
                dayName = "Суббота"
                lessons = ['Программное обеспечение SCADA(лабораторное занятие). Шаяхметова А. С.', 'Программное обеспечение SCADA(лабораторное занятие). Шаяхметова А. С.']
                links = ['https://us04web.zoom.us/j/8506761940?pwd=Mm1sRENaYWVGaTRuYXRmZWYyT01idz09','https://us04web.zoom.us/j/8506761940?pwd=Mm1sRENaYWVGaTRuYXRmZWYyT01idz09']

            elif currentDay == 6:
                dayName = "Воскресенье"
                lessons = ['Расслабся, отдыхай...']
                links = ['Можешь позволить...']

            await message.channel.send('Дата: ' + str(currentDate) + '\n' + 'День недели: ' + dayName + '\n' + 'Уроки на сегодня: ')

            for i in range(1, len(lessons)+1):
                await message.channel.send(str(i)+') ' + str(lessons[i-1]) + "\n" + 'Cсылка: ' + str(links[i-1]))



        # Блок для игр
        if message.content.lower().startswith('сыграем?'):
            await message.channel.send('В какую? Выбери из списка: ' + str(games[0]))

        if message.content.lower().startswith('кость'):
            await message.channel.send('Хорошо я кидаю первый!')
            numberBot = randomizer()
            time.sleep(2)
            await message.channel.send('Амиго, у меня ' + str(numberBot) + '. Теперь ты, думаю удача на моей стороне')
            numberClient = randomizer()
            time.sleep(3)
            await message.channel.send('Твой результат: ' + str(numberClient))
            time.sleep(.5)
            if (numberBot > numberClient):
                await message.channel.send('Это игра требует опыта и некоторых навыков, иди потренеруйся :D')

            elif (numberBot < numberClient):
                await message.channel.send('Дуракам везет')

            else:
                await message.channel.send('Вроде я был сильнее, ну ладно... бывает и такое')
            #await message.channel.send('Данный игры нет в моем арсенале, если хочешь поиграть, попроси администратора добавить ее! Я быстро обучаюсь')

    except:
        return

@client.command( pass_context = True )
async def clear(ctx, amount = 10000):
    print('wa')
    await ctx.channel.purge(limit=amount)

client.run('ODA3NjM3MjU3NzgyOTUxOTM3.YB64zw.UEYaC7SdxjCc53Kg3TL_DWTIk50')



