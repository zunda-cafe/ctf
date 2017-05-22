#! /bin/python

from django.core.management.base import BaseCommand
from redmine import Redmine
import django
import re
from challenge.models import Question, Winner
from datetime import datetime as dt
from datetime import timedelta

class Command(BaseCommand):

    def handle(self, *args, **options):

        API_KEY = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        PROJECT_ID_CTF = 'ctf'
        TRACKER_ID_CTF = 4

        rm = Redmine('http://xxx.xxx.xxx.xxx/redmine', key=API_KEY)
        pj = rm.project.get(PROJECT_ID_CTF)
        issues = rm.issue.filter(project_id=PROJECT_ID_CTF, tracker_id=TRACKER_ID_CTF)
        for i in issues:
            q = Question(title=i.subject,
                         content=i.description,
                         point=int(self.__custom_field(i, 'ポイント')),
                         flag=self.__custom_field(i, 'FLAG'),
                         hint1=self.__custom_field(i, 'ヒント１'),
                         hint2=self.__custom_field(i, 'ヒント２'),
                         answer=self.__custom_field(i, '解説'),
                         disp_no=self.__custom_field(i, '問題番号'),
                         status=self.__status(i),
                         assigned_to=i.assigned_to['name'],
                         created_at=dt.strptime(str(i.created_on),'%Y-%m-%d %H:%M:%S'),
                         updated_at=dt.strptime(str(i.updated_on),'%Y-%m-%d %H:%M:%S'),
                         genre=i.category['name'], )
            q.save()
            for jnl in i.journals:
                notes = jnl['notes']
                m = re.search(r"「(.+)」 さんが正解しました。得点は (\d+) 点です。", notes)
                if m:
                    w = Winner(
                        name=m.group(1),
                        point=m.group(2),
                        answered_at=jnl['created_on'] + timedelta(hours = 9),
                        question = q,
                    )
                    w.save()

    def __custom_field(self, issue, name):
        cfs = issue.custom_fields
        return [cf['value'] for cf in cfs if cf['name'] == name][0]

    def __status(self, issue):
        STATUS_DICT = {'新規': 'new',
                       '非公開': 'private',
                       '公開中': 'public',
                       '取消': 'cancel', }
        return STATUS_DICT[issue.status['name']]
