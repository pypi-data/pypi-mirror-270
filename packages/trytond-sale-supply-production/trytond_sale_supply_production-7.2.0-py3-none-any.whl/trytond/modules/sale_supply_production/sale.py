# This file is part of Tryton.  The COPYRIGHT file at the top level of
# this repository contains the full copyright notices and license terms.
import datetime as dt

from trytond.model import fields
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction


class Sale(metaclass=PoolMeta):
    __name__ = 'sale.sale'

    @classmethod
    def _process_supply(cls, sales, product_quantities):
        pool = Pool()
        Production = pool.get('production')

        productions = []
        for sale in sales:
            productions.extend(sale.create_productions(product_quantities))
        Production.save(productions)
        Production.set_moves(productions)
        super()._process_supply(sales, product_quantities)

    def create_productions(self, product_quantities):
        productions = []
        for line in self.lines:
            production = line.get_production(product_quantities)
            if not production:
                continue
            production.set_planned_start_date()
            productions.append(production)
            assert not line.productions
        return productions


class Line(metaclass=PoolMeta):
    __name__ = 'sale.line'

    productions = fields.One2Many(
        'production', 'origin', "Productions", readonly=True)

    @property
    def has_supply(self):
        return super().has_supply or bool(self.productions)

    def get_supply_state(self, name):
        state = super().get_supply_state(name)
        if self.productions:
            states = {p.state for p in self.productions}
            if states <= {'running', 'done', 'cancelled'}:
                if states == {'cancelled'}:
                    state = 'cancelled'
                else:
                    state = 'supplied'
            else:
                state = 'requested'
        return state

    @classmethod
    def copy(cls, lines, default=None):
        if default is None:
            default = {}
        else:
            default = default.copy()
        default.setdefault('productions', None)
        return super().copy(lines, default=default)

    def get_production(self, product_quantities):
        "Return production for the sale line"
        pool = Pool()
        Production = pool.get('production')
        Date = pool.get('ir.date')
        Uom = pool.get('product.uom')

        with Transaction().set_context(company=self.sale.company.id):
            today = Date.today()

        if (not self.supply_on_sale
                or self.productions
                or not self.ready_for_supply
                or not self.product.producible):
            return

        product = self.product
        quantity = self._get_move_quantity('out')
        if product.supply_on_sale == 'stock_first':
            available_qty = product_quantities[product]
            available_qty = Uom.compute_qty(
                product.default_uom, available_qty, self.unit,
                round=False)
            if quantity < available_qty:
                product_quantities[product] -= Uom.compute_qty(
                    self.unit, quantity, product.default_uom, round=False)
                return

        date = self.shipping_date or today
        if date <= today:
            date = today
        else:
            date -= dt.timedelta(1)
        return Production(
            planned_date=date,
            company=self.sale.company,
            warehouse=self.warehouse,
            location=self.warehouse.production_location,
            product=product,
            bom=product.boms[0].bom if product.boms else None,
            unit=self.unit,
            quantity=quantity,
            state='request',
            origin=self,
            )
