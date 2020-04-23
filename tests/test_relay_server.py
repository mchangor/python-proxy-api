import unittest
import responses
from RelayServer import relay_get
from app import logger


class RelayServerTests(unittest.TestCase):

    @responses.activate
    def test_random_uri(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'https://api.gbif.org/v1/test',
            'body': '{"error": "Not Found"}',
            'status': 404,
            'content_type': 'text/html; charset=utf-8'
        })

        response = relay_get('test', logger)

        self.assertEqual({'error': 'Not Found'}, response.json())
        self.assertEqual(404, response.status_code)

    @responses.activate
    def test_some_species(self):
        responses.add(**{
            'method': responses.GET,
            'url': 'https://api.gbif.org/v1/species/1',
            'body': '{"key":1,"taxonID":"gbif:1","kingdom":"Animalia","scientificName":"Animalia","canonicalName":"Animalia"}',
            'status': 200,
            'content_type': 'text/html; charset=utf-8'
        })

        response = relay_get('species/1', logger)

        self.assertIn("key", response.json())
        self.assertEqual(200, response.status_code)


if __name__ == '__main__':
    unittest.main()
