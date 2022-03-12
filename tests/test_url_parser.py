# https://github.com/florian42/url-shortener.git
# https://Florian42@bitbucket.org/fm_streemy/streemy-event-engine.git
# git@bitbucket.org:fm_streemy/streemy-event-engine.git
# git@github.com:florian42/url-shortener.git
from parser import parse

import pytest


class TestUrlParser:
    @pytest.mark.parametrize(
        'test_input,expected',
        [
            (
                'https://github.com/florian42/url-shortener.git',
                'github.com/florian42/url-shortener',
            ),
            (
                'https://github.com/florian42/url-shortener',
                'github.com/florian42/url-shortener',
            ),
            (
                'https://Florian42@bitbucket.org/fm_streemy/streemy.git',
                'bitbucket.org/fm_streemy/streemy',
            ),
        ],
    )
    def test_parses_http_urls(self, test_input, expected):
        actual = parse(test_input)
        assert actual == expected

    @pytest.mark.parametrize(
        'test_input,expected',
        [
            (
                'git@github.com:florian42/url-shortener.git',
                'github.com/florian42/url-shortener',
            ),
            (
                'git@bitbucket.org:fm_streemy/streemy.git',
                'bitbucket.org/fm_streemy/streemy',
            ),
        ],
    )
    def test_parses_ssh_urls(self, test_input, expected):
        actual = parse(test_input)
        assert actual == expected
