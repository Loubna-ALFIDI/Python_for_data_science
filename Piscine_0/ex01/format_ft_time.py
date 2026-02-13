import time
from datetime import datetime

Seconds = time.time()
now = datetime.now()

print(f"Seconds since January 1, 1970: {Seconds:,.4f} or {Seconds:.2e} in scientific notation")

formatted_date = now.strftime("%b %d %Y")
print(formatted_date)
