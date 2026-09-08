URL_MAX_LENGTH = 255
NIK_MAX_LENGTH = 16

GENDER_CHOICES = [
    ("male", "Male"),
    ("female", "Female"),
]

STATUS_CHOICES = [
    ("registered", "Registered"),
    ("verified", "Verified"),
]

ALBUM_STATUS_CHOICES = [
    ("draft", "Draft"),
    ("published", "Published"),
]

ROLE_DEVELOPER = "developer"
ROLE_ADMINISTRATOR = "administrator"
ROLE_REGULER = "reguler"
ROLE_NONACTIVE = "nonactive"

ACCOUNT_ROLE_CHOICES = [
    (ROLE_DEVELOPER, "Developer"),
    (ROLE_ADMINISTRATOR, "Administrator"),
    (ROLE_REGULER, "Reguler"),
    (ROLE_NONACTIVE, "Nonactive"),
]

ACCOUNT_ROLE_CHOICES_LIMITED = [
    (ROLE_ADMINISTRATOR, "Administrator"),
    (ROLE_REGULER, "Reguler"),
    (ROLE_NONACTIVE, "Nonactive"),
]
