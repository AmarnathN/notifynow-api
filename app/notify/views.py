from rest_framework import views
from rest_framework.response import Response
from core.models import User, UserMail, ForwardMailId
from twilio.rest import Client
import json
import sys
import os


class NotifyView(views.APIView):
    # permission_classes = []

    def post(self, request):
        account_sid = os.getenv("TWILIO_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        try:
            data = request.data
            mail_subject = data.get("subject")
            sender = data.get("sender")
            print("Sender : {} ".format(sender))
            print(mail_subject)
            SECRET_KEY = os.getenv("ENV_KEY")
            print(SECRET_KEY)
            users = list(User.objects.filter(email=sender).values())
            if("Gmail Forwarding Confirmation" in mail_subject  ):
                subject_array = mail_subject.split()
                email_from = subject_array[ len(subject_array) - 1 ]
                user = User.objects.get(email=email_from)
                if(user):
                    userMail = UserMail(user=user, mail_from=sender, user_mail=json.dumps(data))
                    userMail.save()
                else:
                    print("Anonymous mail")
                    return Response({"success": False})
            elif ("+caf_=vayu=notifynow.in" in sender ):
                sender = sender.replace("+caf_=vayu=notifynow.in","")
                user = User.objects.get(email=sender)
                if(user):
                    userMail = UserMail(user=user, mail_from=sender, user_mail=json.dumps(data))
                    userMail.save()
                else:
                    print("Anonymous mail")
                    return Response({"success": False})
            else:
                user = User.objects.get(email=sender)
                userMail = UserMail(
                        user=user, mail_from=sender, user_mail=json.dumps(data)
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
                    to="whatsapp:{}".format(user.phone_number),
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
