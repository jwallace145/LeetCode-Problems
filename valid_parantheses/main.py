from collections import deque


def is_valid_parantheses(s: str) -> bool:
    """Determine if the given string of parantheses is valid or not.

    Args:
        s (str): The string of parantheses. Valid elements are ["(", "[", "{", ")", "]", "}"].

    Returns:
        bool: The boolean of whether or not the string contains valid parantheses.
    """
    parantheses_dict = {"(": ")", "[": "]", "{": "}"}
    # use a deque over builtin python list because builtin list is a dynamically allocated array
    # constant time for append() and pop() but as the array grows, dynamic memory allocation will
    # need to occur thus hurting performance time
    stack = deque()
    for parantheses in s:
        # check to see if open right parantheses
        if parantheses in parantheses_dict:
            stack.append(parantheses)
        # if not open parantheses, must be closing parantheses, ensure stack has elements in it
        elif len(stack) > 0:
            popped_element = stack.pop()
            # ensure the parantheses are of the same type
            if parantheses_dict[popped_element] != parantheses:
                return False
        # if stack does not have elements in it, invalid parantheses
        else:
            return False
    # if the stack contains any remaining open parantheses, not all of them were matched with closing
    # parantheses so return False
    return not stack
