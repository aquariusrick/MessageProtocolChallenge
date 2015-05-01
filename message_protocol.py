possible_messages = 'abcdefghij'  # These are valid messages, they can optionally be prefixed with 'Z'
tuple_prefix = 'MKPQ'  # A message prefixed with this should contain two messages


class InvalidMessageException(Exception):
    pass


def check_message(msg):
    """
    We start out looking for a single valid message.  If we encounter one of the 'tuple_prefix' characters then we're
    looking for two messages following it.  We use recursion to find the two messages associated with any
    tuple_prefix chars we come across.  As long as we find the expected number of messages for each tuple we continue
    on.  Z characters can be skipped because they don't change the validity of the message.
    :param msg:
    :return:
    """
    def validate_messages(pointer=0, num_messages_expected=1):
        for _ in range(num_messages_expected):
            if pointer == len(msg):             # No more messages left, but we expected one
                raise InvalidMessageException()

            current_char = msg[pointer]
            while current_char == 'Z':             # Skip the Z's; they're basically pointless
                pointer += 1
                current_char = msg[pointer]

            if current_char in possible_messages:   # This is a valid message
                pointer += 1
                continue

            elif current_char in tuple_prefix:      # This is a message tuple
                pointer += 1
                pointer = validate_messages(pointer=pointer, num_messages_expected=2)
                continue

            elif current_char.isdigit():      # This is a n-tuple
                expected = ""
                while current_char.isdigit():
                    expected += current_char
                    pointer += 1
                    current_char = msg[pointer]
                pointer = validate_messages(pointer=pointer, num_messages_expected=int(expected))
                continue

            raise InvalidMessageException()

        return pointer

    try:
        pointer = validate_messages(pointer=0, num_messages_expected=1)
        return "VALID" if pointer == len(msg) else "INVALID"
    except InvalidMessageException:
        return "INVALID"

