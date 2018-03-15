import requests

class Flippy:
    """MAIN FLIPPY CLASS"""

    GetMemesApi = 'https://api.imgflip.com/get_memes'
    CaptionImageApi = 'https://api.imgflip.com/caption_image'

    def genMeme(self, template_id, username, password, text0, text1, font="impact", max_font_size="50", boxes={}):
            payload=dict([('template_id',template_id), ('username',username),
            ('password',password),('text0',text0),('text1',text1),
            ('font',font),('max_font_size',max_font_size),
            ('boxes',boxes)])
            results = requests.post(self.CaptionImageApi,params=payload)
            data = results.json()
            if(data["success"] == True):
                return(data["data"]["url"])
            else:
                return(data["error_message"])
    def getAvailableMemes(self):
        results = requests.get(self.GetMemesApi)
        return results.json())
