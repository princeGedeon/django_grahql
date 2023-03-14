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

class CategoryMutation(graphene.Mutation):
    class Arguments:
        name=graphene.String(required=True)

    category=graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,name):
        #Le nom de l'atrtribut en parametre
        category=Category(name=name)
        #Pour save
        category.save()
        return  CategoryMutation(category=category)

class CategoryMutation2(graphene.Mutation):
    class Arguments:
        id=graphene.ID()#Un identifiant
        #name=graphene.String(required=True)
    category=graphene.Field(CategoryType)

    @classmethod
    def mutate(cls,root,info,id):
        category=Category.objects.get(id=id)#Récupérer l'objet
        #category.name=name #Modifier donnée

        category.delete()
        return

class Mutation(graphene.ObjectType):
    add_category=CategoryMutation.Field()
    #update_category=CategoryMutation2.Field()
    delete_category = CategoryMutation2.Field()

schema=graphene.Schema(query=Query,mutation=Mutation)