# uncompyle6 version 3.9.0
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 3.10.9 | packaged by Anaconda, Inc. | (main, Mar  8 2023, 10:42:25) [MSC v.1916 64 bit (AMD64)]
# Embedded file name: sqlite3\test\py25tests.pyc
# Compiled at: 2011-03-08 09:43:22
from __future__ import with_statement
import unittest, sqlite3 as sqlite
did_rollback = False

class MyConnection(sqlite.Connection):

    def rollback(self):
        global did_rollback
        did_rollback = True
        sqlite.Connection.rollback(self)


class ContextTests(unittest.TestCase):

    def setUp(self):
        global did_rollback
        self.con = sqlite.connect(':memory:', factory=MyConnection)
        self.con.execute('create table test(c unique)')
        did_rollback = False

    def tearDown(self):
        self.con.close()

    def CheckContextManager(self):
        """Can the connection be used as a context manager at all?"""
        with self.con:
            pass

    def CheckContextManagerCommit(self):
        """Is a commit called in the context manager?"""
        with self.con:
            self.con.execute("insert into test(c) values ('foo')")
        self.con.rollback()
        count = self.con.execute('select count(*) from test').fetchone()[0]
        self.assertEqual(count, 1)

    def CheckContextManagerRollback(self):
        """Is a rollback called in the context manager?"""
        self.assertEqual(did_rollback, False)
        try:
            with self.con:
                self.con.execute('insert into test(c) values (4)')
                self.con.execute('insert into test(c) values (4)')
        except sqlite.IntegrityError:
            pass

        self.assertEqual(did_rollback, True)


def suite():
    ctx_suite = unittest.makeSuite(ContextTests, 'Check')
    return unittest.TestSuite((ctx_suite,))


def test():
    runner = unittest.TextTestRunner()
    runner.run(suite())


if __name__ == '__main__':
    test()