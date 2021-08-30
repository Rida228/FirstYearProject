get_section_id = """
                SELECT section_id
                FROM sections
                WHERE sections = '{}';
                """
get_student_pw="""select distinct password
                from student
                where "USN" = '{}' 
                limit  1;
                """
get_teacher_pw="""
                select distinct password
                from teachers
                where name = '{}' 
                limit  1;
                """

add_new_student = """
                INSERT INTO student(student_id, section_id, "USN", "Name", password, email, branch)
                VALUES (DEFAULT, {}, '{}', '{}', '{}', '{}', '{}');
                """
add_new_teacher = """
                INSERT INTO teachers (teacher_id, name, password, email, department) 
                VALUES (DEFAULT, '{}', '{}', '{}', '{}');
                 """
get_classes = """
                select class_id,classes.course_id, "link", "time", courses.course_code, department
                from classes
                join courses
                ON classes.course_id = courses.course_id
                where section_id = (select section_id from student where "USN" = '{}' limit 1)
                AND day = '{}';
                """
get_teacher_cls = """
                SELECT sections.sections, courses.course_code, link, "time"
                From classes
                inner join courses on classes.course_id = courses.course_id
				inner join teachers on classes.teacher_id = teachers.teacher_id 
				left join sections on classes.section_id = sections.section_id
				where teachers.name = '{}'
				AND "day" = '{}';
                """
add_class = """
            INSERT INTO classes(
	        section_id, course_id, link, day, "time", class_id, teacher_id)
	        VALUES ({}, {}, '{}','{}', '{}:00', default, {});
            """
get_courseId="""
            SELECT course_id 
	        FROM public.courses
	        where course_code = '{}'
            LIMIT 1;
            """
get_teacher_id = """
                SELECT teacher_id FROM  teachers WHERE name = 'Ananth Raju' limit 1;
                """
get_all_courses = """
                    select course_code
                    from courses;
                """
get_student_list = """SELECT grades.student_id, semester, course_id, student."USN" 
                        FROM grades
                        inner join student on  grades.student_id = student.student_id;
                    """