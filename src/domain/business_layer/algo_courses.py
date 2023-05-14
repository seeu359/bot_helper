from dataclasses import dataclass
from src.domain.models import AlgoCourse


@dataclass
class AlgoCourseData:
    algo_course: AlgoCourse
    salary_per_lesson: int = 750
    lessons_count: int = 3
    premium: int = 1000

    def salary(self):
        if self.algo_course.premium:
            return self.salary_per_lesson * self.lessons_count + self.premium
        return self.salary_per_lesson * self.lessons_count


