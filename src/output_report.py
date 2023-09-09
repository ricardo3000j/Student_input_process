from serializers import output_serializer

class OutputReport:
    """Model for report object"""

    """singleton pattern"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(OutputReport, cls).__new__(cls)
        return cls._instance
    
    @property
    def serialized_output(self):
        return output_serializer(self)
    