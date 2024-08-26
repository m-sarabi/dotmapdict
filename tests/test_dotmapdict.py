import unittest
from dotmapdict import DotDict


class TestDotDict(unittest.TestCase):
    def test_dot_notation(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        self.assertEqual(d.a.b, 1)
        self.assertEqual(d.c, 3)

    def test_update(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        d.update({"a": {"c": 2}})
        self.assertEqual(d.a.b, 1)
        self.assertEqual(d.a.c, 2)
        self.assertEqual(d.c, 3)

    def test_merge(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        d.merge({"a": {"c": 2}})
        self.assertEqual(d.a.b, 1)
        self.assertEqual(d.a.c, 2)
        self.assertEqual(d.c, 3)

    def test_to_dict(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        self.assertEqual(d.to_dict(), {"a": {"b": 1}, "c": 3})
        self.assertEqual(type(d.to_dict()), dict)

    def test_getattr(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        self.assertEqual(d.a.b, 1)
        self.assertEqual(d.c, 3)

    def test_setattr(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        d.a.c = 2
        self.assertEqual(d.a.b, 1)
        self.assertEqual(d.a.c, 2)
        self.assertEqual(d.c, 3)

    def test_delattr(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        del d.a.b
        self.assertEqual(d.a.b, None)
        self.assertEqual(d.a, {})
        self.assertEqual(d.c, 3)

    def test_get(self):
        d = DotDict({"a": {"b": 1}}, c=3)
        self.assertEqual(d.get("a"), {"b": 1})
        self.assertEqual(d.get("c"), 3)
        self.assertEqual(d.get("d", 4), 4)

