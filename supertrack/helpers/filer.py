import os


def ticket_image_upload_path(instance, filename):
    return os.path.join("ticket", str(instance.public_id), filename)

def mercadona_product_image_upload_path(instance, filename):
    return os.path.join("mercadona", str(instance.name), filename)

def mercadona_category_product_image_upload_path(instance, filename):
    return os.path.join("mercadona", str(instance.name), filename)

def consum_product_image_upload_path(instance, filename):
    return os.path.join("consum", str(instance.name), filename)

def consum_category_product_image_upload_path(instance, filename):
    return os.path.join("consum", str(instance.name), filename)
