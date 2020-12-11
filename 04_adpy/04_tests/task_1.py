from unittest.mock import patch

import app
import pytest


class TestSuit:
    @patch('builtins.input')
    def test_secretary_program_start_end(self, m_input):
        m_input.side_effect = ['q']
        assert app.secretary_program_start() is None

    @patch('builtins.input')
    @pytest.mark.parametrize("test_input,expected", [(["11-2"], "Геннадий Покемонов"),
                                                     (["2207 876234"], "Василий Гупкин"),
                                                     (["10006"], "Аристарх Павлов")])
    def test_get_doc_owner_name(self, m_input, test_input, expected):
        m_input.side_effect = test_input
        assert app.get_doc_owner_name() == expected

    def test_get_all_doc_owners_names(self):
        assert app.get_all_doc_owners_names() == {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}

    # ??? Непонятно надо ли такие функции проверять, которые работают через другие функции?
    # def test_show_all_docs_info(self):
    #     assert app.show_all_docs_info() == ''

    @pytest.mark.parametrize("test_input,expected", [
        ({"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
         'invoice "11-2" "Геннадий Покемонов"'),
        ({"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
         'passport "2207 876234" "Василий Гупкин"'),
        ({"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
         'insurance "10006" "Аристарх Павлов"')])
    def test_show_document_info(self, test_input, expected):
        assert app.show_document_info(test_input) == expected

    @patch('builtins.input')
    @pytest.mark.parametrize("test_input,expected", [(["11-2"], '1'),
                                                     (["2207 876234"], '1'),
                                                     (["10006"], '2')])
    def test_get_doc_shelf(self, m_input, test_input, expected):
        m_input.side_effect = test_input
        assert app.get_doc_shelf() == expected

    @patch('builtins.input')
    def test_add_new_doc(self, m_input):
        m_input.side_effect = ['11', 'type doc', 'Owner name', '3']
        query_assert = {"type": "type doc", "number": "11", "name": "Owner name"}
        assert app.show_document_info(query_assert) == 'type doc "11" "Owner name"'

    @patch('builtins.input')
    def test_delete_doc(self, m_input):
        m_input.side_effect = ['11-2','11-2']
        app.delete_doc()
        assert app.get_doc_owner_name() is None

    @patch('builtins.input')
    @pytest.mark.parametrize("test_input,expected", [(['11-2', '3', '11-2'], '3'),
                                                     (['11-2', '4', '11-2'], '4')])
    def test_move_doc_to_shelf(self, m_input, test_input, expected):
        m_input.side_effect = test_input
        app.move_doc_to_shelf()
        assert app.get_doc_shelf() == expected


