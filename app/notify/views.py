from rest_framework import views
from rest_framework.response import Response
from core.models import User, UserMail
from twilio.rest import Client
import json
import sys


class NotifyView(views.APIView):
    # permission_classes = []

    def post(self, request):
        account_sid = "AC26655be2355e4c0ee534631e5376092a"
        auth_token = "dc70288083ae78b1a63be865bf573838"
        try:
            data = request.data
            mail_subject = data.get("subject")
            sender = data.get("sender")
            print("Sender : {} ".format(sender))
            user = list(User.objects.filter(email=sender).values())[0]
            userMail = UserMail(
                    user=User.objects.get(email=sender), user_mail=json.dumps(data)
                )
            userMail.save()
            if "is now on Netflix".lower() in mail_subject.lower():
                client = Client(account_sid, auth_token)
                message = client.messages.create(
                    media_url=[
                        "https://www.gannett-cdn.com/presto/2019/07/24/USAT/4cb62745-ee53-4eca-8905-c34f0da4faf7-VPC_COMING_TO_NETFLIX_AUG_DESK_THUMB.00_00_23_11.Still002.jpg?width=1320&height=744&fit=crop&format=pjpg&auto=webp"
                    ],
                    from_="whatsapp:+14155238886",
                    body=(mail_subject),
                    to="whatsapp:{}".format(user["phone_number"]),
                )
                print(
                    "notify mail from netflix has been whatsapped to {} !!! and mail samed to user mails".format(
                        sender
                    )
                )
            else:
                print(
                    "not valid notify mail from netflix, saved in {} mails".format(
                        sender
                    )
                )

            return Response({"success": True})
        except Exception as e:
            print(e)
            return Response({"success": False})
