import uroman as ur

def get_names(count=10) -> list[str]:
    from faker import Faker

    # fake = Faker('pl_PL')
    fake = Faker('fa_IR')

    uroman = ur.Uroman()
    res  =[uroman.romanize_string(fake.name(), lcode='pus') for _ in range(count)]

    return res


if __name__ == '__main__':
    print(get_names())