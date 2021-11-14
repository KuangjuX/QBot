from nonebot import on_command, CommandSession, session 
from nonebot import on_natural_language, NLPSession, IntentCommand
from .handler import req_top_vedio

@on_command('BiliBili-Top-Vedio', aliases=('BiliBili', 'B站热榜', 'B站视频'))
async def top_vedio(session: CommandSession):
    print("获取B站热榜")
    videos = await req_top_vedio()
    msg = ""
    for vedio in videos:
        msg += vedio["title"]
        msg += "  "
        msg += vedio["short_link"]
        msg += "\n"
        print(msg)
    await session.send(msg)


@on_natural_language(keywords={'B站热榜', 'B站视频', 'BiliBili', 'bilibili'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'BiliBili-Top-Vedio')