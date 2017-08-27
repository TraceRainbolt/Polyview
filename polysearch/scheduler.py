from itertools import groupby, chain, product
from .models import Sections


class Schedule(object***REMOVED***:

    def __init__(self, sections***REMOVED***:
        self.sections = self.to_model_list(sections***REMOVED***

    def to_list(self***REMOVED***:
        return self.sections

    def __repr__(self***REMOVED***:
        return str(self.sections***REMOVED***

    @staticmethod
    def to_model_list(sections***REMOVED***:
        sections = list(chain.from_iterable([(s.section_1, s.section_2***REMOVED*** for s in sections if s***REMOVED******REMOVED******REMOVED***
        sections = [s['class_field'***REMOVED*** for s in sections if s***REMOVED***
        model_list = [***REMOVED***
        for section in sections:
            model_list.append(Sections.objects.all(***REMOVED***.get(class_field=section***REMOVED******REMOVED***
        return model_list

    # These build the possible schedules using the users checked classes.
    @staticmethod
    def create_schedules(courses***REMOVED***:
        course_groups = Schedule.course_groups(courses***REMOVED***
        for init_group in chain.from_iterable(course_groups***REMOVED***:
            for sec_group in chain.from_iterable(course_groups***REMOVED***:
                if init_group.is_compatible(sec_group***REMOVED***:
                    init_group.compatible.add(sec_group***REMOVED***
        all_schedules = list(product(*course_groups***REMOVED******REMOVED***
        return Schedule.filter_valid_schedules(all_schedules***REMOVED***

    @staticmethod
    def filter_valid_schedules(schedules***REMOVED***:
        for schedule in schedules:
            available = set.intersection(*[s.compatible for s in schedule***REMOVED******REMOVED***
            for section in schedule:
                if section not in available:
                    schedules.remove(schedule***REMOVED***
                    break
        return [Schedule(schedule***REMOVED*** for schedule in schedules***REMOVED***

    @staticmethod
    def course_groups(courses***REMOVED***:
        course_groups = [***REMOVED***
        for group in groupby(courses, lambda x: x.get('course_id'***REMOVED******REMOVED***:
            course_groups.append([SectionCombo(j***REMOVED*** for _, j in groupby(
                group[1***REMOVED***, lambda x: x.get('sec_group'***REMOVED******REMOVED******REMOVED******REMOVED***
        return course_groups


class SectionCombo(object***REMOVED***:

    def __init__(self, sections***REMOVED***:
        self.section_1 = next(sections, None***REMOVED***
        self.section_2 = next(sections, None***REMOVED***
        self.time_block = self.make_time_block(***REMOVED***
        self.compatible = set([self***REMOVED******REMOVED***

    def is_compatible(self, other***REMOVED***:
        if self.time_block is None or other.time_block is None:
            return True
        return not self.time_block.overlaps(other.time_block***REMOVED***

    def make_time_block(self***REMOVED***:

        start_1 = self.section_1.get('start', None***REMOVED***
        end_1 = self.section_1.get('end', None***REMOVED***
        days_1 = self.section_1.get('days', None***REMOVED***
        time_block_1 = TimeBlock(start_1, end_1, days_1***REMOVED***

        if self.section_2:
            start_2 = self.section_2.get('start', None***REMOVED***
            end_2 = self.section_2.get('end', None***REMOVED***
            days_2 = self.section_2.get('days', None***REMOVED***
            time_block_2 = TimeBlock(start_1, end_2, days_1***REMOVED***
            if start_2 is None:
                return None
            return TimeBlockCombo(time_block_1, TimeBlock(start_2, end_2, days_2***REMOVED******REMOVED***
        if start_1 is None:
            return None
        return TimeBlockCombo(time_block_1***REMOVED***

    def __repr__(self***REMOVED***:
        id_1 = self.section_1.get('class_field', None***REMOVED***
        id_2 = self.section_2.get(
            'class_field', None***REMOVED*** if self.section_2 else 'empty'
        t_1 = self.section_1.get('type', None***REMOVED***
        t_2 = ' ' + self.section_2.get('type', None***REMOVED*** if self.section_2 else ''
        return "<{***REMOVED*** {***REMOVED***, {***REMOVED***{***REMOVED***>".format(id_1, t_1, id_2, t_2***REMOVED***


class TimeBlockCombo(object***REMOVED***:

    def __init__(self, time_1, time_2=None***REMOVED***:
        self.time_1 = time_1
        self.time_2 = time_2

    # Check all possible collisions between the times
    def overlaps(self, other***REMOVED***:
        overlap = self.time_1.overlaps(other.time_1***REMOVED***
        if self.time_2:
            overlap = overlap or self.time_2.overlaps(other.time_1***REMOVED***
        if other.time_2:
            overlap = overlap or self.time_1.overlaps(other.time_2***REMOVED***
        if self.time_2 and other.time_2:
            overlap = overlap or self.time_2.overlaps(other.time_2***REMOVED***
        return overlap

    def __repr__(self***REMOVED***:
        return "{***REMOVED*** {***REMOVED***".format(self.time_1, self.time_2***REMOVED***


class TimeBlock(object***REMOVED***:

    def __init__(self, start, end, days***REMOVED***:
        self.start = start
        self.end = end
        self.days = list(days***REMOVED***

    def overlaps(self, other***REMOVED***:
        return max(self.start, other.start***REMOVED*** < min(self.end, other.end***REMOVED*** and not set(self.days***REMOVED***.isdisjoint(other.days***REMOVED***

    def __repr__(self***REMOVED***:
        return "{***REMOVED*** - {***REMOVED*** {***REMOVED***".format(self.start, self.end, "".join(self.days***REMOVED******REMOVED***
