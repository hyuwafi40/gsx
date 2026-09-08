from core.models import Brand, Participant


def get_brand_context():
    return Brand.get_solo()


def register_participant(**data):
    return Participant.objects.create(**data)
