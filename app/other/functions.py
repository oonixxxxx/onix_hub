from database import Promo


class Functions:
    def get_referal():
        return f'Реферальная ссылка: '

    def add_promo(promo_line, procent):
        Promo.promos.append([[str(promo_line)], [int(str(procent))]])