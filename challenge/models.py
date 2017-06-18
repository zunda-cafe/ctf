from django.db import models

class Question(models.Model):

    GENRE_CHOICES = (
        ('Binary', 'Binary'),
        ('Crypt', 'Crypt'),
        ('Misc', 'Misc'),
        ('NW', 'NW'),
        ('Programming', 'Programming'),
        ('Web', 'Web'),
    )

    POINT_CHOICES = (
        (100, '100'),
        (200, '200'),
        (300, '300'),
        (400, '400'),
        (500, '500'),
    )

    STATUS_CHOICES = (
        ('new', '新規'),
        ('private', '非公開'),
        ('public', '公開中'),
        ('cancel', '取消'),
    )

    title = models.CharField('タイトル',
        max_length=256)
    content = models.TextField('問題',
        max_length=4096)
    flag = models.CharField('フラグ',
        max_length=256)
    point = models.IntegerField('ポイント',
        choices=POINT_CHOICES,
        default=100)
    genre = models.CharField('ジャンル',
        max_length=256,
        choices=GENRE_CHOICES)
    hint1 = models.TextField('ヒント１',
        max_length=4096,
        blank=True)
    hint2 = models.TextField('ヒント２',
        max_length=4096,
        blank=True)
    answer = models.TextField('解説',
        max_length=4096,
        blank=True)
    disp_no = models.IntegerField('表示番号',
        default=99)
    status = models.CharField('ステータス',
        max_length=16,
        choices=STATUS_CHOICES)
    created_at = models.DateTimeField('作成日時',
        auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)
    assigned_to = models.CharField('担当者', max_length=256)

    def __str__(self):
        return self.title

    def valid_point(self):
        """
        現在の点数を計算する

        >>> q = Question.objects.create(point=500)
        >>> q.valid_point()
        500
        >>> q.hint1 = "hint1"
        >>> q.save()
        >>> q.valid_point()
        400
        >>> q.hint2 = "hint2"
        >>> q.save()
        >>> q.valid_point()
        250
        >>> q.answer = "answer"
        >>> q.save()
        >>> q.valid_point()
        0
        """
        vp = self.point
        if self.answer != "":
            vp = 0
        elif self.hint1 != "" and self.hint2 == "":
            vp = round(self.point * 0.8)
        elif self.hint1 != "" and self.hint2 != "":
            vp = round(self.point * 0.5)
        return vp

    class Meta(object):
        verbose_name = '問題'
        verbose_name_plural = '問題'

class Winner(models.Model):
    name = models.CharField('ハンドル名', max_length=1024)
    point = models.IntegerField('点数')
    answered_at = models.DateTimeField('回答日時', auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    class Meta(object):
        verbose_name = '正解者'
        verbose_name_plural = '正解者'
