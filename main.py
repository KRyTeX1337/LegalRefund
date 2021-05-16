from experta import *

class Result(Fact):
    resultValue = Field(bool)

class ShoppingBuddy(KnowledgeEngine):
    """
    @DefFacts()
    def startup(self):
        yield Result(resultValue=False)
    """
    @Rule(Fact(vertrag="true"),
          salience=3)
    def vertragIst(self):
        self.blaNicht()
        return "test"
    @Rule(Fact(entgeld="true"),
          salience=2)
    def EntgeldIst(self):
        self.blaNicht()
    @Rule(Fact(bla="false"),
          salience=1)
    def blaNicht(self):
        self.declare(Result(resultValue=False))
        self.halt()

    @Rule(salience=0)
    def fail(self):
        #print("sie können zurücktreten")
        self.declare(Result(resultValue=True))
"""
engine = ShoppingBuddy()
engine.reset()
engine.declare(Fact(vertrag=False), Fact(entgeld=False), Fact(bla=True))
engine.run()
result = str(engine.facts.get(4).values())

if result.__contains__("True"):
    print("rücktritt")
else:
    print("nope du hund")
"""

def get_response(answers):
    decision = False
    engine = ShoppingBuddy()
    engine.reset()
    engine.declare(Fact(vertrag=answers["frage0"]), Fact(entgeld=answers["frage1"]), Fact(bla="true"))
    engine.run()
    result = str(engine.facts.get(4).values())
    if result.__contains__("True"):
        return "rücktritt"
    else:
        return "kein rücktritt"

def formatRequest(request):
    answers = request.split("&")
    formattedAnswers = {}
    for x in answers:
        answer = x.split("=")
        formattedAnswers.update({answer[0]:[answer[1]]})
    return formattedAnswers