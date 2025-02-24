from datetime import datetime
from DjangoUeditor.models import UEditorField
from django.db import models

from organization.models import CourseOrg,Teacher

# Create your models here.


class Course(models.Model):
    """
    课程信息
    """
    course_org = models.ForeignKey(CourseOrg,verbose_name="课程机构",null=True,blank=True)
    name = models.CharField(max_length=50,verbose_name="课程名")
    desc = models.CharField(max_length=300,verbose_name="课程描述")
    detail = UEditorField(verbose_name="课程详情",width=600, height=300, imagePath="courses/ueditor/",
                                         filePath="courses/ueditor/", default='')
    is_banner = models.BooleanField(default=False, verbose_name=u"是否轮播")
    teacher = models.ForeignKey(Teacher,verbose_name=u"讲师", null=True, blank=True,related_name="courses_teacher")
    degree = models.CharField(verbose_name="难度",choices=(("cj","初级"),("zj","中级"),("gj","高级")),max_length=2)
    learn_times = models.IntegerField(default=0,verbose_name="学习时长(分钟数)")
    students = models.IntegerField(default=0,verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0,verbose_name="收藏人数")
    image = models.ImageField(upload_to="courses/%Y/%m",verbose_name="封面")
    click_nums = models.IntegerField(default=0,verbose_name="点击数")
    category = models.CharField(default="",max_length=20,verbose_name="课程类别")
    tag = models.CharField(default="",verbose_name="课程标签",max_length=10)
    youneed_know = models.CharField(default="",max_length=300,verbose_name="课程须知")
    teacher_tell = models.CharField(default="",max_length=300,verbose_name="老师告诉你")
    add_time = models.DateTimeField(default=datetime.now,verbose_name="添加时间")

    class Meta:
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    #获取课程章节数
    def get_zj_nums(self):
        return self.lesson_set.all().count()
    get_zj_nums.short_description = "章节数" #自定义函数作为列显示

    def go_to(self):
        from django.utils.safestring import mark_safe
        return mark_safe("<a href='http://www.baidu.com'>跳转</>")
    go_to.short_description = "跳转"
    #获取学习该课程的用户
    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    # 获取课程的章节
    def get_course_lesson(self):
        return self.lesson_set.all()

    def __str__(self):
        return self.name


class Lesson(models.Model):

    """
    课程章节
    """
    course = models.ForeignKey(Course,verbose_name="课程")
    name = models.CharField(max_length=100,verbose_name="章节名")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    # 获取章节所有视频
    def get_lesson_vedio(self):
        return self.video_set.all()

    def __str__(self):
        return self.name


class Video(models.Model):
    """
    章节视频
    """
    lesson = models.ForeignKey(Lesson, verbose_name="章节")
    name = models.CharField(max_length=100, verbose_name="视频名")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长(分钟数)")
    url = models.CharField(max_length=200,default="",verbose_name="访问地址")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    """
    课程资源
    """
    course = models.ForeignKey(Course, verbose_name="课程")
    name = models.CharField(max_length=100, verbose_name="名称")
    download = models.FileField(upload_to="course/resource/%Y%m",verbose_name="资源文件",max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name


class BannerCourse(Course):
    """
    轮播课程
    """
    class Meta:
        verbose_name = "轮播课程"
        verbose_name_plural = verbose_name
        proxy = True