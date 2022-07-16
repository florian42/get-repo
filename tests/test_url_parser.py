import pytest

from get_repo import parse


class TestUrlParser:
    @pytest.mark.parametrize(
        'test_input,expected',
        [
            (
                'https://github.com/florian42/get-repo.git',
                'github.com/florian42/get-repo',
            ),
            (
                'https://github.com/florian42/get-repo',
                'github.com/florian42/get-repo',
            ),
            (
                'https://Florian42@bitbucket.org/something/streamit.git',
                'bitbucket.org/something/streamit',
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
                'git@github.com:florian42/get-repo.git',
                'github.com/florian42/get-repo',
            ),
            (
                'git@bitbucket.org:something/streamit.git',
                'bitbucket.org/something/streamit',
            ),
        ],
    )
    def test_parses_ssh_urls(self, test_input, expected):
        actual = parse(test_input)
        assert actual == expected
