import discord
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="", intents= discord.Intents.all()) # تقدر تغير command_prefix للبريفكس الي تبيه في حال كنت بتضيف اوامر بدون سلاش كوماند ولكن يمكنك تخليه فارغ 

@bot.event #علشان يعلمك ان البوت اونلاين و كذلك يسوي مزامنه بين البوت و الأوامر
async def on_ready():
    print('am on sir')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e) 
        
@bot.tree.command(name="test") # ممكنك تغير اسم الكوماند اذا غيرت كلمة "test" لأي شي تبيه
async def hello(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!",# هنا بيرد على العضو الي استعمل الأمر بمنشن مع الرسالة 
    ephemeral=True) # هنا علشان تظهر للعضو بس، تقدر تخليها False او تشيلها 
      
bot.run("خلي التوكن هنا")
