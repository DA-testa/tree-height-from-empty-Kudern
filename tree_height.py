from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])

def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]

def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, add to stack
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, check if matches last opening bracket
            if len(opening_brackets_stack) == 0:
                # no opening bracket to match with
                return i+1
            last_opening_bracket = opening_brackets_stack.pop()
            if not are_matching(last_opening_bracket.char, next):
                # not a match with the last opening bracket
                return i+1

    # after processing all characters
    if len(opening_brackets_stack) != 0:
        # there are some unmatched opening brackets left
        last_unmatched_opening_bracket = opening_brackets_stack[0]
        return last_unmatched_opening_bracket.position
    
    # all brackets are properly matched
    return "Success"

def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch)

if __name__ == "__main__":
    main()
