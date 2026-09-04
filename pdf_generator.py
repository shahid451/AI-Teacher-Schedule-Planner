from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    PageBreak
)

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch


def create_pdf(timetable, filename):

    # Create PDF document
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    # PDF content
    elements = []

    # Styles
    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    heading_style = styles["Heading2"]
    normal_style = styles["Normal"]


    # =====================================================
    # PDF TITLE
    # =====================================================

    title = Paragraph(
        "AI Teacher Schedule Planner",
        title_style
    )

    elements.append(title)

    subtitle = Paragraph(
        "Automatically Generated Timetable",
        normal_style
    )

    elements.append(subtitle)
    elements.append(Spacer(1, 25))


    # =====================================================
    # EACH CLASS TIMETABLE
    # =====================================================

    for class_name, schedule in timetable.items():

        # Class Heading
        heading = Paragraph(
            f"Class: {class_name}",
            heading_style
        )

        elements.append(heading)
        elements.append(Spacer(1, 12))


        # Table Header
        data = [
            [
                "Day",
                "Period",
                "Subject",
                "Teacher",
                "Room"
            ]
        ]


        # =====================================================
        # ADD TIMETABLE DATA
        # =====================================================

        for day, periods in schedule.items():

            for period, details in periods.items():

                data.append(
                    [
                        day,
                        period,
                        details["subject"],
                        details["teacher"],
                        details["room"]
                    ]
                )


        # =====================================================
        # CREATE TABLE
        # =====================================================

        table = Table(
            data,
            colWidths=[
                0.9 * inch,
                1.0 * inch,
                1.5 * inch,
                1.5 * inch,
                0.7 * inch
            ]
        )


        # =====================================================
        # TABLE DESIGN
        # =====================================================

        table.setStyle(
            TableStyle(
                [
                    # Header
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.HexColor("#263c50")
                    ),

                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.white
                    ),

                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),

                    (
                        "FONTSIZE",
                        (0, 0),
                        (-1, 0),
                        10
                    ),

                    # Body
                    (
                        "BACKGROUND",
                        (0, 1),
                        (-1, -1),
                        colors.white
                    ),

                    (
                        "TEXTCOLOR",
                        (0, 1),
                        (-1, -1),
                        colors.black
                    ),

                    (
                        "FONTNAME",
                        (0, 1),
                        (-1, -1),
                        "Helvetica"
                    ),

                    (
                        "FONTSIZE",
                        (0, 1),
                        (-1, -1),
                        8
                    ),

                    # Alignment
                    (
                        "ALIGN",
                        (0, 0),
                        (-1, -1),
                        "CENTER"
                    ),

                    (
                        "VALIGN",
                        (0, 0),
                        (-1, -1),
                        "MIDDLE"
                    ),

                    # Grid
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),

                    # Padding
                    (
                        "TOPPADDING",
                        (0, 0),
                        (-1, -1),
                        7
                    ),

                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        7
                    ),
                ]
            )
        )


        elements.append(table)
        elements.append(Spacer(1, 25))


    # =====================================================
    # BUILD PDF
    # =====================================================

    doc.build(elements)