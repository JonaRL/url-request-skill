from mycroft import MycroftSkill, intent_file_handler


class UrlRequest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('request.url.intent')
    def handle_request_url(self, message):
        self.speak_dialog('request.url')


def create_skill():
    return UrlRequest()

