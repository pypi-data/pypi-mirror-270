for item in container:
    if search_something(item):
        # Found it!
        process(item)
        break
  # leading comment
else   : #fmt: skip
    # Didn't find anything..
    not_found_in_container()


while i < 10:
    print(i)

# leading comment
else   : #fmt: skip
    # Didn't find anything..
    print("I was already larger than 9")


try  :  # fmt: skip
    some_call()
except Exception :  # fmt: skip
    pass
except :  # fmt: skip
    handle_exception()

else   : # fmt: skip
    pass
finally  :  # fmt: skip
    finally_call()
