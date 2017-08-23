class Schedule:
    pass


class SectionCombo:

    def __init__(section_1, section_2=None***REMOVED***:
        self.section_1 = section_1
        if section_2:
            self.section_2 = section_2

    def compatible(self, other***REMOVED***:
        pass

class TimeBlock:
    def __init__(time_1, time_2=None***REMOVED***:
        self.time_1 = time_1
        if time_2:
            self.time_2 = time_2


    def time_overlap(self, other***REMOVED***:
        s_start_1, s_end_1 = self.time_1
        if self.time_2:
            s_start_2, s_end_2 = self.time_2

        o_start_1, o_end_1 = other.time_1
        if other.time_2:
            o_start_2, o_end_2 = other.time_2
        # Check all possible collisions between the times
        if s_start_1 < o_start_1 < s_end_1:
            return True
        if s_start_1 < o_end_1 < s_end_1:
            return True

        if s_start_2 < o_start_1 < s_end_2:
            return True
        if s_start_2 < o_end_1 < s_end_2:
            return True

        if s_start_1 < o_start_2 < s_end_1:
            return True
        if s_start_1 < o_end_2 < s_end_1:
            return True

        if s_start_2 < o_start_2 < s_end_2:
            return True
        if s_start_2 < o_end_2 < s_end_2:
            return True
        return False




