import csv
import os

import pandas as pd
from django.http import HttpResponse

from dashboard.models import (
    Driver,
    ToolBoxMeetingTopic,
    DriverToolBoxMeetingAttended
)


# -----------------------------------------------------------
# Example Utility / Basic Views
# -----------------------------------------------------------

def remove_null_images(_):
    """
    Updates any Driver object whose .image field is literally
    'Null' (string) to None.
    """
    drivers_with_null = Driver.objects.filter(image='Null')
    for driver in drivers_with_null:
        driver.image = None
        driver.save()
    return HttpResponse("Records updated successfully.")


def import_drivers_from_images(_):
    """
    Loops through image folder, matches filename to driver_number,
    and updates the Driver's image field.
    """
    image_folder = '/Users/AWB/Downloads/img'
    for filename in os.listdir(image_folder):
        driver_number = os.path.splitext(filename)[0]
        try:
            driver = Driver.objects.get(driver_number=driver_number)
            driver.image = f'driver_images/{filename}'
            driver.save()
        except Driver.DoesNotExist:
            pass
    return HttpResponse("Drivers updated successfully.")


def count_uploaded_images(_):
    """
    Counts how many Driver objects have a non-empty image field.
    """
    count = Driver.objects.exclude(image__exact='').count()
    return HttpResponse(f"Number of uploaded images: {count}")


def match_driver_ids(_):
    """
    Reads a CSV with column 'D_Number'; tries to match it with
    a driver_number in Driver model, then writes the matched
    driver.id to a new CSV.
    """
    csv_file_path = '/Users/AWB/Desktop/Book2.csv'

    def get_driver_id(d_number):
        try:
            driver = Driver.objects.get(driver_number=d_number)
            return driver.id
        except Driver.DoesNotExist:
            return None

    df = pd.read_csv(csv_file_path)
    df['Driver_ID'] = df['D_Number'].apply(get_driver_id)
    output_csv_file_path = os.path.join(os.getcwd(), 'output.csv')
    df.to_csv(output_csv_file_path, index=False)

    with open(output_csv_file_path, 'rb') as csv_file:
        response = HttpResponse(csv_file.read(), content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=output.csv'
        return response


def update_models_from_csv(_):
    """
    Reads a CSV (tb.csv) with lines of: driver_id, meeting1, meeting2, ...
    For each row, it updates or creates `DriverToolBoxMeetingAttended` records.
    """
    with open('/Users/AWB/Desktop/tb.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if len(row) >= 3:
                driver_id = int(row[0])
                driver, _ = Driver.objects.get_or_create(id=driver_id)
                for column_index, meeting_count in enumerate(row[1:], start=1):
                    if meeting_count:
                        try:
                            meeting_count = int(meeting_count)
                        except ValueError:
                            continue

                        meeting_topic = ToolBoxMeetingTopic.objects.get(id=column_index)
                        DriverToolBoxMeetingAttended.objects.update_or_create(
                            driver=driver,
                            meeting_topic=meeting_topic,
                            defaults={'no_of_times_attended': meeting_count}
                        )
    return HttpResponse("Models updated from CSV file.")


# def print_user_data_pdf(request, user_id):
#     # Use the correct field name
#     driver = get_object_or_404(Driver, D_ID=user_id)

#     # Replace with your actual HTML template path
#     template_path = 'driver/driver_view.html'
#     context = {'driver': driver}

#     response = HttpResponse(content_type='application/pdf')
#     # Assuming 'D_Name' is a field in your model
#     response['Content-Disposition'] = f'filename="{driver.D_Name}_profile.pdf"'

#     template = get_template(template_path)
#     html = template.render(context)
#     pisa_status = pisa.CreatePDF(html, dest=response)

#     if pisa_status.err:
#         return HttpResponse('We had some errors <pre>' + html + '</pre>')

#     return response
