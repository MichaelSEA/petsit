# scripts/import_data.py
'''
fields:
    0 rating,
    1 sitter_image,
    2 end_date,
    3 text,
    4 owner_image,
    5 dogs, (note: multiple dogs separated by '|' symbol)
    6 sitter,
    7 owner,
    8 start_date,
    9 sitter_phone_number,
    10 sitter_email,
    11 owner_phone_number,
    12 owner_email
'''

import datetime

from sitters.models import Owner, Sitter, Stay


def create_owner(values):
    owner, _ = Owner.objects.get_or_create(name=values[7],
                                           image=values[4],
                                           phone_number=values[11],
                                           email=values[12])
    return owner


def create_sitter(values):
    sitter, _ = Sitter.objects.get_or_create(name=values[6],
                                             image=values[1],
                                             phone_number=values[9],
                                             email=values[10])

    # When a sitter has no stays, their Overall Sitter Rank is equal
    # to the Sitter Score.
    # sitter.sitter_score = sitter.overall_sitter_rank = compute_sitter_score(sitter.name)
    sitter.save()

    return sitter


def create_stay(owner, sitter, values):
    Stay.objects.create(rating=values[0],
                        comments=values[3],
                        sitter=sitter,
                        owner=owner,
                        dogs=values[5],
                        start_date=datetime.datetime.strptime(values[8], '%Y-%m-%d').date(),
                        end_date=datetime.datetime.strptime(values[2], '%Y-%m-%d').date()
                        )
    return


def run():
    print("importing data from reviews.csv...")

    i = 0

    with open('../reviews.csv') as f:
        for line in f:
            if i == 0:
                i += 1
                continue

            values = list(line.split(','))
            owner = create_owner(values)
            sitter = create_sitter(values)
            create_stay(owner, sitter, values)
            i += 1

    print(f"done... processed {i-1} reviews....")