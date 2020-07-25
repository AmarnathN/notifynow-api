from rest_framework import views
from rest_framework.response import Response
from core.models import User, UserMail, ForwardMailId, Consent, Notification
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

            notify_on_whatsApp = False

            if "is now on Netflix".lower() in mail_subject.lower():

                header_elem = soup.select('[id*="-header-copy"]')
                profile = header_elem[0].get_text().strip().replace("For ","")
                print("profile : {}".format(profile))
                
                main_link_elem = soup.select('a[href*="PRIMARY_HERO_IMAGE"]')[0]
                notifcation_link = main_link_elem['href']
                print("notifcation_link : {}".format(notifcation_link))

                # main_img_elem = soup.select('[class*="-component-image-cell"] img')[0]
                notifcation_img = main_link_elem.find('img')['src']
                print("notifcation_img : {}".format(notifcation_img))

                subject = mail_subject.replace("Fwd:","")
                message_body = "{}\n\nDear {},\nPlease find the Netflix Show @ \n\n{}".format(subject,profile,notifcation_link)

                notify_on_whatsApp = True
                notification = Notification.objects.get(notification_type='Netflix')
            
            if "recently added on Prime Video".lower() in mail_subject.lower():
                
                mail_subject_elem = mail_subject.split(',')
                profile = mail_subject_elem[0].replace("Fwd:","")
                print("profile : {}".format(profile))

                main_link_elem = soup.select('a[href*="HE_1"]')[0]
                notifcation_link = main_link_elem['href']
                print("notifcation_link : {}".format(notifcation_link))

                # main_img_elem = soup.select('[class*="-component-image-cell"] img')[0]
                notifcation_img = main_link_elem.find('img')['src']
                print("notifcation_img : {}".format(notifcation_img))

                subject = mail_subject_elem[len(mail_subject_elem) - 1]
                message_body = "{}\n\nDear {},\nPlease find the Prime Video Show @ \n\n{}".format(subject, profile, notifcation_link)
                
                notify_on_whatsApp = True
                notification = Notification.objects.get(notification_type='Prime Video')
                
            
            if notify_on_whatsApp:
                
                try:
                    user_notification_consent =  Consent.objects.get(user=user,notification_type=notification)
                    user_whatsapp_consent = user_notification_consent.whatsapp
                except Exception as e:
                    print(e)
                    print("No Consents Available for user - {} and notification-type - {}".format(user.email,notification.notification_type))
                    return Response({"success": False})

                if user_whatsapp_consent:
                    client = Client(account_sid, auth_token)
                    message = client.messages.create(
                        media_url=[notifcation_img],
                        from_="whatsapp:+14155238886",
                        body=(message_body),
                        to="whatsapp:{}".format(user.phone_number),
                    )
                    print(
                        "notify has been whatsapped to {} !!! and mail saved to user mails".format(
                            sender
                        )
                    )
                else:
                    print(
                        "notify whatsApp has been disabled for user -  {} !!! \n hence no notification sent and mail saved to user mails".format(
                            sender
                        )
                    )
            else:
                print(
                    "not valid notify mail format, saved in {} mails".format(
                        userMail.user.email
                    )
                )

            return Response({"success": True})
        except Exception as e:
            print(e)
            return Response({"success": False})
