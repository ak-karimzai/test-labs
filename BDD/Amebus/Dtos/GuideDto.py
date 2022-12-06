class GuideDto:
    def __init__(self, id, firstName, lastName, patronymic, qualification, biography, experience):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.patronymic = patronymic
        self.qualification = qualification
        self.biography = biography
        self.experience = experience

class CreateGuideDto:
    def __init__(self, firstName, lastName, patronymic, qualification, biography, experience):
        self.firstName = firstName
        self.lastName = lastName
        self.patronymic = patronymic
        self.qualification = qualification
        self.biography = biography
        self.experience = experience
