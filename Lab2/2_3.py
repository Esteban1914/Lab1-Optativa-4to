from suppliers import Suppliers

try:
    suppliers=Suppliers("./Lab2/Compra_y_venta_de_productos.xlsx")
    suppliers.show_unsold()
    
except Exception as e:
    print("Error:",e)