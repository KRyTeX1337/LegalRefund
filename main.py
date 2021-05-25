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

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), salience=3)
    def frage3true(self):
        self.declare(Result(resultValue=True,
                            law="Ich habe die Lieferung erhalten Seit der Lieferung sind bereits mehr als 14 Tage verstrichen."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="false"), salience=3)
    def frage3false(self):
        self.declare(Result(resultValue=True,
                            law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="true"),
          salience=4)
    def frage4true(self):
        self.declare(Result(resultValue=False,
                            law="Sie haben gem. § 15 Abs 1 FAGG ab dem Tag, an dem Sie die Rücktrittserklärung abgesendet haben, 14 Tage Zeit, die erhaltene Ware zurückzusenden. Der/die Unternehmer*in hat Ihnen gem. § 14 FAGG unverzüglich, spätestens jedoch binnen 14 Tagen ab Zugang der Rücktrittserklärung, die geleisteten Zahlungen zu erstatten. Er hat für die Rückzahlung dasselbe Zahlungsmittel zu verwenden, dessen Sie sich bei der damaligen Zahlung bedient haben. Eine Abweichung davon ist nur möglich, wenn Ihnen dadurch keine Kosten entstehen und sie ausdrücklich zustimmen. Versandkosten müssen Ihnen vollständig ersetzt werden, außer Sie haben sich gegen die günstigste Standardlieferung entschieden. Dann muss Ihnen die Differenz zwischen Standardlieferung und gewählter Versandart nicht ersetzt werden."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          salience=4)
    def frage4false(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="true"),
          salience=5)
    def frage5true(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"),
          salience=5)
    def frage5false(self):
        self.declare(Result(resultValue=True,
                            law="Sie wurden nicht (rechtzeitig) über das Rücktrittsrecht belehrt, daher verlängert sich die Rücktrittsfrist um 12 Monate gem §12 Abs 1 FAGG. Erteilt der/die Unternehmer *in die Informationen verspätet, aber innerhalb der 12 Monatsfrist, so endet die Rücktrittsfrist binnen 14 Tagen (die Frist beginnt am Tag, an dem der verbraucher dieser Information erhalten hat)."))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"), Fact(frage6="true"),
          salience=6)
    def frage6true(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"), Fact(frage6="false"),
          salience=6)
    def frage6false(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"), Fact(frage6="false"), Fact(frage7="true"),
          salience=7)
    def frage7true(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    @Rule(Fact(frage0="true"), Fact(frage1="true"), Fact(frage2="true"), Fact(frage3="true"), Fact(frage4="false"),
          Fact(frage5="false"), Fact(frage6="false"), Fact(frage7="false"),
          salience=7)
    def frage7false(self):
        self.declare(Result(resultValue=True, law=""))
        self.halt()

    # print("sie können zurücktreten")
    @Rule(salience=0)
    def rücktritt(self):
        self.declare(Result(resultValue=True,
                            law="Ihren Angaben nach haben Sie die Rücktrittsmöglichkeit nach § 11 FAGG. Da es sich hierbei aber um eine Vorabschätzung handelt, wird die Beratung von Rechtsanwält*innen empfohlen. Die folgenden Ansprechpersonen stehen Ihnen hierfür zur Verfühung: (PLZ eingeben) → Liste von kooperierenden Anwält*innen"))
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
