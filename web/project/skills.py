from datetime import datetime

from django_ask_sdk.skill_adapter import SkillAdapter
import ask_sdk_core.utils as ask_utils
from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_model import Response


class LaunchRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type('LaunchRequest')(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = 'テストスキルです。何か入力してください'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelloWorldIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name('SampleIntent')(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        slots = handler_input.request_envelope.request.intent.slots

        speak_output = 'スロットを読み込めませんでした'
        if type(slots) is dict and 'Time' in slots.keys():
            try:
                date = datetime.fromisoformat(slots['Time'].value)
                labels = ['月', '火', '水', '木', '金', '土', '日']
                speak_output = f'{date.strftime("%Y年%m月%d日")}は{labels[date.weekday()]}曜日です'
            except:
                speak_output = str(slots['Time'].value) + 'はうまく処理できませんでした'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class HelpIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_intent_name('AMAZON.HelpIntent')(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = 'ヘルプを開きました'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )


class CancelOrStopIntentHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return (ask_utils.is_intent_name('AMAZON.CancelIntent')(handler_input) or
                ask_utils.is_intent_name('AMAZON.StopIntent')(handler_input))

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = 'キャンセルしました'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


class SessionEndedRequestHandler(AbstractRequestHandler):

    def can_handle(self, handler_input: HandlerInput) -> bool:
        return ask_utils.is_request_type('SessionEndedRequest')(handler_input)

    def handle(self, handler_input: HandlerInput) -> Response:
        speak_output = '終了しました'

        return (
            handler_input.response_builder
                .speak(speak_output)
                .response
        )


sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(HelloWorldIntentHandler())
sb.add_request_handler(HelpIntentHandler())
sb.add_request_handler(CancelOrStopIntentHandler())
sb.add_request_handler(SessionEndedRequestHandler())

skill = sb.create()
skill_view = SkillAdapter.as_view(skill=skill)
