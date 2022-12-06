from Amebus.Entities.Guide import Guide


class GuideMotherBuilder:
    def init(self, id, firstName):
        self.subjectBuilder = GuideBuilder(id, firstName)

class GuideBuilder:
    def __init__(self, id, firstName):
        self.id = id
        self.firstName = firstName
        self.lastName = ""
        self.patronymic = ""
        self.qualification = ""
        self.biography = ""
        self.experience = 0

    def withLastName(self, new_lastName):
        self.lastName = new_lastName
        return self

    def withPatronymic(self, new_patronymic):
        self.patronymic = new_patronymic
        return self

    def withQualification(self, new_qualification):
        self.qualification = new_qualification
        return self

    def withBiography(self, new_biography):
        self.biography = new_biography
        return self

    def withExperience(self, new_experience):
        self.experience = new_experience
        return self

    def build(self):
        return Guide(
            id=self.id,
            firstName=self.firstName,
            lastName=self.lastName,
            patronymic=self.patronymic,
            qualification=self.qualification,
            biography=self.biography,
            experience=self.experience
        )