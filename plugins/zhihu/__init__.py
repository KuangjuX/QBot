from nonebot import on_command, CommandSession, session 
from nonebot import on_natural_language, NLPSession, IntentCommand
from .handler import req_top_topic

@on_command('ZhiHu-Top-Topic')
async def top_vedio(session: CommandSession):
    print("获取知乎热榜")
    topics = await req_top_topic()
    msg = ""
    for topic in topics:
        question = topic['display_query']
        msg += question
        msg += "  "
        msg += "https://www.zhihu.com/search?q="+str(question)+"&type=content"
        msg += "\n"
    await session.send(msg)


@on_natural_language(keywords={'知乎热搜', '知乎热榜'})
async def _(session: NLPSession):
    return IntentCommand(90.0, 'ZhiHu-Top-Topic')