class Event:
    event_name: ClassVar[str]

    @staticmethod
    def cls_for(event_name: str) -> type[Event]:
        event_cls = _CONCRETE_EVENT_CLASSES.get(event_name)
        if event_cls is not <RANGE_START>None:
            return event_cls<RANGE_END>
        else:
            raise ValueError(f"unknown event name '{event_name}'")

class Event:
    event_name: ClassVar[str]

    @staticmethod
    def cls_for(event_name: str) -> type[Event]:
        event_cls = _CONCRETE_EVENT_CLASSES.get(event_name)
        if event_cls is not None:
            <RANGE_START>

            <RANGE_END>
            return event_cls
        else:
            raise ValueError(f"unknown event name '{event_name}'")


# The user starts adding items to a list and then hits save.
# Ruff should trim the empty lines
a = [
    1,
    2,
    3,<RANGE_START>


    <RANGE_END>
]

print("Don't format this"  )


# The user removed an argument from a call. Ruff should reformat the entire call
call(
    a,
    <RANGE_START>
    <RANGE_END>b,
    c,
    d
)

print("Don't format this"  )


#-----------------------------------------------------------------------------
# The user adds a new comment at the end:
<RANGE_START># <RANGE_END>
#-----------------------------------------------------------------------------

print("Don't format this"  )


def convert_str(value: str) -> str:  # Trailing comment
    """Return a string as-is."""

<RANGE_START>

    return value  # Trailing comment
<RANGE_END>
def test  ():
    pass


def test_comment_indent():
<RANGE_START># A misaligned comment<RANGE_END>
    print("test")


# This demonstrates the use case where a user inserts a new function or class after an existing function.
# In this case, we should avoid formatting the node that directly precedes the new function/class.
# However, the problem is that the preceding node **must** be formatted to determine the whitespace between the two statements.
def test_start ():
    print("Ideally this gets not reformatted" )

<RANGE_START>
def new_function_inserted_after_test_start ():
    print("This should get formatted" )<RANGE_END>
