from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, FileExtensionValidator
from django.conf import settings
from ckeditor.fields import RichTextField
from django.db.models import JSONField
from model_utils import FieldTracker


class CourseModel(models.Model):
    course_name = models.CharField("Course name", max_length=100)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    

    class Meta:
        verbose_name = "Course"

    def __str__(self):
        return self.course_name


class SubjectModel(models.Model):
    subject_name = models.CharField("Subject", max_length=100)
    instruction_hours = models.PositiveSmallIntegerField("Instruction hours", validators=[
        MaxValueValidator(200)])
    created_at = models.DateTimeField("Created at" ,auto_now_add=True)
    course = models.ForeignKey(CourseModel(), on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return self.subject_name

    class Meta:
        verbose_name = "Subject"



def question_files(instance, filename):
    return '\\'.join([settings.BASE_DIR, 'question_files', instance.question_ref_code, filename])

class QuestionModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                    related_name="questions", blank=True)
    question_content = RichTextField(verbose_name="Question", blank=False)
    question_ref_code = models.CharField(max_length=10, unique=True, blank=True)
    opt_1 = RichTextField(verbose_name="A", blank=False)
    opt_2 = RichTextField(verbose_name="B", blank=False)
    opt_3 = RichTextField(verbose_name="C", blank=False)
    opt_4 = RichTextField(verbose_name="D", null=True,blank=True)
    question_file = models.FileField("Question supplementary file", null=True,
            upload_to=question_files, blank=True)
    correct_answer = models.CharField("Correct answer", choices=(("1", "A"), ("2", "B"), ("3", "C"), ("4", "D")),
                                        max_length=1)
    difficulty_level = models.CharField("Difficulty Level", choices=(("easy", "Easy"), ("medium", "Medium"),
                                                            ("hard", "Hard"), ("very hard", "Very hard")), max_length=20)
    numb_of_appeared = models.IntegerField("Number of times the question appeared in exams", default=0)
    correctly_answered_times = models.IntegerField("Number of times the question answered correctly", default=0)
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, related_name="sub_questions", null=True)


    def __str__(self):
        return self.question_ref_code

    class Meta:
        verbose_name = "Question bank"


class AbstractExamModel(models.Model):
    exam_name = models.CharField("Exam Name", max_length=50, unique=True)
    noq_total = models.IntegerField("Number of questions", validators=[MinValueValidator(1)], default=1)
    exam_duration = models.IntegerField("Exam duration in minutes", validators=[MinValueValidator(1)],
                                         default=1)
    
    pass_score = models.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)], default=50)
    is_active = models.BooleanField("Exam model is active?", default=True)
    created_at = models.DateTimeField("Created at", auto_now_add=True)

    class Meta:
        abstract = True
    


class SubjectExamModel(AbstractExamModel):
    subject = models.ForeignKey(SubjectModel, related_name="subject_exams", on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name = "Subject based exam"


    def __str__(self):
        return self.exam_name + self.subject.subject_name

class CourseExamModel(AbstractExamModel):
    course = models.ForeignKey(CourseModel, on_delete = models.CASCADE,
                                                related_name = "course_exam")
    tracker = FieldTracker(fields=['course'])
    
    
    class Meta:
        verbose_name = "Course based exam"


    def __str__(self):
        return self.exam_name + self.course.course_name

class PerSubjectModel(models.Model):
    course_exam = models.ForeignKey(CourseExamModel, on_delete=models.CASCADE,
                                    related_name="exam_for_course")
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE, related_name="subjects_for_exam")
    noq_subject = models.IntegerField("Number of questions in this subject", 
        help_text="Total number of questions should not exceed exam's number of questions", default=0)

    def __str__(self):
        return self.course_exam.exam_name + ' - ' + self.subject.subject_name
    