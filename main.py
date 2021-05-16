from experta import *


class Result(Fact):
    resultValue = Field(bool)


class ShoppingBuddy(KnowledgeEngine):
    """
    @DefFacts()
    def startup(self):
        yield Result(resultValue=False)
    """

    @Rule(Fact(frage0="true"), salience=0)
    def frage0true(self):
        self.declare(Result(resultValue=True,
                            law="Sie handeln als Verbraucher*in im Sinne des § 1 KSchG. Dadurch kann der Kaufvertrag gemäß § 1 FAGG von der Geltung des FAGG erfasst sein und möglicherweise von Ihrem Rücktrittsrecht gemäß § 11 FAGG Gebrauch machen."))
        self.halt()
    @Rule(Fact(frage0="false"), salience=0)
    def frage0false(self):
        self.declare(Result(resultValue=False,
                            law="Da Sie im Rahmen des Betriebs Ihres Unternehmens handeln, gelten Sie nicht als Verbraucher*in, sondern als Unternehmer*in im Sinne des § 1 KSchG. Daher können Sie nicht vom Rücktrittsrecht, welches in § 11 FAGG geregelt ist, Gebrauch machen. Für alternative Rücktrittsmöglichkeiten und eine detaillierte Prüfung Ihrer Rechtsfrage können Ihnen folgende Anwaltskanzleien weiterhelfen:"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), salience=1)
    def frage1true(self):
        self.declare(Result(resultValue=True,
                            law="Ihr*e Vertragspartner*in tritt als Unternehmerperson im Sinne von § 1 KSchG auf, also kann der Kaufvertrag gemäß § 1 FAGG von der Geltung des FAGG erfasst sein. Das bedeutet, dass Sie möglicherweise von Ihrem Rücktrittsrecht gemäß § 11 FAGG Gebrauch machen können."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="false"), salience=1)
    def frage1false(self):
        self.declare(Result(resultValue=False,
                            law="Ihr*e Vertragspartner*in handelt nicht als Unternehmer*in im Sinne des § 1 KSchG. Daher können Sie nicht vom Rücktrittsrecht, welches in § 11 FAGG geregelt ist, Gebrauch machen. Für alternative Rücktrittsmöglichkeiten und eine detaillierte Prüfung Ihrer Rechtsfrage können Ihnen folgende Anwaltskanzleien weiterhelfen:"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), salience=2)
    def frage2true(self):
        self.declare(Result(resultValue=True,
                            law="Der Kauf fällt in den Anwendungsbereich des FAGG, da Unternehmer*in und Verbraucher*in ohne gleichzeitig körperlich anwesend zu sein über ein dafür organisiertes System einen Vertrag abgeschlossen haben (es liegt ein Fernabsatzvertrag gem §3 Z 2 FAGG vor)."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="false"), salience=2)
    def frage2false(self):
        self.declare(Result(resultValue=False,
                            law="Bei dem Kauf handelt es sich nicht um einen Fernabsatzvertrag gem §3 Z 2 FAGG, da der Kauf nicht über ein dafür organisiertes System und/oder ohne körperlichen Anwesenheit erfolgt ist. Für alternative Rücktrittsmöglichkeiten und eine detaillierte Prüfung Ihrer Rechtsfrage können Ihnen folgende Anwaltskanzleien weiterhelfen:"))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"),Fact(frage3="true"), salience=3)
    def frage3true(self):
        self.declare(Result(resultValue=True,
                            law="Ich habe die Lieferung erhalten Seit der Lieferung sind bereits mehr als 14 Tage verstrichen."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="false"), salience=3)
    def frage3false(self):
        self.declare(Result(resultValue=True,
                            law="Die Rücktrittsfrist von 14 Tagen ist noch nicht verstrichen."))
        self.halt()

    # print("sie können zurücktreten")
    @Rule(salience=-1)
    def rücktritt(self):
        self.declare(Result(resultValue=True,
                            law="Ihren Angaben nach haben Sie die Rücktrittsmöglichkeit nach § 11 FAGG. Da es sich hierbei aber um eine Vorabschätzung handelt, wird die Beratung von Rechtsanwält*innen empfohlen. Die folgenden Ansprechpersonen stehen Ihnen hierfür zur Verfühung: (PLZ eingeben) → Liste von kooperierenden Anwält*innen"))


"""
engine = ShoppingBuddy()
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
    engine = ShoppingBuddy()
    engine.reset()
    for i in range(len(answers)):
        engine.declare(Fact(**{'frage' + str(i): answers[i]}))
    engine.run()
    result = list(engine.facts.get(engine.facts.last_index-1).values())
    return {"value":str(result[0]),"law":result[1]}


def formatRequest(request):
    answers = request.split("&")
    formattedAnswers = []
    for x in answers:
        answer = x.split("=")
        formattedAnswers.append(answer[1])
    return formattedAnswers
