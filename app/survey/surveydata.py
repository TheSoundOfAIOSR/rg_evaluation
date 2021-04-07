from constants import SURVEY_DATA
from utils import load_json, write_to_json


class question:
    def __init__(self, cnt: int, opType: str, query: str, responses: list) -> None:
        self.id = "q" + str(cnt)
        self.opType = opType
        self.query = query
        self.responses = responses

    def __repr__(self) -> str:
        # char(10) means \n. '\' not allowed in f-strings
        return f"""Q. {self.query + chr(10)}
        {chr(10).join(
            [f"A{i}. {ans}" for i, ans in enumerate(self.responses)])}"""


class SurveyData:

    count = 0

    def __init__(self) -> None:
        self.questions = list()
        self.get_from_file()

    def get_from_file(self, fName: str = SURVEY_DATA):
        """
        Loads existing questions from survey file
        """
        questions_raw = load_json(fName)
        for ques in questions_raw:
            print(ques)
            self.questions.append(
                question(
                    cnt=SurveyData.count,
                    opType=ques["type"],
                    query=ques["question"],
                    responses=ques["fields"],
                )
            )
            SurveyData.count += 1

    def get_questions(self):
        """
        Returns an iterable for the questions
        """
        for ques in self.questions:
            yield ques

    def get_all_questions(self):
        """
        Returns a list of all questions
        """
        return self.questions

    def add_question(self, opType: str, query: str, responses: list):
        """
        Adds a new question to the survey permanently
        """
        self.questions.append(
            question(
                cnt=SurveyData.count, opType=opType, query=query, responses=responses
            )
        )
        SurveyData.count += 1

        questions_raw = load_json(SURVEY_DATA)
        questions_raw.append({"type": opType, "question": query, "fields": responses})
        write_to_json(SURVEY_DATA, questions_raw)

    # TODO: Add Update, Delete and Reorder methods
