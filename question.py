class QuestionSet:
    def __init__(self, question: str, answer: list[str]):
        self.question = question
        self.answer = answer
        
    def get_answer_list(self):
        return self.answer
      
questions = [
    QuestionSet('What is the name of the Islamic charity given during the month of Ramadan?', ['Zakat', 'Zakt']),
    QuestionSet('In what city is the Kaaba located?', ['Mecca', 'Mekah']),
    QuestionSet('What is the first qibla for muslims?', ['Al-Aqsa Mosque', 'Masjid Al-Aqsa', 'Al-Aqsa', 'al aqsa']),
    QuestionSet('What is the holy book of Islam?', ['Al-Quran', 'quran', 'Al quran', 'Quran', 'Al-quran']),
    QuestionSet('What is the first pillar of Islam?', ['The shahada', 'Shahada', 'shahada', 'Declaration of faith']),
    QuestionSet('How many names does Allah have?', ['99', 'Ninety-nine', 'ninety nine', 'ninety-nine']),
    QuestionSet('Who was the first woman to embrace Islam?', ['Khadijah', 'Khadijah binti Khuwaylid', 'khadijah', 'khadijah bint khuwaylid']),
    QuestionSet('Who is the last prophet of Islam?', ['Muhammad', 'muhammad', 'Prophet Muhammad', 'prophet muhammad']),
    QuestionSet('How many times a day do Muslims pray?', ['5', 'five', 'Five']),
    QuestionSet('What is the pilgrimage to Mecca called?', ['Hajj', 'hajj']),
]
