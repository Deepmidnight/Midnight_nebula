from Mytests.api import PetFriends
from Mytests.settings import valid_email, valid_password

pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    status, result = pf.get_api_key(email, password)
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_post_new_friends(name='Zlati', animal_type='retriever', age='3', pet_photo='images/retriver.jpg'):
    """Проверка функционала добавления питомца с корректными данными (по кличке)"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    # Добавляем питомца
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_post_new_friends_2(name='Zlati', animal_type='retriever', age='3', pet_photo='images/retriver.jpg'):
    """Проверка функционала добавления питомца с корректными данными (по типу)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['animal_type'] == animal_type


def test_post_new_friends_3(name='Zlati', animal_type='retriever', age='3', pet_photo='images/retriver.jpg'):
    """Проверка функционала добавления питомца с корректными данными (по возрасту)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age


def test_post_new_friends_4(name='Zlati', animal_type='retriever', age='3', pet_photo='images/retriver.jpg'):
    """Проверка функционала добавления питомца с корректными данными (по фото)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['pet_photo'] != pet_photo


def test_post_new_friends_5(name='Zlati', animal_type='retriever', age='3', ):
    """Проверка функционала добавления питомца с корректными данными (без фото)"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends_without_photo(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_add_new_pet_with_negative_age(name='Zlati', animal_type='retriever', age='-3',
                                       pet_photo='images/retriver.jpg'):
    """Проверка функционала добавления питомца с отрицательным возрастом - Баг"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.post_new_friends(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['age'] == age


def test_delete_pet():
    """Проверка функционала удаления питомца"""
    # Получаем ключ auth_key и запрашиваем список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Проверяем - если список своих питомцев пустой, то добавляем нового и опять
    # запрашиваем список своих питомцев
    if len(my_pets['pets']) == 0:
        pf.post_new_friends(auth_key, "Eminem", "cat", "5", "images/eminem.jpg")
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Берём id первого питомца из списка и отправляем запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = pf.delete_pet(auth_key, pet_id)

    # Ещё раз запрашиваем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    # Проверяем что статус ответа равен 200 и в списке питомцев нет id удалённого питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_put_self_pet_info(name='Zlati', animal_type='retriever', age='3'):
    """Проверка функционала изменения клички питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['name'] == name


def test_put_self_pet_info_2(name='Zlati', animal_type='golden retriever', age='3'):
    """Проверка функционала изменения информации о виде питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['animal_type'] == animal_type


def test_put_self_pet_info_3(name='Zlati', animal_type='retriever', age='18'):
    """Проверка функционала изменения информации о возрасте питомца"""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.put_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)
    assert status == 200
    assert result['age'] == age
