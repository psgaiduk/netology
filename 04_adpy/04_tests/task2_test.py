import app_task_2
import pytest

#  ???Не нашёл как проверить именно response сделал через строку, не знаю можно ли так делать
class TestSuit:
    def test_create_ya_disk_folder(self):
        app_task_2.create_ya_disk_folder('one')
        assert str(app_task_2.look_ya_disk_folder('one')) == '<Response [200]>'