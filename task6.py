# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
import user as user


@pytest.fixture()
def new_user():
    return {
        user.User('John', '1', '3'),
        user.User('Jack', '2', '3'),
        user.User('Monica', '3', '2')
    }


def test_1(new_user):
    new_project = user.Project()
    result = new_project.get_users('module/users.json')
    assert result == new_user


def test_2():
    new_project = user.Project()
    new_project.get_users('module/users.json')
    new_project.login('John', '1')
    assert new_project.active_user == user.User('John', '1', '3')


def test_3():
    new_project = user.Project()
    new_project.get_users('module/users.json')
    with pytest.raises(user.LevelException,
                       match='Нельзя создать пользователя не залогиневшись или если ваш уровень меньше'):
        new_project.add_user('Ivan', '5', '5')


if __name__ == '__main__':
    pytest.main(['-vv'])
