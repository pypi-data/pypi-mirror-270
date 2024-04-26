import os
import unittest
from unittest.mock import patch
from gaia._template import TemplateManager


class TestTemplateManager(unittest.TestCase):

    def setUp(self):
        self.template_manager = TemplateManager('/tmp')

    @patch('os.listdir')
    def test_get_all_templates(self, mock_listdir):
        mock_listdir.return_value = ['template1', 'template2']
        result = self.template_manager.get_all_templates()
        self.assertEqual(result, ['template1', 'template2'])

    @patch('os.path.exists')
    def test_is_template_exists(self, mock_exists):
        mock_exists.return_value = True
        result = self.template_manager._TemplateManager__is_template_exists(
            'test_template'
            )
        self.assertTrue(result)

    @patch('os.path.exists')
    def test_create_template_exists(self, mock_exists):
        mock_exists.return_value = True
        with self.assertRaises(Exception):
            self.template_manager.create_template('existing_template', 'content')

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="content")
    def test_get_template_content(self, mock_open, mock_exists):
        mock_exists.return_value = True
        result = self.template_manager.get_template_content('existing_template')
        self.assertEqual(result, 'content')

    @patch('os.path.exists')
    @patch('os.remove')
    def test_delete_template(self, mock_remove, mock_exists):
        mock_remove.return_value = None
        mock_exists.return_value = True
        self.template_manager.delete_template('existing_template')

    @patch('os.path.exists')
    @patch('os.path.join')
    def test_get_template_path(self, mock_join, mock_exists):
        mock_join.return_value = '/tmp/existing_template'
        mock_exists.return_value = True
        result = self.template_manager.get_template_path('existing_template')
        self.assertEqual(result, '/tmp/existing_template')


if __name__ == '__main__':
    unittest.main()
