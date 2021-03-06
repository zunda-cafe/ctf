# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-05-22 11:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='タイトル')),
                ('content', models.TextField(max_length=4096, verbose_name='問題')),
                ('flag', models.CharField(max_length=256, verbose_name='フラグ')),
                ('point', models.IntegerField(choices=[(100, '100'), (200, '200'), (300, '300'), (400, '400'), (500, '500')], default=100, verbose_name='ポイント')),
                ('genre', models.CharField(choices=[('Binary', 'Binary'), ('Crypt', 'Crypt'), ('Misc', 'Misc'), ('NW', 'NW'), ('Programming', 'Programming'), ('Web', 'Web')], max_length=256, verbose_name='ジャンル')),
                ('hint1', models.TextField(blank=True, max_length=4096, verbose_name='ヒント１')),
                ('hint2', models.TextField(blank=True, max_length=4096, verbose_name='ヒント２')),
                ('answer', models.TextField(blank=True, max_length=4096, verbose_name='解説')),
                ('disp_no', models.IntegerField(default=99, verbose_name='表示番号')),
                ('status', models.CharField(choices=[('new', '新規'), ('private', '非公開'), ('public', '公開中'), ('cancel', '取消')], max_length=16, verbose_name='ステータス')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('assigned_to', models.CharField(max_length=256, verbose_name='担当者')),
            ],
            options={
                'verbose_name': '問題',
                'verbose_name_plural': '問題',
            },
        ),
        migrations.CreateModel(
            name='Winner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1024, verbose_name='ハンドル名')),
                ('point', models.IntegerField(verbose_name='点数')),
                ('answered_at', models.DateTimeField(verbose_name='回答日時')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='challenge.Question')),
            ],
            options={
                'verbose_name': '正解者',
                'verbose_name_plural': '正解者',
            },
        ),
    ]
