class CreateSubjectAndRecordDto:
    def __init__(self, ownerId, private, name, description, type, nameRecord, keywords, content):
        self.ownerId = ownerId
        self.private = private
        self.name = name
        self.description = description
        self.type = type
        self.nameRecord = nameRecord
        self.keywords = keywords
        self.content = content

class SubjectAndRecordsDto:
    def __init__(self, ownerId, private, name, description, records):
        self.ownerId = ownerId
        self.private = private
        self.name = name
        self.description = description
        self.records = records