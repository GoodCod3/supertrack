import os


def ticket_image_upload_path(instance, filename):
    return os.path.join("ticket", str(instance.pk), filename)