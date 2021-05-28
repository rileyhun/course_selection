import re

def course_normalization(
    input_string: str
):
    """
    Function that normalizes student entered course information
    Args:
        :param input_string = string composed of department, course number, semester, and year
        :return: dictionary with the properties and values for department, course number, semester and year parsed from input string

    Example:
    >>> course_normalization("CS111 2016 Fall")
    """

    # parse input string into constituent properties
    regex_pattern = re.compile("([a-zA-Z]+)[\s\-:]?(\d+)\s(\d{2}(?:\d{2})?)[\s]?([a-zA-Z]+)")
    groups = regex_pattern.search(input_string)
    if groups:
        department = groups.group(1)
        course_number = groups.group(2)
        year = groups.group(3)
        semester = groups.group(4)
    else:
        regex_pattern = re.compile("([a-zA-Z]+)[\s\-:]?(\d+)\s([a-zA-Z]+)[\s]?(\d{2}(?:\d{2})?)")
        groups = regex_pattern.search(input_string)
        if groups:
            department = groups.group(1)
            course_number = groups.group(2)
            semester = groups.group(3)
            year = groups.group(4)
        else:
            raise ValueError("input_string invalid and does not contain requisite properties - department, course number, "
                             "semester, and year")

    # validate year
    if len(year) not in [2,4]:
        raise ValueError("input string must contain year that is either 2 or 4 digits")
    # validate semester
    if not semester.lower() in ("f", "w", "s", "su", "fall", "spring", "winter", "summer"):
        raise ValueError("input string does not contain valid semester")

    # standardize semester
    semester_map = {"f": "Fall", "w": "Winter", "s": "Spring", "su": "Summer"}
    if len(semester) <= 2:
        semester = semester_map[semester.lower()]
    else:
        semester = semester.title()
    # standardize year
    if len(year) == 2:
        year = "20%s" % year

    return {
        "department": department.upper(),
        "course_number": int(course_number),
        "semester": semester,
        "year": int(year)
    }


