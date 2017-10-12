from sitters.models import Owner, Sitter, Stay

def run():
    print("Deleting all model instance data....")
    Stay.objects.all().delete()
    Sitter.objects.all().delete()
    Owner.objects.all().delete()
    print("done...")