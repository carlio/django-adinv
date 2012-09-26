import unittest
from adinv.chooser.decorator import chooser, registered_choosers
from django.core.exceptions import ImproperlyConfigured

class DecoratorTest(unittest.TestCase):
    
    def test_without_calling(self):
        """
        Tests that the `chooser` decorator can be used without calling it
        (ie, can be used like '@chooser')
        """
        @chooser
        def chooser_without_calling(slot, *args):
            return 'test_output_1'
        
        self.assertTrue('chooser_without_calling' in registered_choosers)
        self.assertEqual('test_output_1', registered_choosers['chooser_without_calling'](None) )

    def test_with_name(self):
        """
        Tests that the `chooser` decorator honours the 'name=' argument
        when registering
        """
        @chooser(name='lovely')
        def chooser_explicitly_named(slot, *args):
            print 'cockls'
            return 'test_output_2'
        
        self.assertTrue('lovely' in registered_choosers)
        self.assertEqual('test_output_2', registered_choosers['lovely'](None) )

    def test_without_name(self):
        """
        Tests that the decorator cannot be called without specifying the name (ie,
        can't be used like '@chooser()')
        """
        try:
            @chooser()
            def chooser_no_name_given(slot, *args):
                return 'test_output_3'
        except ImproperlyConfigured:
            # this is expected
            self.assertFalse('chooser_no_name_given' in registered_choosers)
        else:
            self.fail('Should have thrown an improperly configured exception')