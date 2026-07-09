import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sem_lo2.auth import authenticate, create_user, find_user


def test_seed_and_auth():
    # This test assumes seed_data has been run
    u = find_user('admin')
    assert u is not None
    a = authenticate('admin', 'adminpass')
    assert a is not None
