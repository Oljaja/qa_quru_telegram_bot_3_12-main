from dataclasses import dataclass


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    mobile: str
    address: str
    gender: str
    birth_year: str
    birth_month: str
    birth_day: int
    subject: str
    hobby: str
    picture: str
    state: str
    city: str


olga_larionova = User(first_name='Olga',
                     last_name='Larionova',
                     email='test@gmail.com',
                     mobile='8999955555',
                     address='Angelovo',
                     gender='Other',
                     birth_year='1998',
                     birth_month='August',
                     birth_day=21,
                     subject='Economics',
                     hobby='Sports',
                     picture='111.jpg',
                     state='NCR',
                     city='Delhi')


