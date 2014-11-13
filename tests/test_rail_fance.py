from ccrypt.rail_fence import RailFence
from ccrypt.utils import k27


params = {
    'alphabet': k27,
    'rails': 3
}


def test_params():
    r = RailFence(**params)
    assert r.alphabet == k27
    assert r.rails == 3

