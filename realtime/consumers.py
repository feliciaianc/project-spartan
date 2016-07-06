import json

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from channels import Group

from chat.models import Room, Message


def ws_add(message):
    Group("chat").add(message.reply_channel)


def ws_message(message):
    data = json.loads(message['text'])
    room = get_object_or_404(Room, slug=data['room_slug'])
    user = get_object_or_404(User, username=data['user_name'])
    message = Message.objects.create(room=room, message=data['text'],
                                     submitter=user)
    dic = {
        'message': data['text'],
        'submitter': user.username
    }
    Group("chat").send({'text': json.dumps(dic)})


def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
