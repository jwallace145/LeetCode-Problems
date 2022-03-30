from valid_parantheses.main import is_valid_parantheses


class TestIsValidParantheses:
    def test_simple_parantheses(self):
        assert is_valid_parantheses("()") == True

    def test_nested_parantheses(self):
        assert is_valid_parantheses("(){[]}") == True

    def test_single_parantheses(self):
        assert is_valid_parantheses("(") == False

    def test_right_parantheses(self):
        assert is_valid_parantheses("({((") == False

    def test_left_parantheses(self):
        assert is_valid_parantheses("()}}}") == False

    def test_too_many_left_parantheses(self):
        assert is_valid_parantheses("()((((((") == False
