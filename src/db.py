class StudentsRegistry:
    """object to store students"""

    """Singleton pattern"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StudentsRegistry, cls).__new__(cls)
        return cls._instance


student_registry = StudentsRegistry()
