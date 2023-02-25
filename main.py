import discord
from discord import app_commands
from discord.ext import commands

Thehyper = commands.Bot(command_prefix="", intents= discord.Intents.all()) # تقدر تغير command_prefix للبريفكس الي تبيه في حال كنت بتضيف اوامر بدون سلاش كوماند ولكن يمكنك تخليه فارغ 

@Thehyper.event #علشان يعلمك ان البوت اونلاين و كذلك يسوي مزامنه بين البوت و الأوامر
async def on_ready():
    print('am on sir')
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e) 
        
@Thehyper.tree.command(name="letsstart") # ممكنك تغير اسم الكوماند اذا غيرت كلمة "letsstart" لأي شي تبيه
async def letsstart(interaction: discord.Integration):
    await interaction.response.send_message(f"Hey {interaction.user.mention}!",# هنا بيرد على العضو الي استعمل الأمر بمنشن مع الرسالة 
    ephemeral=True) # هنا علشان تظهر للعضو بس، تقدر تخليها False او تشيلها 
      
Thehyper.run("خلي التوكن هنا")
