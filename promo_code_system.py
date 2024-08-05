import random
import string

class promosys:
    def __init__(self):
        self.promo_codes = {}
        self.discount_rate = 0.60  # 60% off

    def generate_promo_code(self, length=8):
        """this fn generates a unique promo code Parameters: int , Returns: str """
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        self.promo_codes[code] = {'used_times': 0}
        return code

    def apply_promo_code(self, code, original_price):
        # impliment  the promo code to the given price and returns the discounted price , return tuple
        if code in self.promo_codes:
            self.promo_codes[code]['used_times'] += 1
            discount = original_price * self.discount_rate
            final_price = original_price - discount
            return final_price, self.promo_codes[code]['used_times']
        else:
            return None, None

if __name__ == "__main__":
    promo_system = promosys()
    
    promo_code = promo_system.generate_promo_code()
    print(f"generated Promo Code: {promo_code}")
    

    original_price = 100.0 
    for _ in range(3):  #for using promo code multiple times
        final_price, used_times = promo_system.apply_promo_code(promo_code, original_price)
        print(f"final $ after applying promo code: ${final_price:.2f}")
        print(f"promo code used {used_times} time")
