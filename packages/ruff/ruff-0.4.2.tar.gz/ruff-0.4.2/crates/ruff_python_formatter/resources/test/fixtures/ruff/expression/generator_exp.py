(a for b in c)

# parens around generator expression not required
len(a for b in c)

# parens around generator expression required
sum((a for b in c), start=0)

# black keeps these atm, but intends to remove them in the future:
# https://github.com/psf/black/issues/2943
f((1 for _ in a))

# make sure source parenthesis detection isn't fooled by these
f((1) for _ in (a))

# combination of the two above
f(((1) for _ in (a)))

bases = tuple(
     (base._meta.label_lower if hasattr(base, "_meta") else base)
     for base in flattened_bases
)


# black keeps these atm, but intends to remove them in the future:
# https://github.com/psf/black/issues/2943
len(
    ( # leading
    a for b in c
     # trailing
    )
)

len(
    # leading
    a for b in c
    # trailing
)

a = (
    aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    for f in bbbbbbbbbbbbbbb
    if f not in ccccccccccc
)

a = (
    [1, 2, 3,]
    for f in bbbbbbbbbbbbbbb
    if f not in ccccccccccc
)

aaaaaaaaaaaaaaaaaaaaa = (
    o for o in self.registry.values if o.__class__ is not ModelAdmin
)

# Regression test for: https://github.com/astral-sh/ruff/issues/7623
tuple(
    0  # comment
    for x in y
)

tuple(
    (0  # comment
    for x in y)
)

tuple(
    (  # comment
        0 for x in y
    )
)
