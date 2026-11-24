from dataclasses import dataclass, field


@dataclass(frozen=True)
class Course:
    code: str
    title: str


@dataclass
class Student:
    student_id: str
    name: str
    _courses: list[Course] = field(default_factory=list, init=False, repr=False)

    def enroll(self, course: Course) -> None:
        if all(existing.code != course.code for existing in self._courses):
            self._courses.append(course)

    def get_courses(self) -> tuple[Course, ...]:
        return tuple(self._courses)


if __name__ == "__main__":
    student = Student("S001", "Allie")
    student.enroll(Course("PHY101", "Introduction to Programming"))

    for course in student.get_courses():
        print(f"{student.name} is enrolled in {course.code}: {course.title}")
