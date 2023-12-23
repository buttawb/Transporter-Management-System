from PIL import Image
from dashboard.models import Driver
import os
import sys
sys.path.append('/Users/AWB/Documents/HGGC_NEW/mysite')



image_folder = '/Users/AWB/Downloads/img'

for filename in os.listdir(image_folder):
    driver_number = os.path.splitext(filename)[0]  # Assuming the file name is the driver number
    driver, created = Driver.objects.get_or_create(D_Number=driver_number)
    if created:
        driver.D_Image = f'driver_images/{filename}'  # Update with your upload path
        driver.save()
