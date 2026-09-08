# import logging
# from datetime import datetime
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from core.models import Participant

# logger = logging.getLogger(__name__)

# GENDER_MAP = {
#     "laki-laki": "male",
#     "male": "male",
#     "pria": "male",
#     "perempuan": "female",
#     "female": "female",
#     "wanita": "female",
# }


# def _parse_date(value):
#     if not value:
#         return None
#     if isinstance(value, datetime):
#         return value.date()
#     value = str(value).strip()
#     for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%d/%m/%Y"):
#         try:
#             return datetime.strptime(value, fmt).date()
#         except ValueError:
#             continue
#     return None


# def _clean(value, default=""):
#     if value is None:
#         return default
#     return str(value).strip()


# def _is_valid_email(value):
#     try:
#         validate_email(value)
#         return True
#     except ValidationError:
#         return False


# def upsert_participant_from_data(data):
#     email = _clean(data.get("email"))
#     name = _clean(data.get("nama lengkap") or data.get("name"))
#     stage_name = _clean(data.get("nama panggung") or data.get("stage_name"))
#     nik = _clean(data.get("nomor nik") or data.get("nik"))
#     whatsapp = _clean(data.get("nomor whatsapp") or data.get("whatsapp"))
#     gender = _clean(data.get("jenis kelamin") or data.get("gender"))
#     region = _clean(data.get("region"))
#     photo_close = _clean(data.get("photo closeup") or data.get("photo_close"))
#     photo_selfie = _clean(data.get("photo selfie") or data.get("photo_selfie"))
#     instagram = _clean(data.get("instagram"))
#     tiktok = _clean(data.get("tiktok"))
#     facebook = _clean(data.get("facebook"))
#     birthdate = _parse_date(data.get("tanggal lahir") or data.get("birthdate"))

#     if not email or not name or not stage_name or not nik:
#         raise ValueError("Field wajib tidak lengkap")

#     if not _is_valid_email(email):
#         raise ValueError("Email tidak valid")

#     normalized_gender = GENDER_MAP.get(gender.lower(), gender) if gender else ""

#     existing = Participant.objects.filter(nik=nik).first()
#     if existing:
#         fields_to_compare = {
#             "email": email,
#             "name": name,
#             "stage_name": stage_name,
#             "whatsapp": whatsapp,
#             "gender": normalized_gender,
#             "region": region,
#             "photo_close": photo_close,
#             "photo_selfie": photo_selfie,
#             "instagram": instagram,
#             "tiktok": tiktok,
#             "facebook": facebook,
#             "birthdate": birthdate,
#             "status": "registered",
#         }
#         changed = False
#         for field, value in fields_to_compare.items():
#             if getattr(existing, field) != value:
#                 changed = True
#                 break

#         if not changed:
#             logger.info("Participant with NIK %s already up to date", nik)
#             return existing, False

#     participant, created = Participant.objects.update_or_create(
#         nik=nik,
#         defaults={
#             "email": email,
#             "name": name,
#             "stage_name": stage_name,
#             "whatsapp": whatsapp,
#             "gender": normalized_gender,
#             "region": region,
#             "photo_close": photo_close,
#             "photo_selfie": photo_selfie,
#             "instagram": instagram,
#             "tiktok": tiktok,
#             "facebook": facebook,
#             "birthdate": birthdate,
#             "status": "registered",
#         },
#     )
#     logger.info("Participant %s with NIK %s", "created" if created else "updated", nik)
#     return participant, created
import logging
from datetime import datetime
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from core.models import Participant

logger = logging.getLogger(__name__)

GENDER_MAP = {
    "laki-laki": "male",
    "male": "male",
    "pria": "male",
    "perempuan": "female",
    "female": "female",
    "wanita": "female",
}


def _parse_date(value):
    if not value:
        return None
    if isinstance(value, datetime):
        return value.date()
    value = str(value).strip()
    if "T" in value:
        try:
            return datetime.fromisoformat(value.replace("Z", "+00:00")).date()
        except ValueError:
            pass
    for fmt in ("%Y-%m-%d", "%d-%m-%Y", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            continue
    return None


def _clean(value, default=""):
    if value is None:
        return default
    return str(value).strip()


def _is_valid_email(value):
    try:
        validate_email(value)
        return True
    except ValidationError:
        return False


def upsert_participant_from_data(data):
    email = _clean(data.get("email"))
    name = _clean(data.get("nama lengkap") or data.get("name"))
    stage_name = _clean(data.get("nama panggung") or data.get("stage_name"))
    nik = _clean(data.get("nomor nik") or data.get("nik"))
    whatsapp = _clean(data.get("nomor whatsapp") or data.get("whatsapp"))
    gender = _clean(data.get("jenis kelamin") or data.get("gender"))
    region = _clean(data.get("region"))
    photo_close = _clean(data.get("photo closeup") or data.get("photo_close"))
    photo_selfie = _clean(data.get("photo selfie") or data.get("photo_selfie"))
    instagram = _clean(data.get("instagram"))
    tiktok = _clean(data.get("tiktok"))
    facebook = _clean(data.get("facebook"))
    birthdate = _parse_date(data.get("tanggal lahir") or data.get("birthdate"))

    if not email or not name or not stage_name or not nik:
        raise ValueError("Field wajib tidak lengkap")

    if not _is_valid_email(email):
        raise ValueError("Email tidak valid")

    normalized_gender = GENDER_MAP.get(gender.lower(), gender) if gender else ""

    defaults = {
        "email": email,
        "name": name,
        "stage_name": stage_name,
        "whatsapp": whatsapp,
        "gender": normalized_gender,
        "region": region,
        "photo_close": photo_close,
        "photo_selfie": photo_selfie,
        "instagram": instagram,
        "tiktok": tiktok,
        "facebook": facebook,
        "birthdate": birthdate,
        "status": "registered",
    }

    participant, created = Participant.objects.update_or_create(
        nik=nik,
        defaults=defaults,
    )

    logger.info("Participant %s with NIK %s", "created" if created else "updated", nik)
    return participant, created
