import Question


class Questions:
    def __init__(self):
        self.questionList = []

    def createQuestions(self):
        #0
        self.addQuestion(
            Question.Question("Zu welchem Zweck haben Sie die Ware gekauft?",
                                           "Ich habe die Ware für private Zwecke gekauft oder plane, ein Unternehmen zu gründen und benötige die Ware zur Aufnahme des Betriebs dieses Unternehmens.",
                                           "Ich betreibe bereits ein Unternehmen und benötige zum Betrieb des Unternehmens die Ware."))
        #1
        self.addQuestion(
            Question.Question("Haben Sie die Ware von einem Unternehmer gekauft?",
                                           "Mein*e Vertragspartner*in verkauft die Ware in einem auf Dauer angelegtem System (Online-Shop) und operiert scheinbar zumindest auf Kostendeckungsbasis, um diesen Betrieb weiter aufrecht zu erhalten.",
                                           "Es handelt sich nur um eine Privatperson – sie verkauft die Ware, ohne dass Absicht auf eine andauernde Erwerbstätigkeit auf diesem Weg erkennbar ist."))
        #2
        self.addQuestion(
            Question.Question("Erfolgte der Kauf über ein dafür organisiertes System und ohne körperliche Anwesenheit?",
                              "Es handelt sich um einen Webshop, welcher genau für diesen Vertriebszweck geschaffen wurde, außerdem war keine der Parteien bei der Bestellung anwesend. (Es handelt sich um einen Fernabsatzvertrag gem §3 Z 2 FAGG)",
                              "Die Ware wurde zwar elektronisch bestellt, der gewählte Weg wurde aber nur als Ausnahme genutzt oder der Weg ist für den Vertrieb auf diese Weise von der anderen Partei nicht beabsichtigt oder die Bestellung erfolgte unter Anwesenheit beider Parteien."))
        #3
        self.addQuestion(
            Question.Question("Ist die Rücktrittsfrist von 14 Tagen verstrichen?",
                                           "Ich habe die Lieferung erhalten Seit der Lieferung sind bereits mehr als 14 Tage verstrichen.",
                                           "Die Rücktrittsfrist von 14 Tagen ist noch nicht verstrichen."))
        #4
        self.addQuestion(
            Question.Question("Haben Sie innerhalb von 14 Tage nach Erhalt der Ware dem/der Verkäufer*in mitgeteilt, dass Sie vom Vertrag zurücktreten möchten?",
                              "Ich habe den/die Verkäufer*in von meinem Rücktritt informiert. Dieser muss keiner bestimmten Form entsprechen und kann auch über ein Formular auf der Website des Unternehmens erfolgt sein.",
                              "Eine solche Erklärung habe ich nicht abgegeben."))
        #5
        self.addQuestion(
            Question.Question(
                "Wurden Sie über Ihr gesetzliches Rücktrittsrecht vor der Bestellung informiert?",
                "Die Widerrufsbelehrung erfolgte entweder auf einer der Seiten vor dem Bestellbutton oder innerhalb der allgemeinen Geschäftsbedingungen. Dort wurde die Belehrung direkt angeführt oder verlinkt. Mir wurde auch ein Muster-Widerrufsformular bereitgestellt, beziehungsweise habe ich mit dem Erhalt der Lieferung Zugang zu diesen Informationen erhalten. (gem §7 FAGG)",
                "Eine Widerrufsbelehrung wurde weder auf einer Seite vor dem Bestellbutton, in den AGB, noch mit der Lieferung bereitgestellt. Selbst wenn eine Belehrung vorliegt, wurde kein Widerrufsformular zur Verfügung gestellt. Die Widerrufsbelehrung ist auch nicht nach Erhalt der Lieferung erfolgt."))
        #6
        self.addQuestion(
            Question.Question(
                "Erfolgte eine nachträgliche Widerrufsbelehrung?",
                "Es erfolgte eine nachträgliche Widerrufsbelehrung innerhalb von zwölf Monaten ab Lieferung",
                "Eine nachträgliche Widerrufsbelehrung innerhalb von zwölf Monaten ab Lieferung ist nicht erfolgt."))
        # 7
        self.addQuestion(
            Question.Question("Sind seit der Lieferung mehr als ein Jahr und 14 Tage verstrichen?",
                              "Seit dem Erhalt der Lieferung sind bereits mehr als zwölf Monate und 14 Tage verstrichen",
                              "Die Frist von zwölf Monaten und 14 Tagen ab Lieferung ist noch nicht verstrichen."))


    def addQuestion(self, question):
        self.questionList.append(question)

    def jsonable(self):
        return self.__dict__
