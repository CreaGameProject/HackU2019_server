from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json


@csrf_exempt
def webhook(request):
    req = json.loads(request.body)
    intent_name = req['queryResult']['intent']['displayName']
    speak_output = 'よくわかりませんでした'

    if intent_name == 'DayOfWeekIntent':
        key = req['queryResult']['parameters']['Time']
        relation_days_dict = {
            '今日': 0,
            '明日': 1,
            '明後日': 2,
        }

        date = timezone.now() + timezone.timedelta(days=relation_days_dict[key])
        labels = ['月', '火', '水', '木', '金', '土', '日']
        speak_output = f'{date.strftime("%Y年%m月%d日")}は{labels[date.weekday()]}曜日です'

    return JsonResponse({'fulfillmentText': speak_output})
