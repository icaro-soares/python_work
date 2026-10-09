def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info


user_profile = build_profile(
        first_name='ícaro',
        last_name='oliveira',
        city='recife',
        age=30,
        country='brazil',
)

for k, v in user_profile.items():
    print(f"{k}: {v}")
