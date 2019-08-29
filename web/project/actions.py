import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

from api.models import AlarmTask


@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    intent_name = req['queryResult']['intent']['displayName']
    speak_output = 'よくわかりませんでした'

    if intent_name == 'AlarmIntent':
        date_string = req['queryResult']['parameters']['datetime']
        date = timezone.datetime.fromisoformat(date_string)

        AlarmTask.objects.create(sounds_at=date)
        speak_output = f'{date.strftime("%-m月%-d日%-H時%-M分%-S秒にアラームタスクをセットしました")}'

    if intent_name == 'AlarmDeleteIntent':
        for task in AlarmTask.objects.all():
            task.delete()
        speak_output = '全てのアラームタスクを削除しました'

    return JsonResponse({'fulfillmentText': speak_output})
