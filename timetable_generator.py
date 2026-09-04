import random


def generate_timetable(teachers, subjects, rooms, classes):

    # =====================================================
    # DAYS AND PERIODS
    # =====================================================

    days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday"
    ]

    periods = [
        "Period 1",
        "Period 2",
        "Period 3",
        "Period 4"
    ]


    # =====================================================
    # TIMETABLE DICTIONARY
    # =====================================================

    timetable = {}


    # =====================================================
    # TRACK BUSY TEACHERS AND ROOMS
    # =====================================================

    teacher_busy = {}
    room_busy = {}
    teacher_daily_load = {}


    # =====================================================
    # INITIALIZE DICTIONARIES
    # =====================================================

    for day in days:

        teacher_busy[day] = {}
        room_busy[day] = {}
        teacher_daily_load[day] = {}

        for period in periods:

            # Teachers busy in this period
            teacher_busy[day][period] = []

            # Rooms busy in this period
            room_busy[day][period] = []

        # Set daily teaching load for every teacher
        for teacher in teachers:

            teacher_daily_load[day][teacher["name"]] = 0


    # =====================================================
    # GENERATE TIMETABLE FOR EACH CLASS
    # =====================================================

    for cls in classes:

        class_name = cls["class_name"]

        timetable[class_name] = {}


        # =================================================
        # EACH DAY
        # =================================================

        for day in days:

            timetable[class_name][day] = {}


            # =============================================
            # EACH PERIOD
            # =============================================

            for period in periods:

                assigned = False


                # Randomize subjects
                shuffled_subjects = list(subjects)
                random.shuffle(shuffled_subjects)


                # =============================================
                # FIND AVAILABLE SUBJECT
                # =============================================

                for subject in shuffled_subjects:

                    matching_teachers = []


                    # =========================================
                    # FIND MATCHING AVAILABLE TEACHERS
                    # =========================================

                    for teacher in teachers:

                        if (
                            teacher["subject"].lower()
                            == subject["name"].lower()

                            and teacher["name"]
                            not in teacher_busy[day][period]

                            and teacher_daily_load[day][teacher["name"]]
                            < 4
                        ):

                            matching_teachers.append(
                                teacher
                            )


                    # =========================================
                    # FIND AVAILABLE ROOMS
                    # =========================================

                    available_rooms = []

                    for room in rooms:

                        if (
                            room["room_number"]
                            not in room_busy[day][period]

                            and int(room["capacity"])
                            >= int(cls["students"])
                        ):

                            available_rooms.append(
                                room
                            )


                    # =========================================
                    # ASSIGN TEACHER + SUBJECT + ROOM
                    # =========================================

                    if matching_teachers and available_rooms:

                        teacher = random.choice(
                            matching_teachers
                        )

                        room = random.choice(
                            available_rooms
                        )


                        # Mark teacher as busy
                        teacher_busy[day][period].append(
                            teacher["name"]
                        )


                        # Mark room as busy
                        room_busy[day][period].append(
                            room["room_number"]
                        )


                        # Increase teacher daily workload
                        teacher_daily_load[day][
                            teacher["name"]
                        ] += 1


                        # Save timetable information
                        timetable[class_name][day][period] = {

                            "subject": subject["name"],

                            "teacher": teacher["name"],

                            "room": room["room_number"]

                        }


                        assigned = True

                        break


                # =============================================
                # IF NO VALID COMBINATION IS FOUND
                # =============================================

                if not assigned:

                    timetable[class_name][day][period] = {

                        "subject": "-",

                        "teacher": "-",

                        "room": "-"

                    }


    # =====================================================
    # RETURN GENERATED TIMETABLE
    # =====================================================

    return timetable