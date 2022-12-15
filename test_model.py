from datetime import date, timedelta
import pytest

from model import Batch, OrderLine


today = date.today()
tomorrow = today + timedelta(days=1)
later = tomorrow + timedelta(days=10)


def make_batch_and_line(sku, batch_qty, line_qty):
    return (
        Batch('batch-001', sku, batch_qty, date.today()),
        OrderLine('order-123', sku, line_qty)
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch("batch-001", "SMALL-TABLE", qty=20, eta=date.today())
    line = OrderLine("order-ref", "SMALL-TABLE", 2)

    batch.allocate(line)

    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = make_batch_and_line("ELEGANT_LAMP", 20, 2)
    assert large_batch.can_allocate(small_line)


# def test_cannot_allocate_if_available_smaller_than_required():
#     pytest.fail("todo")


# def test_can_allocate_if_available_equal_to_required():
#     pytest.fail("todo")


# def test_prefers_warehouse_batches_to_shipments():
#     pytest.fail("todo")


# def test_prefers_earlier_batches():
#     pytest.fail("todo")
