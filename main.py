from experta import *


class Result(Fact):
    resultValue = Field(bool)


class LegalRefund(KnowledgeEngine):
    """
    @DefFacts()
    def startup(self):
        yield Result(resultValue=False)
    """

    @Rule(Fact(frage0="true"), salience=0)
    def frage0true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="false"), salience=0)
    def frage0false(self):
        self.declare(Result(resultValue=False,
                            law="Sie handeln als Unternehmer*in. Daher können Sie nicht vom Rücktrittsrecht Gebrauch machen. Für alternative Möglichkeiten und eine detaillierte Prüfung Ihrer Rechtsfrage können Ihnen folgende Anwaltskanzleien weiterhelfen. (Rechtsgrundlagen: § 1 Konsumentenschutzgesetz, § 11 Fern- und Auswärtsgeschäfte-Gesetz)"))

    @Rule(Fact(frage0="true"), Fact(frage1="true"), salience=1)
    def frage1true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="false"), salience=1)
    def frage1false(self):
        self.declare(Result(resultValue=False,
                            law="Ihr*e Vertragspartner*in handelt nicht als Unternehmer*in. Daher können Sie nicht vom Rücktrittsrecht Gebrauch machen. Für alternative Rücktrittsmöglichkeiten und eine detaillierte Prüfung Ihrer Rechtsfrage können Ihnen folgende Anwaltskanzleien weiterhelfen. (Rechtsquellen: § 1 Konsumentenschutzgesetz, § 11 Fern- und Auswärtsgeschäfte-Gesetz)"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), salience=2)
    def frage2true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="false"), salience=2)
    def frage2false(self):
        self.declare(Result(resultValue=False,
                            law="Bei dem Kauf handelt es sich nicht um einen Fernabsatzvertrag, da der Kauf nicht über ein dafür organisiertes System und/oder ohne körperlichen Anwesenheit erfolgt ist. (Rechtsquellen: gem §3 Z 2 Fern- und Auswärtsgeschäfte-Gesetz)"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), salience=3)
    def frage3true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="false"), salience=3)
    def frage3false(self):
        self.declare(Result(resultValue=False,
                            law="Bei dem Kauf handelt es sich nicht um einen Fernabsatzvertrag, da der Kauf nicht über ein dafür organisiertes System und/oder ohne körperlichen Anwesenheit erfolgt ist. (Rechtsquellen: gem §3 Z 2 Fern- und Auswärtsgeschäfte-Gesetz)"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="true"),
          salience=4)
    def frage4true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          salience=4)
    def frage4false(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="true"),
          Fact(frage5="true"),
          salience=5)
    def frage5true(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"),
          salience=5)
    def frage5false(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="true"),
          Fact(frage5="true"), Fact(frage6="true"),
          salience=6)
    def frage6false(self):
        self.declare(Result(resultValue=False, law="Haben Sie keine Rücktrittserklärung binnen 14 Tagen abgeschickt und wurden Sie rechtmäßig über das Rücktrittsrecht belehrt, so kann kein Rücktritt mehr erklärt werden (§11 FAGG). "))
        self.halt()

    # print("sie können zurücktreten")
    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="true"),
          Fact(frage5="true"), Fact(frage6="false"),
          salience=6)
    def rücktritt(self):
        self.declare(Result(resultValue=False,
                            law="Ihren Angaben nach haben Sie die Rücktrittsmöglichkeit nach § 11 FAGG. Da es sich hierbei aber um eine Vorabschätzung handelt, wird die Beratung von Rechtsanwält*innen empfohlen. Die folgenden Ansprechpersonen stehen Ihnen hierfür zur Verfühung:"))
        self.halt()

"""
engine = LegalRefund()
engine.reset()
engine.declare(Fact(vertrag=False), Fact(entgeld=False), Fact(bla=True))
engine.run()
result = str(engine.facts.get(4).values())

if result.__contains__("True"):
    print("rücktritt")
else:
    print("nein")
"""


def get_response(answers):
    decision = False
    engine = LegalRefund()
    engine.reset()
    for i in range(len(answers)):
        engine.declare(Fact(**{'frage' + str(i): answers[i]}))
    engine.run()
    result = list(engine.facts.get(engine.facts.last_index - 1).values())
    return {"value": str(result[0]), "law": result[1]}


def formatRequest(request):
    answers = request.split("&")
    formattedAnswers = []
    for x in answers:
        answer = x.split("=")
        formattedAnswers.append(answer[1])
    return formattedAnswers
