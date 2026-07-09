import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from sem_lo2.auth import authenticate, create_user, find_user
from sem_lo2.operations import load_products, sell_product, purchase_product, load_finances
from sem_lo2.seed_data import generate as seed_generate


def test_seed_and_auth_and_operations(tmp_path):
    # setup: seed data into a temporary data directory
    # change environment to use tmp_path as sem_lo2/data
    repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    data_dir = os.path.join(repo_root, 'data')
    # run seed to populate data (writes into repo data)
    seed_generate()

    u = find_user('admin')
    assert u is not None
    a = authenticate('admin', 'adminpass')
    assert a is not None

    catalog = load_products()
    assert len(catalog.products) >= 3

    # perform a sale as seller
    seller = authenticate('seller', 'sellerpass')
    p = catalog.products[0]
    before_stock = p.stock
    tx = sell_product(seller, p.id, 1)
    assert tx.kind == 'sale'
    # reload products and finances
    catalog2 = load_products()
    p2 = catalog2.find(p.id)
    assert p2.stock == before_stock - 1

    fin = load_finances()
    assert fin.balance != 0.0
