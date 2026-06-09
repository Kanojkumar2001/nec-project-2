from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf_report(
    report_name,
    content
):

    doc = SimpleDocTemplate(report_name)

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "Sales Forecast Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1,12))

    story.append(
        Paragraph(
            content.replace("\n", "<br/>"),
            styles["BodyText"]
        )
    )

    doc.build(story)

    return report_name