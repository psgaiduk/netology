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

