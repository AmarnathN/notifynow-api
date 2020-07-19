from rest_framework import views
from rest_framework.response import Response
from core.models import User, UserMail, ForwardMailId
from twilio.rest import Client
import json
import sys
import os
from bs4 import BeautifulSoup


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
            elif(len(users)>0):
                user = User.objects.get(email=sender)
                userMail = UserMail(
                        user=user, mail_from=sender, user_mail=json.dumps(data)
                    )
                userMail.save()
            else:
                print("Anonymous mail")
                user = User.objects.get(email="anonymous@gmail.com")
                userMail = UserMail(
                        user=user, mail_from=sender, user_mail=json.dumps(data)
                    )
                return Response({"success": False})
                
            html_data = data.get('stripped-html')
            soup = BeautifulSoup(html_data,'html.parser')

            if "is now on Netflix".lower() in mail_subject.lower():
                # print(soup.prettify())
                header_elem = soup.select('[id*="-header-copy"]')
                profile = header_elem[0].get_text().strip().replace("For ","")
                print("profile : {}".format(profile))
                
                main_link_elem = soup.select('a[href*="PRIMARY_HERO_IMAGE"]')[0]
                notifcation_link = main_link_elem['href']
                print("notifcation_link : {}".format(notifcation_link))

                # main_img_elem = soup.select('[class*="-component-image-cell"] img')[0]
                notifcation_img = main_link_elem.find('img')['src']
                print("notifcation_img : {}".format(notifcation_img))

                message_body = "{} \n\nPlease find the Show @ \n\nDear {},\n{}".format(mail_subject,profile, notifcation_link)
                client = Client(account_sid, auth_token)
                
                message = client.messages.create(
                    media_url=[notifcation_img],
                    from_="whatsapp:+14155238886",
                    body=(message_body),
                    to="whatsapp:{}".format(user.phone_number),
                )
                print(
                    "notify mail from netflix has been whatsapped to {} !!! and mail saved to user mails".format(
                        sender
                    )
                )
            else:
                print(
                    "not valid notify mail from netflix, saved in {} mails".format(
                        userMail.user.email
                    )
                )

            return Response({"success": True})
        except Exception as e:
            print(e)
            return Response({"success": False})
