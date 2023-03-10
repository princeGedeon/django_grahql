import graphene
from graphene_django import DjangoObjectType
from graphene_django import DjangoListField
from quiz.models import Category, Question, Quizzes, Answer


class CategoryType(DjangoObjectType):
    class Meta:
        model=Category
        fields=('id','name')


class QuizzesType(DjangoObjectType):
    class Meta:
        model = Quizzes
        fields = ('id', 'title','category',)


class QuestionType(DjangoObjectType):
    class Meta:
        model=Question
        fields=('quiz','title','technique','difficulty')



class AnswerType(DjangoObjectType):
    class Meta:
        model = Answer
        fields = ('question', 'answer_text')


"""class Query(graphene.ObjectType):
   all_quizzes=DjangoListField(QuizzesType)
"""

"""class Query(graphene.ObjectType):
   all_quizzes=graphene.List(QuizzesType)

   def resolve_all_quizzes(root,info):
       return Quizzes.objects.all()"""

"""class Query(graphene.ObjectType):
   all_quizzes=graphene.List(QuizzesType)
   all_questions = graphene.List(QuestionType)

   def resolve_all_quizzes(root,info):
       return Quizzes.objects.all()

   def resolve_all_questions(root,info):
       return Question.objects.all()"""

"""class Query(graphene.ObjectType):
   all_quizzes=graphene.Field(QuizzesType,id=graphene.Int())


   def resolve_all_quizzes(root,info,id):
       return Quizzes.objects.get(pk=id)"""

class Query(graphene.ObjectType):
   all_quizzes=graphene.Field(QuizzesType,id=graphene.Int())
   all_answers = graphene.List(AnswerType, id=graphene.Int())




   def resolve_all_quizzes(root,info,id):
       return Quizzes.objects.get(pk=id)

   def resolve_all_answers(root,info,id):
       return Answer.objects.filter(question=id)
schema=graphene.Schema(query=Query)