"""This file should have our order classes in it."""
class AbstractMelonOrder(object):
    """DOCSTRING"""

    def __init__(self, species, qty, order_type, shipped=False):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.order_type = order_type


    def get_total(self):
        """Calculate price."""

        base_price = 5
       
        if self.species == "christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        if self.order_type == "international" and self.qty < 10:
            total += 3 

        return total

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""

    tax = 0.08

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "domestic")


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    tax = 0.17

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""

        super(InternationalMelonOrder, self).__init__(species, qty, "international")
        
        self.country_code = country_code


    def get_country_code(self):
        """Return the country code."""

        return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """A Government order is created."""

    tax = 0
    passed_inspection = False

    def __init__(self, species, qty):
        """Initialize melon order attributes"""

        super(GovernmentMelonOrder, self).__init__(species, qty, "government")


    def mark_passed(self):
        """Mark melon(s) have passed security inspection."""

        self.passed_inspection = True
