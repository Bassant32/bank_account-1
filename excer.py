import numpy as np

# إنشاء polynomial
p = np.poly1d([3, 2, 1])

print("المعادلة الأصلية:")
print(p)

# التكامل
integrated = p.integ()
print("\nالتكامل غير المحدد:")
print(integrated)