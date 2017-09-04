from itertools import groupby, chain, product
from .models import Sections

HOUR_OFFSET = 14

class Schedule(object***REMOVED***:

    def __init__(self, sections***REMOVED***:
        self.section_combos = sections
        self.sections = self.to_model_list(***REMOVED***
        self.view_list = self.get_schedule_view_list(***REMOVED***
        self.longest_block = self.find_longest(self.view_list***REMOVED***
        self.longest_break = self.find_longest_break(self.view_list***REMOVED***
        self.number_of_classes = self.get_value("classes"***REMOVED***
        self.number_of_open = self.get_value("open"***REMOVED***
        self.number_of_closed = self.get_value("closed"***REMOVED***

        self.avg_rating, self.lowest_rating, self.highest_rating = self.rating_info(***REMOVED***

    def to_list(self***REMOVED***:
        return self.sections

    def rating_info(self***REMOVED***:
        ratings = [***REMOVED***
        for section_combo in self.section_combos:
            rating_1 = section_combo.section_1['instructor__rating'***REMOVED***
            rating_2 = section_combo.section_2['instructor__rating'***REMOVED***
            for rating in rating_1, rating_2:
                if rating: ratings.append(rating***REMOVED***
        if ratings:
            average = float(sum(ratings***REMOVED******REMOVED*** / float(len(ratings***REMOVED******REMOVED***
            lowest = min(ratings***REMOVED***
            highest = max(ratings***REMOVED***
            return average, lowest, highest
        return None

    def find_longest(self, view_list***REMOVED***:
        longest = 0
        view_list = map(list, map(None, zip(*view_list***REMOVED******REMOVED******REMOVED***
        for column in view_list:
            length = max(sum(1 for i in column if i***REMOVED*** for _, i in groupby(column***REMOVED******REMOVED***
            if length > longest:
                longest = length
        return "{***REMOVED***".format(minimalNumber(longest / 2.0***REMOVED******REMOVED***

    def find_longest_break(self, view_list***REMOVED***:
        longest = 0
        view_list = map(list, map(None, zip(*view_list***REMOVED******REMOVED******REMOVED***
        for column in view_list:
            test_longest = max(self.find_breaks(column***REMOVED******REMOVED***
            if test_longest > longest:
                longest = test_longest
        return "{***REMOVED***".format(minimalNumber(longest / 2.0***REMOVED******REMOVED***

    def get_value(self, value_type***REMOVED***:
        if value_type == "classes":
            return len(self.sections***REMOVED***
        else:
            return len(self.sections.filter(status=value_type.title(***REMOVED******REMOVED******REMOVED***

    def __repr__(self***REMOVED***:
        return str(self.sections***REMOVED***

    def get_schedule_view_list(self***REMOVED***:
        view_list = [[False for _ in range(5***REMOVED******REMOVED*** for _ in range(30***REMOVED******REMOVED***
        true_indexes = [***REMOVED***
        for section in self.section_combos:
            if section.time_block:
                true_indexes += section.time_block.view_indexes(***REMOVED***
        for i, j in true_indexes:
            view_list[i***REMOVED***[j***REMOVED*** = True
        return view_list

    def to_model_list(self***REMOVED***:
        sections = list(chain.from_iterable([(s.section_1, s.section_2***REMOVED*** for s in self.section_combos if s***REMOVED******REMOVED******REMOVED***
        sections = [s['class_field'***REMOVED*** for s in sections if s***REMOVED***
        model_list = Sections.objects.all(***REMOVED***.filter(class_field__in=sections***REMOVED***
        return model_list

    @staticmethod
    def find_breaks(column***REMOVED***:
        trigger = False
        length = 0
        breaks = [0***REMOVED***
        for val in column:
            if val:
                if trigger:
                    breaks.append(length***REMOVED***
                    length = 0
                else:
                    trigger = True
                continue
            if trigger:
                length += 1
        return breaks


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
        if schedules == [(***REMOVED******REMOVED***:
            return [***REMOVED***
        for schedule in schedules[::***REMOVED***:
            available = set.intersection(*[s.compatible for s in schedule***REMOVED******REMOVED***
            for section in schedule:
                if section not in available:
                    schedules.remove(schedule***REMOVED***
                    break
        return [Schedule(schedule***REMOVED*** for schedule in schedules***REMOVED***
        
    @staticmethod
    def course_groups(courses***REMOVED***:
        course_groups = [***REMOVED***
        # This mess of a loop simply creates all the sectioncombo objects
        # These are needed to build schedules
        for group in groupby(courses, lambda x: x.get('course_id'***REMOVED******REMOVED***:
            sec_groups = groupby(group[1***REMOVED***, lambda x: x.get('sec_group'***REMOVED******REMOVED***
            combos = [***REMOVED***
            for _, sec_group in sec_groups:
                lecture = None
                labs = [***REMOVED***
                for section in sec_group:
                    # What we're doing here is finding the "main" class
                    # This is b/c we need multiple section combos with the
                    # same lecture/activity. However activities can also be
                    # combo-ed with labs, so thats why this is SO ugly
                    if section['type'***REMOVED*** == 'LEC' or section['type'***REMOVED*** == 'ACT':
                        if lecture:
                            continue
                        else:
                            lecture = section
                    else:
                        labs.append(section***REMOVED***
                for lab in labs:
                    if lecture:
                        # Make sure the lecture/lab combo is compatible.
                        time_block_1 = TimeBlock(lecture['start'***REMOVED***, lecture['end'***REMOVED***, lecture['days'***REMOVED******REMOVED***
                        time_block_2 = TimeBlock(lab['start'***REMOVED***, lab['end'***REMOVED***, lab['days'***REMOVED******REMOVED***
                        if time_block_1.overlaps(time_block_2***REMOVED***:
                            continue
                        combos.append(SectionCombo(iter([lecture, lab***REMOVED******REMOVED******REMOVED******REMOVED***
                    else:
                        combos.append(SectionCombo(iter([lab***REMOVED******REMOVED******REMOVED******REMOVED***
            course_groups.append(combos***REMOVED***
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

    def view_indexes(self***REMOVED***:
        time_2 = self.time_2
        if time_2:
            return self.time_1.view_indexes(***REMOVED*** + time_2.view_indexes(***REMOVED***
        return self.time_1.view_indexes(***REMOVED***

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
        self.days = set(days***REMOVED***

    def view_indexes(self***REMOVED***:
        indexes = [***REMOVED***
        for col in self.days_to_cols(***REMOVED***:
            for row in self.time_to_rows(***REMOVED***:
                indexes.append((row, col***REMOVED******REMOVED***
        return indexes

    def days_to_cols(self***REMOVED***:
        vals = {'M': 0, 'T' : 1, 'W' : 2, 'R' : 3, 'F' : 4***REMOVED***
        cols = [***REMOVED***
        for day in self.days:
            cols.append(vals[day***REMOVED******REMOVED***
        return cols

    def time_to_rows(self***REMOVED***:
        start_h = self.start.hour * 2 - HOUR_OFFSET
        end_h   = self.end.hour * 2 - HOUR_OFFSET
        start_m, end_m = self.start.minute, self.end.minute
        start =  start_h + int(round(start_m / 60.0***REMOVED******REMOVED***
        end =  end_h + int(round(end_m / 60.0***REMOVED******REMOVED***
        rows = range(start, end***REMOVED***
        return rows

    def overlaps(self, other***REMOVED***:
        return max(self.start, other.start***REMOVED*** < min(self.end, other.end***REMOVED*** and not self.days.isdisjoint(other.days***REMOVED***

    def __repr__(self***REMOVED***:
        return "{***REMOVED*** - {***REMOVED*** {***REMOVED***".format(self.start, self.end, "".join(self.days***REMOVED******REMOVED***


def minimalNumber(x***REMOVED***:
    if type(x***REMOVED*** is str:
        if x == '':
            x = 0
    f = float(x***REMOVED***
    if f.is_integer(***REMOVED***:
        return int(f***REMOVED***
    else:
        return f